---
bundle:
  name: work
  display_name: Work
  version: 0.4.0
  description: A small, provider-neutral Work profile for live Amplifier hosts.

includes:
  - bundle: work:bundles/work-session.yaml
  - bundle: work:behaviors/work-skills.yaml
  - bundle: work:behaviors/work-execution.yaml

session:
  orchestrator:
    config:
      programmatic_dispatch: true

tools:
  - module: tool-filesystem
    source: git+https://github.com/microsoft/amplifier-module-tool-filesystem@main
  - module: tool-apply-patch
    source: git+https://github.com/microsoft/amplifier-bundle-filesystem@main#subdirectory=modules/tool-apply-patch
    config:
      engine: native
  - module: tool-search
    source: git+https://github.com/microsoft/amplifier-module-tool-search@main
  - module: tool-delegate
    source: git+https://github.com/microsoft/amplifier-foundation@main#subdirectory=modules/tool-delegate
    config:
      features:
        self_delegation:
          enabled: true
        session_resume:
          enabled: true
        context_inheritance:
          enabled: true
          max_turns: 10
        provider_selection:
          enabled: true
      settings:
        exclude_tools: [tool-delegate]
        exclude_hooks: []
        timeout: null
        max_llm_calls: null
---

@work:context/system.md
