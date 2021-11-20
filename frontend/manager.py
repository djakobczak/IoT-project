import logging
from typing import List

from client import Client

LOG = logging.getLogger(__name__)


class ClientManager:

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_crosswalks_names(self):
        crosswalks = self.client.get_all_crosswalks()
        return [cross['name'] for cross in crosswalks]

    def get_stats(self, crosswalks_names: List[str] = None, data_range: List[tuple] = None):
        stats = self.client.get_all_stats()

        if crosswalks_names:
            stats = list(filter(
                lambda stat: stat['crosswalk_name'] in crosswalks_names, stats)
            )
            LOG.debug("Crosswalk names filtered stats: %s", stats)

        return stats
