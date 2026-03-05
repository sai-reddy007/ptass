from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_roles
from app.db.session import get_db
from app.models.models import RoleName, User, Vulnerability
from app.schemas.domain import VulnerabilityCreate

router = APIRouter(prefix="/vulnerabilities", tags=["vulnerabilities"])


@router.get("")
def list_vulnerabilities(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Vulnerability).filter(Vulnerability.organization_id == current_user.organization_id).all()


@router.post("")
def create_vulnerability(
    payload: VulnerabilityCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(RoleName.super_admin, RoleName.security_admin, RoleName.developer)),
):
    vuln = Vulnerability(organization_id=current_user.organization_id, **payload.model_dump())
    db.add(vuln)
    db.commit()
    db.refresh(vuln)
    return vuln


@router.patch("/{vuln_id}/status")
def update_status(
    vuln_id: int,
    status: str,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(RoleName.super_admin, RoleName.security_admin, RoleName.developer)),
):
    vuln = db.query(Vulnerability).filter(Vulnerability.id == vuln_id, Vulnerability.organization_id == current_user.organization_id).first()
    if not vuln:
        raise HTTPException(status_code=404, detail="Not found")
    vuln.status = status
    db.commit()
    return vuln
