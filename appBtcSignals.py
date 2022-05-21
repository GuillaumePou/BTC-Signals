# -*- coding: utf-8 -*-
"""
@author: GuillaumePou
"""

import streamlit as st

from src.main.pages.main_indicators import page_indicators
from src.main.pages.mayer_multiple import page_mayer

YEAR_MA = "2 Year Moving Average"
FEAR_AND_GREED = "Fear And Gread"
GOLDEN_RATIO = "Golden ratio"
MAIN_PAGE = "Main"
MAYER = "Mayer Multiple"
PI_CYCLE = "Pi Cycle Top"
PUELL = "Puell Multiple"

PAGES = [MAIN_PAGE, YEAR_MA, FEAR_AND_GREED, GOLDEN_RATIO, MAYER, PI_CYCLE, PUELL]


def main():
    # %% the GUI
    st.title('Bitcoin Signals visualisation')

    page = st.sidebar.selectbox(label="Page",
                                options=PAGES)

    match page:
        case "Main":
            page_indicators()
        case "Mayer Multiple":
            page_mayer()
        case _:
            return 0

    st.info(
        """ By: [GuillaumePou](https://github.com/GuillaumePou) | 
        Code Source: [GitHub](https://github.com/GuillaumePou/BTC-Signals) |
        Data Powered by [!]()"""
    )


if __name__ == "__main__":
    main()
