from integrations.base import BaseAdapter


class BugcrowdAdapter(BaseAdapter):
    name = "bugcrowd"

    def healthcheck(self) -> dict:
        return {"status": "stubbed", "api": "bugcrowd"}

    def fetch_findings(self) -> list[dict]:
        return [{"external_id": "BC-100", "title": "SQLi report", "severity": "critical"}]
