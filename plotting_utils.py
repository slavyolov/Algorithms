import plotly.express as px # plotly== 5.5.0
import pandas as pd         # pandas==1.2.4


def plot_anomalies_and_time_series(df: pd.DataFrame, x_axis: str, y_axis_line: str, y_axis_bar: str) -> None:
    """
    The plot is used to display time series data as well as predicted anomaly labels

    Args:
        df: pd.DataFrame to plot
        x_axis: Values from this column or array are used to position marks along the x axis in cartesian coordinates
        y_axis_line: Values from this column or array are used to position marks along the y axis in cartesian
            coordinates
        y_axis_bar: Values from this column or array are used to position marks along the y axis in cartesian
            coordinates
    Returns:

    """

    fig = px.line(df, x=x_axis, y=y_axis_line, title='Time Series with Range Slider and Selectors')

    fig.update_xaxes(
        rangeslider_visible=True,
        rangeselector=dict(
            buttons=list([
                dict(count=1, label="1m", step="month", stepmode="backward"),
                dict(count=6, label="6m", step="month", stepmode="backward"),
                dict(count=1, label="YTD", step="year", stepmode="todate"),
                dict(count=1, label="1y", step="year", stepmode="backward"),
                dict(step="all")
            ])
        )
    )

    fig.add_bar(x=df[x_axis], y=df[y_axis_bar], name="Last year")
    fig.show()
    
# Demo :
df = pd.DataFrame([['2022-01-01', 0.3, 0],
               ['2022-01-02', 0.4, 0],
               ['2022-01-03', 0.5, 0],
               ['2022-01-04', 0.4, 0],
               ['2022-01-05', 0.5, 0],
               ['2022-01-06', 0.4, 0],
               ['2022-01-07', 0.5, 0],
               ['2022-01-08', 0.83, 1],
               ['2022-01-09', 0.87, 1],
               ['2022-01-10', 0.93, 1],
               ['2022-01-11', 0.99, 1],
               ['2022-01-12', 0.5, 0],
               ['2022-01-13', 0.5, 0]
              ], columns=['date', 'value', 'prediction'])

plot_anomalies_and_time_series(df=df, x_axis='date', y_axis_line='value', y_axis_bar='prediction')
