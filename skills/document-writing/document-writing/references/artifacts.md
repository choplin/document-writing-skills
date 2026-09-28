# Durable editorial artifacts

Persist intermediate artifacts when the work spans sessions, agents, or a
substantial document. The artifacts are the handoff contract; conversation
history is not.

Resolve `scripts/artifact-lineage.py` relative to this skill's `SKILL.md`, then
use that absolute path for deterministic publication and lineage inspection.
The helper derives revision identities and predecessors from the immutable
files, computes whole-file SHA-256 digests, and rejects invalid or ambiguous
lineage. It does not decide whether an artifact is complete, qualitatively
acceptable, or approved by the human author.

The helper requires Python 3.9 or later to be available as `python3`. It uses
only the Python standard library and installs no package dependencies. If that
runtime is unavailable, report the missing prerequisite and do not attempt the
deterministic artifact operations manually.

Its stable command contract is:

```text
python3 <document-writing-skill>/scripts/artifact-lineage.py digest PATH
python3 <document-writing-skill>/scripts/artifact-lineage.py next ROOT ARTIFACT
python3 <document-writing-skill>/scripts/artifact-lineage.py publish ROOT ARTIFACT --body-file PATH [--based-on PATH ...]
python3 <document-writing-skill>/scripts/artifact-lineage.py inspect ROOT
```

Every successful command writes JSON to standard output. `inspect` includes
the current head of each artifact lineage and stale upstream references from
those current heads; superseded historical revisions remain immutable but do
not keep repaired lineages invalid.
Invalid input, a digest mismatch, a superseded upstream reference, a malformed
revision, or ambiguous heads produces a nonzero exit. Other failures write a
JSON error to standard error. `publish` accepts a reviewed body without YAML
frontmatter, creates the next numbered file without overwriting any existing
revision, records the current head as `supersedes`, and computes each
`--based-on` digest. Treat its returned path as the exact published revision.

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
  reverse-outline/001.md
  semantic-spine/001.md
  meaning-tree/001.md
  plot/001.md
  draft/001.md
  draft/002.md
  reconstruction/001.md
  comparison/001.md
  acceptance/001.md
```

Omit inapplicable kinds. The immutable revision files and their links are the
complete workflow history.

## Working candidates and author decisions

A numbered planning artifact is a durable handoff candidate, not an autosave or
a record of AI editing history. Develop the candidate, self-review it, and apply
review findings inline before assigning the next revision number. Repeat that
internal cycle as needed without preserving each intermediate state as a
durable artifact. Its publication does not replace the semantic or editorial
conditions of the workflow stage that consumes it.

Publish a semantic-spine revision only after the agent has presented its
synthesis and the author has explicitly confirmed or corrected it. Summarize
the agreed reader-valued root and important branches and note that mutual
confirmation occurred. Record material unresolved choices and useful
provenance, but do not turn the body into a transcript or node-by-node approval
record.

An unconfirmed agent synthesis is a working candidate, not a semantic-spine
revision and not an input to composition. The author need not inspect or approve
the complete lower meaning tree; source-determined decisions below the shared
spine may remain there.

Publish an expanded meaning-tree revision after verifying it downward and
upward. Lower branches may change during composition when writing exposes a
source-supported defect. A change to the shared semantic spine requires a new
agent synthesis, mutual confirmation, and spine revision; a source-determined
repair below the spine does not.

Publish a plot revision when reader-path decisions are substantial enough to
matter across sessions or handoffs. Base it on the meaning tree. A plot records
entry, order, grouping, emphasis, passage movement, representation, and ending;
it neither changes the tree's logic nor creates another author-approval gate.

Working candidates are not durable workflow state. Keep them within the active
phase and do not make later phases or resumability depend on an unnumbered file,
mutable status record, or review log.

For a substantial explanatory, argumentative, procedural, or narrative
document, preserve a meaning tree that starts from the reader-valued root,
identifies the author-shared semantic spine, derives lower meanings top down,
and records the upward support check. Its body is free-form, and each branch
uses the representation and depth its material requires.

Preserve the draft-only reconstruction and its comparison with the intended
tree when the round trip is material to resumability or review. The
reconstruction records what a fresh reader recovered; the comparison records
how omissions, additions, changed relations, and changed claim strength were
resolved. The final reconstruction and comparison use `based_on` to identify the
exact final draft revision they checked. A later meaning-affecting edit requires
new downstream revisions.

## Revision header

Begin each artifact with minimal YAML frontmatter in the subset the helper
accepts: top-level fields may appear in any order; artifact names, predecessor
paths, and upstream paths are non-empty plain or JSON-quoted strings;
`revision` is a positive integer; and `based_on` is a non-empty list containing
one `path` and SHA-256 `digest` per item. YAML comments, tags, anchors, and
aliases are unsupported. Omit `based_on` when there are no upstream inputs.

```yaml
---
artifact: meaning-tree
revision: 2
supersedes: meaning-tree/001.md
based_on:
  - path: semantic-spine/002.md
    digest: sha256:<digest of that exact file>
---
```

The body is free-form Markdown. End with a short `Revision note` describing
what changed and why. Do not add empty metadata merely to satisfy a schema.

Past revisions are immutable. To change one after it has been published, finish
and internally review the replacement, then write the
next numbered revision and point `supersedes` at the prior revision. The first
revision omits `supersedes`. Publish the reviewed body with the helper rather
than selecting the number, predecessor, or digests manually. Paths are relative
to the artifact root unless the source is external.

## Detecting upstream changes

Before using an artifact, run the helper's `inspect ROOT` operation. If it
reports a digest mismatch or superseded upstream reference, inspect the actual
change and create a new downstream revision that records the reviewed upstream
revision. Do not reproduce head selection or hashing manually.

An upstream change does not automatically invalidate every word downstream.
It requires review. Even when no body text changes, create a new revision if it
is important to record that the newer premise was considered.

The helper reports the latest published artifact as the revision not
superseded by another revision in the same lineage. Publication records a
durable candidate; it does not prove that a semantic spine was shared, a meaning
tree was sound, or a draft passed its round-trip comparison. Record those facts
in the artifact body and its source decisions rather than inferring them from a
revision number. Branches are allowed, but the helper reports multiple heads as
ambiguous instead of choosing between them.

A generated status page or index may be used for convenience only if it can be
rebuilt from these files. It is never authoritative state.

## Handoff packet

Pass the exact latest relevant artifacts, not a summary from memory. A drafting
or editorial reviewer normally needs:

- assignment or brief;
- semantic spine;
- expanded meaning tree;
- plot or equivalent current composition decisions;
- source locations or discovery notes;
- current draft;
- terminology decisions;
- known deviations and unresolved decisions;
- latest reconstruction comparison when revising an existing draft.

A copyeditor may receive a narrower packet, but must still know the audience,
document kind, house style, protected terminology, and intervention boundary.
