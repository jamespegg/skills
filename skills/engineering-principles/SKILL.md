---
name: engineering-principles
description: Use when designing, implementing, refactoring or reviewing architecture and code. Optimise for local reasoning, discoverable capability-based structure, cohesive packages, explicit dependencies and simple operations, with proportionate rigour.
license: Apache-2.0
metadata:
  author: jamespegg
  version: "1.1.0"
---

# Architecture and Engineering Principles

> **Optimise for local reasoning.** A developer should be able to find, understand, change and verify a capability by examining a small, obvious part of the codebase, without navigating layers of indirection or hidden dependencies.

Language-independent defaults for small projects maintained by one person and future coding agents. Prefer the simplest **coherent** design meeting actual requirements. Apply rigour proportionately, never mechanically. See `tech-preferences` for what to build with, and `verifiable-trust` for AI risk and permission boundaries.

## Justify complexity before implementing it

- **Challenge the requirement, not only the code.** Before adding a component, behaviour, dependency or defensive mechanism, identify the concrete need and the simplest end-to-end outcome. Deleting an unnecessary requirement is often better than implementing it elegantly.
- **Distinguish evidence from hypotheticals.** Defend against credible failures according to their likelihood, consequence and recoverability; do not build elaborate machinery for speculative scenarios. Preserve strong safeguards for credentials, permissions and irreversible persistent-state changes.
- **Make complexity earn its keep.** Each new concept, validation, layer, configuration option or test should reduce a real risk or enable a real capability. Reuse the platform or an existing installer where it removes work, rather than rebuilding its responsibilities.
- **Prefer a small complete solution.** Avoid temporary compatibility code in inactive replacements when the cutover will remove it, unless a real consumer or migration step needs it. Do not solve duplication by introducing a framework that is harder to navigate than the duplicated code.
- **Revisit the finished design.** After behaviour works, check whether responsibilities, branches or dependencies can disappear without weakening essential behaviour. Optimise for fewer concepts and faster comprehension, not minimum lines or arbitrary limits.

## Structure and navigation

- **Organise by capability, not architectural layer.** Packages and directories describe what software does, not generic labels such as `ports`, `adapters`, `models` or `services`, unless an architectural term truly is the clearest domain-specific name.
- **Make names and navigation obvious.** Meaningful package, file, type and function names should let a contributor predict where code belongs.
- **Prefer fewer cohesive packages.** Keep related responsibilities together; use descriptive separate files *within a package* before creating new package boundaries.
- **High cohesion, loose coupling.** Code that changes for the same reason usually belongs together; unrelated capabilities have minimal explicit dependencies.
- **Keep structure shallow.** No nesting, fragmentation or extra layers without a real boundary.
- **Avoid dumping grounds.** No catch-all `utils`, `common`, `helpers` or `misc`. Assign behaviour a clear owner.
- **Separation of concerns does not require separation into packages.** Package count and file size are not goals.

## Implementation and dependencies

- **Design APIs for consumers.** Expose small predictable operations; hide implementation detail consumers needn't understand.
- **Prefer concrete dependencies.** Use direct calls unless a meaningful boundary, substitutable implementation or test requirement justifies an interface. Don't create interfaces by habit.
- **Make effects explicit.** No hidden mutable global state, surprising side effects or magic wiring.
- **Clarity over cleverness or speculative reuse.** A little duplication can be preferable to a shared abstraction coupling unrelated features. Don't build imaginary extension points.
- **Handle errors deliberately.** Fail clearly, retain useful context, clean up resources and explain recovery behaviour.
- **Use concurrency only when worth its complexity.** Start sequential; if warranted, make ownership, cancellation, timeouts and shutdown comprehensible.
- **Keep deployable service boundaries coherent.** A service owns an obvious capability with explicit contracts across services; independent deployment does not require excessive internal layering.

## Configuration, runtime and operations

- **Separate code from deployment settings.** Externalise secrets and environment-dependent values. Prefer reviewable version-controlled structured configuration for application policy when appropriate. Never embed credentials.
- **Reproducible builds and releases.** Declare/pin dependencies, build once, promote immutable identifiable artefacts.
- **Replaceable processes, intentional durable state.** Predictable startup, graceful shutdown, recovery. Distinguish temporary process state from durable user data, identity and repositories.
- **Meaningfully consistent environments.** Comparable paths/dependencies in development, CI and deployment; explicit differences.
- **Observable and operable.** Useful errors, structured logs, health checks and documented repeatable validation/recovery commands over manual ritual.

## Verification and evolution

- **Test observable behaviour, not incidental implementation.** Prefer test-first red → green vertical slices at agreed public seams for behaviour changes; exercise important success, failure and recovery paths with independently grounded expectations. Don't write brittle implementation-coupled or tautological tests just to satisfy a process. Static checks must enforce real invariants.
- **Small complete changes.** Solve the problem without unrelated refactoring, hypothetical infrastructure or abandoned compatibility layers. Preserve contracts unless deliberately changing them.
- **Durable discoverable decisions.** Document non-obvious constraints, rationale and operations where maintainers will look, not only in chat. Avoid verbose or duplicated instructions.
- **Make the codebase teach its own architecture.** Clear layout, contracts and executable conventions should reduce agent instruction needs. If agents repeatedly fail, improve structure, documentation or checks before adding standing rules.
- **Self-explanatory over instruction-dependent systems.** Documentation should preserve intent and non-obvious choices, not compensate for confusing code.
- **Proportionate rigour.** Fast reversible learning for experiments; stronger security, observability, verification and recovery for production or consequential changes.

## Quick design check

Before adding a package, dependency, abstraction or process, consider:

1. Is the underlying requirement necessary, and what is the smallest outcome that solves it?
2. Where would someone naturally look for this capability, and can it be understood locally?
3. Does this boundary correspond to a real responsibility or reason to change?
4. Does this complexity address an evidenced need or consequential risk more simply than the direct approach?
5. Can important behaviour and failures be verified, and any consequential change recovered?

This is a lightweight decision aid, **not a mandatory checklist for every edit**. When a convention harms navigation, name the trade-off and choose the simpler design.

## Influences, not mandatory frameworks

- [Effective Go](https://go.dev/doc/effective_go), [Go Code Review Comments](https://go.dev/wiki/CodeReviewComments), [Go Proverbs](https://go-proverbs.github.io/): expressive names, small consumer-oriented interfaces, explicit errors and avoiding needless abstraction.
- [The Twelve-Factor App](https://12factor.net/): clean configuration, repeatable builds, environment consistency, disposable processes and operational visibility.

These inspirations do **not** mandate Go, environment variables for every setting, or statelessness where durable state is intentional.
