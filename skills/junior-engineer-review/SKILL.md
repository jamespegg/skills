---
name: junior-engineer-review
description: Sense-check agent-generated code for junior software engineer readability, maintainability, and safe modification. Use when reviewing code, diffs, or implementation plans created by an agent to ensure the result is simple, intuitive, locally understandable, easy to debug, explicit in control flow, appropriately abstracted, and explainable by a reasonably capable new team member without hidden context.
license: Apache-2.0
metadata: 
  author: jamespegg
  version: "0.0.1"
---

# Junior Engineer Review

Use this skill to review whether generated code can be understood, modified, debugged, and explained by a reasonably capable new team member.

Treat the main test as total cognitive load. Good code should feel obvious in its local file, make sense in the wider package structure, and avoid relying on hidden author intent.

## Review Posture

- Prioritize readability, traceability, and safe modification over cleverness.
- Review the code as if the next maintainer has repository context, but not the agent's private reasoning.
- Prefer concrete findings tied to code locations over broad style opinions.
- Avoid blocking on subjective taste unless it materially affects comprehension, debugging, or change safety.
- Preserve useful elegance, but reject niche language features, compressed expressions, and clever flows that make the code harder to explain.

## Review Process

1. Identify the generated or changed code and the behavior it is meant to support.
2. Trace the main execution path from entry point to side effects.
3. Check whether a new team member could explain each step without reading unrelated directories first.
4. Look for places where orchestration, validation, persistence, formatting, or error handling are mixed together.
5. Compare the chosen abstractions and dependencies against the actual problem size.
6. Review tests for behavior documentation and change confidence.
7. Report only issues that meaningfully affect readability, maintainability, debugging, or safe modification.

## Guardrails

- **Naming**: Prefer names that explain intent without comments. Flag vague names, encoded domain assumptions, or names that only describe mechanics.
- **Functions**: Prefer one clear responsibility. Flag functions that mix orchestration, validation, persistence, formatting, and presentation unless the file's scale makes that simpler.
- **Abstractions**: Avoid interfaces, factories, strategies, registries, or generic wrappers unless there are at least two real implementations, a clear testing boundary, or an existing project convention.
- **Files**: Split by domain or concept, not arbitrary technical ceremony. Flag tiny files that force navigation without reducing complexity.
- **Directories**: Prefer intuitive navigation and package-oriented grouping. A reader should not need full tree knowledge to find the relevant code.
- **Control flow**: Prefer straight-line readable flow. Flag clever chaining, overused ternaries, nested callbacks, and deeply nested branches that obscure the path or complicate tests.
- **Error handling**: Keep errors close to the operation that caused them. Flag distant, generic, swallowed, or context-poor errors.
- **Execution traceability**: Prefer explicit flows over implicit magic. Flag hidden callbacks, dynamic dispatch, reflection, global registration, or lifecycle hooks when they obscure what runs.
- **Tests**: Tests should document behavior and useful edge cases, not only implementation mechanics. Flag brittle tests that mirror private structure or miss the important path.
- **Comments**: Comments should explain why something is necessary, not repeat what the code says. Flag comments used to compensate for unclear code.
- **Dependencies**: Avoid libraries for small problems. Flag new dependencies when local code would be simpler, clearer, and lower risk.

## Output

Lead with findings ordered by severity. For each finding, include:

- Location: file and line when available.
- Problem: the cognitive-load or maintainability issue.
- Why it matters: how it affects a new team member's ability to understand, modify, debug, or explain the code.
- Suggested change: a simpler direction, not a large rewrite unless needed.

If the code passes the sense check, say that clearly and note any residual risks or test gaps.

Keep the tone practical and kind. The aim is to make generated code easier for humans to own, not to punish harmless differences in style.
