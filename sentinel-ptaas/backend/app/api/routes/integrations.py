from fastapi import APIRouter, Depends

from app.api.deps import require_roles
from app.models.models import RoleName
from app.services.integrations import fetch_tool_findings, get_tool_health
from app.services.jira import create_or_update_jira_ticket

router = APIRouter(prefix="/integrations", tags=["integrations"])


@router.get("/status")
def integration_status(_=Depends(require_roles(RoleName.super_admin, RoleName.security_admin))):
    return get_tool_health()


@router.post("/fetch/{tool_name}")
def fetch_tool(tool_name: str, _=Depends(require_roles(RoleName.super_admin, RoleName.security_admin))):
    return {"tool": tool_name, "items": fetch_tool_findings(tool_name)}


@router.post("/jira/sync/{vuln_id}")
def jira_sync(vuln_id: int, _=Depends(require_roles(RoleName.super_admin, RoleName.security_admin))):
    return create_or_update_jira_ticket(vuln_id=vuln_id)
