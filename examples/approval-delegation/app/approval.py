
from dataclasses import dataclass
from datetime import datetime, timezone

@dataclass
class ProxyGrant:
    owner: str
    proxy: str
    valid_from: datetime
    valid_until: datetime
    revoked: bool=False

def can_proxy_approve(grant, actor, owner, now):
    if grant.revoked: return False
    if actor != grant.proxy or owner != grant.owner: return False
    return grant.valid_from <= now <= grant.valid_until

def approve(grant, actor, owner, now):
    if not can_proxy_approve(grant,actor,owner,now):
        raise PermissionError("proxy approval denied")
    return {
        "status":"approved",
        "actor":actor,
        "on_behalf_of":owner,
        "approved_at":now.isoformat(),
        "mode":"proxy"
    }
