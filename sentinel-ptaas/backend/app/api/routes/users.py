from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.api.deps import require_roles
from app.db.session import get_db
from app.models.models import RoleName, User

router = APIRouter(prefix="/users", tags=["users"])


@router.get("")
def list_users(db: Session = Depends(get_db), _=Depends(require_roles(RoleName.super_admin, RoleName.security_admin))):
    return db.query(User).all()
