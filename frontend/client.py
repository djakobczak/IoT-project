import logging
from typing import Any, Dict
import requests


LOG = logging.getLogger(__name__)


class Client:
    CROSSWALK_ENDPOINT = '/crosswalks'
    STATISTICS_ENDPOTIN = '/statistics'
    TOKEN_ENDPOINT = '/login/access-token'

    def __init__(self, base_url: str, username: str, passwd: str) -> None:
        self.base_url = base_url
        self.username = username
        self.passwd = passwd
        self.token = None

    def _send_request(self,
                      endpoint: str,
                      method: str = 'get',
                      body: Any = None,
                      query_params: Dict[str, str] = None,
                      headers: Dict[str, str] = None,
                    ) -> dict:
        url = f"{self.base_url}{endpoint}"
        if query_params:
            params = "&".join(f'{key}={val}' for key, val in query_params.items())
            url += f"?{params}"

        LOG.debug("Send request to %s", url)
        if method == 'get':
            response = requests.get(url, headers=headers)
        elif method == 'post':
            response = requests.post(url, data=body, headers=headers)
        elif method == 'delete':
            response = requests.delete(url, data=body, headers=headers)
        else:
            raise ValueError(f'Invalid request method ({method})')

        if not response.ok:
            LOG.error("Got invalid response from backend: [%s] %s",
                      response.status_code, response.text)

        response_data = response.json()
        LOG.debug("Got response: %s", response_data)
        return response_data

    def get_all_crosswalks(self):
        auth_header = self._prepare_auth_header()
        return self._send_request(self.CROSSWALK_ENDPOINT, headers=auth_header)

    def get_all_stats(self):
        auth_header = self._prepare_auth_header()
        return self._send_request(self.STATISTICS_ENDPOTIN, headers=auth_header)

    def delete_crosswalk(self, name: str):
        auth_header = self._prepare_auth_header()
        return self._send_request(self.CROSSWALK_ENDPOINT + f"/{name}", headers=auth_header, method='delete')

    def _get_token(self):
        data = f'grant_type=&username={self.username}&password={self.passwd}&scope=&client_id=&client_secret='
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded'
        }
        LOG.info('Get token')
        response = self._send_request(self.TOKEN_ENDPOINT,
                                      method='post',
                                      body=data,
                                      headers=headers)
        return response['access_token']

    def _prepare_auth_header(self):
        if not self.token:
            self.token = self._get_token()
        return {'Authorization': f'Bearer {self.token}'}
