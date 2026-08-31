# Evidence Packet — Example

## Observed Behavior
- Authorized proxy can approve during the active window
- Expired proxy is rejected
- UI labels proxy approval explicitly

## Machine Checks
- Authorization test: PASS
- Expiry boundary test: PASS
- Existing approval regression: PASS

## Read-back
Audit log records `actor`, `on_behalf_of`, and proxy validity source.

## Unknowns
- Cross-region clock skew is not exercised in this example

## Decision
`pass` for the bounded example; production release would still use the project's release gate.
