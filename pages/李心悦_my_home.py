import streamlit as st
from PIL import Image
page = st.sidebar.radio("main",['intro','disclaimer','ep','music', 'test','secret'])

def page_1():
    "intro"
    st.markdown("<h1 style='text-align: center; color: black;'>优雅四元数</h1>", unsafe_allow_html=True)
    st.markdown("<h2 style='text-align: center; color: grey;'>-Elegant Quaternion-</h2>", unsafe_allow_html=True)
    st.write("-------------------------------------------------------------------------------------")
    st.image("李心悦_power.jpg")
    st.write("-------------------------------------------------------------------------------------")
    st.write("艺梦世界。听起来很美好是吧？的确。它的住人们都衣食无忧，有麻烦的话也可以请管理员帮忙。\n 不过这么完美的世界，竟然还会有人想要把它毁灭掉？")
    st.write("而这些人，就是母亲们…… 她们众志成城，准备让艺梦世界陷入灾难，然后再用暴力的铁拳统治世界，让所有不是母亲的人都笼罩在母亲的阴影之下…… 简直就是一股反和平势力。")
    st.write("（母亲内心OS：你们都没有见识到战争时代的辛苦！我们是在帮你们！你们还不感恩！啊啊啊jsebog hwerifu c！）")
    st.write(" ")
    st.write("别慌。我不是什么叛逆小青年。我10岁就想出了邪恶母亲这档事，现在只是稍微修缮一下。")
    st.write("不过有压迫就有反抗。神明们给了艺梦世界的人们幻想之力（还给了个别几个人神力），以便她们把母亲们驱逐出艺梦世界，把自己的天地夺回。")
    st.write(" ")
    st.write("顺便一提，管理员们大多数都是女的。")

def page_2():
    "disclaimer"
    st.markdown("<h1 style='text-align: center; color: red;'>免责声明：<", unsafe_allow_html=True)
    st.markdown(":red[这个世界是完全虚构的，它也不代表我真实的想法!]", unsafe_allow_html=False)
    st.markdown(":red[如有雷同，纯属巧合！]", unsafe_allow_html=False)
    st.markdown(":red[如有阅读本网站造成的财物与人身伤害，本人概不负责。]", unsafe_allow_html=False)

def page_3():
    "ep"
    st.write('施工中……')

def page_4():
    "music"
    st.markdown("<h1 style='text-align: center; color: green;'>清醒梦小乐章<", unsafe_allow_html=True)
    st.write("-------------------------------------------------------------------------------------")
    st.write("#### 1. Recalcitration (作曲：Blackhole)")
    st.audio("李心悦_1enter.mp3")
    st.write("随着一心入睡，她周围的景象逐渐从一片黑变成一片凌晨的天空。")
    st.write("“嗯？成功了？”")
    st.write("她自从听说过艺梦世界就非常想进去一探究竟。不过，我们都知道，艺梦世界是虚构的，所以我们这些现实世界的住人，就只能眼巴巴地望着幻想住人们的美好生活。")
    st.write("不过，她貌似是读了太多关于艺梦世界的作品，而且还跟它的创作者有联系，所以就在脑内构建了一个接近艺梦世界的世界进去冒险。")
    st.write("早在之前，她就在梦中造出了其他世界，并在其中畅游。她是一个做清醒梦的专家，很容易就可以改变她做的梦。")
    st.write("“应该是成功了吧？太好了！”")
    st.write("她挥了挥手，并且改变了她飞行的方向。她眼下的景色瞬间从一片湖变成了一片森林。她现在面朝太阳，不过并没有感到刺眼。")
    st.write("透过一层朝雾，她看见了一条小道。")
    st.write("--")
    st.write("这就是第一首曲子。")
    st.write("它入选的原因主要是因为开头与结尾。 我听到开头就想到了一个人飞过一片幽深的森林上空。")
    st.write("很巧的是，歌名的意思是“不服从/踢回去/执拗”。 在特意查之前，我还以为这个词是关于钙的……")
    st.write("-------------------------------------------------------------------------------------")
    st.write("#### 2. Renascent (作曲：Blackhole)")
    st.audio("李心悦_2genso.mp3")
    st.write("她在桥上遇到了一位粉色头发，头戴草莓的玩家。")
    st.write("那位玩家一看见一心就走上去，邀请一心跟她玩。")   
    st.write("一心答应了。")
    st.write("--")
    st.write("入选原因：结尾。")
    st.write("-------------------------------------------------------------------------------------")
    st.write("#### 3. Surface (作曲：Dimrain47)")
    st.audio("李心悦_3surface.mp3")
    st.write("那位玩家的力量，属实是非常强大。创造彩虹，施展大魔法，都在她的掌控之下。玩累了，就在海边的石头上画画看着月亮。")
    st.write("等回过神来，她的心中升起了一丝担心。")
    st.write("她呆在这里未免有点太久了……")
    st.write("-------------------------------------------------------------------------------------")
    st.write("#### 4. Blood Coagulant (作曲：DM Dokuro)")
    st.audio("李心悦_4mom.mp3")
    st.write("--")
    st.write("如果要完全地介绍我的幻想世界，就不得不能选一首曲子来介绍那些邪恶的母亲们啦！")
    st.write("这首曲子我觉得我选的非常好。开头，00：51那里的混乱，01：34那里的更多混乱，与随后而来的呼声，都是这首曲子入选的原因。")
    st.write("在现在的设定之中，她们非常凶暴，总是喜欢给上面的世界造成苦难（照她们的说辞，这样会让她们的孩子“坚强起来”），而且还口口声声说她们是真正的神。（管理员与四大天王：开玩笑的吧？）")
    st.write("还有，母亲制造的小手工会被非常珍视，甚至有专属的拍卖会。 不过，【这条信息已被宇宙爱母协会消除】")
    st.write("-------------------------------------------------------------------------------------")
    st.write("#### 5. At the Speed of Light (作曲：Dimrain47)")
    st.audio("李心悦_5atsol.mp3")
    st.write("-论理式-")
    st.write("“地狱其实没那么恐怖。无非就是热了一点，暗了一点，管理员们也很少下来。”（他是地狱最强者，所以说出这话也是理所当然的。）")
    st.write("-电子透帕斯-")
    st.write("在月亮上的景象肯定非常不可思议吧。按照他的说法，月亮上的地面其实是黑色的，岩石里还镶嵌了五颜六色的宝石。")
    st.write("-恩赛法罗斯-")
    st.write("在风暴洋的中心度日肯定非同凡响吧，毕竟几乎每分钟都有雷落在你的附近。不过真亏她能忍得了80年的孤独啊…… 即使她有了能上网的电脑，我个人感觉也不能缓解吧。")
    st.write("*")
    st.write("他们因为各种原因，定居在了与世隔绝的地方。他们回来的时候，肯定会对现在的艺梦世界又惊又喜吧。")
    st.write("--")
    st.write("我选这首歌的时候，脑子里想的是“与地球隔绝”这件事。")
    st.write("作曲家自己说了他是以“在宇宙之中飞行，探索其奥秘”这个印象作曲，不过自从*某个*关卡的出现，它就跟‘地狱’挂钩了……")
    st.write("-------------------------------------------------------------------------------------")
    st.write("#### 6. Turn To The Light (作曲：島白)")
    st.audio("李心悦_6light.mp3")
    st.write("“啥？你说你想走？看来没办法了呢。”")
    st.write("“我跟你搭个车去中心之塔吧。你只要搭乘那里的电梯到232层，上去找一个叫深乐的神就行了……”")
    st.write("一心点了点头。")
    st.write("“那，下次见吧。记得回来看看哦！”")
    st.write("一心回头看那位玩家的时候，在她的眼里看出了不舍。")
    st.write("-------------------------------------------------------------------------------------")
    st.write("#### 7. Through The Gates(作曲：Dimrain47)")
    st.audio("李心悦_7quat.mp3")
    st.write("电梯门缓慢地打开了。映入眼帘的是一个卧室，一位灰绿头发的神坐在床边的椅子上。")
    st.write("“你是一心对吧？我是深乐，你要找的那位。想回到现实世界的话，就躺这床上，盖好被子就行了。剩下的事情我来做。”")
    st.write("一心照做了。她对眼前这个神深信不疑。")
    st.write("深乐从口袋之中拿出了一个四面体。它发出的光让一心情不自禁的感到了一股睡意。她逐渐闭上了眼睛。")
    st.write("她在梦中梦之中，似乎看到了四位战士在梦之世界的奇妙冒险……")
    st.write("--")
    st.write("这就是最后一首曲子啦！别担心，一心有回到现实世界。不过她貌似因此睡过头了……")
    st.write("1：11到1：36是我最喜欢的部分。")

def page_5():
    'test'
    st.markdown("<h1 style='text-align: center; color: purple;'>小测试<", unsafe_allow_html=True)
    #st.write('为了完整效果，请不要取消任何勾选！')
    st.write("-------------------------------------------------------------------------------------")
    st.write('假设你有电子宠物的话，你会给它点什么饮料？（现实的效果会对它适用，就像喝能量饮料睡不着）')
    cbf1, cbf2 = st.columns(2)
    with cbf1:
        cb1 = st.checkbox('水')
        cb2 = st.checkbox('果汁')
    with cbf2:
        cb3 = st.checkbox('能量饮料')
        cb4 = st.checkbox('可乐')   
    if cb1:
        st.write('你获得了3分')
    elif cb2:
        st.write('你获得了2分')
    elif cb3 or cb4:
        st.write('你获得了1分')
    st.write("-------------------------------------------------------------------------------------")
    st.write('在下面的选项中，你最喜欢什么颜色组合？')
    st.image("李心悦_colex.png")
    cbf3, cbf4 = st.columns(2)
    with cbf3:
        cb5 = st.checkbox('深蓝色与青色')
        cb6 = st.checkbox('绿色，黄色，紫色与品红色')
    with cbf4:
        cb7 = st.checkbox('橙色，黄色与紫色')
        cb8 = st.checkbox('红色与黑色')   
    if cb5:
        st.write('你获得了3分')
    elif cb6:
        st.write('你获得了2分')
    elif cb7:
        st.write('你获得了3分')
    elif cb8:
        st.write('你获得了1分')
    st.write("-------------------------------------------------------------------------------------")
    choice3 = st.radio('哪句话最接近你的性格？', ['士可杀不可辱', '退一步海阔天空', '书本是人类进步的阶梯'])
    if choice3 == '士可杀不可辱':
        sct=3
    #elif choice3 ==   
    #elif choice3
    st.write ("你获得了", sct ,"分")
    st.write("未完待续…… 分越高，你在艺梦世界就会活得越好。")

        
def page_6():
    'secret'
    st.write("施工中……")
    c1, c2, c3, c4 = st.columns(4)
    with c1:
        st.text_input(label = "pw", value="", max_chars=1, key="ak", type="default", label_visibility="hidden")
        #st.text_area(label = "1", value="", height=30, max_chars=1, key="ak",  label_visibility="hidden")
    with c2:
        st.text_input(label = "pw", value="", max_chars=1, key="bk", type="default", label_visibility="hidden")
        #st.text_area(label = "2", value="", height=30, max_chars=1, key="bk",  label_visibility="hidden")
    with c3:
        st.text_input(label = "pw", value="", max_chars=1, key="ck", type="default", label_visibility="hidden")
        #st.text_area(label = "3", value="", height=30, max_chars=1, key="ck",  label_visibility="hidden")
    with c4:
        st.text_input(label = "pw", value="", max_chars=1, key="dk", type="default", label_visibility="hidden")
        #st.text_area(label = "4", value="", height=30, max_chars=1, key="dk",  label_visibility="hidden")
        
if page == 'intro':
    page_1()
elif page == 'disclaimer':
    page_2()
elif page == 'ep':
    page_3()
elif page == 'music':
    page_4()
elif page == 'test':
    page_5()
elif page == 'secret':
    page_6()