# Amplifier Unified presentation adapter

Discover actions at runtime with `app_control` operation `list_actions` and
`args: {prefix: "canvas."}`. The following contracts were inspected in Unified
source revision `6749dbe6980d8ad2111ef5f5a9a9200b94d8a086` (0.19.0) on
2026-09-20; older hosts may only support snapshots. This document is
optional guidance, not an application dependency.

## Standalone snapshot

```
app_control({operation: "dispatch", args: {action: "canvas.show", args: {
  kind: "html", title: "Comparison", path: "outputs/comparison.html"
}}})
```

The path must be inside the selected workspace. Alternatively pass small inline
`content`. Read `/canvas` using `get_state`; inspect render reports and document
controls. An accepted publication is not a browser-confirmed render. Use the
discovered `canvas.interact` schema to operate ordinary controls, then reread
the document. HTML scripts run in an opaque sandbox without network, parent DOM,
cookies, or direct tool calls. Embed dependencies instead of loading CDNs.

## Persistent canvas app

If `canvas.apps.create` exists, use it for an app that needs later edits and
shared state. Create once with `{title, content, manifest, initialState}` and
retain the returned app ID. Read the full current schema before constructing
the manifest. A version-1 manifest defines `stateSchema`, `events`, `requests`,
and `theme`. Events have a payload `schema` and an `updates` mapping from a
top-level state field to a payload field. Do not invent arbitrary host actions.

For example, a shared selection can use:

```json
{
  "version": 1,
  "theme": "inherit",
  "stateSchema": {
    "type": "object",
    "properties": {"selection": {"type": "string"}},
    "required": ["selection"],
    "additionalProperties": false
  },
  "events": {
    "choose": {
      "schema": {
        "type": "object",
        "properties": {"value": {"type": "string"}},
        "required": ["value"],
        "additionalProperties": false
      },
      "updates": {"selection": "value"}
    }
  },
  "requests": {}
}
```

Supply `initialState: {selection: "first"}` alongside that manifest. Schemas
cannot contain references or regular expressions. Current limits include
500,000 HTML characters, a 32 KB manifest, and 100 KB of shared JSON state.

Inside HTML, wait for `window.canvasApp.ready`, read `snapshot.app.state`, and
use `subscribe`, `getSnapshot`, and `emit(name, payload)` for stateful controls.
For multiple editable fields, prefer one `canvasApp.createDraft({delay: 150})`
store. Call `draft.update({field: value})` for local changes and provide an
explicit Save/Retry button calling `draft.flush()`. Render pending values from
`draft.get()` and surface errors from `draft.getStatus()`. Failed writes retain
their values; do not create independent save owners for notes and drawings.

For a custom save path, call `beginEdit()` before non-form edits and capture
`getEditVersion()` when saving. `patch(fields, {commit: version})` or
`emit(name, payload, {commit: version})` acknowledges all unfinished input up to
that version, so include every pending field in the saved operation. Native
form input advances the edit version automatically. An unrelated event must
not acknowledge a failed note or drawing save. Use `setDirty(false)` only for
a user-requested discard, never as a workaround after a failed save.
`reportError` and `reportReady` report rendering failures and recovery.
Ordinary HTML must still have a useful local fallback without this bridge.

For the single-field `choose` manifest above, this explicit Save/Retry path
acknowledges the native input edit only after the host accepts it:

```html
<label>Selection <select id="selection"><option>first</option><option>second</option></select></label>
<button id="save">Save</button><output id="status" aria-live="polite"></output>
<script type="module">
const selection = document.querySelector('#selection');
const save = document.querySelector('#save');
const status = document.querySelector('#status');
const bridge = window.canvasApp;
if (!bridge) {
  save.onclick = () => { status.textContent = 'Selected locally: ' + selection.value; };
} else {
  let pending = false;
  const render = snapshot => {
    if (!pending) selection.value = snapshot.app.state.selection;
  };
  render(await bridge.ready);
  bridge.subscribe(render);
  selection.addEventListener('input', () => {
    pending = true;
    status.textContent = 'Unsaved';
  });
  save.onclick = async () => {
    const commit = bridge.getEditVersion();
    selection.disabled = save.disabled = true;
    status.textContent = 'Saving…';
    try {
      await bridge.emit('choose', {value: selection.value}, {commit});
      pending = false;
      render(bridge.getSnapshot());
      status.textContent = 'Saved';
    } catch (error) {
      status.textContent = 'Save failed; retry: ' + error.message;
    } finally {
      selection.disabled = save.disabled = false;
    }
  };
}
</script>
```

This pattern owns exactly one editable field. With multiple fields, use the
shared draft or save all pending fields together. An event without `commit`
can persist state while leaving the view dirty and blocking later revisions.
Verify both state readback and the attached view's clean status after saving.

Before an edit, dispatch `canvas.apps.inspect` with `{id, includeSource: true}`.
Use the inspected `app.revision` as `expectedRevision` and `app.stateRevision`
as `expectedStateRevision` on mutations.
`revise` changes content with optional manifest/title/migratedState; `state`
applies a patch; `event` sends a named payload. Preserve the same ID and tab.
Handle stale revisions by rereading and reconciling, not blindly retrying.
Dirty views can block revision/restoration; preserve unsaved user changes.
Reuse a stable dispatch ID when retrying the same operation.

The bridge does not allow arbitrary filesystem/network/tool calls. Current
requests may declare only `theme.preview`, `theme.apply`, or `theme.revert`.
`canvasApp.request(name, input)` queues a request without executing it. Inspect
the exact request with `canvas.apps.inspect {id, requestId}` before resolving.
`canvas.apps.resolve` takes the current revisions, `requestId`, `approve`, and
an explicit attached `clientId`; an agent can approve only changes covered by
the user's instruction. Preview affects the selected client; applying a theme
affects the shared shell. Events and saved state do not automatically start an agent turn.
Do not simulate OpenAI follow-up-message APIs or claim autonomous callbacks.

## Current observations

On hosts exposing `context.read`, read a bounded surface representation with
`{surfaceId, representation: "state", fields: ["selection"], revision: "1:3"}`.
The revision identifies definition and state revisions. Other representations
are `summary`, `view`, and `image`. Treat stale-revision errors as conflicts;
reduce fields or use paged `get_state` for state exceeding the 24 KB limit.
State changes may produce notices before an already scheduled model request,
but neither notices nor edits start a new model turn.

Image observations require a visible canvas registered with
`canvasApp.observeCanvas(canvas, draw)` and a provider advertising vision.
The read returns a receipt; typed image content is delivered to the next
provider request. This is not an arbitrary HTML screenshot, and a notice alone
does not establish that the agent received pixels. Missing, hidden, stale,
or disconnected views must be reported as such. For explicitly requested visual
collaboration, `context.focus {surfaceId, requests: 1}` can request bounded
prefetch; `requests: 0` ends it. It is not a persistent subscription.

Verify publication, render status, user interaction, state readback, and revision
handling separately. A browser must be attached for visible acceptance.
