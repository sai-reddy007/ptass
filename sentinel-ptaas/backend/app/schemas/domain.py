from pydantic import BaseModel


class AssetCreate(BaseModel):
    name: str
    asset_type: str
    environment: str = "prod"


class VulnerabilityCreate(BaseModel):
    external_id: str
    asset_id: int
    severity: str
    cvss: str
    title: str
    description: str = ""
    poc: str = ""
    remediation: str = ""
    status: str = "open"
    source: str = "manual"


class ScanCreate(BaseModel):
    asset_id: int
    tool: str
    schedule_cron: str = ""
