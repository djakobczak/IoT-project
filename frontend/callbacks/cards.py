import logging

from dash.dependencies import Output, Input

from app import app


@app.callback(
    Output("sum-badge", "children"),
    Input("crosswalk-filter", "value")
)
def update_sum_badge(crosswalk):
    stats_df = app.client.get_stats([crosswalk] if crosswalk else None)
    total_pedestrians = stats_df['pedestrians'].sum()
    return total_pedestrians


@app.callback(
    Output("avg-badge", "children"),
    Input("crosswalk-filter", "value")
)
def update_avg_badge(crosswalk):
    stats_df = app.client.get_stats([crosswalk] if crosswalk else None)
    avg_pedestrians = stats_df['pedestrians'].mean()
    return avg_pedestrians
