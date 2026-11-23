---
bundle:
  name: work-python-dev
  display_name: Work · Python development
  version: 0.1.0
  description: Work with fast advisory checks after Python edits.

includes:
  - bundle: work:bundle.md
  - bundle: git+https://github.com/microsoft/amplifier-bundle-python-dev@main#subdirectory=behaviors/python-edit-feedback.yaml
---

@work:context/system.md
