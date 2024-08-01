'''我的主页'''
import streamlit as st

page = st.sidebar.radio('个人的推荐', ['音乐推荐','游戏推荐','动漫推荐', "吐槽专区"])

"""
根据地用户：所有人可见
根据地用途：工具分享、兴趣推荐
原创模块：全部原创
"""

def page_1():
    '''
    音乐推荐
    '''
    st.write("生活中不少的音乐 以下几首音乐都是我特别推荐大家去听的")
    st.write("----------------------------------------------------")
    st.write("(以下排名不分先后)")
    st.link_button('酷狗音乐', 'https://www.kugou.com/')
    st.link_button('第一首歌:光', 'https://www.kugou.com/share/dqgeha1CPV2.html#25jevv73')
    st.link_button('第二首歌：今天不是明天', 'https://www.kugou.com/share/dqhXv7bCPV2.html#ar2aqncf')
    st.link_button('第三首歌：Diamond eyes', 'https://www.kugou.com/share/dqiwj38CPV2.html#hash=B961327AA54432130FF0ACA5266D3C13&album_id=70312024')
    st.link_button('第四首歌：Reimei', 'https://www.kugou.com/share/dqNuR40CPV2.html#hash=61BE3D312DA9E695EF88C6EFFA132D8C&album_id=35214825')


    
def page_2():
    '''
    游戏推荐
    '''
    st.write("游戏,被称为第9门艺术。以下游戏都是我精挑细选给大家整理出来的神作，他们有些是国产新星，有些则大家耳熟能详")
    st.write('我先问大家问题')
    st.write('哪款游戏是复古风和变态难度而著名？')
    cb1 = st.checkbox('A.塞尔达传说')
    cb2 = st.checkbox('B.马里奥')
    cb3 = st.checkbox('C.喵斯')
    cb4 = st.checkbox('D.茶杯头')
    b1 = st.button('第1题答案')
    if b1:
        if cb1 == False and cb2 == False and cb3 == False and cb4 == True:
            st.write('回答正确！')
            st.write('''《‌茶杯头》‌是一款以BOSS对战为主的经典横版卷轴类射击游戏。‌ 受上世纪30年代动画片的启发，‌游戏在画面和音效上都努力再现了当时的技术，‌
                     如传统的赛璐璐手绘动画、‌水彩背景以及原声爵士乐录音等。‌玩家在游戏中扮演茶杯头或马克杯人，‌
                     还清欠魔鬼的债务而奋战。‌游戏的背景设定在一个名为墨池岛的神奇地方，‌
                     两兄弟茶杯头和马克杯人在智者水壶公公的照料下过着无忧无虑的生活。‌
                     然而，‌他们因一场赌博而负债累累，‌被迫开始一段冒险之旅，‌收集欠债人的灵魂以偿还债务。‌
                     《‌茶杯头》‌的游戏模式包括单人模式和本地双人合作模式，‌让玩家能够体验不同的挑战和合作乐趣。‌
                     游戏的角色设定丰富，‌每个角色都有其独特的技能和攻击方式，‌使得游戏过程充满变化和策略性。‌
                     此外，‌《‌茶杯头》‌的背景音乐由Kristofer Maddigan创作，‌为游戏增添了浓厚的艺术氛围和情感深度。‌
                     总的来说，‌《‌茶杯头》‌是一款充满挑战和乐趣的游戏，‌它将玩家带入一个充满奇幻色彩的世界，‌
                     通过不断的冒险和挑战，‌让玩家体验到成长的喜悦和成功的满足''')
            st.image('Leo茶杯头.jpg')
        else:
            st.write('再想想')
    st.write('下一题')
    st.write('什么游戏是因为坑爹著名，在疫情期间被各大主播游玩？')
    cb11 = st.checkbox('A.猫里奥')
    cb21 = st.checkbox('B.神回避')
    cb31 = st.checkbox('C.I wanna')
    b2 = st.button('第2题答案')
    if b2:
        if cb11 == False and cb21 == False and cb31 == True:
            st.write('回答正确！')
            st.write('''iwanna官方正版手游是一款风靡海内外的跳跃闯关类游戏，全称：i wanna be the Creator，别名：我想成为创造者。该游戏采用经典的街机像素玩法，玩家将会以冒险家的身份去探秘未知的地下世界，游戏的关卡丰富，每一关的怪物和迷宫地图都大不相同，玩家可以选择合适的难度进行冒险闯关。
                                iwanna游戏中还内置关卡编辑器，玩家可以通过它自行制作或者是修改关卡的内容，让游戏的玩法有无穷的扩展性，经过全球海量的玩家的努力，目前已经有近10W张丰富有趣的关卡地图等待玩家们发现以及挑战了。
                                此外，iwanna官方正版手游还支持多人联机模式，玩家可以叫上自己的朋友一起联机闯关，找回当初那种拿游戏机进行双人闯关的感觉，在者就是游戏的难度系数较高，玩法比较丰富，是一款很值得推荐给大家的游戏。''')
            st.image('LeoIwanna.jpg')
        else:
            st.write('再想想')
    st.write('下一题')
    st.write('哪款游戏是米哈游做的回合制游戏?')
    cb12 = st.checkbox('A.原神')
    cb22 = st.checkbox('B.崩坏3')
    cb32 = st.checkbox('C.崩坏：星穹铁道')
    b3 = st.button('第3题答案')
    if b3:
        if cb12 == False and cb22 == False and cb32 == True:
            st.write('回答正确！')
            st.write('''崩坏星穹铁道是一款由米哈游发行的全新3d回合制策略rpg游戏，该游戏继承了经典的崩坏ip，拥有庞大的崩坏系列世界观，能够带给玩家全新的剧情故事体验。超清精致的美术动画设计，让你能够享受一场超爽快的视觉盛宴，还有不同的战斗人物等你收集。''')
            st.image('Leo崩铁.jpg')
        else:
            st.write('再想想')
    st.write('下一题')
    st.write('什么音游以乱动的判定线为出名？')
    cb13 = st.checkbox('A.喵斯')
    cb23 = st.checkbox('B.phigros')
    b3 = st.button('第3题答案')
    if b2:
        if cb13 == False and cb23 == True:
            st.write('回答正确！')
            st.write('''《Phigros》是由Pigeon Games（鸽游）开发的节奏类游戏。
Pigeon Games是由初创通过bilibili视频网站发起的、由众多节奏类游戏爱好者组成的完全用爱发电的项目组。我们希望Phigros新颖的游戏模式和精心制作的插画与关卡可以让你感受到节奏类游戏的魅力。''')
            st.image('Leo360截图20240730210532260.jpg')
        else:
            st.write('再想想')

def page_3():
    '''
    动漫推荐
    '''
    st.write('敬请期待')
def page_4():
    '''
    吐槽专区
    '''
    st.write('吐槽专区')
    with open('Leoleave_messages.txt','r', encoding='utf-8') as f:
        messages_list = f.read().split('\n')
    for i in range(len(messages_list)):
        messages_list[i] = messages_list[i].split('#')
    for i in messages_list:
        if i[1] == '空中飞人':
            with st.chat_message('(((((((((((っ•ω•)っ Σ(σ｀•ω•´)σ 起飞！'):
                st.write(i[1]+': '+i[2])
        elif i[1] == '神金':
            with st.chat_message('（◐ˍ◑）'):
                st.write(i[1]+': '+i[2])
        elif i[1] == '我没有名字':
            with st.chat_message('⊙▃⊙'):
                st.write(i[1]+': '+i[2])
        elif i[1] == '派蒙':
            with st.chat_message('o(´^｀)o'):
                st.write(i[1]+': '+i[2])
        elif i[1] == '三月七':
            with st.chat_message(' '):
                st.write(i[1]+': '+i[2])
        elif i[1] == '安比':
            with st.chat_message('?'):
                st.write(i[1]+': '+i[2])
    name = st.selectbox("我是谁来着?哦对，我是 ", ['空中飞人','神金','我没有名字','派蒙','三月七','安比'])
    new_message = st.text_input('我想吐槽 ')
    if st.button('发送吐槽'):
        messages_list.append([str(int(messages_list[-1][0])+1), name, new_message])
        with open('Leoleave_message.txt', 'w', encoding='utf-8') as f:
            message = ''
            for i in messages_list:
                message += i[0] + '#' + i[1] + '#' + i[2] + '\n'
            message = message[:-1]    
            f.write(message)

#------------------工作区------------------
if page == '音乐推荐':
    page_1()
elif page == '游戏推荐':
    page_2()
elif page == '动漫推荐':
    page_3()
elif page == "吐槽专区":
    page_4()
