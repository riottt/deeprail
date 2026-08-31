
# DeepRail Agent Instructions

This project uses DeepRail.

For every active work item:
- obtain the active Task Packet with `deeprail task --project . --work-id <WORK_ID> --write`;
- remain inside the active workflow responsibility;
- record artifacts and evidence via the DeepRail CLI;
- never treat executor self-report as completion evidence;
- check `deeprail gate` before requesting a transition;
- follow A / EA / S policy and explicit Decision Rights;
- reinvest repeated human intervention, failure, or uncertainty into reusable controls.
