from abc import ABC, abstractmethod


class BaseAdapter(ABC):
    name: str

    @abstractmethod
    def healthcheck(self) -> dict:
        pass

    @abstractmethod
    def fetch_findings(self) -> list[dict]:
        pass
