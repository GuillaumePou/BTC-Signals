import streamlit as st

class PagePlot:
  
  def __init__(self, title, descr):
    self.title = title
    self.descr = descr

  def display(self):
    st.header(self.title)

    st.write(self.descr)

    st.write(self.plot_metric())

    self.add_comments()