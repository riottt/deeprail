# DeepRail 10-minute Quickstart

You do not need to read all of DeepRail first. Try one Work end to end.

## 0. Install (from a repository checkout)

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .
deeprail version
```

## 1. Add it to a target project

```bash
deeprail init \
  --target /path/to/your-project \
  --profile lightweight \
  --communication en \
  --artifacts en \
  --adapter generic
```

If an existing agent instruction file is present, DeepRail appends only its managed block instead of replacing the whole file.

## 2. Doctor

```bash
deeprail doctor --project /path/to/your-project
```

## 3. Start a Work

```bash
deeprail work-start \
  --project /path/to/your-project \
  --title "Proxy approval" \
  --intent "Allow an authorized proxy to approve during a bounded absence"
```

Note the returned `DRW-...` id.

## 4. Hand a Task Packet to the agent

```bash
deeprail task --project /path/to/your-project --work-id DRW-... --write
```

`.deeprail/runs/<WORK_ID>/...md` is the execution contract containing the current workflow, evidence, and decision rights.

## 5. Record evidence

Example:

```bash
deeprail evidence-add \
  --project /path/to/your-project \
  --work-id DRW-... \
  --type observed_behavior \
  --description "Reproduced and confirmed the current approval behavior" \
  --verified
```

## 6. Check the gate and move forward

```bash
deeprail gate --project /path/to/your-project --work-id DRW-...
deeprail work-advance --project /path/to/your-project --work-id DRW-... --to shape --actor human
```

If the gate is not satisfied, the transition is rejected.

## 7. Verify requires independent evidence

```bash
deeprail evidence-add ... --type machine_check --actor tool --verified
deeprail evidence-add ... --type independent_evaluation --actor ai --independent --verified
```

## 8. Audit

```bash
deeprail audit-verify --project /path/to/your-project --work-id DRW-...
```

State mutations are recorded in the hash-chain audit.

## Next

- [Runnable Example](../../examples/approval-delegation/README.md)
- [Evidence Gates](evidence-gates.md)
- [Production Adoption](production-adoption.md)
- [Diagnostic](diagnostic.md)
- [Standard](../../standard/README.md)
