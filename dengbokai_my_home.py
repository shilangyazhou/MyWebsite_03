'''我的主页'''
import streamlit as st
from PIL import Image
import time

page = st.sidebar.radio('我的首页', [':heart_eyes:兴趣推荐', ':wrench:图片处理小程序', ':book:智能词典', ':writing_hand:留言社区', ':star:网址导航'])
"""
工作室名字：邓帅哥的工作室
"""
"""
根据地用户：个人使用、只有几个人知道的:secret:秘基地、分享后所有人可见
"""
"""
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站
"""
"""
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区、我的软件推荐
"""
"""
现有模块改进灵感：添加更多互动
"""
"""
原创模块：我的软件推荐
"""
"""
原创模块一句话功能介绍：推荐一些好用的软件
"""
"""
-----------------------------------------
"""
def page_1():
    '''我的兴趣推荐'''
    st.write("#### :red[#我的爱好:]")
    st.write("##### 旅行(有时候)")
    st.image('dengbokai_去沙漠看金字塔.png')
    st.write("##### 编程(最爱)")
    st.image('dengbokai_logo.png')
    st.write("##### 还有游泳(还不是很会)")
    st.image('dengbokai_去海边游泳.png')

def page_2():
    '''我的图片处理工具'''
    st.write("#### :red[#图片处理小程序]")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        tab1, tab2, tab3, tab4 = st.tabs(["原图", "改色1", "改色2", "改色3"])
        with tab1:
            st.write("### :red[这是原图]")
            st.image(img)
        with tab2:
            st.write("### :red[这是2,1,0的RGB改色图片]")
            st.image(img_change(img, 2, 1, 0))
        with tab3:
            st.write("### :red[这是0,2,0的RGB改色图片]")
            st.image(img_change(img, 0, 2, 0))
        with tab4:
            st.write("### :red[这是1,0,2的RGB改色图片]")
            st.image(img_change(img, 1, 0, 2))

def page_3():
    '''我的智能词典'''
    st.write('#### :red[#智能词典]')
    with open('dengbokai_words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    with open('dengbokai_check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(f'##### :blue[单词解释：{words_dict[word][1]}]')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('dengbokai_check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + "\n"
            message = message[:-1]
            f.write(message)
        st.write(f':red[查询次数：{times_dict[n]}]')
        if word == 'python':
            st.code('''
                    # 恭喜你触发隐藏彩蛋，这是几行python代码
                    import turtle
                    print('Hello, world!')
                    for i in range(3):
                    turtle.forward(100)
                    turtle.left(60)
                    turtle.done()
            ''')
        elif word == 'ballon':
            st.balloons()
        elif word == 'snow':
            st.snow()

def page_4():
    '''我的留言区'''
    st.write("#### :red[#我的留言区]")
    with open('dengbokai_leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌞'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '匿名用户':
            with st.chat_message('👤'):
                st.text(i[1] + '：' + i[2])
        elif i[1] == '作者':
            with st.chat_message('🎃'):
                st.markdown(f'###### :red[{i[1]}：{i[2]}]')       
    name = st.selectbox('我是……', ['阿短', '编程猫', '匿名用户', '作者'])
    new_message = st.text_input('良言一句三冬暖，恶语伤人六月寒。说点什么吧……')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('dengbokai_leave_messages.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + "#" + '\n'
            message = message[:-1]
            f.write(message)

def page_5():
    '''我的软件推荐'''
    st.write('#### :red[#网址导航]')
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    with col1:
        st.link_button('Streamlit', 'https://streamlit.io/')
        st.link_button('Github', 'https://www.github.com/')
        st.link_button('编程猫社区', 'https://shequ.codemao.cn/')
        st.link_button( "YouTube", "https://www.youtube.com/")
    with col2:
        st.link_button( "百度一下", "https://www.baidu.com/")
        st.link_button( "哔哩哔哩", "https://www.bilibili.com/")
        st.link_button( "优酷", "https://www.youku.com/")
        st.link_button( "爱奇艺", "https://www.iqiyi.com/")
    with col3:
        st.link_button( "Python官网", "https://www.python.org/")
        st.link_button( "知乎", "https://www.zhihu.com/")
        st.link_button( "央视网", "https://www.cctv.com/")
        st.link_button( "QQ邮箱", "https://mail.qq.com/")
    with col4:
        st.link_button( "网易邮箱", "https://email.163.com")
        st.link_button( "4399小游戏", "https://www.4399.com")
        st.link_button( "必应", "https://www.bing.com/")
        st.link_button( "淘宝", "https://www.taobao.com/")
    st.write("#### Streamlit部分页面展示：")
    st.image('dengbokai_slogan.png')

#----------------功能函数区--------------------------
def img_change(img, rc, gc, bc):
    '''图片处理'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img

roading = st.progress(0, '开始加载')
time.sleep(0.5)
for i in range(1, 101, 2):
    time.sleep(0.02)
    roading.progress(i, '正在加载'+str(i)+'%')
roading.progress(100, '加载完毕！')

if page == ':heart_eyes:兴趣推荐':
    page_1()
elif page == ':wrench:图片处理小程序':
    page_2()
elif page == ':book:智能词典':
    page_3()
elif page == ':writing_hand:留言社区':
    page_4()
elif page == ':star:网址导航':
    page_5()
