import logging
from typing import Dict
import requests


LOG = logging.getLogger(__name__)


class Client:
    CROSSWALK_ENDPOINT = '/crosswalks'
    STATISTICS_ENDPOTIN = '/statistics'

    def __init__(self, base_url: str) -> None:
        self.base_url = base_url

    def _send_request(self, endpoint: str,
                      query_params: Dict[str, str] = None):
        url = f"{self.base_url}{endpoint}"
        if query_params:
            params = "&".join(
                '='.join([key, val] for key, val in qparam)
                for qparam in query_params)
            url += f"?{params}"

        LOG.debug("Send request to %s", url)
        response = requests.get(url)
        response_data = response.json()
        LOG.debug("Got response: %s", response_data)
        return response_data

    def get_all_crosswalks(self):
        return self._send_request(self.CROSSWALK_ENDPOINT)

    def get_all_stats(self):
        return self._send_request(self.STATISTICS_ENDPOTIN)
