from integrations.base import BaseAdapter


class GenericToolAdapter(BaseAdapter):
    def __init__(self, name: str):
        self.name = name

    def healthcheck(self) -> dict:
        return {"status": "stubbed", "tool": self.name}

    def fetch_findings(self) -> list[dict]:
        return [{"external_id": f"{self.name.upper()}-1", "title": f"{self.name} sample issue", "severity": "medium"}]
