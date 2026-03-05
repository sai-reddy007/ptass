from pathlib import Path

from fastapi import APIRouter, Depends, File, UploadFile
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_roles
from app.db.session import get_db
from app.models.models import Report, RoleName, User
from app.services.tasks import parse_report

router = APIRouter(prefix="/reports", tags=["reports"])
UPLOAD_ROOT = Path("/tmp/uploads")
UPLOAD_ROOT.mkdir(parents=True, exist_ok=True)


@router.post("/upload")
async def upload_report(
    file: UploadFile = File(...),
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(RoleName.super_admin, RoleName.security_admin, RoleName.developer)),
):
    suffix = Path(file.filename).suffix.lower()
    filename = f"{current_user.organization_id}_{file.filename}"
    dest = UPLOAD_ROOT / filename
    content = await file.read()
    dest.write_bytes(content)

    report = Report(
        organization_id=current_user.organization_id,
        filename=file.filename,
        file_type=suffix.replace(".", ""),
        storage_path=str(dest),
        status="processing",
    )
    db.add(report)
    db.commit()
    db.refresh(report)
    parse_report.delay(report.id)
    return {"report_id": report.id, "status": report.status}
