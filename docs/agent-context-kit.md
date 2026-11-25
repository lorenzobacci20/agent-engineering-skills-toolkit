# Agent Context Kit roadmap

Agent Context Kit is a proposal for a separate, provider-neutral framework that helps coding agents retrieve and maintain durable context. Treat skill packages as consumers of documented interfaces. A project should be able to use the skills with local evidence even if it never adopts the framework.

| Milestone | Capability | Evidence required before progressing |
| --- | --- | --- |
| Persistent context | Versioned records with an owner, scope, source, observation time, and a distinction between verified and pending claims | Synthetic replay preserves ownership and historical state, and rejects references across unauthorized scopes |
| Context packs | Task-scoped selection from local indexes and targeted evidence | Repeatable pack contents and budgets on synthetic retrieval and stale-data cases |
| Freshness and consistency | Compare dated observations and identify broken links, conflicting authoritative claims, and stale snapshots | Fixtures distinguish a recent summary from a recent observation and report unresolved disagreement |
| Checkpoint planning | Route a durable observation to its owner and propose an update, a candidate, or no action | Tests cover conflicts, duplicate suppression, rejected writes, and retry behavior |
| MCP adapter | Expose bounded queries and checkpoint proposals using documented schemas | Interoperability checks in explicitly supported clients, with data isolation and access rules exercised |

Start with synthetic records and a read-only local interface. Keep adapter access within explicit workspace and data scope. Require a separate approval path and audit trail for any future write capability. Keep reference source, facts, and observations attributable throughout the workflow. Evaluate the framework using synthetic workloads before considering operational data or provider-specific adapters.

This proposal belongs in its own repository if approved. The 0.1.0 distribution contains the skills and their evaluation materials.
