---
name: memory-checkpoint
description: Decide whether to persist a durable fact, decision, correction, or unresolved hypothesis after engineering work. Use for checkpoint requests, knowledge handoffs, or reconciling overlapping memory entries.
---

# Memory Checkpoint

1. Extract at most one claim per potential update. Record the source, its observation date if material, scope, and why a later session would use the information.
2. Choose the source of record first. Keep implementation details, architecture, and operational procedures in the project or its tracker. Use a shared memory store only for cross-session context that belongs there. Reference an existing authoritative record when that meets the need.
3. Inspect the destination for a matching claim and relevant superseded entries. Deduplicate equivalent claims. For a conflict, check effective dates, authority, and directness. Preserve historical evidence when it still matters.
4. Decide the disposition. Write verified facts or explicit durable decisions to the authoritative location when permitted. Put useful uncertain claims in a candidate record with a promotion condition. Skip transient, redundant, or sensitive items without a suitable destination.
5. Verify authorized writes by rereading the affected records and checking links or repository validation. Keep uncertain claims visibly pending, including in downstream summaries. Report the outcome and unresolved conflict when an explicit checkpoint was requested.

Request authority when a necessary write is outside the approved scope. Keep secrets and unneeded personal data out of receipts and storage. For record shapes and examples, see the [checkpoint worksheet](references/checkpoint.md).
