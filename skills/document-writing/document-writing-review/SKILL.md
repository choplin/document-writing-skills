---
name: document-writing-review
description: >-
  Performs a holistic editorial review and revision of an existing document.
  Applies when the draft may have the wrong focus, conceptual emphasis,
  explanation depth, order, or reader progression—not merely awkward sentences.
  Builds an editorial assignment, reverse outline, content model, diagnosis,
  and revised plot before substantive, line, and copy edits.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
metadata:
  description-role: trigger
---

# Document Review

Review from the whole document inward. Read
`../document-writing/references/workflow.md` and
`../document-writing/references/content-model.md`, then follow the
existing-document branch. If work will span sessions or files, also follow
`../document-writing/references/artifacts.md`.

## Workflow

1. Establish the editorial assignment: audience and prior knowledge, use,
   intended outcome, document kind, constraints, degree of intervention, and
   protected content.
2. Read diagnostically and make a recursive reverse outline of what the draft
   actually establishes. Recover lower-level meaning units, how they group, and
   how each group composes a higher-level meaning.
3. State the governing focus you can recover, conflicts within it, and any
   plausible alternatives. Distinguish unclear expression from an unsettled
   idea.
4. Build an editorial diagnosis covering substance, support, conceptual
   emphasis, order, proportion, representation, and reader movement.
5. Read the recursive content-model guide, then build a model whose root is the
   recovered or revised focus. For each developed non-leaf unit, show what it
   establishes, which children establish it, and how they compose that meaning.
   Do not treat the existing order or boundaries as the intended hierarchy.
6. Propose a free-form revised plot that linearizes the content model for the
   reader through order, grouping, emphasis, boundaries, and representation.
   Do not copy the model node by node or revise prose until the proposed path is
   coherent. Ask only when competing plots would materially change the author's
   position or scope.
7. Revise substantively against the plot. Realize each higher-level unit as a
   connected passage whose composition is recoverable; do not assign one
   sentence or paragraph to each content-model node.
8. Apply a connected line edit and then local copyedit through
   `document-writing-base`.
9. Verify the result against the assignment, focus, content model, plot, and
   protected content. Reconstruct the major meaning hierarchy from the prose
   and reject a draft that covers every child but does not establish its parent
   meanings.
10. When the assignment requires reader evidence, hand the complete draft to
   `document-reader-review`. Work accepted findings through
   `document-reader-revise`, then repeat every editorial pass affected by those
   decisions before acceptance.

Use planning principles and editorial heuristics from
`document-writing-standards` in stages 2–6. They are aids to diagnosis and
judgment, not independent mandates. Use conformance checks only after the
document's substance and structure are stable.

## Review context

Any editorial reviewer receives the relevant audience, focus, content model,
reverse outline, current plot, sources, and intervention boundary. Editorial
reviewers may be blind to one another's conclusions, but never blind to the
context needed to judge why the document exists.

Reader personas are not editorial reviewers. They follow
`document-reader-review` and must not receive the author's intent, focus, plot,
or another persona's findings. Their constrained prior knowledge is the
measurement, not missing editorial context.

## Routing findings

Name the earliest artifact that owns each issue. A missing parent meaning,
unclear composition, orphaned child, missing premise, misplaced definition, or
inverted conceptual emphasis is a developmental issue even when its symptom
appears in one sentence. Do not repair it through the smallest possible local
edit merely because the anchor is easy to locate.

If the user permits only content-preserving changes, return upstream issues as
observations and confine the revision to that boundary. If the task is truly
wording-only, use `document-writing-prose` instead.

## Deliverable

Lead with the revised document or link. Then give a concise account of the
recovered focus, principal plot changes, important content decisions, passes
completed, context limitations, and unresolved questions. Preserve intermediate
artifacts according to the artifact reference so the work can resume without
conversation history.
