"""Optional public-library and real calculation-engine acceptance tests."""
import os
from pathlib import Path
import shutil
import subprocess

import pytest

ROOT = Path(__file__).resolve().parents[1]


def reference(name, extension):
    return ROOT / 'skills' / f'artifact-template-{name}' / 'assets' / f'reference.{extension}'


def test_document_reference_can_be_edited_without_changing_source(tmp_path):
    docx = pytest.importorskip('docx')
    source = reference('minimal-letterhead', 'docx')
    before = source.read_bytes()
    doc = docx.Document(source)
    doc.paragraphs[0].text = 'Project update'
    doc.add_paragraph('The sample milestone is complete.')
    output = tmp_path / 'updated.docx'
    doc.save(output)
    saved = docx.Document(output)
    assert saved.paragraphs[0].text == 'Project update'
    assert saved.paragraphs[-1].text == 'The sample milestone is complete.'
    assert source.read_bytes() == before


def test_presentation_reference_retains_editable_shapes(tmp_path):
    pptx = pytest.importorskip('pptx')
    source = reference('business-review', 'pptx')
    before = source.read_bytes()
    deck = pptx.Presentation(source)
    deck.slides[0].shapes[0].text = 'Quarterly operating review'
    output = tmp_path / 'updated.pptx'
    deck.save(output)
    saved = pptx.Presentation(output)
    assert len(saved.slides) == 5
    assert saved.slides[0].shapes[0].text == 'Quarterly operating review'
    assert all(any(shape.has_text_frame for shape in slide.shapes) for slide in saved.slides)
    assert source.read_bytes() == before


@pytest.mark.parametrize('name,inputs,expected', [
    ('analytics-dashboard', {'A2':'Visits','C2':15,'D2':10}, {'B2':15,'D2':5}),
    ('financial-budget', {'A2':'Team','C2':100,'D2':90}, {'B2':100,'B3':90,'B4':-10}),
    ('operating-calendar', {'B2':'Review','D2':'Done'}, {'B2':1,'B3':1}),
    ('project-tracker', {'A2':'T1','B2':'Task','D2':'Blocked'}, {'B2':1,'B3':0,'B4':1}),
    ('sales-pipeline', {'A2':'Opportunity','D2':200,'E2':.25}, {'B2':200,'B3':50}),
    ('three-statement-forecast', {'B2':100,'B3':40,'B4':20,'B5':10,'B6':5,'B7':50,'B8':100,'B9':25},
     {'B6':35,'B9':80,'B10':105,'B16':0}),
])
def test_template_formulas_calculate_in_real_engine(tmp_path, name, inputs, expected):
    openpyxl = pytest.importorskip('openpyxl')
    office = os.environ.get('WORK_SOFFICE') or shutil.which('soffice')
    if not office:
        pytest.skip('LibreOffice required for actual calculation acceptance')
    source = reference(name, 'xlsx')
    before = source.read_bytes()
    workbook = openpyxl.load_workbook(source)
    for cell,value in inputs.items(): workbook['Inputs'][cell] = value
    draft = tmp_path / 'input.xlsx'
    workbook.save(draft)
    output = tmp_path / 'calculated'
    output.mkdir()
    subprocess.run([office, f'-env:UserInstallation={(tmp_path / "profile").as_uri()}',
                    '--headless', '--convert-to', 'xlsx', '--outdir', str(output), str(draft)],
                   check=True, capture_output=True, text=True, timeout=120)
    saved = openpyxl.load_workbook(output / draft.name, data_only=True)
    for cell,value in expected.items():
        assert saved['Summary'][cell].value == pytest.approx(value), (name,cell)
    assert source.read_bytes() == before
    formulas = openpyxl.load_workbook(output / draft.name, data_only=False)
    assert any(cell.data_type == 'f' for row in formulas['Summary'] for cell in row)


def test_pdf_generation_and_form_fill_round_trip(tmp_path):
    reportlab = pytest.importorskip('reportlab.pdfgen.canvas')
    pypdf = pytest.importorskip('pypdf')
    source = tmp_path / 'form.pdf'
    canvas = reportlab.Canvas(str(source))
    canvas.drawString(40,800,'Sample intake')
    canvas.acroForm.textfield(name='project',x=40,y=740,width=240,height=24)
    canvas.save()
    reader = pypdf.PdfReader(source)
    assert 'project' in reader.get_fields()
    writer = pypdf.PdfWriter(clone_from=reader)
    writer.update_page_form_field_values(writer.pages[0], {'project':'Test project'}, auto_regenerate=False)
    output = tmp_path / 'filled.pdf'
    writer.write(output)
    saved = pypdf.PdfReader(output)
    assert saved.get_fields()['project']['/V'] == 'Test project'
    assert 'Sample intake' in saved.pages[0].extract_text()
