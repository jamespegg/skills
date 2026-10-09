---
name: tech-preferences
description: Apply James's technology choices and exclusions when selecting stacks, building software, adding dependencies, reviewing architecture or considering migrations. Flag meaningful deviations early, ask before unfamiliar technology, and respect recorded decisions.
license: Apache-2.0
metadata:
  author: jamespegg
  version: "1.0.0"
---

# Tech Preferences

Use these defaults for James's personal software projects. This skill is about **what to build with**; `engineering-principles` is about how to design it, and `verifiable-trust` concerns AI verification and execution risks.

## How to apply

1. First inspect repository state, relevant `AGENTS.md` instructions and documented decisions. Existing technology is evidence, not automatically a permanent architectural decision.
2. For new work, follow the defaults below. In existing projects, **flag meaningful deviations early** and recommend alignment where useful; explain trade-offs and ask before migrating. Never make a migration incidentally.
3. If James chooses to retain a deviation, record that decision and its rationale in the appropriate repository documentation. Don't reopen it unless requested or materially new evidence warrants reconsideration.
4. Proactively suggest modern alternatives when they offer meaningful improvement or a learning opportunity, clearly distinguishing proven from experimental technology and explaining risk, operational cost and reversibility. **Ask before introducing any unfamiliar technology.** Avoid short-lived fads.
5. "Explore" means interest, **not** approval to adopt. Recorded project decisions and explicit exclusions take precedence over generic preferences. Prefer reusing existing conventions and infrastructure.

## Languages and frontend

| Classification | Guidance |
| --- | --- |
| **Prefer** | Go for new backends, CLIs and developer tools. Go standard library first; small focused libraries when useful. |
| **Prefer** | React + TypeScript + Vite for frontends, npm as package manager, ESLint and Prettier. Zustand for shared state. |
| **Accept** | Tailwind CSS; choose component, routing, query, form and validation libraries case by case. No mandated design system. |
| **Strongly avoid** | Next.js unless there is an exceptionally strong, concrete reason over React + Vite. Ask before introducing. |
| **Avoid** | Redux, Java, C#/.NET, PHP and heavyweight enterprise frameworks unless explicitly required. |
| **Scripting** | Just as task runner. Only tiny development glue in Bash; no substantial Bash scripts. Go for reusable tools. Python mainly for machine learning, not general scripting. |
| **Explore** | Microfrontends and Module Federation, not defaults. |
| **Quality** | Responsive and accessible UI, proportional to project maturity. |

## Applications, interfaces and data

- **Repository and deployment structure:** One monorepo per side project, product or self-contained concept. Prefer distinct backend domains as small **independently deployed microservices**, even on small projects. Do not combine frontend and backend into one monolithic application. Independently deployed does *not* imply separate repositories or infrastructure stacks.
- **APIs:** gRPC + Protobuf by default, with REST/JSON gateway for browser or external clients. Buf and gRPC libraries/frameworks are welcome. Generate frontend TypeScript API clients from the REST gateway's OpenAPI contract by default. Protobuf-generated clients need not imply direct browser gRPC, but OpenAPI matches this preferred browser integration. GraphQL backed by gRPC is an area to explore only deliberately.
- **Databases:** PostgreSQL default. SQLite for genuinely small/embedded cases; MongoDB familiar and acceptable when suitable. GORM is familiar; `sqlc` is an interesting alternative to evaluate, not a mandatory default. Avoid stored procedures.
- **Communication:** Use synchronous flows for immediate consistency requirements and asynchronous flows for deliberately eventual consistency. Prefer fact/event-driven integration over command-like messaging where appropriate. Use Dapr's pub/sub, service invocation and related capabilities where helpful, without introducing needless indirection.
- **Identity:** Hosted OIDC/OAuth rather than home-grown auth. Auth0 familiar; Stytch worth exploring with permission. Keep authorisation explicit.

## Infrastructure, operations and security

- **Hosting:** Existing **Rackspace Spot Kubernetes only**. Use Kubernetes even for small projects; do not introduce a new cloud or hosting platform without approval.
- **GitOps:** Argo CD + Kustomize for first-party services; Helm for third-party applications. Avoid Terraform. Reuse current infrastructure and deployment conventions.
- **Development:** Devcontainers, Just and Docker/Compose; reproducible tooling and documented local setup.
- **CI/CD:** GitHub Actions with separate build, release and deploy/promotion workflows. Reuse existing flows. Build once, version an immutable artefact and promote the *same* artefact. Multi-stage minimal container images, pinned base images, non-root runtime, immutable image tags.
- **Configuration:** Environment variables for environment-specific settings, Kubernetes Secrets for credentials, suitable additional secrets solutions only when needed. Reviewable application policy may belong in version-controlled structured configuration; never embed secrets.
- **Telemetry:** OpenTelemetry instrumentation, structured logs, metrics, distributed traces; Grafana ecosystem with Prometheus, Loki and Tempo.
- **Resilience:** Explicit errors, reasonable timeouts, bounded retries, Kubernetes health/readiness probes, graceful shutdown and resource limits. Use Dapr where it reduces custom plumbing. Add advanced resilience patterns only when justified.
- **Security:** Secure by default even in experiments: least privilege, restricted permissions, non-root containers, validated inputs and security/dependency scanning.

## Verification, dependencies and documentation

- Test meaningful behaviour changes, not necessarily TDD; cover success, failure and recovery without tests that merely restate implementation.
- Go `testing` package + Testcontainers for integration tests. Frontend Vitest + React Testing Library + Playwright.
- Enforce formatter, linter, type checks and security scanning in CI; checks should enforce real invariants.
- Use focused dependencies; embrace genuinely useful improvements rather than avoiding modern tools. Automate **minor/patch** updates; **major** upgrades require approval. Unfamiliar dependencies also require approval regardless of version.
- Maintain concise README, architecture and operations documentation, clear build/test commands and ADRs for important non-obvious decisions.

When recommending technology, clearly identify the default, material deviations, trade-offs, what needs explicit approval, and any decision worth recording. Avoid repeatedly debating settled choices.
