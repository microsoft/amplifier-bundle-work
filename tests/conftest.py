"""Explicit candidate override; normal tests resolve the canonical main include."""
import os
from pathlib import Path

from amplifier_foundation import BundleRegistry
import pytest


@pytest.fixture(autouse=True)
def candidate_foundation_include(monkeypatch):
    """Qualify unpublished Foundation manifests without changing maintained URLs."""
    candidate = os.environ.get("WORK_FOUNDATION_BUNDLE")
    if not candidate:
        return
    root = Path(candidate).expanduser().resolve(strict=True)
    assert (root / "bundle.md").is_file()
    canonical = "git+https://github.com/microsoft/amplifier-foundation@main"
    original_init = BundleRegistry.__init__

    def init(registry, *args, **kwargs):
        prior = kwargs.get("include_source_resolver")

        def resolve(source):
            if source == canonical:
                return str(root / "bundle.md")
            prefix = canonical + "#subdirectory="
            if source.startswith(prefix):
                path = (root / source[len(prefix):]).resolve()
                assert path.is_relative_to(root)
                return str(path)
            return prior(source) if prior else None

        kwargs["include_source_resolver"] = resolve
        original_init(registry, *args, **kwargs)

    monkeypatch.setattr(BundleRegistry, "__init__", init)


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
