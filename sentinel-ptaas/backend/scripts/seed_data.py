"""Simple seed script for Sentinel PTaaS local development."""

from app.core.security import get_password_hash
from app.db.session import SessionLocal
from app.models.models import Asset, Organization, RoleName, User, Vulnerability


def run_seed():
    db = SessionLocal()
    org = Organization(name="Acme Security")
    db.add(org)
    db.flush()

    admin = User(
        email="admin@acme.test",
        full_name="Security Admin",
        hashed_password=get_password_hash("Passw0rd!"),
        role=RoleName.security_admin,
        organization_id=org.id,
    )
    db.add(admin)

    asset = Asset(organization_id=org.id, name="app.acme.test", asset_type="webapp")
    db.add(asset)
    db.flush()

    vuln = Vulnerability(
        external_id="MAN-1",
        organization_id=org.id,
        asset_id=asset.id,
        severity="high",
        cvss="8.8",
        title="Broken Access Control",
        source="manual",
    )
    db.add(vuln)
    db.commit()
    db.close()
    print("Seed complete")


if __name__ == "__main__":
    run_seed()
