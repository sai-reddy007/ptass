from celery import Celery

from app.core.config import settings

celery_app = Celery("sentinel_worker", broker=settings.redis_url, backend=settings.redis_url)


@celery_app.task(name="queue_scan")
def queue_scan(scan_id: int):
    # Placeholder: invoke integration adapter run.
    return {"scan_id": scan_id, "status": "started"}


@celery_app.task(name="parse_report")
def parse_report(report_id: int):
    # Placeholder: parse report types PDF/JSON/CSV/XML and persist vulnerabilities.
    return {"report_id": report_id, "parsed": True}
