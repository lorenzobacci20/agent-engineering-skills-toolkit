---
name: behavior-reconstruction
description: Recover observable software contracts from authorized source, specifications, and local fixtures to document, migrate, or compare behavior. Use when replacing a component or establishing equivalence for an existing interface.
---

# Behavior Reconstruction

1. Identify the owned or explicitly authorized artifacts, version, interface, and purpose. Choose whether to document the contract or also build and compare a replacement. Agree on the behavior in scope and the surfaces available for observation.
2. Read the relevant entry point and approved documentation. Capture ordinary, boundary, and failure cases with local synthetic inputs. Preserve stimulus, output, conditions, and the anchor for each observation.
3. Mark each claim as **observed**, **inferred**, or **unknown**. Keep implementation guesses separate from observable rules. For consequential ambiguities, choose the smallest permitted local observation that distinguishes the alternatives.
4. Specify input/output, state transitions, error behavior, side effects, ordering, and tolerances where they were observed. Choose an explicit comparator and explain each normalization. Preserve properties such as ordering and rounding unless the contract permits a difference.
5. Run equivalent cases on both versions when available. Record differences, skipped cases, and fixture limits. Claim equivalence only for the exercised inputs, states, and tolerances.

Limit work to approved source, documented interfaces, and ordinary local behavior. Exclude bypass, exploit reproduction, protected asset replication, and live probing. Use the [contract and evidence table](references/contract.md) for a migration or a material behavioral discrepancy.
