# DeepRail 10-minute Quickstart

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install -e .

deeprail init --target /path/to/project --profile lightweight --communication en --artifacts en --adapter generic
deeprail doctor --project /path/to/project
deeprail work-start --project /path/to/project --title "Proxy approval" --intent "Allow an authorized proxy to approve during a bounded absence"
deeprail task --project /path/to/project --work-id DRW-... --write
```

Record evidence, check the gate, then transition. Executor self-report alone never satisfies a completion gate.
