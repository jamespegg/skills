# Skills

Reusable engineering skills for James's personal projects.

| Skill | Purpose |
| --- | --- |
| [Junior Engineer Review](skills/junior-engineer-review/SKILL.md) | Check AI-generated code for human readability and maintainability. |
| [Tech Preferences](skills/tech-preferences/SKILL.md) | Choose preferred technology, explore alternatives deliberately and avoid excluded tools. |
| [Engineering Principles](skills/engineering-principles/SKILL.md) | Design code for local reasoning and simple operations. |
| [Verifiable Trust](skills/verifiable-trust/SKILL.md) | Independently verify AI work and bound autonomy. |
| [Setup James Skills](skills/setup-james-skills/SKILL.md) | Reconcile three guidance skill references in a repository's root `AGENTS.md`. |

For workflow selection and execution, use Matt Pocock's [`ask-matt`](https://github.com/mattpocock/skills/tree/main/skills/engineering/ask-matt) and related engineering skills. Navigator is retired; these skills contain James's own technical guidance.

Install skills using the agent's normal skill installer. Invoke `setup-james-skills` per repository to reconcile the root `AGENTS.md`. References are for discovery; they do not themselves install or guarantee loading the full skills.

## Releasing skills

Use **Actions → Release → Run workflow** on `main`, then choose **major**, **minor**, or **patch**. This is a manual, stable-only release; there is no automatic bump or release-candidate mode.

**First run:** choose **major** to initialise the repository at `v2.0.0`. The workflow updates every `skills/*/SKILL.md` metadata version to `2.0.0`. Later runs increment the latest strict `vMAJOR.MINOR.PATCH` tag (for example, `v2.0.0` → `v2.0.1` for patch). All skills always share the same version.

The workflow validates the skill metadata, runs packaging tests, creates one ZIP per skill (including its agent metadata and any future supporting files), commits the version changes to `main`, tags the versioned commit, and attaches all ZIPs to a GitHub Release with generated notes. The `SKILL.md` file is at the **root** of each ZIP, ready for direct upload.

It prepares and validates packages **before** pushing a commit or tag. If the GitHub Release upload fails after the versioned commit and tag have been pushed, rerun the workflow from `main` to retry publishing that tag rather than accidentally incrementing the version again. The workflow requires `contents: write` permission and a branch policy permitting the Actions bot to push the release commit.
