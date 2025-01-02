import streamlit as st
import numpy as np

# 设置网页信息  page_icons用于显示表情
st.set_page_config(page_title="空中使者——基于优化理论的无人机编队控制方法", page_icon=":drone:", layout="wide")



# _ _itelics用法      :blue[]: 颜色用法      :sunglasses: 表情用法(笑脸)     控制字号st.markdown('<font size="6">这是大号字体</font>', unsafe_allow_html=True)
# use CSS
custom_style="""
<style>
    .Font6Bold {
        font-weight:bold;
        font size:150px;
    }
</style>
"""

#st.markdown('<span class="Font6Bold"> _:blue[空中使者]_——基于优化理论的无人机编队控制方法</span>', unsafe_allow_html=True)

st.title('_:blue[空中使者]_——基于优化理论的无人机编队控制方法')


# 侧边栏
with st.sidebar:
    LocPri = st.sidebar.selectbox(
        "定位原理类型",
        (
            "二维定位",
            "三维定位",
        ),
    )

    # 分隔线 
    st.divider()

    # 侧边栏中选择数据分类
    DirPri = st.sidebar.radio(
        "纯方向无源定位: ",
        ("几何原理", "计算几何"),
    )

# 定位维度    
if LocPri == "二维定位":
    st.bar_chart(np.random.randn(50,3))
    st.markdown(r'''$\left.\left\{\begin{array}{c}x_n=\sqrt{1-{z_n}^2}\cdot\cos{(2\pi n\phi)}\\y_n=\sqrt{1-{z_n}^2}\cdot\sin{(2\pi n\phi)}\\z_n=\frac{2n-1}{N-1}\end{array}\right.\right.$''')   
if LocPri == "三维定位":
    st.bar_chart(np.random.randn(50,3))
    st.markdown(r'''$\left.\left\{\begin{array}{c}x_n=\sqrt{1-{z_n}^2}\cdot\cos{(2\pi n\phi)}\\y_n=\sqrt{1-{z_n}^2}\cdot\sin{(2\pi n\phi)}\\z_n=\frac{2n-1}{N-1}\end{array}\right.\right.$''')    







# # 侧边栏————————————————————————————————————————————————————————————————————
# # 侧边栏中选择数据集
# dataset = st.sidebar.selectbox(
#     "定位原理类型",
#     (
#         "二维定位",
#         "三维定位",
#     ),
# )
 
# # 侧边栏中选择数据分类
# data_type = st.sidebar.radio(
#     "数据分类: ",
#     ("测试集", "验证集", "所有数据"),
# )
 
# # 右侧页面中的模拟操作
# st.header(f"数据集： {dataset}")
# st.divider()
# st.write(f"数据分类： 【{data_type}】")
# ###############################


# #————————————————————
# #横向的标签页
# tab1, tab2, tab3 = st.tabs(["1. 选择数据", "2. 配置数据", "3. 绘制图形"])
 
# with tab1:
#     st.write("可以调用方法一")
 
# with tab2:
#     st.write("可以调用方法二")
 
# with tab3:
#     st.write("可以调用方法三")
# #####################















# #跳转页面
# if st.button("GoTo Page 2"):

#     st.switch_page("pages/page2.py")



# datalist = ("", "人口数据", "环境数据", "交易数据")

# if "dataset" not in st.session_state:

#     option = st.selectbox(

#         "请选择数据集",

#         datalist,

#     )

# else:

#     option = st.session_state.dataset

#     option = st.selectbox(

#         "请选择数据集",

#         datalist,

#         index=datalist.index(option),

#     )

# if option == "":

#     st.write("当前尚未选择数据集")

# else:

#     st.write("你当前选择的是: 【", option, "】")

# st.session_state.dataset = option




# # 初始化pygame
# pygame.init()

# # 设置屏幕尺寸
# screen_width = 800
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height), pygame.NOFRAME)  # NOFRAME 去掉窗口边框
# pygame.display.set_caption("无人机飞行动画")

# # 设置颜色
# WHITE = (255, 255, 255)

# # 加载无人机图片（假设图片已经下载，路径可以替换为实际路径）
# drone1_image = pygame.image.load("pic\drone1.png")  # 左下角飞行的无人机
# drone2_image = pygame.image.load("pic\drone1.png")  # 右上角飞行的无人机

# # 调整无人机的大小
# drone_width = 50
# drone_height = 50
# drone1_image = pygame.transform.scale(drone1_image, (drone_width, drone_height))
# drone2_image = pygame.transform.scale(drone2_image, (drone_width, drone_height))

# # 设置无人机的初始位置
# drone1_x, drone1_y = 0, screen_height
# drone2_x, drone2_y = screen_width, 0

# # 设置无人机的速度
# speed = 5

# # 主循环：创建帧并保存为图像
# def generate_frame():
#     # 填充背景色
#     screen.fill(WHITE)

#     # 更新无人机的位置
#     global drone1_x, drone1_y, drone2_x, drone2_y
#     drone1_x += speed
#     drone1_y -= speed
#     drone2_x -= speed
#     drone2_y += speed

#     # 确保无人机不会飞出屏幕
#     if drone1_x > screen_width:
#         drone1_x = screen_width
#     if drone1_y < 0:
#         drone1_y = 0
#     if drone2_x < 0:
#         drone2_x = 0
#     if drone2_y > screen_height:
#         drone2_y = screen_height

#     # 绘制无人机
#     screen.blit(drone1_image, (drone1_x, drone1_y))
#     screen.blit(drone2_image, (drone2_x, drone2_y))

#     # 将pygame屏幕转换为PIL图像
#     pygame.image.save(screen, "frame.jpg")
#     img = Image.open("frame.jpg")
#     return img

# # 创建Streamlit的组件
# def display_animation():
#     while True:
#         img = generate_frame()

#         # 将图片转换为流媒体格式
#         buffered = BytesIO()
#         img.save(buffered, format="JPEG")
#         img_str = buffered.getvalue()

#         # 在Streamlit中展示图片
#         st.image(img_str, use_column_width=True)

# # 使用streamlit显示页面
# st.title("无人机飞行动画")
# st.write("这是一个无人机飞行的动画演示。")

# # 显示动画
# display_animation()

