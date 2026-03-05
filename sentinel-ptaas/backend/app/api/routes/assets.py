from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import get_current_user, require_roles
from app.db.session import get_db
from app.models.models import Asset, RoleName, User
from app.schemas.domain import AssetCreate

router = APIRouter(prefix="/assets", tags=["assets"])


@router.get("")
def list_assets(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Asset).filter(Asset.organization_id == current_user.organization_id).all()


@router.post("")
def create_asset(
    payload: AssetCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(require_roles(RoleName.super_admin, RoleName.security_admin, RoleName.developer)),
):
    asset = Asset(organization_id=current_user.organization_id, **payload.model_dump())
    db.add(asset)
    db.commit()
    db.refresh(asset)
    return asset
