---
name: document-writing
description: >-
  Plans, drafts, and revises substantial documents through a durable editorial
  workflow. Applies to books and chapters, technical documentation, academic
  writing, and general explanatory or argumentative documents when the work
  must establish the audience, governing idea, content model, and reader
  progression before polishing prose. Also applies when an existing draft
  needs developmental editing rather than sentence cleanup alone.
allowed-tools: Read, Write, Edit, Glob, Grep, Bash, Task, AskUserQuestion
metadata:
  description-role: trigger
---

# Document Writing

Treat writing as a sequence of editorial decisions, not as prose followed by a
large lens sweep. Establish what the document is trying to do and how the reader
will get there; only then draft and edit at progressively smaller scales.

Read [workflow.md](references/workflow.md) before starting. Read
[artifacts.md](references/artifacts.md) whenever the work will span files,
sessions, or agents. Read [content-model.md](references/content-model.md) before
building or recovering a content model. Select exactly one relevant plot
template from `assets/` after the earlier planning artifacts exist; a template
is a prompt for thought, not a form that must be filled completely.

When maintaining or evaluating this skill rather than using it for a document,
read [evaluation.md](references/evaluation.md). Do not load evaluation
expectations into the agent being forward-tested.

Use `document-writing-standards` according to the roles in its lens index.
Planning principles inform the brief, focus, content model, and plot. Editorial
heuristics support judgment during developmental and line editing. Local checks
belong near copyediting. A heuristic observation is not automatically a defect,
and a local finding does not authorize changing the document's argument.

## Choose the route

- **New document:** assignment → discovery → focus → content model → plot →
  draft → developmental edit → line edit → copyedit → reader review when
  required → proof and acceptance.
- **Existing document:** editorial assignment → diagnostic reading → reverse
  outline → editorial diagnosis → content model → revised plot → substantive
  revision → line edit → copyedit → reader review when required → proof and
  acceptance.
- **Settled content and structure:** route wording-only work to
  `document-writing-prose`, detection-only work to `document-writing-audit`, or
  selected findings to `document-writing-apply`.

Combine adjacent planning stages for a short, low-risk document, but do not skip
their decisions. If the document's governing idea or reader progression is not
yet stable, prose editing is premature.

## Gotcha: planning artifacts are not prose

Planning commonly makes writing worse when a section-to-claim table, concept
inventory, or list of proposition-level relations becomes the draft one row at
a time. The result is complete and explicit but makes the reader reconstruct
which details combine into each larger point. Planning has succeeded only when
it shows recursively how lower-level meaning establishes higher-level meaning.
Never expose `first`, `second`, a heading sequence, or repeated definitions in
the document merely because they organized the planning artifact.

## 1. Establish the assignment

Record the audience, their relevant prior knowledge, use situation, intended
reader outcome, reading behavior, document kind, scope, constraints, sources,
and unresolved questions. Distinguish lookup use from passages that must still
be read continuously: an independently referenceable section is not a bag of
independently written sentences. For revision, also record the permitted degree
of intervention and what must be preserved.

Infer ordinary details where one interpretation is strongly supported. Ask only
when alternatives would materially change the document. Mark assumptions as
assumptions; do not silently promote them to facts.

The assignment is usable when a new editor can tell what success means without
recovering intent from conversation history.

## 2. Discover the material

Read the sources and existing draft before imposing an outline. Capture useful
facts, claims, examples, constraints, disagreements, gaps, and provenance.
Separate what the material establishes from what the author wants to argue.

For an existing draft, create a reverse outline of the structure that actually
exists. Recover what each passage establishes, group passages into larger
meaning units, and state how the lower-level units compose each parent. Record
repetition, orphaned material, and missing composition; do not rewrite the
outline into the structure you wish existed.

Stop for a source or scope decision only when the central argument cannot be
supported from the available material. Local uncertainty may remain visible.

## 3. Find the focus

Write a compact statement of:

- the governing question, problem, or reader task;
- the central answer, controlling idea, or intended change in the reader;
- why it matters to this audience;
- the tension, gap, or obstacle that makes the document necessary;
- the boundaries that keep the document from becoming a survey of everything.

This is not final prose. Revise it freely until it distinguishes the document
from a generic treatment of the topic. A familiar surface topic is not
necessarily the focus; identify the question, distinction, or consequence that
actually carries the document.

## 4. Build the content model

Build a recursive model of the meaning the document must establish. Begin with
the focus as the proposed root. Decompose it into lower-level meaning units only
where doing so changes the explanation, argument, narrative, evidence, or
writer's choices. For every developed non-leaf unit, make three things clear:

- what the unit establishes as a whole;
- which lower-level units establish it; and
- how those children combine to produce the parent meaning.

Meaning units may be realized later as a document, part, section, paragraph,
several sentences, one sentence, scene, example, or step. Do not choose their
granularity from the source's existing boundaries or the target's headings.
Branches need not reach the same depth.

Use familiar logical or narrative patterns as a vocabulary for composition, not
as a closed taxonomy or required label. A unit may combine patterns, distinguish
different perspectives, or describe its composition in ordinary prose. The
separate guide lists common patterns and the content-model gate.

Include concepts, facts, claims, evidence, examples, procedures, decisions,
constraints, alternatives, and provenance at the units where they affect the
composition. A concept inventory, claim list, or graph of proposition-level
edges is source material for the model, not a complete model by itself.

Concept treatment remains part of this stage, but serves the relationships.
Rank concepts by argumentative centrality and reader novelty:

- Assume established domain knowledge when the named audience can reasonably
  supply it.
- Develop a central unfamiliar concept from motivating context toward a usable
  definition.
- Introduce a secondary unfamiliar concept briefly at the point of need.
- Avoid naming a minor abstraction when ordinary prose is clearer.
- Explain the particular property the argument depends on, even when the term
  itself is familiar.

Do not proceed until a new writer can explain how the document's major units
build its root meaning without relying on headings or conversation history.

## 5. Make the plot

Choose the template that matches the document:

- [general plot](assets/plot-general.md)
- [book or chapter plot](assets/plot-book.md)
- [technical-document plot](assets/plot-technical.md)
- [academic plot](assets/plot-academic.md)

The content model describes how meaning composes independently of presentation.
The plot linearizes that recursive structure into the experience of this reader.
Choose where the reader enters, the order in which units become available, what
to group or separate, where to slow down or turn, and where physical boundaries
or representations help. Preserve the content model's composition while making
the path natural for the audience and document kind.

A plot may map one meaning unit to several passages or realize several units in
one passage. It does not copy the content model node by node, duplicate all of
its relations, or require every passage to fill the same beat fields. Use entry,
pressure, development, turn, landing, and handoff only where those questions
clarify an important transition.

Choose representations at this stage: prose for connective reasoning, steps for
action, a table for repeated fields or comparison, a diagram for topology or
flow, and code for executable detail. These are judgments, not mandatory
transformations.

Do not equate the plot with a table of contents. Headings and section ownership
may be added after the movement is coherent. A plot made only of headings,
topic lists, concept-placement notes, or one-row section summaries fails the
plot gate even when every required fact appears somewhere.

Test the plot as a whole:

- Does its sequence answer the governing question or enable the reader task?
- Can the reader recover how lower-level units establish each important
  higher-level meaning, rather than merely encounter all component facts?
- Does each movement earn its place and prepare what follows?
- Are central claims supported and limitations visible?
- Does conceptual emphasis match argumentative importance rather than ease of
  definition?
- Does the chosen document kind match the reader's use?

For a continuously read passage, also be able to narrate how the selected path
lets the reader build the root meaning. If the account collapses into a list of
covered claims or repeats the content model without a reader-facing choice,
revise the plot. Resolve plot-level failures upstream. Do not ask a sentence
lens to repair them.

## 6. Draft and edit from large scale to small scale

Draft against the accepted plot while preserving claim status and source
boundaries. For each higher-level meaning unit, write a connected passage in
which the composition of its children becomes intelligible. Do not assign one
sentence or paragraph to each node: content-model boundaries are semantic, not
prose formatting instructions. In revision work, the old draft supplies
material and evidence, not boundaries or shapes that must survive.

After drafting a substantial unit, reconstruct its meaning, children, and
composition from the prose alone. If the prose merely mentions every child, or
if its paragraphs can be reordered without changing the reasoning or narrative,
recompose it before local polishing.

A draft may discover a better focus, relationship, or structure; when it does,
revise the upstream artifact first or alongside the draft so the durable intent
does not become false.

Run these passes in order:

1. **Developmental edit:** argument, coverage, order, section purpose,
   proportion, conceptual emphasis, representation, and fidelity to the
   recursive content model. Reject a draft that covers every planned claim but
   does not let the reader recover how its larger meanings are composed.
2. **Line or stylistic edit:** paragraph movement, continuity, emphasis,
   transitions, sentence shape, voice, and cadence in the target language. Read
   the passage as a whole; do not preserve one-sentence-per-node realization.
3. **Copyedit:** terminology consistency, references, grammar, syntax, notation,
   and house style.
4. **Reader review, when required:** reader comprehension, persuasion, decision,
   and action evidence from `document-reader-review`, followed by author-owned
   decisions through `document-reader-revise`.
5. **Proof and acceptance:** final completeness, formatting, cross-references,
   rendering, and success against the assignment and plot.

Give editorial reviewers the audience, focus, content model, plot, and
relevant sources.
Independence means they do not see one another's findings; it does not mean
withholding the context required for editorial judgment.

Reader personas follow a different contract. Dispatch them only through
`document-reader-review`; never give them the author's intent, focus, plot, or
another persona's output. Reader review returns reactions rather than repairs.
Route substantive reader findings through `document-reader-revise`, then return
explicitly author-approved changes to the earliest editorial artifact they
affect. Delegated writing authority does not let the agent approve a reader
finding on the author's behalf.

Classify every editorial or accepted reader issue by the earliest artifact that
can resolve it, then return it there:

- wrong promise or scope → assignment or focus;
- missing or misconceived substance or relations → discovery or content model;
- wrong progression or emphasis → plot;
- paragraph or sentence realization → line edit;
- local correctness or consistency → copyedit.

After an upstream revision, inspect its downstream dependents before continuing.
Do not mechanically preserve text whose premise changed.

In a durable workflow, a pass that changes a relation, passage movement, section
order, or conceptual emphasis creates a new upstream revision and then a new
draft revision. Do not combine such changes with a line or copyedit and write
them only into the delivery file; that makes the plot unable to govern the
document.

## 7. Accept the document

Acceptance asks whether the document works, not whether every heuristic fired:

- The intended reader can reach the promised understanding, decision, or task.
- Required scope is covered and excluded scope has not leaked in.
- Important claims retain support, qualification, and provenance.
- The reader progression realizes the plot's governing axis.
- A reader can recover the major meaning units and how their children establish
  them at every level developed in the content model.
- Co-ordinate items, dependencies, qualifications, perspectives, and narrative
  changes have not silently become a different composition.
- The document does not read as plot rows, concept entries, or independent
  claims expanded one sentence at a time.
- Conceptual explanation is proportional to novelty and importance.
- Representations serve the relationships they were chosen for.
- Line and copyediting introduced no loss or contradiction.
- When reader review was selected, persona coverage and takeaway divergence are
  reported, and accepted findings have passed back through their owning
  editorial stages.
- The delivered format is complete and usable.

Reader review does not certify external truth. Route systematic claim
verification to a separate external fact-checking workflow.

Revise failures at their owning stage. If resolution requires new authority,
evidence, or a material scope choice, report it instead of hiding it with fluent
prose.

## Delivering the work

Lead with the finished document or its link. Then identify the latest durable
planning artifacts, the editorial passes completed, material deviations from
the plot, and unresolved decisions. Do not claim an independent review unless a
separate context actually performed it.

## Success criteria

- [ ] Audience knowledge and intended use shaped content and terminology.
- [ ] Discovery preceded commitment to a structure.
- [ ] A governing focus and content model existed before the plot.
- [ ] The content model recursively showed how lower-level units establish each
      developed parent meaning.
- [ ] The plot linearized that model for the reader without copying its nodes or
      becoming a table of contents.
- [ ] The draft was composed from movements rather than by expanding planning
      entries one sentence at a time.
- [ ] Developmental decisions preceded line and copy edits.
- [ ] Reader review, when required, remained independent from editorial review
      and left substantive decisions with the author.
- [ ] Lens observations were interpreted in document context and routed to the
      stage that owned the problem.
- [ ] Durable artifacts make the work resumable without chat history.
- [ ] Acceptance was checked against the assignment and plot.
