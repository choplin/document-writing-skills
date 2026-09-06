# Repository instructions

- Keep all skills portable and agent-agnostic. Do not add runtime-specific
  hooks or hidden state as a dependency of a skill.
- Treat this repository as one installation unit: editorial and reader-review
  skills may delegate to one another by their declared skill names.
- Keep editorial review, persona-based reader review, and external fact-checking
  as separate responsibilities.
- Write skill instructions and documentation in English.
- Preserve durable workflow state through immutable revision artifacts and
  `based_on` digests. Do not introduce a mutable state file or event log.
- Run `scripts/validate-skills.sh` and `git diff --check` before committing skill
  changes.
