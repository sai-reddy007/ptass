from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_roles
from app.db.session import get_db
from app.models.models import RoleName, Scan, User
from app.schemas.domain import ScanCreate
from app.services.tasks import queue_scan

router = APIRouter(prefix="/scans", tags=["scans"])


@router.get("")
def list_scans(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Scan).filter(Scan.organization_id == current_user.organization_id).all()


@router.post("/trigger")
def trigger_scan(
    payload: ScanCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(RoleName.super_admin, RoleName.security_admin)),
):
    scan = Scan(organization_id=current_user.organization_id, **payload.model_dump(), status="queued")
    db.add(scan)
    db.commit()
    db.refresh(scan)
    queue_scan.delay(scan.id)
    return {"message": "scan queued", "scan_id": scan.id}
