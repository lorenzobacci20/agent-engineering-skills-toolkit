# Verification receipt

The checker takes one UTF-8 JSON file, up to 128 KiB. Construct the receipt using the field contract below. The source distribution includes synthetic receipts under its examples directory.

| Scope | Required fields |
| --- | --- |
| Document | candidate, stages |
| Candidate | commit (40 or 64 lowercase hex digits), digest (sha256: plus 64 lowercase hex digits), target |
| Every supplied stage | evidence (opaque reference), outcome (passed or failed) |
| implementation | commit |
| build | commit, digest |
| ci | commit |
| publication | digest |
| deployment | digest, target, rollout |
| runtime | digest, target, rollout |

Include the expected rollout in the candidate when verifying deployment or runtime. Derive that expectation from the authorized release intent or a separately verified dispatch record. With rollout absent, a matching success report cannot establish either stage. Every stage is optional in the input. Unknown fields and repeated JSON keys are rejected. String fields other than fixed outcomes and digests contain printable, nonempty identifiers without leading or trailing spaces. Every JSON result includes `verification_scope: supplied_receipt_consistency`. Read `complete` and the six stage statuses within that scope. MISSING indicates absent evidence, missing expected rollout, or a successful runtime record without a verified matching deployment. MISMATCH means an identifier conflicts with the expected release. FAILED means a matching check recorded failure. VERIFIED means the supplied stage is internally consistent and reports success.

Run the checker with Python 3.10 or newer. From the distribution root:

~~~sh
python skills/deployment-verification/scripts/check-receipt.py examples/synthetic-project/release-current.json
~~~

For a standalone installation, substitute the paths to the installed skill and the receipt.

~~~sh
python "<installed-skill>/scripts/check-receipt.py" "<receipt.json>"
~~~

Exit 0 means all stages verified structurally. Exit 1 means a well-formed receipt has gaps, failures, or mismatches. Exit 2 means invalid input or a file read error. This is an offline check of supplied claims. Confirm each source, sample time, coverage, and relevant expiry separately. A runtime observation marked VERIFIED is scoped to its supplied rollout and exercised behavior.
