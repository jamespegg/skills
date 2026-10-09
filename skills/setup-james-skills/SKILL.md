---
name: setup-james-skills
description: Create or reconcile a repository's root AGENTS.md references to the tech-preferences, engineering-principles and verifiable-trust skills. Use when asked to set up, refresh or validate James's personal engineering guidance; preserve existing instructions and make repeat runs idempotent.
license: Apache-2.0
metadata:
  author: jamespegg
  version: "1.0.0"
---

# Setup James Skills

Reconcile **only the current repository's root `AGENTS.md`** so coding agents can discover:

- `tech-preferences` — preferred, experimental and avoided technologies;
- `engineering-principles` — design for local reasoning;
- `verifiable-trust` — independent verification and bounded AI autonomy.

This is a **mutating setup skill**. Explicit invocation authorises a bounded `AGENTS.md` change, not cross-repo changes, skill installation, or unrelated refactoring.

## Reconciliation procedure

1. Determine the repository root and read `AGENTS.md` if it exists. Inspect existing references and documented project exceptions; preserve repository-specific instructions and unrelated content.
2. Check whether all three skills are installed/discoverable in the current agent environment. Report missing skills; **do not claim installation or install silently**. References may still be written to assist future setup.
3. Find the exact marker pair `<!-- james-skills:start -->` and `<!-- james-skills:end -->`. If both appear *exactly once* in the right order, replace **only the contents of that managed block** with the canonical block below if needed. If markers are incomplete, duplicated or malformed, preserve the file and report the ambiguity rather than guessing.
4. If no managed block exists, find any equivalent existing personal-guidance section. Update that section in place where this is unambiguous to avoid duplication. Otherwise append the canonical block separated by blank lines; create root `AGENTS.md` if absent.
5. Keep all unrelated instructions untouched; avoid whole-file reformatting. Follow repository line-ending conventions and ensure a final newline.
6. Re-read and diff the result. Confirm exactly one managed block and each of the three skill references once **within the block**. Re-running must make no changes. Report whether created/updated/already correct, and any unavailable skills.

## Canonical managed block

Copy the following exact block, including markers:

```markdown
<!-- james-skills:start -->
## Personal engineering guidance

Apply these skills when relevant, without turning every small change into ceremony:

- **`tech-preferences`** — Prefer James's established stack and exclusions when selecting technology or considering migrations.
- **`engineering-principles`** — Optimise for local reasoning through cohesive capabilities, clear names and explicit dependencies.
- **`verifiable-trust`** — Independently verify AI work and bound permissions, time, data, money and irreversible actions.

Documented project decisions take precedence over generic defaults. Flag meaningful deviations early, recommend an approach and ask before changing established technology. When James chooses to retain a deviation, record the decision and don't reopen it without a request or material new evidence.

Use installed skill content when available; these references are not the full guidance. If a skill is missing, report that rather than pretending it was applied. Source: [jamespegg/skills](https://github.com/jamespegg/skills).
<!-- james-skills:end -->
```

## Boundaries

- Keep references concise; don't copy skill bodies into `AGENTS.md`. The skills repository is authoritative for their content.
- Preserve project policies, existing decisions, nested `AGENTS.md` files, application code, workflows and dependencies.
- Modify only the repository explicitly in scope. Don't overwrite a documented choice to exclude these references without discussing the conflict.
- A mention in `AGENTS.md` does not itself install, load or guarantee invocation of a skill. Be transparent if the agent environment lacks skill discovery.
