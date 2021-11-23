from enum import Enum
import logging
from typing import List

from client import Client
from pandas import DataFrame, to_datetime


LOG = logging.getLogger(__name__)
ALL_CROSSWALK_PLACEHOLDER = "all"


class AggregationTimeType(Enum):
    MINUTES = "m"
    HOUR = "h"
    DAY = "d"


class ClientManager:

    def __init__(self, client: Client) -> None:
        self.client = client

    def get_crosswalks_names(self):
        crosswalks = self.client.get_all_crosswalks()
        return [cross["name"] for cross in crosswalks]

    def get_stats(
        self,
        crosswalks_names: List[str] = None
    ) -> DataFrame:
        stats = self.client.get_all_stats()
        df = DataFrame(stats)
        df["timestamp"] = to_datetime(df["timestamp"])

        if crosswalks_names and ALL_CROSSWALK_PLACEHOLDER not in crosswalks_names:
            df = df[df.crosswalk_name.isin(crosswalks_names)]
            LOG.debug("Crosswalk names filtered stats: %s", df)

        df = df.groupby("timestamp", as_index=False).sum()
        return df
