---
name: deployment-verification
description: Verify how far a software release reached from source commit to runtime. Use when confirming a deployment, validating a rollback, or reporting delivery progress for a target environment.
---

# Deployment Verification

1. Identify the expected source revision, immutable artifact digest, and target environment. When verifying deployment or runtime, identify the expected rollout independently of the observations being checked. If an identifier is missing, report the claim that cannot yet be linked to it. Historic receipts and smoke tests can only speak to their observed versions and targets.
2. Collect evidence that establishes each applicable stage. Use version control for implementation, a build record for the artifact, the relevant run for CI, a registry receipt for publication, the deployment controller for rollout, and an observation tied to the running release for runtime.
3. Match identifiers across each transition. Match the expected rollout ID on both deployment and runtime evidence as well as the environment and digest. Check timestamps against the requested observation window. A green generic health endpoint establishes availability only. A failed check or mismatched identifier blocks the corresponding claim.
4. Record a status and evidence anchor for each stage. Distinguish a failed operation, missing evidence, and identity mismatch. For a rollback, bind a fresh observation to the replacement rollout and preserve the original attempt separately.
5. Use read-only authorized evidence. Ask for authorization before operations that trigger deployments, rollbacks, migrations, or tests with live side effects. Keep receipts free of credentials and unnecessary data.

The [receipt contract](references/receipt.md) defines the offline input and output. For a local receipt in that format, run the installed [checker](scripts/check-receipt.py) when Python and permission to execute it are available. Report its exit code and use its stage statuses. If the checker did not run, label the assessment manual and compare each stage with the identifiers in the candidate before assigning a status. A reported `passed` outcome can still yield MISMATCH. Confirm the origin and current validity of every receipt in the system that issued it.
