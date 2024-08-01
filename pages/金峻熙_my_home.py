'''我的主页'''
import streamlit as st
from PIL import Image
import base64

page = st.sidebar.radio('我的首页', ['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区',"我的照片集",'我的调查问卷'])
#"""
#工作室名字：金峻熙基地
#根据地用户：只有几个人知道的秘密基地
#根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站
#最喜欢的现有模块：留言区
#现有模块改进灵感：留言区添加回复留言的功能
#原创模块：我的动漫推荐
#原创模块一句话功能介绍：通过图片和视频的形式推荐我喜欢的动漫
#"""
def page_1():
    '''我的兴趣推荐'''
    st.write("### 大家好，我叫金峻熙")
    pa,pb = st.columns([2,3])
    with pa:
        st.write("我喜欢打篮球")
    with pb:
        st.image("金峻熙_打篮球.jpg")
    pc,pd = st.columns([2,3])
    with pc:
        st.write("我也喜欢弹吉他，下面是我的演奏")
    with pd:
        st.video("金峻熙_吉他演奏.mp4")
    pe,pf = st.columns([2,3])
    with pe:
        st.write("我还很喜欢旅游，分享几张我旅游时的照片")
    with pf:
        st.image("金峻熙_佛像.jpg")
        st.image("金峻熙_熊猫.jpg")
    st.write("最后我想分享一下我最喜欢的歌曲《加州旅馆》")
    with open("金峻熙_加州旅馆.mp3","rb") as f:
        mymp3 = f.read()
    st.audio(mymp3,format="audio/mp3",start_time=0)

def page_2():
    '''我的图片处理工具'''
    
    st.write("### 我的图片处理工具")
    uploaded_file = st.file_uploader("#### 请上传图片",type=['png','jpg','jpeg'])
    if uploaded_file:
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        #tab1,tab2,tab3,tab4 = st.tabs(['原图','改色1','改色2','改色3'])
        ph,pj,pk,pl = st.columns([3,2,2,2])
        #with pg:
            #st.write("### 原图")
            #st.image(img)
        with ph:
            #st.write("### 调换gb数值")
            #st.image(img_change(img,0,2,1))
            qa = st.checkbox("##### 调换rgb值")
            qb = st.checkbox("##### 增强对比度")
            qc = st.checkbox("##### 转为黑白")
        if qa:
            with pj:
                #st.write("### 调换rg数值")
                #st.image(img_change(img,1,0,2))
                qd = st.checkbox("###### 调换rg数值")
                
            with pk:
                #st.write("### 调换rb数值")
                #st.image(img_change(img,2,1,0))
                qd = st.checkbox("###### 调换gb数值")
                
            with pl:
                qd = st.checkbox("###### 调换rb数值")
                
            
        
        
def page_3():
    '''我的智能词典'''
    st.write("### 我的智能词典")

    with open("words_space.txt","r",encoding='utf-8') as f:
        words_list = f.read().split("\n")
    
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split("#")

    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
    with open("check_out_times.txt","r",encoding='utf-8') as f:
        times_list = f.read().split("\n")
    
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split("#")

    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    word = st.text_input("请输入要查询的单词")
    if word in words_dict:
        cixing, ciyi = words_dict[word][1].split('.')
        st.write('单词的意思是：', ciyi)
        st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')
        #st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open("check_out_times.txt","w",encoding='utf-8') as f:
            message = ''
            for k,v in times_dict.items():
                message += str(k) + "#" + str(v) + "\n"
            message = message[:-1]
            f.write(message)
        st.write("查询次数：",times_dict[n])
        if word == "balloon":
            st.balloons()
        elif word == "snow":
            st.snow()
        elif word == "jinjunxi":
            st.write("恭喜你发现宝藏！")

def page_4():
    '''我的留言区'''
    st.write("### 我的留言区")
    with open("leave_messages.txt","r",encoding="utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split("#")
    for i in messages_list:
        if i[1] == "阿短":
            with st.chat_message("🌞"):
                st.write(i[1],":",i[2])
        elif i[1] == "编程猫":
            with st.chat_message("🍥"):
                st.write(i[1],":",i[2])
        elif i[1] == "匿名":
            with st.chat_message("👤"):
                st.write(i[1],":",i[2])
            
    name = st.selectbox("我是...",["阿短","编程猫",'匿名'])
    new_message = st.text_input("想要说的话...")
    if st.button("留言"):
        messages_list.append([str(int(messages_list[-1][0])+1),name,new_message])
        with open("leave_messages.txt","w",encoding="utf-8") as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]
            f.write(message)
    #st.write('----')
    #msg_lst = new_message
    #begin, end = st.slider('选择显示的留言信息：', 1, len(msg_lst), (1, len(msg_lst)))
    #for i in range(begin-1, end):
        #st.write(msg_lst[i])
def page_5():
    '''我的照片集'''
    st.write("### 我的照片集")
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        # 获取图片文件的名称、类型和大小
        file_name = uploaded_file.name
        file_type = uploaded_file.type
        file_size = uploaded_file.size
        img = Image.open(uploaded_file)
        st.image(img)
        with open(img,"rb") as g:
            imgs = base64.b64encode(g.read())
        with open("image_base64.txt", "w",encoding='utf-8') as f:
            f.write(imgs)
        
def page_6():
    '''我的调查问卷'''
    st.write("### 我的调查问卷")
    a=0
    #zql = st.progress(0,"你已答对0题")
    #zql.progress(a,"你已答对"+str(a)+"题")
    st.write("我兴趣爱好包括以下哪个？")
    col1,col2,col3,col4 = st.columns([1,1,1,1])
    with col1:
        cb1 = st.checkbox("A.篮球")
    with col2:
        cb2 = st.checkbox("B.排球")
    with col3:
        cb3 = st.checkbox("C.羽毛球")
    with col4:
        cb4 = st.checkbox("D.乒乓球")
    b1 = st.button("回答")
    if b1:
        if cb1 == True and cb2 == False and cb3 == False and cb4 == False:
            st.write("答对了！")
            #a = a+1
            #zql.progress(a,"你已答对"+str(a)+"题")
        else:
            st.write("答错了，再去看看第一页吧！")
            #zql.progress(a,"你已答对"+str(a)+"题")
    st.write("在图片处理功能里可以对图片进行怎样的处理？")
    col5,col6 = st.columns([1,1])
    with col5:
        cb5 = st.checkbox("A.调换rg")
    with col6:
        cb6 = st.checkbox("B.调换gb")
    col7,col8 = st.columns([1,1])
    with col7:
        cb7 = st.checkbox("C.调换rb")
    with col8:
        cb8 = st.checkbox("D.以上均可")
    b2 = st.button("回答 ")
    if b2:
        if cb5 == False and cb5 == False and cb7 == False and cb8 == True:
            st.write("答对了！")
            #a = a+1
            #zql.progress(a,"你已答对"+str(a)+"题")
        else:
            st.write("答错了，再去看看第二页吧！")
            #zql.progress(a,"你已答对"+str(a)+"题")
    st.write("在第三页的词典中，查询以下哪个单词有特效？")
    po,pp,pq,pr = st.columns([1,1,1,1])
    with po:
        qo = st.checkbox("A.birthday")
    with pp:
        qp = st.checkbox("B.happy")
    with pq:
        qq = st.checkbox("C.snow")
    with pr:
        qr = st.checkbox("D.根本没有特效，站主胡说。")
    b3 = st.button(" 回答")
    if b3:
        if qo == False and qp == False and qq == True and qr == False:
            st.write("答对了！")
            #a = a+1
            #zql.progress(a,"你已答对"+str(a)+"题")
        else:
            st.write("答错了，再去看看第三页吧！")
            #zql.progress(a,"你已答对"+str(a)+"题")
    st.write("在第四页的留言板中，阿短的头像是什么")
    ps,pt,pu,pv = st.columns([1,1,1,1])
    with ps:
        qs = st.checkbox("A.小花朵")
    with pt:
        qt = st.checkbox("B.小笑脸")
    with pu:
        qu = st.checkbox("C.小太阳")
    with pv:
        qv = st.checkbox("D.小贝壳")
    b4 = st.button(" 回答 ")
    if b4:
        if qs == False and qt == False and qu == True and qv == False:
            st.write("答对了！")
            #a = a+1
            #zql.progress(a,"你已答对"+str(a)+"题")
        else:
            st.write("答错了，再去看看第四页吧！")
            #zql.progress(a,"你已答对"+str(a)+"题")
        #zql.progress(a,"你已答对"+str(a)+"题")
        #st.write("你答对了"+str(a)+"题")
        st.write("感谢您访问本站！")
def img_change(img,rc,gc,bc):
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
def img_change_co(img):
    '''增强对比度滤镜'''
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            # 获取RGB值
            r = img_array[x, y][0]
            g = img_array[x, y][1]
            b = img_array[x, y][2]
            # RGB值中，哪个更大，就再大一些
            if r == max(r, g, b):
                if r >= 200:
                    r = 255
                else:
                    r += 55
            elif g == max(r, g, b):
                if g >= 200:
                    g = 255
                else:
                    g += 55
            else:
                if b >= 200:
                    b = 255
                else:
                    b += 55
            img_array[x, y] = (r, g, b)
    return img

def img_change_bw(img):
    '''图片黑白滤镜'''
    img = img.convert('L') # 转换为灰度图
    return img
if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page == '我的照片集':
    page_5()
elif page == '我的调查问卷':
    page_6()