'''我的主页'''
import streamlit as st
from PIL import Image


page = st.sidebar.radio('我的首页', ['我✨', '我的图片换色小工具📷', '我的高级English词典📘', '我的推荐🕵️‍♂️', '我的"流"言区💬'])
"""
工作室名字：jybc工作室
根据地用户：分享后所有人可见
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站……
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、我的游戏、留言区
现有模块改进灵感：完美
原创模块：我
原创模块一句话功能介绍：我
"""
def page_1():
    '''我✨'''
    st.write("---------------------------------我✨-------------------------------------")
    st.write("技能：经过多年的努力，我的厨艺已经炉火纯青了，只要你能给我教程，我都能做出来。（当然，成功率是50%）")
    st.write('其实我非常多才多艺，真正技能绝对不止这一点，but空间有限')
    st.write("---------------------------------荣誉✨-------------------------------------")
    st.write("去年我获得了蓝桥杯大赛省级一等奖")
    st.write("当然我的编程水平绝对不止这么一点，毕竟我可是能做出这个网站的Man，只是我的荣誉太多了实在放不下，只好选一个最不起眼的塞在这里了")
    st.write("----------------------------------爱好✨---------------------------------------")
    st.write("平时我喜欢玩玩球类运动,例如乒乓球、网球、羽毛球")
    st.write("空闲的时候我还喜欢看看小说")
    st.write('-----------------------------------------------------------------------------')
    st.write('除了本主站之外，我还将我的有趣内容分享在了其他网站中')
    go = st.selectbox('你的支持是我最大的动力，去支持一下up吧！', ['我的抖音', '我的bilibili'])
    if go == '我的抖音':
        st.link_button('帮我点赞', 'https://www.douyin.com/')
    elif go == '我的bilibili':
        st.link_button('帮我一键三连', 'https://www.bilibili.com/')

def page_2():
    '''我的图片换色小工具📷'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    st.markdown( "[点击这里访问百度](https://www.baidu.com)"  )  
    uploaded_file = st.file_uploader("上传图片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        tab1,tab2,tab3,tab4,tab5 = st.tabs(["原图", "改色1", "改色2", "改色3", "自定义"])
        with tab1:
            st.image(img)
        with tab2:
            st.write('### :gold[这是一张201的rgb]')
            st.image(img_change(img, 2, 0, 1))
        with tab3:
            st.write('### :gold[这是一张102的rgb]')
            st.image(img_change(img, 1, 0, 2))
        with tab4:
            st.write('### :gold[这是一张000的rgb]')
            st.image(img_change(img, 0, 0, 0))
        with tab5:
            a = st.text_input('请输入r(r=0, g=1, b=2,将三个值赋值给新的r g b)')
            d = st.text_input('请输入g(不用在意底下的报错信息)')
            c = st.text_input('请输入b(填完之后请稍等一会儿，切勿刷新)')
            st.image(img_change(img, a, d, c))


def page_3():
    '''我的高级English词典📘'''
    st.write('高级English词典📘')
    with open('hjy_words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
        
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]

    with open('hjy_check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
        
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
        
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        st.write(f'##### :blue[{words_dict[word][1]}]')
        n = words_dict[word][0]

        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1

        with open('hjy_check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''

            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) +'\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
    elif word == 'python!':
                st.code('''
                        # 恭喜你触发彩蛋，这是一行python代码
                        print('hello world')''')
    elif word == 'balloon!':
                st.balloons()
    elif word == 'snow!':
                st.snow()
    elif len(word) > 0:
        st.write("可恶，没想到你居然找到了这个没在词典的单词")

def page_4():
    '''我的推荐🕵️‍♂️'''
    st.write("------:✨:我的推荐🕵️‍♂️:✨:------")
    st.write()
    st.markdown( "[暮色回响](https://www.bilibili.com/video/BV1nJ4m137mP/?share_source=copy_web)"  )  
    
    
def page_5():
    '''我的"流"言区💬'''
    st.write('我的"流"言区💬')
    
    with open('hjy_leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
        
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')

    for i in messages_list:
        if i[1] == '作者大大':
            with st.chat_message('✨'):
                st.write(f"###### ：{i[1]+'：'+i[2]}")
        elif i[1] == '阿短':
            with st.chat_message('🌞'):
                st.write(i[1]+'：'+i[2])
        elif i[1] == '编程猫':
            with st.chat_message('🍥'):
                st.text(i[1]+'：'+i[2])
        elif i[1] == '一个帅气的江湖键盘侠':
            with st.chat_message('🗡️'):
                st.text(i[1]+'：'+i[2])
        elif i[1] == '小丑':
            with st.chat_message('🤡'):
                st.text(i[1]+'：'+i[2])
        else:
            with st.chat_message('👤'):
                st.text(i[1]+'：'+i[2])

    q = st.text_input('请自定义您的个性名称')
    name = st.selectbox('我是……', ['一个帅气的江湖键盘侠', '匿名用户', '小丑', q])
    message = ''
    if name == '作者大大':
        st.write('居然还想要冒充我，没门儿！！')
        name = ''
    else:
        new_message = st.text_input('想要流传千古的话……(After write 请发射)')
        if st.button('fire'):
            messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
            with open('hjy_leave_messages.txt', 'w', encoding='utf-8') as f:
                for i in messages_list:
                    message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
                message = message[:-1]
                f.write(message)
            st.rerun()
            

#--------------------------------------功能函数区--------------------------------------

def img_change(img, rc, gc, bc):
    rc, gc, bc = int(rc), int(gc), int(bc)
    width, height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x, y] = (r, g, b)
    return img


if page == '我✨':
    page_1()
elif page == '我的图片换色小工具📷':
    page_2()
elif page == '我的高级English词典📘':
    page_3()
elif page == '我的推荐🕵️‍♂️':
    page_4()
elif page == '我的"流"言区💬':
    page_5()