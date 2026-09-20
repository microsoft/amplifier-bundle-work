---
name: openai-docs
description: Research OpenAI APIs, models, and product behavior using current official documentation. Use for OpenAI integration or product questions, not Amplifier self-knowledge.
compatibility: "Requires an available web search or fetch tool for current official OpenAI documentation."
user-invocable: true
---

# OpenAI documentation

Use mounted search/fetch tools or an authorized documentation connector to find
the user's specific topic on official OpenAI sources. Fetch the supporting page,
not only its search snippet. Prefer developers.openai.com and platform.openai.com
for APIs; use the product's official documentation for ChatGPT and Codex.

Preserve explicitly requested models, endpoint versions, and product context.
Check changing details such as models, prices, limits, and supported parameters
against current pages. Keep citations adjacent to the claims they support.
Distinguish documented behavior from inference and runtime observations. If the
source cannot be fetched, state the limit rather than supplying invented links
or calling stale knowledge current.

For implementation, inspect the actual SDK and host integration. Keep API keys
in the host's authorized secret configuration. Do not treat Codex-only tools,
ChatGPT product features, or subscription benefits as public API capabilities.
When the user says "this app" inside Amplifier, inspect Amplifier's own contracts;
this skill does not redefine the current host as Codex.
