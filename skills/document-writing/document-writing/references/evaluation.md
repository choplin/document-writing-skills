# Workflow evaluation

Use these cases when changing the workflow or the role of a lens. They preserve
observed failure modes outside the ordinary writing context.

## Revision policy

Treat every workflow revision as a restructuring step until the basic flow has
worked across the coverage cases below. Re-derive one coherent current workflow
from the new evidence, then replace or remove instructions whose model of the
work no longer fits. An additive correction is appropriate only after the basic
flow is established and the new behavior is genuinely local.

Runtime instructions describe the current desired behavior in positive terms.
Keep historical alternatives, superseded behavior, failure descriptions, and
regression-specific prohibitions in this evaluation reference. Compatibility
with earlier skill behavior or artifact semantics is outside the design goal.

Review each candidate revision for both kinds of accumulation: extra rules that
leave an obsolete flow intact, and extra fields that reduce an agent's useful
freedom. Prefer fewer governing principles whose outcomes can be observed in
the artifacts and final document.

## Method

Give a fresh writing agent the task, source material, audience and use
information, and the installed skill. Keep this file and reference outputs out
of that agent's context. Inspect the intermediate artifacts and final document.
Use separate fresh contexts for handoff checks and blind comparisons.

A run passes when the observable work shows that it:

- establishes a root connecting a reader-recognizable situation or problem,
  the document's answer or method, and its value or consequence;
- derives the target content model downward from that root;
- uses an existing draft's reverse outline as diagnosis and material rather
  than as the topology of the target model;
- verifies the proposed model upward from evidence and claim status;
- chooses different depths and forms according to local explanatory need;
- develops a branch below the section level when the diagnosed reader problem
  occurs inside a section;
- gives both the whole document and its central continuous passages a coherent
  reader movement;
- leaves the writer free to combine several meanings in a passage or develop
  one meaning across several passages;
- records a fresh writer's content-model explanation and passage sketch before
  the plot phase;
- repairs content-model and plot findings inline before publishing one complete
  candidate for human inspection;
- waits for human acceptance of each published content-model and plot revision
  before starting its dependent phase;
- produces prose whose larger meanings and movement can be reconstructed by a
  fresh reader;
- preserves source boundaries, qualifications, provenance, and author-owned
  decisions; and
- preserves enough durable artifacts for a fresh context to resume the work.

When a direct no-skill revision is available, compare final documents blindly.
The workflow output should be at least as coherent and readable while delivering
its intended reader outcome.

## Existing-draft direction case

Supply a draft whose headings and section order are plausible but whose central
argument requires a different hierarchy. The reverse outline should accurately
describe the old draft. The target model should begin from a reader-centered
root, derive the meanings required by that root, and only then map old material
into the new structure. Fail the run when the target tree can be obtained mainly
by renaming, regrouping, or reordering the old sections.

## Depth case

Supply a draft whose document-level topic and section order are sound but whose
reader failure occurs within one important section. The reverse outline,
content model, and plot should follow that branch below the section level and
guide a new internal movement. Fail the run when those artifacts stop at section
summaries.

## Freedom and continuity case

Supply material containing a connected explanation that needs both a broad
movement and several supporting relationships. The content model may use any
form and uneven depth. Give it to a fresh writer with the assignment and source
material. Pass when the writer can create a coherent passage with natural
paragraphing. Fail when the artifact prescribes a uniform record shape, drives
one sentence or paragraph per entry, or yields prose that reads as fragments
joined in sequence.

## Composition handoff case

Give a fresh writer only the assignment, focus, content model, and relevant
source material. Ask them to explain why the children of one central branch
establish its parent and sketch the movement of that passage. Topic labels,
presentation labels, order alone, or a named relation without the participating
meanings fail this case.

## Root-value case

Supply technically complete material whose source organization begins from the
system rather than the reader. Pass when the model roots the document in a
problem, task, question, or situation the intended reader recognizes and makes
the value of the answer or method intelligible. The final presentation may
reveal that connection gradually when the genre calls for it.

## Plot-family coverage

Maintain at least one forward test for each family:

- **Book or chapter:** the work-level promise governs chapter and passage arcs.
- **Technical document:** reader use determines the document kind and the
  movement of a central continuous passage.
- **Academic document:** the research situation leads to a contribution whose
  claims, evidence, warrants, and qualifications remain reconstructable.
- **Existing draft:** diagnosis of the old document and design of the target
  document remain distinct artifacts and directions of work.

## Editorial-boundary case

Supply a developmental problem that is visible in one sentence but owned by the
focus, content model, or plot. Pass when it returns to that stage and the
downstream artifacts are reconsidered. Conformance checks should remain local
to correctness and consistency after substance and structure stabilize.

## Lineage case

Create two revisions of an upstream focus or content-model artifact. A plot
based on the first revision needs a new reviewed revision after the upstream
change, even when its body remains suitable. Derive this from immutable
revision artifacts and `based_on` digests.

## Planning-publication gate case

Supply a content-model candidate and a plot candidate with defects that an
independent AI review can identify. Pass when the agent repairs each candidate
inline, publishes only the internally complete result as a numbered revision,
and pauses for the human author to read it before beginning the dependent phase.
Human acceptance without changes must not create a duplicate revision. If the
human requests a change, the replacement receives the next number only after
its own internal review and repair. Fail when AI review iterations become
numbered artifacts, unresolved AI findings are handed to the human, or plotting
or drafting starts before the corresponding human acceptance.

## Reader-review boundary case

Give a fresh agent a complete proposal whose acceptance depends on a decision
maker and a skeptical peer. Pass when the stable document goes to both personas
without author intent or editorial planning, their reactions remain intact, and
substantive responses return through author decision and the affected editorial
stages. Reader review provides reader evidence rather than factual certification.
