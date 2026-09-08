---
name: document-writing
description: >-
  Plans, drafts, and revises substantial documents from framing through
  delivery. Applies to books and chapters, technical documentation, academic
  writing, and explanatory or argumentative documents whose audience,
  governing idea, content design, and reader progression must be established
  before prose is finalized.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
metadata:
  description-role: trigger
---

# Document Writing

Carry the document from the change it should create for its reader through
delivery. Keep one semantic direction across planning, drafting, editing,
reader evidence, and acceptance while letting each phase use the form and depth
its material needs.

The governing direction is:

```text
reader's situation, problem, or task
                ↓
       root meaning and value
                ↓
       top-down content design
                ↓
 bottom-up verification from material
                ↓
       reader-facing plot and prose
```

When maintaining this workflow, read
[evaluation.md](references/evaluation.md). Keep evaluation material outside a
forward-test agent's context.

## Select the route

- **New or substantially rebuilt document:** run the complete workflow below.
- **Existing document:** add diagnostic reading and a reverse outline, then
  design the target document afresh from its reader-centered root.
- **Settled content and structure:** delegate a connected wording revision to
  `document-writing-prose`, detection to `document-writing-audit`, and approved
  local findings to `document-writing-apply`.

Small documents may combine adjacent artifacts while preserving the decisions
and checks owned by each phase.

For work spanning files, sessions, or agents, read
[artifacts.md](references/artifacts.md) before publishing the first durable
artifact. Use its revision, lineage, storage, and resume contract throughout the
workflow.

## Write the document

### 1. Frame the outcome

Establish the audience, prior knowledge, use and reading situation, intended
outcome, document kind, scope, constraints, sources, and unresolved questions.
For revision, include the intervention boundary and protected content.

When document-kind conventions affect framing or route selection, read only the
matching section of [document-kinds.md](references/document-kinds.md). Apply
`document-writing-standards` and load only the planning guidance relevant to
the current decisions.

Establish a focus and proposed root that connect a problem, question, task, or
situation recognizable to the reader with the document's answer, method,
position, or experience and the value or consequence it creates.

### 2. Learn and diagnose

Collect what the source material establishes, suggests, or leaves open,
including provenance and claim status.

Apply `document-writing-standards` and load planning guidance for claim support,
epistemic status, and diagnosis only when those judgments arise.

For an existing document, recover what its passages currently cause a reader to
understand. Locate support, gaps, repetition, emphasis, and movement at the level
where they affect the reader. Preserve this reverse outline as a diagnosis and
material inventory for later mapping.

### 3. Design and verify the content

Load [content-model.md](references/content-model.md) when this phase begins.
Give it the assignment, focus, relevant sources, and, for an existing document,
the diagnosis and reverse outline. Follow its complete content-design procedure.

This phase is complete when a complete content-model candidate has passed that
internal check, been published as a durable revision, and been read and accepted
by the human author. Hand the accepted content model, assignment, focus, and
relevant sources to the matching plot guide. The accepted model governs what the
document must establish while leaving plot and prose free to realize it
naturally.

### 4. Plot the reader's experience

Choose one guide:

- [general document](assets/plot-general.md)
- [book or chapter](assets/plot-book.md)
- [technical document](assets/plot-technical.md)
- [academic document](assets/plot-academic.md)

Use it to choose the reader's entry, order, grouping, pace, emphasis, local
passage movement, physical boundaries, ending, and representations. The plot
owns the path through the modeled content.

Apply `document-writing-standards` and load only planning guidance relevant to
the plot decisions being made.

Review the working plot against the accepted content model, assignment, and
relevant sources. Correct findings inline and repeat until the candidate is
coherent and ready for the author; do not preserve those internal iterations as
durable revisions. Publish the complete candidate as the next plot revision,
then wait for the human author to read and accept it before drafting. If they
request changes, complete the same internal review-and-repair cycle before
publishing another revision.

### 5. Draft and edit

Draft connected movements and passages against the content model and plot while
preserving source boundaries and claim status. Apply
`document-writing-standards` at each pass and load only guidance matching its
editorial stage, prose language, and current judgment. Then run the passes from
larger decisions to smaller ones:

1. developmental edit for substance, support, architecture, proportion,
   representation, and reader movement;
2. connected line edit through `document-writing-base`;
3. local copyedit through `document-writing-base`;
4. reader review through `document-reader-review` when acceptance requires
   evidence from intended readers;
5. author resolution through `document-reader-revise` and repetition of every
   editorial pass affected by an accepted finding; and
6. proof of the complete rendered object.

### 6. Accept and deliver

Accept the document when the intended reader can reach the promised outcome;
the root is supported at its stated strength; central passages carry coherent
internal movement; uncertainty, provenance, and protected content survive; and
the final references, format, and rendering are usable.

Lead the delivery with the document or its link. Then identify the latest
durable artifacts, completed passes, material departures from the plot, and
unresolved decisions.

## Coordinate context and revision

Give each phase the exact current artifacts it needs. Content design receives
the assignment, focus, sources, and diagnosis. Plotting receives the
human-accepted content model. Drafting and editorial review receive the
assignment, focus, human-accepted content model, human-accepted plot, sources,
and intervention boundary.

Independent editorial reviewers receive the same governing context while
working without one another's conclusions. Reader personas receive the finished
document and their assigned reader context through `document-reader-review`;
their reactions return to the author for substantive decisions.

Route a failure to its earliest owner:

- reader promise or scope → assignment or focus;
- substance, support, or semantic relationship → discovery or content design;
- order, grouping, emphasis, representation, or passage movement → plot;
- paragraph or sentence realization → line edit;
- local correctness or consistency → copyedit.

When an upstream decision changes, review its downstream artifacts and create
new durable revisions for the affected decisions and prose. Report choices that
require new authority, evidence, or scope.

A durable planning revision is a complete candidate for human inspection, not
a record of AI editing history. Perform self-review and inline repair before
publishing it. Human acceptance without changes advances the workflow without
creating another revision; changes requested after inspection produce a new
revision only after its working candidate has passed the same internal checks.
