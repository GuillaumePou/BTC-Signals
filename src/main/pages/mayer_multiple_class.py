import streamlit as st

from src.main.pages.default_page import PagePlot
from src.main.engine.extraction.loading import get_btc_daily
from src.main.engine.plot.plotly import plot_current_multiple


class MayerMultiple(PagePlot):
  "Mayer Multiple page"
  
  TITLE = 'Mayer multiple'
  DESCR = 'The mayer multiple has been first used by Trace Mayer, it is the multiple between the 200 days moving average of bitcoin price and the current price. Trace Mayer evaluated that the best returns was obtained by accumulating bitcoins when the multiple is below 2.4.'

  def __init__(self):
    super(self.TITLE, self.DESCR)

  def plot_metric():
    return plot_current_multiple(get_btc_daily())

  def add_comments():

    df_btc_daily = get_btc_daily()
    mayer_mean = df_btc_daily['Mayer'].mean()
    mayer_today = df_btc_daily.loc[len(df_btc_daily) - 1, 'Mayer']
    mayer_percent = (df_btc_daily.loc[:, 'Mayer'] > mayer_today).sum() / len(
        df_btc_daily.loc[:, 'Mayer']) * 100

    st.write('Today, the 200 days moving average is **\\$ {}** and the btc price is **\\$ {}**'
             .format(round(df_btc_daily.dropna().loc[len(df_btc_daily) - 1, '200MaOpen'], 1),
                     round(df_btc_daily.dropna().loc[len(df_btc_daily) - 1, 'Open']), 1))

    st.write('Today, the mayer multiple is **{}**, the average multiple is _{}_, the multiple has been '
             'higher **{}**% of the time'.format(mayer_today.round(2), mayer_mean.round(2), mayer_percent.round(2)))