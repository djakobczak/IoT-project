from client import Client


class ClientManager:

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_crosswalks_names(self):
        crosswalks = self.client.get_all_crosswalks()
        return [cross['name'] for cross in crosswalks]

    def get_stats(self):
        stats = self.client.get_all_stats()
        return stats
