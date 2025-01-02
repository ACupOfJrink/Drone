import streamlit as st

page1 = st.Page("pages/page1.py", title="无源定位算法设计")

page2 = st.Page("pages/page2.py", title="算法对比")

pg = st.navigation([page1, page2])

pg.run()