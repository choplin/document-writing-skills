# document-writing

This family builds documents from the change they should create for a reader.
It establishes a reader-centered root, designs the meanings required to support
that root, verifies them against the available material, and turns them into a
reader-facing plot before drafting or substantive revision. Developmental
editing comes before line editing, copyediting, reader testing when required,
and proof.

Intermediate artifacts can be stored as immutable Markdown revisions with
explicit lineage. There is no mutable state file or separate event log; current
heads and upstream changes are derived from revision files and their digests.

## Choose by task

| Task | Skill | Result |
|---|---|---|
| Create or substantially rebuild a document | `document-writing` | Orchestrated planning, drafting, editorial passes, and acceptance |
| Holistically revise an existing draft | `document-writing-review` | The existing-document route through the governing workflow |
| Write inside an already settled plan | `standards` | Relevant planning, editorial, and language guidance used during composition |
| Improve prose without changing content or structure | `prose` | A connected line edit |
| Inspect stable prose without changing it | `audit` | Local conformance findings only |
| Apply approved local findings | `apply` | Content-preserving edits with stale-anchor and preservation checks |

`base` is internal machinery for the line, copyedit, audit, and apply lanes.

## Workflow

For a new document:

```text
assignment → discovery → reader-centered root → top-down content model
           → bottom-up support check → AI repair → human acceptance
           → plot → AI repair → human acceptance → draft
           → developmental edit → line edit → copyedit
           → reader review when required → proof/acceptance
```

For an existing document:

```text
editorial assignment → diagnostic reading → reverse outline
                     → reader-centered root → new top-down content model
                     → map recovered material → support check → AI repair
                     → human acceptance → revised plot → AI repair
                     → human acceptance
                     → substantive revision → line/copy
                     → reader review when required → proof
```

The reverse outline describes the existing document and supplies material and
diagnosis. The target content model is designed separately from its root, then
checked against that recovered material. Its representation and depth follow
the needs of the document. The plot chooses how the reader encounters the
modeled meanings, including the internal movement of central continuous
passages. Templates are supplied for general documents, books or chapters,
technical documents, and academic work.

## Lens placement

`document-writing-standards` classifies guidance by use:

- planning principles inform focus, concept treatment, document kind,
  representation, argument, and plot;
- editorial heuristics support contextual judgment during developmental and
  line editing;
- conformance checks detect local correctness and consistency defects after the
  larger decisions are stable.

Only the third category flows directly through `audit` and `apply`. Editorial
reviewers receive the relevant audience and plot context; “blind” means
independent of other editorial reviewers' conclusions, not deprived of document
intent.

## Reader-side acceptance

The bundled `document-reader` system tests a different boundary after a complete
draft is editorially stable. Its personas report what intended readers
understood, rejected, or would act on without seeing the author's intent or the
editorial plot. `document-reader-review` returns findings only;
`document-reader-revise` puts every substantive response to the author before
changing the document.

Use reader review when comprehension, persuasion, decision quality, or ability
to act is material to acceptance. If accepted findings change substance or
structure, return to the earliest affected editorial stage and repeat downstream
passes. Do not interpret a clean reader review as factual verification; that is
a separate external workflow.

## Durable artifacts

For multi-session work, store artifacts beside the target in a
`<document>.writing/` directory unless the project defines another location.
Each artifact revision records its kind, revision number, predecessor, and the
paths and SHA-256 digests of upstream artifacts. Revisions are immutable. A
changed upstream digest triggers downstream review and a new revision, not a
central status mutation.

AI self-review and inline repair happen while a planning candidate is still
being made. Only a complete content model or plot that is ready for the human
author receives a revision number. The human reads that exact revision before
the dependent phase begins. Acceptance without changes keeps the same revision;
author-requested changes receive the next number only after another internal
review-and-repair cycle.

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

## Skills

| Skill | Responsibility |
|---|---|
| `document-writing` | Orchestrator for new documents and substantial revisions |
| `standards` | Planning principles, editorial heuristics, local checks, and Japanese/English profiles |
| `base` | Shared context-aware line/copy/audit/apply machinery |
| `review` | Entry adapter selecting the existing-document route |
| `prose` | Content-preserving line edit |
| `audit` | Local conformance findings without edits |
| `apply` | Application of selected local findings |

The reader-review skills are documented in
[`../document-reader/README.md`](../document-reader/README.md).
