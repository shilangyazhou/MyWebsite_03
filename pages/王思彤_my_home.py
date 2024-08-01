'''我的主页'''
import streamlit as st
from PIL import Image,ImageOps,ImageFilter,ImageDraw


st.write('工作室名字：Silence')
st.write('根据地用户：个人使用、分享后所有人可见')
st.write('根据地用途：兴趣推荐, 图片处理, 智能词典, 留言区,知识问答')


page = st.sidebar.radio('我的首页', ['兴趣推荐', '图片处理', '智能词典', '留言区','知识问答'])

audio_file = open('王思彤_久石让 - Summer (菊次郎的夏天).mp3','rb')
audio_bytes = audio_file.read()
image = Image.open('王思彤_钢琴图片.png')

def page_1():
    '''我的兴趣推荐'''
    st.markdown('**:musical_keyboard:我的爱好是弹钢琴**')
    st.write('---------------------------------------')
    st.markdown('***:musical_score: 钢琴简介 :musical_score:***')
    st.write('钢琴是一种键盘乐器，由意大利人巴托罗密欧·克里斯多佛利在1709年发明。钢琴由琴键和金属弦音板组成，一般88键钢琴音域范围从27.5Hz至4186.01Hz，108键钢琴则最高至7902.13Hz，几乎囊括了乐音体系中的全部乐音，是音域最广的乐器之一，普遍用于独奏、重奏和伴奏。')
    st.image(image,caption='弹钢琴中...')
    st.markdown('***:musical_note: 代表人物 :musical_note:***')
    st.write('肖邦、贝多芬、莫扎特等音乐家')
    st.markdown('***:notes: 钢琴的分类 :notes:***')
    st.write('三角钢琴、立式钢琴')
    st.markdown('***:headphones:: 下面是我最喜欢的钢琴曲 :headphones:***')
    st.write('菊次郎的夏天.mp3')
    st.audio(audio_bytes,format='audio/ogg')
    
    
def page_2():
    '''图片处理'''
    st.write(":sunglasses: 图片换色小程序 :sunglasses:")
    unloaded_file = st.file_uploader('上传图片', type=['png', 'jpg', 'jpeg'])
    if uploaded_file:
        img = Image.open(uploaded_file)
        st.image(img)
        st.image(img_change(img,0,1,2))
        tab1, tab2, tab3, tab4 = st.tabs(["og",'color1','color2','color3'])
        with tab1:
            st.image(img)
        with tab2:
            st.image(img_change(img, bc,gc,rc))
        with tab3:
            st.write("### :red [这是一张102的rgb]")
            st.image(img_change(img, 1, 0, 2))
        with tab4:
            st.write("### :red [这是一张102的rgb]")
            st.image(img_change(img, 0, 0, 0))

def page_3():
    '''智能词典'''
    st.write('智能词典')
    # 从本地文件中将词典信息读取出来，并存储在列表中
    with open('王思彤_words_space.txt', 'r', encoding='utf-8') as f:
        words_list = f.read().split('\n')
    # 将列表中的每一项内容再进行分割，分为“编号、单词、解释”
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    # 将列表中的内容导入字典，方便查询，格式为“单词：编号、解释”
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]), i[2]]
    # 从本地文件中将单词的查询次数读取出来，并存储在列表中
    with open('王思彤_check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    # 将列表转为字典
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        times_dict[int(i[0])] = int(i[1])
    # 创建输入框
    word = st.text_input('请输入要查询的单词')
    # 显示查询内容
    if word in words_dict:
        # 输出查询的单词内容
        cixing, ciyi = words_dict[word][1].split('.')
        st.write('单词的意思是：', ciyi)
        st.text('单词的词性是：' + cixing + '.')
        st.text('这是词典中的第' + str(words_dict[word][0]) + '个单词')
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('王思彤_check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.text('单词被查询次数为：' + str(times_dict[n]))
        if word == 'python':
            st.code('''
                    #恭喜你触发彩蛋，这是一行python代码
                    print('hello world')''')
        elif word == 'balloon':
            st.balloons()
        elif word =='snow':
            st.snow()



def page_4():
    '''我的留言区'''
    st.write('我的留言区')
    with open ('王思彤_leave_messages.txt', "r", encoding = "utf-8") as f:
        messages_list = f.read().split("\n")
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('🌟'):
                st.write(i[1]+':',i[2])
        elif i[1] =='编程猫':
             with st.chat_message('🌠'):
                st.text(i[1]+':'+i[2])
            
        name = st.selectbox('我是...',['阿短','编程猫'])
        new_message = st.text_input('想要说的话....')
        if st.button('留言'):
            messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
            with open ('王思彤_leave_messages.txt',"w", encoding = "utf-8") as f:
                message = ""
                for i in messages_list:
                    message += i[0] + "#" + i[1] + "#" + i[2] + "\n"
                message = message[:-1]
                f.write (message)      
                

def page_5():
    '''知识问答'''
    cb = st.checkbox('勾选选项')
    if cb:
        st.write('选项被勾选', cb)

    st.write('-----------------------')
    st.markdown('**1.(多选题)你知道吗：为什么要设置公网和私网？为什么不让每一个设备都直接连接到公网上?**')
    cb1 = st.checkbox('易于管理')
    cb2 = st.checkbox('效率高')
    cb3 = st.checkbox('网速快')
    cb4 = st.checkbox('安全性好')
    l = [cb1, cb2, cb3, cb4]
    if st.button('确认答案'):
        if True in l:
            st.write('***其实都不对，答案是“历史问题，不得已而为之**”')
        else:
            st.write('**8好厉害！确实都不对，真实答案是“历史问题，不得已而为之”，下面就让我来讲讲吧！***')
    st.write('-----------------------')
    st.write('**2.(多选题)下面哪些小程序可以被嵌入网页中**')
    cb1 = st.checkbox('A.turtle绘图作品')
    cb2 = st.checkbox('B.图片处理工具')
    cb3 = st.checkbox('C.智能词典工具')
    cb4 = st.checkbox('D.pygame小游戏')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == False and cb2 == True and cb3 == True and cb4 == False:
            st.write('回答正确！')
        else:
            st.write('再想想')

#--------------------功能函数区---------------------
def img_change(img,rc,gc,bc):
    '''图片处理'''
    width,height = img.size
    img_array = img.load()
    for x in range(width):
        for y in range(height):
            r = img_array[x,y][rc]
            g = img_array[x,y][gc]
            b = img_array[x,y][bc]
            img_array[x,y] = (r,g,b)
    return img
    
if page == '兴趣推荐':
    page_1()
elif page == '图片处理':
    page_2()
elif page == '智能词典':
    page_3()
elif page == '留言区':
    page_4()
elif page == '知识问答':
    page_5()