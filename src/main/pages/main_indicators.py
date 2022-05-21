import streamlit as st

from src.main.engine.plot.indicators import plot_gauge_chart_mayer


def page_indicators():
    st.header('Indicators')

    st.write(plot_gauge_chart_mayer(0, 4, 1.18, 1.7))