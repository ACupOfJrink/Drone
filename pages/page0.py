import streamlit as st
from PIL import Image
import base64
from io import BytesIO

def image_to_base64(image):
    buffered = BytesIO()
    image.save(buffered, format="PNG")
    return base64.b64encode(buffered.getvalue()).decode()

# 设置网页信息  page_icons用于显示表情
st.set_page_config(page_title="空中使者——队形算法", layout="wide")

# 使用 CSS style
st.markdown(
    """
    <style>
    .center {
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .kai-font {
        font-family: "KaiTi", "楷体", serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown(
    """
    <style>
    .kai-font_center {
        font-family: "KaiTi", "楷体", serif;
        text-align: center;
    }
    </style>
    """,
    unsafe_allow_html=True
)


st.title("队形算法设计")

st.header('''目标问题''')

st.markdown(r'''假设队形变换在无障碍物情况下进行变换，则无人机$i$从$P_i$到$$P_{j}^{'}$$的所有路线中直线路径最短，那么问题就可以将队形变化变成优化问题。该优化问题需要求解在最小时间内的队形变化方案，该优化问题实际上是一个指派问题。若编队中有$$n$$架飞机，则潜在的指派方案就有$$n!$$种。目标函数为能量耗费$$E(K)$$和使用时间$$T(t)$$的加权平均，则优化问题的数学表达式为''')


#st.latex方法更加，直接可使公式居中
st.latex(r'''min\;\;J(\xi(k),\xi(k+1))=\alpha E(k)+(1-\alpha) \textit{T}(k) \\ \begin{cases} \textit{E}(k) = {\sum^{n}_{i=1}} \textit{E}_i (k) \\ \textit{T}(k)=max\{ t_1(k),t_2(k), \cdots , t_n(k) , \alpha\in [0,1]\} \end{cases}''')


st.header("算法设计")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown('''<p class="kai-font_center">队形实时切换</p>''',unsafe_allow_html=True)
    st.image(Image.open('./images/image_duixing1.png'),caption='基于指派算法的实时切换',width=350)
with col2: 
    st.markdown('''<p class="kai-font_center">队形时变队形</p>''',unsafe_allow_html=True)
    st.image(Image.open('./images/image_duixing3.png'),caption='基于阿基米德螺线的时变队形',width=350)
with col3:
    st.markdown('''<p class="kai-font_center">队形变化仿真</p>''',unsafe_allow_html=True)
    st.image(Image.open('./images/image_duixing2.png'),caption='基于粒子群算法的变化仿真',width=350)


col11, col12 = st.columns(2)
col111, col112 = st.columns(2)

st.header("算法对比")

with col11:
    st.image(Image.open('./images/result1block.png'),caption='队形变换示意图',width=560)  
      
with col12:
    #with col111:
    st.image(Image.open('./images/result3UAV2.png'),caption='两种队形变换的概念图',width=580)

    #with col112:
    #st.markdown('')
    st.image(Image.open('./images/result3UAV3.png'),caption='两种队形变换的概念图',width=580)

#col30, col31, col32 = st.columns(3)

st.image(Image.open('./images/result2juzhen.png'),caption='两种队形变换的概念图',width=1170)

col22, col23 = st.columns(2)

with col22:
    st.image(Image.open(r'images\result4ConnectMatrix.png'),caption='两种队形变换的概念图',width=580)
with col23:
    st.image(Image.open(r'images\result5UAVroute.png'),caption='两种队形变换的概念图',width=580)

col30, col31 = st.columns([0.55,0.45])
with col30:
    st.image(Image.open(r'images\result66pic.png'),caption='两种队形变换的概念图',width=635)

with col31:
    st.image(Image.open(r'images\result7computationtime.png'),caption='两种队形变换的概念图',width=525)


st.header("算法设计")
