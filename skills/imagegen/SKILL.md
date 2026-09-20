---
name: imagegen
description: Generate or edit raster images using a mounted image-generation capability. Use for illustrations, photos, textures, and bitmap assets; use visualize for HTML diagrams.
compatibility: "Requires a mounted image generation or editing adapter. Text generation and filesystem tools alone cannot run this workflow."
user-invocable: true
---

# Image generation

Discover the host's mounted image-generation tools and read their actual schema.
This bundle does not install a provider, supply API credits, or inherit another
application's image-generation service. Keep provider and model selection under
the user's and host's control.

Determine whether the task creates a new image or edits an existing one. Inspect
every edit target and label reference images by role. Specify subject, framing,
style, dimensions/aspect ratio, output format, background/alpha, exact text, and
the properties an edit must preserve. Do not change an established vector asset
system into bitmaps merely because image generation is available.

Call the mounted tool with the requested constraints. Save a workspace copy of
project assets using the returned file operation, without overwriting originals
unless requested. Inspect the result for content, spelling, framing, artifacts,
and actual transparency when needed. Iterate on the failed property while
preserving accepted parts.

If no tool is mounted, identify that requirement and continue independent work.
An external API fallback requires an available authorized provider and credentials
from host configuration; never expose secrets or silently select a paid service.
Do not describe a prompt, SVG placeholder, or unexecuted request as a generated image.
