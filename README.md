# document-writing-skills

Portable [Agent Skills](https://agentskills.io) for planning, drafting, editing,
and reader-testing substantial documents.

The repository is one installation unit. It contains the editorial workflow and
the reader-side review system that tests whether a complete draft works on its
intended audience.

## Workflow boundary

```text
assignment → discovery → focus → content model → plot → draft
           → developmental edit → line edit → copyedit
           → reader review when required → author-owned revision
           → proof and acceptance
```

The review systems answer different questions:

| System | Question | Authority |
|---|---|---|
| `document-writing-review` | Does the document's substance, structure, and prose hold together? | May diagnose and revise within the editorial assignment |
| `document-reader-review` | What happens when an intended reader encounters the complete draft? | Reports reactions and takeaway divergence; never proposes edits |
| `document-reader-revise` | What should reader findings change? | Puts substantive decisions to the author, then applies only those decisions |
| External fact-checking | Are the document's claims true against authoritative sources? | Separate workflow; no fact-checking skill is required by this repository |

A reader review is not a second copyedit and never certifies factual accuracy.
If it triggers substantive revision, return the document to the earliest owning
editorial stage before proof and acceptance.

## Install

Works with Claude Code, Codex, Cursor, Kimi, and other clients supported by the
[`skills`](https://github.com/vercel-labs/skills) CLI:

```bash
skills add choplin/document-writing-skills --list
skills add choplin/document-writing-skills --skill '*'
```

Install the complete repository. Skills delegate to one another by name, while
the Agent Skills standard does not resolve dependencies between individually
selected skills.

For a local checkout:

```bash
skills add ./skills --skill '*' -a claude-code codex -g -y
```

## Structure

```text
skills/
  document-writing/   editorial workflow, standards, plots, and durable artifacts
  document-reader/    persona-based reader review and author-led revision
scripts/
  validate-skills.sh  strict validation for every skill
```

See [the editorial workflow](skills/document-writing/README.md) and
[the reader review system](skills/document-reader/README.md) for the individual
skills and their operating contracts.

## Validate

Install [`skill-validator`](https://github.com/agent-ecosystem/skill-validator)
and run:

```bash
scripts/validate-skills.sh
git diff --check
```

Strict validation covers frontmatter, skill structure, referenced files, and
internal links. Lefthook runs the relevant skill validation before commits, and
GitHub Actions runs the complete validation suite on pushes and pull requests.

The Nix development shell supplies lefthook:

```bash
nix develop
lefthook install
```

## Skill groups

### Editorial workflow

`document-writing`, `document-writing-standards`, `document-writing-base`,
`document-writing-review`, `document-writing-prose`, `document-writing-audit`,
and `document-writing-apply`.

### Reader review

`document-reader-review`, `document-reader-base`,
`document-reader-newcomer`, `document-reader-skeptical-peer`,
`document-reader-implementer`, `document-reader-decision-maker`,
`document-reader-domain-expert`, and `document-reader-revise`.

## License

MIT. See [LICENSE](./LICENSE).
