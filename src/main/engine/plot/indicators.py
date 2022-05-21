import plotly.graph_objects as go


def plot_gauge_chart_mayer(min_indicator, max_indicator, value, previous_week_value):
    fig = go.Figure(go.Indicator(
        domain={'x': [0, 1], 'y': [0, 1]},
        value=value,
        mode="gauge+number+delta",
        title={'text': "Mayer Multiple"},
        delta={'reference': 1.7},
        gauge={'axis': {'range': [min_indicator, max_indicator]},
               'steps': [
                   {'range': [min_indicator, 1.7], 'color': "blue"},
                   {'range': [1.7, 2.4], 'color': "lightgray"},
                   {'range': [2.4, max_indicator], 'color': "red"}]
               }))

    return fig
