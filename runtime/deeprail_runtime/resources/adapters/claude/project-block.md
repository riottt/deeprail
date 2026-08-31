
<!-- deeprail:start -->
## DeepRail Runtime

This project uses DeepRail for evidence-gated AI-native work.

Before executing a work item:
1. Run `deeprail work-status --project . --work-id <WORK_ID>`.
2. Run `deeprail task --project . --work-id <WORK_ID> --write` and follow the active Task Packet.
3. Record created artifacts with `deeprail artifact-add`.
4. Record evidence with `deeprail evidence-add`; do not use self-report as completion evidence.
5. Run `deeprail gate --project . --work-id <WORK_ID>` before requesting a transition.
6. Use `deeprail work-advance` only when the gate passes and the A / EA / S policy allows the actor.
7. Record decisions and reinvest reusable learning.

DeepRail semantics are defined by the installed profile + workflow + evidence policy, not by ad-hoc prompt changes.
<!-- deeprail:end -->
