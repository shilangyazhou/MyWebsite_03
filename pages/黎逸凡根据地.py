'''我的主页'''
import streamlit as st
from PIL import Image
import time
import datetime
import requests
page = st.sidebar.radio('我的首页',['我的兴趣推荐', '我的图片处理工具', '我的智能词典', '我的留言区' , '随机笑话生成', '旅游目的地推荐', '健身计划生成器', '科目介绍'])
st.title("网站评分")
rating = st.slider("请为我们的网站打分（1-5 星）", 1, 5, 3)
st.write(f"您给出的评分为：{rating} 星")
st.title("用户评论")
user_comment = st.text_area("请留下您对网站的宝贵意见：")
submit_button = st.button("提交")
if submit_button:
    st.write("感谢您的评论！")
"""
工作室名字：龙马工作室
根据地用户：个人使用、只有几个人知道的秘密基地、分享后所有人可见……
根据地用途：工具分享、数据收集、兴趣推荐、经历分享、综合主站……
最喜欢的现有模块：兴趣推荐、图片处理工具、智慧词典、留言区
现有模块改进灵感：……
原创模块：……
原创模块一句话功能介绍：……
"""
def page_1():
    '''我的兴趣推荐'''
    with open('黎逸凡_霞光.mp3','rb' ) as f:
        mymp3 = f.read( )
    st.audio(mymp3,format='audio/mp3',start_time=0) 
    st.image('黎逸凡_slogan.png')
    st.write("以下是一些适合您的阅读推荐：")
    st.write("1. 《百年孤独》 - 加西亚·马尔克斯")
    st.write("2. 《平凡的世界》 - 路遥")
    st.write("3. 《人类简史》 - 尤瓦尔·赫拉利")
    st.write("推荐的音乐风格和歌手：")
    st.write("1. 流行音乐：周杰伦、Taylor Swift")
    st.write("2. 古典音乐：贝多芬、莫扎特")
    st.write("适合您的运动项目和相关资源：")
    st.write("1. 跑步：专业跑鞋推荐")
    st.write("2. 瑜伽：线上瑜伽课程")
    pass 

def page_2():
    '''我的图片处理工具'''
    st.write(":sunglasses:图片换色小程序:sunglasses:")
    uploaded_file = st.file_uploader("上传照片", type=['png', 'jpeg', 'jpg'])
    if uploaded_file:
        try:
            img = Image. open(uploaded_file)
            st. image(img)
            st. image(img_change(img, 0,1,2))
            tab1, tab2, tab3, tab4 = col2. tabs(["原图", "改色1","改色2","改色3"])
            with tab1:
                st.image(img)
            with tab2:
                st.image(img_change(img, 2 ,1, 0))
            with tab3:
                st.write('### :red[这是一张102的rgb]')
                st.image(img_change(img, 2,0,1))
            with tab4:
                st.image(img_change(img, 1,1,0))
                st.write('### :red[这是一张012的rgb]')
            ch = st.toggle('反色滤镜')
            bw = st.toggle('黑白滤镜')
            co = st.toggle('增强对比度')

            message = ''
            if ch:
                message += '反色' + ','
            if bw:
                message += '黑白' + ','
            if co:
                message += '增强对比度'
                st.write('你将会得到一张', message, '的图片')
            if ch:
                img = apply_inverse_color(img)  
            if bw:
                img = apply_black_white_filter(img) 
            if co:
                img = apply_contrast_enhancement(img)  

            st.image(img)
        except FileNotFoundError as fnfe:  
            st.error(f"文件未找到错误: {fnfe}")
        except IOError as ioe:
            st.error(f"输入输出错误: {ioe}")
        except Exception as e:  
            st.error(f"发生未知错误: {e.__class__.__name__}: {e}")


def page_3():
    '''我的智慧词典'''
    st.write('智慧词典')
    with open('黎逸凡_words_space.txt', 'r', encoding='utf-8') as f:
        words_list =f.read().split('\n')
    for i in range(len(words_list)):
        words_list[i] = words_list[i].split('#')
    words_dict = {}
    for i in words_list:
        words_dict[i[1]] = [int(i[0]),i[2]]
        
    with open('黎逸凡_check_out_times.txt', 'r', encoding='utf-8') as f:
        times_list = f.read().split('\n')
    for i in range(len(times_list)):
        times_list[i] = times_list[i].split('#')
    times_dict = {}
    for i in times_list:
        try:  # 新增：添加错误处理
            times_dict[int(i[0])] = int(i[1])
        except ValueError:
            print(f"无法将 {i[0]} 或 {i[1]} 转换为整数") 
    word = st.text_input('请输入要查询的单词')
    if word in words_dict:
        st.write(words_dict[word])
        n = words_dict[word][0]
        if n in times_dict:
            times_dict[n] += 1
        else:
            times_dict[n] = 1
        with open('黎逸凡_check_out_times.txt', 'w', encoding='utf-8') as f:
            message = ''
            '''字典键值对遍历'''
            for k, v in times_dict.items():
                message += str(k) + '#' + str(v) + '\n'
            message = message[:-1]
            f.write(message)
        st.write('查询次数：', times_dict[n])
        
        st.write(f'#####：blue［{words_dict[word][1]}]')
    else:
        st.write(f"{word} 未在词典中")
        new_word = st.text_input("请输入要添加的单词")
        new_definition = st.text_input("请输入释义")
        if st.button("添加"):
            words_dict[new_word] = new_definition
            st.markdown("<h1 style='color: green;'>恭喜添加成功！</h1>", unsafe_allow_html=True)
            st.write(f"已成功添加 {new_word} 及其释义")
    if word == 'python' :
        st.code('''
            # 恭喜你触发彩蛋，这是一行python代码
            print('hello world')''')
    elif word == 'balloon':
        st.balloons ()
    elif word == 'snow':
        st.snow()
    


def page_4():
    '''我的留言区'''
    with open('黎逸凡_leave_messages.txt', 'r', encoding='utf-8') as f:
        messages_list =f.read().split('\n')
    number1 = st.slider('数据 1：', 1, 100, 50)
    number2, number3 = st.slider('数据 2 和 3：', 1, 10, (4, 6))
    st.write('数据 1：', number1)
    st.write('数据 2-3：', number2, '-', number3)
    st.write('----')
    msg_lst = ['留言 1', '留言 2', '留言 3', '留言 4', '留言 5', '留言 6', '留言 7', '留言 8']
    begin, end = st.slider('选择显示的留言信息：', 1, len(msg_lst), (1, len(msg_lst)))
    for i in range(begin - 1, end):
        st.write(msg_lst[i])
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    st.text("主人留言")
    for i in messages_list:
        if i[1] == '阿短':
            with st.chat_message('💯'):
                st.text(i[1]+':'+i[2])
    st.text("客人留言")
    for i in messages_list:
        if i[1] == '编程猫':
            with st.chat_message('🔢'):
                st.text(i[1]+':'+i[2])
    '''新增留言内容'''
    name = st.selectbox('我是......',['阿短','编程猫'])
    new_message = st.text_input('想要说的话......')
    if st.button('留言'):
        messages_list.append([str(int(messages_list[-1][0])+1),name, new_message])
        with open('黎逸凡_leave messages.txt','w',encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] +'\n'
            message =message[:-1]
            f.write(message)

def page_5():
    """
    随机笑话生成页面
    """
    st.title("随机笑话生成")
    url = "https://v2.jokeapi.dev/joke/Any"
    response = requests.get(url)
    data = response.json()
    if data["type"] == "single":
        st.write(data["joke"])
    elif data["type"] == "twopart":
        st.write(data["setup"])
        st.write(data["delivery"])
def page_6():
    """
    旅游目的地推荐页面
    """
    st.title("旅游目的地推荐")
    destinations = [
        {"name": "巴黎", 
         "attractions": ["埃菲尔铁塔", "卢浮宫", "巴黎圣母院", "凡尔赛宫", "香榭丽舍大道"],
         "food": ["法式长棍面包", "法式焗蜗牛", "马卡龙"]},
        {"name": "东京", 
         "attractions": ["东京塔", "银座", "上野公园", "新宿", "涩谷"],
         "food": ["寿司", "拉面", "天妇罗"]},
        {"name": "悉尼", 
         "attractions": ["悉尼歌剧院", "悉尼港大桥", "达令港", "邦迪海滩", "悉尼塔龙加动物园"],
         "food": ["海鲜", "肉派", "维吉麦"]},
        {"name": "伦敦", 
         "attractions": ["大本钟", "伦敦塔桥", "白金汉宫", "大英博物馆", "特拉法加广场", "伦敦眼"],
         "food": ["炸鱼薯条", "英式早餐", "约克郡布丁"]},
        {"name": "纽约", 
         "attractions": ["自由女神像", "时代广场", "中央公园", "帝国大厦", "大都会艺术博物馆", "百老汇"],
         "food": ["汉堡", "热狗", "披萨"]}
    ]
    selected_destination = st.selectbox("选择旅游目的地", [destination["name"] for destination in destinations])
    for destination in destinations:
        if destination["name"] == selected_destination:
            st.subheader("热门景点")
            for attraction in destination["attractions"]:
                st.write(attraction)
            st.subheader("特色美食")
            for food_item in destination["food"]:
                st.write(food_item)

def page_7():
    """
    健身计划生成器页面
    """
    st.title("健身计划生成器")
    fitness_goal = st.selectbox("选择您的健身目标", ["增肌", "减脂", "塑形", "增强体能"])
    days_per_week = st.number_input("每周锻炼天数", min_value=1, max_value=7, value=3)
    exercise_preference = st.multiselect("选择您的锻炼偏好", ["力量训练", "有氧运动", "瑜伽", "HIIT"])
    st.subheader("您的健身计划")
    if fitness_goal == "增肌":
        st.write("**增肌计划**")
        if "力量训练" in exercise_preference:
            st.write("  - 周一、周三、周五：杠铃卧推 3 组，每组 8-10 次；哑铃肩推 3 组，每组 8-10 次；深蹲 3 组，每组 8-10 次。")
        if "有氧运动" in exercise_preference:
            st.write("  - 周二、周四、周六：慢跑 30 分钟。")
    elif fitness_goal == "减脂":
        st.write("**减脂计划**")
        if "有氧运动" in exercise_preference:
            st.write("  - 周一、周三、周五：跳绳 15 分钟，开合跳 3 组，每组 30 次。")
        if "HIIT" in exercise_preference:
            st.write("  - 周二、周四、周六：进行高强度间歇训练，如波比跳 3 组，每组 12 次；俯撑交替提膝 3 组，每组 20 次。")
    elif fitness_goal == "塑形":
        st.write("**塑形计划**")
        if "瑜伽" in exercise_preference:
            st.write("  - 周一、周三、周五：进行瑜伽的各种体式练习，如树式、三角式、战士式等，每个体式保持 5-10 个呼吸。")
        if "力量训练" in exercise_preference:
            st.write("  - 周二、周四、周六：进行轻重量的力量训练，如哑铃侧平举 3 组，每组 12-15 次；臀桥 3 组，每组 15-20 次。")
    elif fitness_goal == "增强体能":
        st.write("**增强体能计划**")
        if "有氧运动" in exercise_preference:
            st.write("  - 每天进行 30 分钟以上的有氧运动，如游泳、骑自行车。")
        if "HIIT" in exercise_preference:
            st.write("  - 每周进行 2-3 次 HIIT 训练，如登山跑 3 组，每组 60 秒。")

    st.write("请根据个人身体状况和能力适当调整计划，如有需要，可咨询专业健身教练。")

def page_8():
    """
    科目介绍页面
    """
    st.title("科目介绍")
    subjects = ["语文", "数学", "英语", "物理", "化学", "生物", "历史", "地理", "政治"]
    selected_subject = st.selectbox("选择您想了解的科目", subjects)
    if selected_subject == "语文":
        st.write("语文是一门基础学科，注重培养阅读理解、写作表达和语言运用能力。")
    elif selected_subject == "数学":
        st.write("数学培养逻辑思维和解决问题的能力，涵盖代数、几何等多个领域。")
    elif selected_subject == "英语":
        st.write("英语是国际通用语言，包括听、说、读、写等方面的学习。")
    elif selected_subject == "物理":
        st.write("物理研究自然界的物质、能量和它们之间的相互作用。")
    elif selected_subject == "化学":
        st.write("化学探索物质的组成、结构、性质和变化规律。")
    elif selected_subject == "生物":
        st.write("生物研究生命现象和生命活动规律。")
    elif selected_subject == "历史":
        st.write("历史了解过去的事件、人物和社会发展。")
    elif selected_subject == "地理":
        st.write("地理研究地球表面的自然和人文现象。")
    elif selected_subject == "政治":
        st.write("政治涉及国家、政府、社会制度和政治思想等方面的知识。")


def img_change(img,rc,gc,bc) :
    '''图片处理'''
    width, height = img. size
    img_array = img. load()
    for x in range(width) :
        for y in range (height):
            r = img_array[x, y][rc]
            g = img_array[x, y][gc]
            b = img_array[x, y][bc]
            img_array[x,y] = (r, g, b)
    return img
    
            

if page == '我的兴趣推荐':
    page_1()
elif page == '我的图片处理工具':
    page_2()
elif page == '我的智能词典':
    page_3()
elif page == '我的留言区':
    page_4()
elif page =='随机笑话生成':
    page_5()
elif page =='旅游目的地推荐':
    page_6()
elif page =='健身计划生成器':
    page_7()
elif page =='科目介绍':
    page_8()

