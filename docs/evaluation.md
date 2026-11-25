# Evaluation

The [case manifest](../evals/scenarios.json) defines two synthetic tasks per skill, including stale evidence, conflicting identifiers, and scope boundaries. Tests check the package, fixture paths and rubric structure. The receipt tests additionally assert deterministic outcomes on positive and negative inputs.

## Compare skill-assisted and unassisted runs

1. Freeze the candidate revision, cases, scoring rubric, provider, model, client version, tool permissions, time/context limits, and model settings. Record any backend setting that cannot be held fixed. Exclude real logs, credentials, private projects, and live targets.
2. For each case, copy only its declared inputs into separate clean directories, plus any identical harness needed in both conditions. Use a fresh session each time. Hide rubrics and answers from the agent. Use the same task prompt in both arms. In A, provide no skill and keep unrelated skills disabled. In B, install only the declared skill and record whether discovery and loading succeeded. If testing explicit invocation instead, use a separate experiment with an invocation line only in B. Report the changed procedure.
3. Randomize arm order per case. Choose and record a seed, replicate count, timeout, and inclusion rules before collecting results. Pair repetitions by case. Separate timeouts, refusals, setup failures, and completed runs. Record requested assistance separately from any help actually provided.
4. Score anonymized outputs with the frozen rubric. For each criterion record pass or fail and the supporting excerpt. A case passes when every critical criterion passes and at least 80% of all criteria pass. Record scope violations separately even if text claims compliance. Use a second grader or document the adjudication for disagreements.
5. Compare paired outcomes by case, then report the corpus aggregate and number of usable pairs. Report variability and missing telemetry. These synthetic scenarios have limited external validity.

| Metric | Recording rule |
| --- | --- |
| Correctness and instruction adherence | Criterion pass counts, case pass, scope violations |
| Defects and false positives | Compare supported findings to the fixture oracle, count missing defects and unsupported defect claims separately |
| Evidence quality | Count relevant claims with a specific source or receipt and the correct scope or version |
| Tokens | Record provider-reported input and output tokens, cached input where available, otherwise unavailable |
| Wall time | Start at request dispatch and stop at terminal result or the declared timeout |
| Human intervention | Count human turns and classify as clarification, approval, or rescue |
| Discovery | Record visible skill, explicit trigger or selection, and skill load evidence when observable |

Keep one row per run with case ID, condition, randomization position, repeat index, versions, fixture revision, prompt hash, terminal status, measurements, and a reference to a redacted output. Keep a scored row per criterion and grader. Preserve the raw local receipts under the applicable retention policy.

One independent forward check exercised Behavior Reconstruction on the tie-order fixture. The reviewer identified the concrete mismatch, preserved ordering in the comparator, bounded parity to the observed fixtures, and left case folding unknown. All four criteria matched after the output was produced. The check used a single skill-assisted run. A paired A/B study has not been run. The [compatibility record](compatibility.md) reports separate local client trials, including a missed CI commit mismatch, an unsupported claim about timestamp checking, and a deduplication failure. The trials used different evidence paths and cannot estimate the effect of installing a skill.
