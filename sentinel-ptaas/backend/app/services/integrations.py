from integrations.registry import ADAPTERS


def get_tool_health() -> dict:
    return {name: adapter.healthcheck() for name, adapter in ADAPTERS.items()}


def fetch_tool_findings(tool_name: str) -> list[dict]:
    adapter = ADAPTERS.get(tool_name)
    if not adapter:
        return []
    return adapter.fetch_findings()
