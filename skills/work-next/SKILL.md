---
name: work-next
description: Orient the user to the next unit of work in repositories that use a canonical parent GitHub issue with linked execution-sized child issues. Use when asked "what's next?", "what should I work on?", for progress/status orientation, or when deciding which planned issue should be picked up next. Read the repository's work-tracking guidance and canonical parent issue, inspect linked child issues and relevant open PRs, respect dependencies and stop conditions, and report progress plus the single next actionable child. Do not modify code, issues, PRs, or planning state unless separately asked.
license: Apache-2.0
metadata:
  author: jamespegg
  version: "0.0.1"
---

# Work Next

Use this skill for orientation in repositories that track delivery through a canonical parent GitHub issue and linked execution-sized children.

The parent issue owns the plan and high-level status. Child issues own executable scope. Repository documents own durable technical context, constraints and acceptance criteria. Do not recreate a second status ledger in Markdown or chat.

## Process

1. Identify the current repository and read its local agent guidance only far enough to find the work-tracking section and canonical parent issue.
2. Fetch the canonical parent issue with GitHub CLI. Read its objective, working model, linked-child section, dependencies and any explicit replanning gate.
3. Fetch the linked child issues needed to establish their current states. Do not assume a checkbox or copied title is current when the issue state disagrees.
4. Check relevant open pull requests when needed to distinguish an unstarted child from work already in flight. Prefer explicit issue/PR links or closing references over branch-name guesses.
5. Select the single next actionable child:
   - finish an already in-flight child before starting another, unless the parent explicitly permits independent parallel work;
   - otherwise choose an open child whose explicit dependencies are satisfied;
   - respect the order and stop conditions recorded by the parent;
   - never jump to a later high-level milestone that has not been decomposed into an execution-sized child.
6. If no executable child exists but the parent still has unfinished high-level work, report that the next action is planning/decomposition rather than implementation.
7. If repository guidance, parent status, child state, PR state or recent Git history conflict materially, call out the conflict instead of guessing.

## GitHub lookup

Prefer the authenticated `gh` CLI. Typical reads are:

```sh
gh issue view <parent> --json number,title,state,body,url
gh issue view <child> --json number,title,state,body,url
gh pr list --state open --json number,title,body,url,headRefName,baseRefName
```

Use narrower queries when the repository has many children or PRs. Read comments only when the issue body or PR linkage is insufficient.

This skill is read-only. Do not update issue bodies, close issues, create branches, start implementation, or change the repository merely because the user asked for orientation.

## Output

Respond briefly with three bullets:

- **Progress:** what has completed, what is currently in flight, and any material blocker or stale-plan conflict.
- **Next:** the single next actionable child issue, including its issue number, concrete deliverable and blocking dependency if any.
- **Reasoning:** the repository's suggested reasoning level/model-effort guidance when it is explicitly recorded; otherwise omit model-setting claims rather than inventing them.

Aim for roughly 100–150 words unless the user asks for detail. Link the relevant parent/child issue instead of repeating the full plan.

Treat "what's next?" as a request for orientation, not authorisation to execute the work.
