---
name: plugin-management
description: Discover, inspect, connect, or remove Amplifier bundles, MCP integrations, and Smart Tools using the host's available management actions.
user-invocable: true
---

# Integration management

Inspect mounted tools first. Use an existing capability when it meets the task.
When a needed external service is absent, discover the host's integration
catalog and management schemas. A skill supplies instructions; it does not
install an executable, connect an account, or provide another host's OAuth grant.

On Amplifier Unified, use `app_control` `list_actions` with prefix `smartTools.`
or `bundles.`. Read the returned schemas and current state before mutations.
Distinguish a Python Git Smart Tool installation from configuring and connecting
a standard MCP server. A Codex plugin manifest is not a supported installer
input. Use the host's returned IDs; never invent an integration identifier.

Verify the operation receipt, connection state, and advertised tools before
using a new integration. Track long-running operation IDs to completion. Keep
credentials in the host's private connection configuration or environment
references. Report missing authorization or a required user sign-in precisely.

Remove integrations or change permissions only within the requested scope.
Do not uninstall a dependency just because another capability looks preferable.
If management actions are absent, provide the exact bundle/MCP configuration
needed without claiming it has been installed or connected.
