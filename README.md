# Agent Engineering Skills

Give coding agents repeatable engineering procedures for decisions that depend on evidence, authorization, or an accurate handoff. Each skill defines when to use it, how to inspect evidence, what result to produce, and where to stop. Synthetic cases make those behaviors testable.

## Skills

| Skill | Use it to | Result |
| --- | --- | --- |
| [Context Retrieval](skills/context-retrieval/SKILL.md) | Resolve a live claim using a small, relevant set of sources | Decision, dated references, and uncertainty |
| [Memory Checkpoint](skills/memory-checkpoint/SKILL.md) | Decide which facts, decisions, and hypotheses should survive a session | Verified update, pending candidate, or a reason to skip |
| [Project Session](skills/project-session/SKILL.md) | Start, resume, or hand off work with an accurate repository baseline | Reproducible handoff with test and revision evidence |
| [Behavior Reconstruction](skills/behavior-reconstruction/SKILL.md) | Document an authorized interface or compare a replacement | Observable contract and scoped equivalence evidence |
| [Deployment Verification](skills/deployment-verification/SKILL.md) | Establish how far a specific release reached | Stage-by-stage report bound to the commit, digest, target, and rollout |

## Try it

Follow the [installation guide](docs/installation.md) to install one skill in a scratch project. Start a new client session and try this request with the example receipt.

> Use Deployment Verification to assess the six delivery stages in release-wrong-rollout.json. Explain whether the matching digest and the green smoke check prove that the expected rollout was verified. Work only with this local fixture.

[Open the synthetic receipt](examples/synthetic-project/release-wrong-rollout.json). For a context exercise, use [the preview evidence](examples/synthetic-project/rollout-notes.md) to decide which release was observed in preview-west.

## How it works

- [skills/](skills/) contains independently installable [Agent Skills](https://agentskills.io/specification) packages. Each entry point links to a worksheet or a receipt contract where useful.
- [examples/](examples/synthetic-project/) and [evals/](evals/scenarios.json) contain synthetic inputs, observable criteria, and negative cases.
- [scripts/](scripts/) and [tests/](tests/) check package structure, local Markdown destinations, fixture references, and the behavior of the offline receipt checker.

Run the deterministic checks from the repository root with Python 3.10 or newer.

~~~sh
python -B scripts/validate.py
python -B -m unittest discover -s tests -v
~~~

The [compatibility record](docs/compatibility.md) reports package validation, client discovery, and mixed results from local Ollama trials. The [evaluation protocol](docs/evaluation.md) defines a paired comparison with and without the skills. The study has yet to run. Receipt checking verifies supplied identifiers and outcomes. Live verification still requires authoritative evidence and the appropriate access.

See the [methodology](docs/methodology.md) for how procedures handle evidence and authorization. See the [release checklist](docs/release.md) for scope and maintenance decisions and the [Agent Context Kit roadmap](docs/agent-context-kit.md) for the separate framework proposal. Start a change with the [contributing guide](CONTRIBUTING.md). The proposed distribution license is [MIT](LICENSE).
