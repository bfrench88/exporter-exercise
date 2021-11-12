"""Redis exporter"""

import os
import time
from prometheus_client import start_http_server, Gauge, Enum, Info
import redis


class AppMetrics:
    """
    Representation of Prometheus metrics and loop to fetch and transform
    application metrics into Prometheus metrics.
    """

    def __init__(self, redis_host, redis_port=6379, polling_interval_seconds=5):
        self.redis_host = redis_host
        self.redis_port = redis_port
        self.polling_interval_seconds = polling_interval_seconds

        # Prometheus metrics to collect
        # self.current_requests = Gauge("app_requests_current", "Current requests")
        # self.pending_requests = Gauge("app_requests_pending", "Pending requests")
        # self.total_uptime = Gauge("app_uptime", "Uptime")
        # self.health = Enum("app_health", "Health", states=["healthy", "unhealthy"])
        self.redis_conn = redis.Redis(host=redis_host, port=redis_port, db=0)

        self.braze_redis_build_version_info = Info("braze_redis_version", "Redis version")
        self.braze_redis_keys = Gauge("braze_redis_keys", "Braze Redis keys")


    def run_metrics_loop(self):
        """Metrics fetching loop"""

        while True:
            self.fetch()
            time.sleep(self.polling_interval_seconds)

    def fetch(self):
        """
        Get metrics from application and refresh Prometheus metrics with
        new values.
        """

        redis_info=self.redis_conn.info()

        # Update Prometheus metrics with application metrics
        # self.current_requests.set(status_data["current_requests"])
        self.braze_redis_keys.set(self.redis_conn.dbsize())
        self.braze_redis_build_version_info.info({'version': redis_info['redis_version']})

def main():
    """Main entry point"""

    polling_interval_seconds = int(os.getenv("POLLING_INTERVAL_SECONDS", "10"))
    exporter_port = int(os.getenv("EXPORTER_PORT", "9877"))
    redis_host = os.getenv("REDIS_HOST", "127.0.0.1")
    redis_port = int(os.getenv("REDIS_PORT", "6379"))

    app_metrics = AppMetrics(
        redis_port=redis_port,
        redis_host=redis_host,
        polling_interval_seconds=polling_interval_seconds,
    )
    start_http_server(exporter_port)
    app_metrics.run_metrics_loop()

if __name__ == "__main__":
    main()
