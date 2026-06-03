# Judging rubric

Binary checks only. Each task lists checks; a task passes if all **required** checks pass.

## Check types (prefer top to bottom)
1. **Programmatic (preferred):** `tests_pass`, `file_modified`, `command_exit_0`, `diff_contains`, `no_secret_introduced`. Deterministic, cheap, un-gameable.
2. **Assertion on output:** exact/regex/JSON-field match against an expected value.
3. **LLM-as-judge (only for fuzzy criteria):** "Does the diff explain *why* in the PR description?" Use sparingly.

## LLM-judge rules (when unavoidable)
- **Binary verdict** (`pass`/`fail`/`unknown`) with a one-sentence reason. Give it an **`unknown`** escape hatch to curb hallucination.
- Judge with a **different model** than the one that generated the work.
- **Calibrate first:** before trusting a judge check, a human labels ~20 examples and confirms the judge agrees. Re-calibrate if the judged criterion changes.
- Judge **one dimension per call** (don't ask one prompt to score five things).
- Beware position/verbosity/self-preference bias (research §7.3) — keep judged criteria narrow and concrete.

## Example task verdict
```
TASK migration-ordering
  [required] tests_pass .................. PASS   (programmatic)
  [required] additive_migration_only ..... PASS   (diff_contains check)
  [optional] pr_explains_expand_contract . PASS   (llm-judge, calibrated)
  → TASK PASS
```

## Governance
This rubric is **agent-immutable**. Changes require two human approvers + rationale (RULES.md §R4). The agent may *propose* new checks via PR; it may not relax existing ones to make itself pass.
