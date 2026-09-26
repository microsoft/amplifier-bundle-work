"""Explicit candidate override; normal tests resolve the canonical main include."""
import os
from pathlib import Path

from amplifier_foundation import BundleRegistry
import pytest


@pytest.fixture(autouse=True)
def candidate_imagegen_include(monkeypatch):
    candidate = os.environ.get("WORK_IMAGEGEN_BUNDLE")
    if not candidate:
        return
    root = Path(candidate).expanduser().resolve(strict=True)
    assert (root / "bundle.md").is_file()
    canonical = "git+https://github.com/microsoft/amplifier-bundle-imagegen@main"
    sources = {
        canonical: root / "bundle.md",
        canonical + "#subdirectory=behaviors/skills.yaml": root / "behaviors/skills.yaml",
    }
    original_init = BundleRegistry.__init__

    def init(registry, *args, **kwargs):
        prior = kwargs.get("include_source_resolver")

        def resolve(source):
            if source in sources:
                return str(sources[source])
            return prior(source) if prior else None

        kwargs["include_source_resolver"] = resolve
        original_init(registry, *args, **kwargs)

    monkeypatch.setattr(BundleRegistry, "__init__", init)
