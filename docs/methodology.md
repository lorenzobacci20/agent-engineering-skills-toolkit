# Methodology

Treat a procedure as testable when a reader can identify its trigger, inputs, decisions, outputs, and stopping point. Keep the essentials in the entry point and load references only for the current decision.

| Principle | Practice |
| --- | --- |
| Minimal context | Retrieve the index and evidence that can change the outcome. Stop when the decision is supported. |
| Source authority and freshness | Match the claim's scope and the observation date to a source that can establish it. |
| Knowledge ownership | Preserve a single authoritative destination, link duplicates, and give uncertain claims a promotion condition. |
| Deterministic verification | Use fixed inputs for checks, bind evidence to an exact revision or rollout, and record missing checks. |
| Authorization and oversight | Identify what the task grants before writes, uploads, and operational changes. Let the maintainer approve the release. |
| Reproducible evaluation | Keep fixtures synthetic and rubrics observable. Distinguish deterministic checks, client observations, and paired experiments. |
| Portability | Use the open skill package format and provider-specific instructions only at the installation boundary. |

Project documentation, trackers, runtime observations, and shared memory can each establish different claims. Preserve a date and anchor when a decision depends on volatile information. Store no credentials or unnecessary personal data.

[NIST SSDF](https://csrc.nist.gov/pubs/sp/800/218/final) and [SLSA provenance](https://slsa.dev/spec/v1.2/provenance) provide further software delivery context. The skills make no conformance claims. [Strix](https://github.com/usestrix/strix), [Ponytail](https://github.com/DietrichGebert/ponytail), and [SkillOpt](https://github.com/microsoft/SkillOpt) are independent projects. Their code and skills are outside this distribution's dependencies.
