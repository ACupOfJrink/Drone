import streamlit as st

page_1 = st.Page("pages/page_1.py", title="首页")

page0 = st.Page("pages/page0.py", title="队形算法")

page1 = st.Page("pages/page1.py", title="定位算法")

page2 = st.Page("pages/page2.py", title="云端模拟")

page3 = st.Page("pages/page3.py", title="避障算法")

pg = st.navigation([page_1, page0, page1, page3, page2])

pg.run()