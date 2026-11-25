"""Check the identifiers and status fields in an offline release receipt."""

import argparse
import json
import re
import sys

MAX_BYTES = 128 * 1024
COMMIT = re.compile(r"(?:[0-9a-f]{40}|[0-9a-f]{64})")
DIGEST = re.compile(r"sha256:[0-9a-f]{64}")
STAGES = {
    "implementation": ("commit",),
    "build": ("commit", "digest"),
    "ci": ("commit",),
    "publication": ("digest",),
    "deployment": ("digest", "target", "rollout"),
    "runtime": ("digest", "target", "rollout"),
}


def unique_object(pairs):
    result = {}
    for key, value in pairs:
        if key in result:
            raise ValueError("duplicate JSON key")
        result[key] = value
    return result


def fields(record, expected, label):
    if not isinstance(record, dict) or record.keys() != set(expected):
        raise ValueError(f"unexpected fields in {label}")


def identifier(value, label, pattern=None):
    if not isinstance(value, str) or not value or value != value.strip() or not value.isprintable():
        raise ValueError(f"invalid identifier for {label}")
    if pattern and not pattern.fullmatch(value):
        raise ValueError(f"invalid identifier format for {label}")


def evaluate(document):
    fields(document, ("candidate", "stages"), "receipt")
    candidate = document["candidate"]
    candidate_keys = {"commit", "digest", "target"}
    if isinstance(candidate, dict) and "rollout" in candidate:
        candidate_keys.add("rollout")
    fields(candidate, candidate_keys, "candidate")
    patterns = {"commit": COMMIT, "digest": DIGEST}
    for key, value in candidate.items():
        identifier(value, key, patterns.get(key))

    stages = document["stages"]
    if not isinstance(stages, dict) or stages.keys() - STAGES.keys():
        raise ValueError("unexpected release stage")

    result = {}
    for stage, keys in STAGES.items():
        if stage not in stages:
            result[stage] = "MISSING"
            continue
        entry = stages[stage]
        fields(entry, ("evidence", "outcome", *keys), stage)
        for key in ("evidence", *keys):
            identifier(entry[key], f"{stage}.{key}", patterns.get(key))
        if entry["outcome"] not in ("passed", "failed"):
            raise ValueError(f"invalid outcome for {stage}")

        expected = {key: candidate[key] for key in keys if key in candidate}
        if any(entry[key] != value for key, value in expected.items()):
            result[stage] = "MISMATCH"
        elif "rollout" in keys and "rollout" not in expected:
            result[stage] = "MISSING"
        elif entry["outcome"] == "failed":
            result[stage] = "FAILED"
        elif stage == "runtime" and result["deployment"] != "VERIFIED":
            result[stage] = "MISSING"
        else:
            result[stage] = "VERIFIED"

    return {
        "verification_scope": "supplied_receipt_consistency",
        "complete": all(status == "VERIFIED" for status in result.values()),
        "stages": result,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("receipt", help="UTF-8 JSON file")
    args = parser.parse_args()
    try:
        with open(args.receipt, "rb") as receipt:
            data = receipt.read(MAX_BYTES + 1)
        if len(data) > MAX_BYTES:
            raise ValueError("receipt exceeds 128 KiB")
        result = evaluate(json.loads(data.decode("utf-8"), object_pairs_hook=unique_object))
    except (OSError, ValueError, RecursionError):
        # Errors omit input content, file paths, and exception details.
        print("Invalid or unreadable release receipt. Check the receipt contract.", file=sys.stderr)
        return 2
    print(json.dumps(result, indent=2))
    return 0 if result["complete"] else 1


if __name__ == "__main__":
    sys.exit(main())
