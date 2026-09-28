# document-writing

This family turns an author's intended meaning into a document whose readers can
recover and use that meaning. It collaborates with the author near the root,
expands the lower meaning tree autonomously, gives one composition owner the
reader-facing plot and complete draft, and verifies the result by reconstructing
meaning from the finished prose.

Intermediate artifacts use immutable Markdown revisions with explicit lineage
when work spans sessions or agents. There is no mutable workflow state or event
log; current heads and upstream changes are derived from revision files and
their digests.

## Choose by task

| Task | Skill | Result |
|---|---|---|
| Create or substantially rebuild a document | `document-writing` | Shared semantic spine, complete draft, semantic round trip, editorial finish, and acceptance |
| Holistically revise an existing draft | `document-writing-review` | Existing-draft diagnosis followed by the governing workflow |
| Consult writing guidance or evaluate prose | `document-writing-standards` | Relevant planning, editorial, and language guidance |
| Improve prose without changing settled meaning or structure | `document-writing-prose` | A connected line edit |
| Inspect stable prose without changing it | `document-writing-audit` | Local conformance findings only |
| Apply approved local findings | `document-writing-apply` | Content-preserving edits with stale-anchor and preservation checks |

`document-writing-base` is internal machinery selected by the prose, audit, and
apply entry points. `document-writing-standards` loads only the material relevant
to the current language, editorial stage, and lenses.

## Workflow

For a new document:

```text
assignment and sources
  → collaborate on reader-valued root and semantic spine
  → agent expands and verifies the meaning tree
  → one owner plots the reader path, composes, and developmentally edits
  → fresh reviewer reconstructs meaning from the draft alone
  → compare and revise
  → factual/domain verification and holistic prose edit
  → deterministic local audit
  → reader review when required
  → final reconstruction and comparison
  → proof and acceptance
```

For an existing document:

```text
editorial assignment
  → reader-side diagnosis and reverse outline of the old draft
  → collaborate on a new reader-valued root and semantic spine
  → design the target meaning tree independently of old headings
  → map useful material into the target tree
  → plot, compose, reconstruct, compare, verify, edit, and accept
```

The author and agent collaborate only through the depth needed to constrain the
document's governing meaning. The author is asked about root-level,
high-impact, uncertain, or author-owned semantic choices, not to approve every
lower branch, outline revision, or prose plan.

Mutual agreement on the governing meaning is the workflow's primary acceptance
boundary. Before composition, the agent articulates its understanding of the
meaning tree from the root through the depth needed to constrain the document;
the author explicitly confirms or corrects it. The conversation may take any
natural form and does not require node-by-node approval, but drafting, review,
artifacts, or lens conformance cannot substitute for this two-way confirmation.
Afterward, lower-tree expansion and prose work proceed autonomously unless a
confirmed meaning must change.

The meaning tree governs what the document establishes and how its meanings
compose. The plot maps that logic into the reader's entry, order, grouping,
pace, emphasis, representations, passage movement, and ending. One composition
owner makes the plot and prose decisions while preserving the shared semantic
spine. Writing may expose and repair source-determined defects in lower
branches; a change to an author-owned meaning returns to the author.

## Semantic round trip

A fresh reviewer receives the complete draft and reader context without the
intended tree or author intent. The reviewer reconstructs the root, major
supporting meanings, central section propositions, important paragraph roles,
examples, qualifications, and unresolved questions.

The workflow compares that recovered tree with the intended tree. It revises
omitted or invented claims, changed strength, lost conditions, misplaced
support, ambiguous relations, misleading examples, and an unrecoverable entry.
This tests what the document communicates. External truth remains the
responsibility of source verification or a separate fact-checking workflow.

## Lens placement

`document-writing-standards` preserves local writing guidance without turning
the document into a sequence of independent lens outputs:

- planning guidance shapes the semantic spine, lower meaning tree, and plot;
- editorial guidance is used by the composition owner across connected
  passages and the complete document; and
- deterministic checks run only after meaning and structure are stable.

A clean local audit is necessary when applicable, but never sufficient evidence
that the document works as a whole.

## Reader-side acceptance

`document-reader-review` tests the intended-reader boundary after the draft is
editorially stable. Its personas receive the finished document and their reader
context, not the author's intent or meaning tree. `document-reader-revise`
returns substantive decisions to the author before changing the document.

Reader review, editorial review, and external fact-checking remain separate
responsibilities. If an accepted finding changes meaning or structure, repeat
the affected tree comparison and downstream checks.

## References

### Editorial workflow

- [Editors Canada: Professional Editorial Standards](https://editors.ca/publications/professional-editorial-standards/) and [The Fundamentals of Editing](https://editors.ca/publications/professional-editorial-standards/fundamentals-editing/)
- [CIEP: About proofreading and editing](https://www.ciep.uk/resource/about-proofreading-and-editing.html), [Editorial glossary](https://www.ciep.uk/resource/editorial-glossary.html), [The publishing workflow](https://www.ciep.uk/learn-and-develop/the-ciep-competency-framework/the-publishing-workflow.html), and [What is an editorial brief?](https://www.ciep.uk/resource/what-is-an-editorial-brief-and-how-does-it-help-both-authors-and-editorial-professionals.html)
- [Purdue OWL: Genre analysis and reverse outlining](https://owl.purdue.edu/owl/graduate_writing/introduction_to_writing/documents/drafting-your-document/handouts/genre-analysis-activity.pdf)

### Technical writing

- Google Technical Writing on [audience](https://developers.google.com/tech-writing/one/audience), [document scope and organization](https://developers.google.com/tech-writing/one/documents), and [large-document outlines](https://developers.google.com/tech-writing/two/large-docs)
- [Diátaxis](https://diataxis.fr/start-here/) and its [workflow guidance](https://www.diataxis.fr/how-to-use-diataxis/)

### Academic writing

- [ICMJE: Preparing a Manuscript for Submission](https://icmje.org/recommendations/browse/manuscript-preparation/preparing-for-submission.html)
- [EQUATOR Network](https://www.equator-network.org/)
- [Taylor & Francis: Writing your paper](https://authorservices.taylorandfrancis.com/wp-content/uploads/2021/03/Writing_your_paper_ebook.pdf)

### Original lens sources

- [`japanese-tech-writing`](https://gist.github.com/k16shikano/fd287c3133457c4fd8f5601d34aa817d): Japanese technical prose, argument, reader load, voice, and notation
- [`cognitive-rhythm-writing`](https://gist.github.com/k16shikano/eb2929f13ed19c97188393d297be8432): cognitive pacing and Japanese cadence
- [`writing-clearly-and-concisely`](https://github.com/obra/the-elements-of-style/tree/05fc4f0d2b97b7c042dd9949ad658568e4a1324e/skills/writing-clearly-and-concisely): English mechanics, composition, and concision

## Durable artifacts

For multi-session work, first use a location selected by the user or project.
Otherwise prefer an existing ignored repository work area such as
`.agents/document-writing/<document-relative-path>.writing/`, then the user's
persistent platform state area. Do not place artifacts beside a
version-controlled document unless that location was explicitly selected.

Useful artifact kinds include `brief`, `discovery`, `reverse-outline`,
`semantic-spine`, `meaning-tree`, `plot`, `draft`, `reconstruction`, `comparison`, and
`acceptance`. Revisions are immutable and record upstream paths and SHA-256
digests. Artifact publication records a durable candidate; it does not imply
human approval or qualitative success.

## Skills

| Skill | Responsibility |
|---|---|
| `document-writing` | End-to-end workflow for new documents and substantial revisions |
| `document-writing-review` | Entry point for the existing-document route |
| `document-writing-prose` | Content-preserving connected line edit |
| `document-writing-audit` | Local conformance findings without edits |
| `document-writing-apply` | Application of selected local findings |
| `document-writing-base` | Internal context-aware line/copy/audit/apply machinery |
| `document-writing-standards` | Planning principles, editorial heuristics, local checks, and language profiles |

The reader-review skills are documented in
[`../document-reader/README.md`](../document-reader/README.md).
