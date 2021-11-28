from datetime import datetime, timedelta
import logging

from dash.dependencies import Output, Input

from app import app


@app.callback(
    Output("sum-badge", "children"),
    [Input("crosswalk-filter", "value"),
     Input('interval-component', 'n_intervals')]
)
def update_sum_badge(crosswalk, n_intervals):
    stats_df = app.client.get_stats([crosswalk] if crosswalk else None)
    if stats_df.empty:
        return "Brak danych"
    total_pedestrians = stats_df['pedestrians'].sum()
    return total_pedestrians


@app.callback(
    Output("avg-badge", "children"),
    Input("crosswalk-filter", "value")
)
def update_avg_badge(crosswalk):
    stats_df = app.client.get_stats([crosswalk] if crosswalk else None)
    if stats_df.empty:
        return "Brak danych"
    n_days = 7  # !TODO fixme
    start_date = datetime.today() - timedelta(days=n_days)
    stats_df = stats_df.loc[stats_df["timestamp"] > start_date]
    avg_pedestrians = stats_df['pedestrians'].sum() / n_days
    return int(avg_pedestrians)
