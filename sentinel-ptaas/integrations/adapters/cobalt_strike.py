from integrations.base import BaseAdapter


class CobaltStrikeAdapter(BaseAdapter):
    name = "cobalt_strike"

    def healthcheck(self) -> dict:
        return {"status": "stubbed", "endpoint": "teamserver"}

    def fetch_findings(self) -> list[dict]:
        return [{"external_id": "CS-1", "title": "Beacon detected", "severity": "high"}]
