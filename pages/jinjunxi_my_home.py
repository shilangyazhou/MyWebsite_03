'''我的主页'''
import streamlit as st

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区','我的'])
#"""
#工作室名字：…
#根据地用户：个人使用、只有几个人知道的秘密基地、分享后所有人可见……
#根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站……
#最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区
#现有模块改进灵感：……
#原创模块：……
#原创模块一句话功能介绍：……
#"""
def page_1():
    '''我的兴趣推荐'''
    st.write("大家好，我叫金峻熙")
    st.write("我喜欢打篮球")
    st.write("我也喜欢弹吉他，下面是我的演奏")
    st.video("吉他演奏.mp4")
    st.write("我还很喜欢旅游，分享几张我旅游时的照片")
    st.image("佛像.jpg")
    st.image("熊猫.jpg")
    st.write("最后我想分享一下我最喜欢的歌曲《加州旅馆》")
    with open("加州旅馆.mp3","rb") as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)

def page_2():
    '''我的图片处理工具'''
    pass

def page_3():
    '''我的智能词典'''
    pass

def page_4():
    '''我的留言区'''
    pass

def page_5():
    '''我的'''
    pass

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的':
    page_5()