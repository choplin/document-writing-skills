# Durable editorial artifacts

Persist intermediate artifacts when the work spans sessions, agents, or a
substantial document. The artifacts are the handoff contract; conversation
history is not.

## Storage

Choose the artifact root in this order:

1. Use a working location named by the user or repository.
2. For a document in a version-controlled workspace, use a repository-local,
   writable working area that is already excluded from version control. When
   `.agents/` exists and is excluded, use
   `.agents/document-writing/<document-relative-path>.writing/`. Do not create
   `.agents/` or change ignore rules merely to obtain this location.
3. Otherwise, use the platform's persistent per-user state area. On systems
   following the XDG Base Directory specification, use
   `$XDG_STATE_HOME/document-writing/<workspace-id>/`, or
   `~/.local/state/document-writing/<workspace-id>/` when `XDG_STATE_HOME` is
   unset. Preserve the document's workspace-relative path beneath that root
   and use the `<document>.writing/` suffix. Choose a deterministic,
   collision-resistant workspace identifier so another repository cannot
   share the artifact root accidentally.
4. If no persistent writable location is available, ask the user where to keep
   durable artifacts before creating them.

Do not place artifacts beside a version-controlled document unless the user or
repository explicitly selects that location. For supplied text with no durable
destination, keep artifacts in the response unless persistence would clearly
help and an in-scope persistent location is available.

Use one directory per artifact kind and immutable, zero-padded revisions:

For example, a repository that provides an ignored `.agents/` directory may
store artifacts for `docs/guide.md` as:

```text
.agents/document-writing/docs/guide.md.writing/
  brief/001.md
  discovery/001.md
  focus/001.md
  content-model/001.md
  plot/001.md
  plot/002.md
  reverse-outline/001.md
  draft/001.md
  draft/002.md
  acceptance/001.md
```

Omit inapplicable kinds. The immutable revision files and their links are the
complete workflow history.

## Working candidates and human gates

A numbered planning artifact is a complete candidate ready for human
inspection, not an autosave or a record of AI editing history. Develop the
candidate, self-review it, and apply review findings inline before assigning the
next revision number. Repeat that internal cycle as needed without preserving
each intermediate state as a durable artifact.

After publishing a content-model or plot revision, present that exact revision
to the human author and wait for them to read and accept it before starting the
dependent phase. Acceptance without changes does not create a new revision. If
the author requests changes, use the published revision as the basis for a new
working candidate, complete its internal review and inline repair, and only then
publish the next numbered revision.

Working candidates are not durable workflow state. Keep them within the active
phase and do not make later phases or resumability depend on an unnumbered file,
mutable status record, or review log.

For a substantial explanatory, argumentative, procedural, or narrative
document, preserve a content model that starts from the reader-centered root,
derives its supporting meanings top down, and records the upward support check.
Its body is free-form, and each branch uses the representation and depth its
material requires. A short document may combine the content model and plot when
the semantic design and reader-facing choices remain separately inspectable.

## Revision header

Begin each artifact with minimal YAML frontmatter:

```yaml
---
artifact: plot
revision: 2
supersedes: plot/001.md
based_on:
  - path: focus/002.md
    digest: sha256:<digest of that exact file>
  - path: content-model/001.md
    digest: sha256:<digest of that exact file>
---
```

The body is free-form Markdown. End with a short `Revision note` describing
what changed and why. Do not add empty metadata merely to satisfy a schema.

Past revisions are immutable. To change one after it has been published for
human inspection, finish and internally review the replacement, then write the
next numbered revision and point `supersedes` at the prior revision. The first
revision omits `supersedes`. Paths are relative to the artifact root unless the
source is external.

## Detecting upstream changes

Before using an artifact:

1. Resolve each `based_on.path`.
2. Compute the SHA-256 digest of the whole referenced file.
3. Compare it with the recorded digest.
4. Check whether a newer revision now supersedes the referenced revision.
5. If either check differs, inspect the actual change and create a new
   downstream revision that records the reviewed upstream revision.

An upstream change does not automatically invalidate every word downstream.
It requires review. Even when no body text changes, create a new revision if it
is important to record that the newer premise was considered.

The latest published artifact is a revision not superseded by another revision
in the same lineage. Publication alone does not make a content model or plot
usable by its dependent phase; that also requires the human acceptance described
above. Branches are allowed; do not silently choose between two heads when they
embody materially different decisions.

A generated status page or index may be used for convenience only if it can be
rebuilt from these files. It is never authoritative state.

## Handoff packet

Pass the exact latest relevant artifacts, not a summary from memory. A drafting
or editorial reviewer normally needs:

- assignment or brief;
- focus;
- content model;
- plot;
- source locations or discovery notes;
- current draft;
- known deviations and unresolved decisions.

A copyeditor may receive a narrower packet, but must still know the audience,
document kind, house style, protected terminology, and intervention boundary.
