---
name: document-writing
description: >-
  Plans, drafts, and revises substantial documents by first sharing their
  governing meaning with the author, then expanding, composing, and verifying
  that meaning through finished prose. Applies to technical, academic,
  explanatory, argumentative, and book-length work.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
metadata:
  description-role: trigger
---

# Document Writing

Turn the author's intended meaning into a document that lets its reader reach
the intended understanding, decision, or action. Treat writing as a semantic
design activity: establish the governing meaning with the author, develop it
recursively, realize it as connected prose, then recover the meaning from the
prose and compare the two.

```text
author intent and sources
        ↕ collaborate
reader-valued root and semantic spine
        ↓ agent expands
complete meaning tree
        ↓ composition owner plots the reader path
reader-facing plot
        ↓ same owner composes
complete draft
        ↕ fresh reconstruction and revision
recovered meaning tree
        ↓ factual and editorial finish
final candidate
        ↓ final reconstruction
verified document
```

The author owns what the document means. The writing agent owns how settled
meaning becomes a readable document. Do not replace either responsibility with
approval of a large intermediate outline.

The workflow's primary invariant is **mutual agreement on the governing
meaning before composition**. The agent must express its current understanding
of the meaning tree back to the author, from the root through the branches deep
enough to constrain the document. The author must explicitly confirm or correct
that understanding. Until both directions have occurred, do not create or
substantively revise the target document.

This is one semantic handoff, not a prescribed meeting or artifact ceremony.
Its format, length, and number of conversational turns follow the work. It does
not require approval of every node, the complete lower tree, headings, or a
prose plan. A request to write does not replace the handoff when the agent has
not yet shown what it understood.

Treat this agreement as more important than drafting progress, review counts,
lens conformance, or polished prose. Those downstream activities can be
repeated and repaired; prose built from an unshared governing meaning cannot be
accepted as progress.

When maintaining or evaluating this workflow, read
[evaluation.md](references/evaluation.md). Keep evaluation cases and reference
outputs outside a forward writing agent's context.

## Select the route

- **New or substantially rebuilt document:** use the complete workflow below.
- **Existing document:** first diagnose the current reader experience and make
  a reverse outline. Use the draft as material, not as the target hierarchy.
- **Settled meaning and structure:** delegate connected wording revision to
  `document-writing-prose`, local detection to `document-writing-audit`, and
  approved local findings to `document-writing-apply`.

For work spanning files, sessions, or agents, read
[artifacts.md](references/artifacts.md) before publishing a durable artifact.
Use immutable revisions and `based_on` digests without making artifact
publication an approval ceremony.

## Build the document

### 1. Frame and learn

Establish the intended reader, prior knowledge, reading or work situation,
useful outcome, document kind, scope, constraints, sources, protected content,
and unresolved questions. For revision, also record the intervention boundary.

When document-kind conventions affect the work, read only the matching section
of [document-kinds.md](references/document-kinds.md). Apply
`document-writing-standards` progressively, loading only the planning guidance
needed for the current judgment.

Collect what the available material establishes, suggests, or leaves open.
Record provenance and epistemic status. For an existing draft, recover what its
passages currently cause a reader to understand, including gaps, repetition,
misplaced emphasis, and unsupported transitions.

### 2. Share the semantic spine

Load [meaning-tree.md](references/meaning-tree.md) when this phase begins.
Apply it to collaborate with the author from the root downward.

Distinguish the reader outcome from the document's substantive root. The reader
outcome explains why reading matters; the root states the governing meaning the
reader must understand or judge. For a product or design document, the root
normally expresses the user or organizational value of the subject, not merely
that a designer will understand its components or decisions.

Develop the root and important branches through ordinary conversation. When the
tree is deep enough to constrain the document, present a coherent synthesis of
the agent's understanding: its root, the meanings that establish it, and their
material relations, conditions, and qualifications. Ask the author to confirm
or correct that understanding. Continue at the meaning level until the author
explicitly confirms the current synthesis. Do not compose while confirmation is
absent or while the author is still correcting its governing meaning.

The confirmed portion is the **semantic spine**. It fixes the author-owned part
of the document's governing logic. It is not a mechanical outline and need not
map one node to one heading or paragraph. Existing prose, source material, or an
agent-authored artifact cannot establish this agreement. When durable handoff
is useful, publish a semantic-spine revision only after confirmation; the
artifact summarizes the agreed meaning without requiring a transcript or
node-by-node evidence.

After agreement, expand lower branches, compose, edit, apply lenses, and review
autonomously. Return to this handoff only when the root or another agreed
meaning must change.

### 3. Expand and verify the meaning tree

Develop the semantic spine downward until the difficult branches can guide
coherent passages without unstated reasoning. Include the claims, reasons,
mechanisms, distinctions, evidence, examples, conditions, and consequences the
reader needs. State how children combine to establish each parent.

Treat the complete meaning tree as the document's logical design. Derive it
recursively from the root: every child must contribute to its parent, sibling
meanings must jointly establish or develop that parent, and every material leaf
must have a traceable path of contribution back to the root. The tree determines
which meanings are governing, supporting, subordinate, or out of scope.
Available material may substantiate or refine this logic, but a topic inventory,
source organization, or existing document cannot substitute for it.

Maintain terminology with the tree: give each concept one primary name, its
intended meaning and scope, important distinctions, and any source or code name
that must remain traceable. For a material example, record the inputs,
operation, expected result, and the proposition it demonstrates.

Verify upward from developed leaves to the root. Check that evidence supports
the stated strength, examples actually instantiate their propositions, and no
branch depends on unstated author intent. Repair lower branches directly when
accepted sources determine the answer. Return to the author only when the
repair would alter the shared semantic spine or requires new authority.

### 4. Plot, compose, and develop the draft

Give one writing agent ownership of composition through developmental editing.
Provide the brief, semantic spine, expanded meaning tree, sources, terminology,
protected content, and applicable house style. Composition decisions remain
with that owner throughout the complete draft and developmental edit.

Read the plot guide matching the document kind when choosing the reader-facing
realization:

- [general document](references/plot-general.md)
- [book or chapter](references/plot-book.md)
- [technical document](references/plot-technical.md)
- [academic document](references/plot-academic.md)

Derive the plot and document architecture from the meaning tree before
composing prose. The meaning tree governs what the document establishes and how
its meanings support one another. The plot governs how the intended reader
encounters that logic: entry, order, grouping, pace, emphasis, passage movement,
representation, and ending. Plot decisions may rearrange or combine tree nodes
for comprehension, but may not replace their hierarchy or contribution
relations.

For every central section and paragraph, identify its governing proposition,
its parent meaning, and how it advances that parent. Let logical role, reader
need, and explanatory difficulty determine order, emphasis, and development
depth.

The composition owner chooses the entry, order, headings, paragraph grouping,
representations, examples, transitions, emphasis, and ending required by the
reader and genre. It may combine several tree nodes in one passage or develop
one node across several passages, but these choices must realize the tree's
support relations and priorities. Freedom of presentation does not permit a
different logical hierarchy to govern the prose.

Attach source material, prior prose, examples, and technical detail to the
meanings they support only after the logical design exists. Material belongs in
the document when it contributes to a node at appropriate scope and prominence;
otherwise omit it, move it to a separately scoped artifact, or revise the tree
through the appropriate authority boundary.

Draft connected passages, then developmentally edit the complete document for
substance, support, architecture, proportion, representation, and reader
movement. Writing may expose a missing relation, unnatural example, ambiguous
term, or misplaced distinction. Repair the prose and lower meaning tree
together when sources settle the issue. Ask the author only when the discovery
changes an author-owned meaning.

### 5. Reconstruct and compare

Give a fresh reviewer the finished draft, intended audience, and reading
situation, but not the semantic spine, meaning tree, author intent, source
outline, or suspected defects. Ask the reviewer to reconstruct from the
document alone:

- the document's root and major supporting meanings;
- each central section's governing proposition;
- the contribution of its paragraphs and important examples;
- the relations among claims, evidence, conditions, and consequences; and
- the qualifications and unresolved questions a reader should retain.

Compare the recovered tree with the intended tree. Compare not only whether
meanings occur, but also their hierarchy, support relations, sequence,
prominence, and development depth. Look for omitted or invented claims, changed
strength, lost conditions, misplaced support, ambiguous relations, examples
that imply the wrong generalization, and a root the reader cannot recover from
the document's entry and progression. The comparison fails when the intended
meanings are present but do not govern the logic a reader reconstructs.

Revise and repeat until material differences are resolved. Change prose when
the intended meaning was not realized. Change the lower meaning tree when
writing exposed a source-supported defect. Return to the author when the shared
semantic spine itself must change.

This round trip tests semantic recoverability, not external truth.

### 6. Verify truth and finish the prose

Verify domain meanings, factual claims, quotations, calculations, and examples
against authoritative sources or the appropriate external fact-checking
workflow. Keep editorial review, reader review, and external fact-checking as
separate responsibilities even when all are required before delivery.

Apply `document-writing-standards` in this order:

1. holistic editorial guidance for paragraph movement, information order,
   continuity, voice, diction, and cadence across the complete document;
2. language and terminology guidance while preserving the intended tree; and
3. deterministic local checks only after meaning and structure are stable.

Use lenses as guidance or checks at their declared control level. Do not split
the document into one independent rewrite per lens, and do not treat a clean
local audit as evidence that the document works as a whole.

Run `document-reader-review` when acceptance requires evidence from intended
readers. Resolve substantive findings through `document-reader-revise`, then
repeat every affected semantic, editorial, factual, and local check. Finally,
proof the complete rendered object.

After these passes, reconstruct and compare the meaning of the exact final
candidate. Any later change capable of affecting meaning or recoverability,
including a factual correction, example correction, holistic edit, reader
revision, or proof-driven edit, requires another fresh reconstruction and
comparison. Deterministic local edits must pass their preservation check; repeat
reconstruction when that check cannot establish that the change was semantically
neutral.

### 7. Accept and deliver

Read the final document from its first line without planning artifacts. Accept
it only when an intended reader can identify what the document is, why it
matters, and what it enables; recover its governing meaning and central
propositions; follow the support and examples; distinguish settled claims from
limits and open questions; and use the rendered object as intended. The accepted
reconstruction comparison must be based on the exact delivered draft revision.

Lead delivery with the document or its link. Then report the shared semantic
spine, material author decisions, verification performed, unresolved questions,
and any departures that affect meaning. Do not lead with workflow artifacts.

## Coordinate authority and revision

The author need not review every intermediate artifact. Ask only for semantic
choices whose alternatives would materially change the document. A request to
discuss feedback, inspect an artifact, or consider an option does not authorize
publishing external records or making unrelated changes.

When an author-owned decision changes, revise the affected meaning-tree branch,
draft, reconstruction comparison, and downstream checks. Preserve durable
lineage where the work requires it, but derive status from immutable revisions
rather than a mutable workflow record.

Independent reviewers receive only the context their evidence requires:

- meaning-tree verification receives the tree and accepted sources;
- reconstruction receives the finished draft and reader context, not intent;
- editorial review receives the draft and intended meaning;
- reader personas receive the finished document and their reader context; and
- fact-checking receives the claims and authoritative sources it must verify.
