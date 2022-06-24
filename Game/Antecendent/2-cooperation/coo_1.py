# coding:utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from naoqi import ALProxy
import Tkinter as tk
from PIL import ImageTk, Image
import random
import tkMessageBox
import pandas as pd
import time


ip = '192.168.1.107'
# 连接机器人，修改ip地址即可，设定语言为中文
tts = ALProxy("ALTextToSpeech", ip, 9559)
tts.setLanguage("Chinese")
# tts.say("我们开始吧！")
leds = ALProxy('ALLeds', ip, 9559)

# 新建窗口，设定大小
deck1 = tk.Toplevel()
deck1.title("Play with Nao Robot - Round 2")
deck1.configure(bg="white")
# 定义window size，当前屏幕大小
# deck1.minsize(width=deck1.winfo_screenwidth(), height=deck1.winfo_screenheight())
deck1.attributes('-fullscreen', True)
# deck.geometry("1080x720")


frame = tk.Frame(deck1, bg='lightblue')
frame.pack(side='top', expand='no', fill='x')

frame_l = tk.Frame(deck1, bg="white")
frame_l.pack(side='left', expand='yes', fill='y')

frame_r = tk.Frame(deck1, bg="white")
frame_r.pack(side='right', expand='yes', fill='y')

cardback = ImageTk.PhotoImage(Image.open("C:/Users/hci/Documents/exp_cooperation/images_0/robot_cooperation.png"))
cards = []
names = []
grades = pd.read_csv('cooperation1.csv')
count_match = grades['count_match'][1]
count_lose = grades['count_lose'][1]
count_grades = 1 * (count_match - count_lose)

period = 0
session = 1
random_list = [0, 1, 2, 3, 4, 5, 6, 7, 8]
rank_ID = 0
participant_record = []
participant_record_rankID = []
participant_record_cardsNum = []
participant_record_buttonNum = []
participant_record_period = []
participant_record_left = []
participant_record_right = []
participant_record_choice = []

result_match = ['太棒了', '真厉害', '真好', '哈哈', '真开心']
result_mismatch = ['真遗憾', '真可惜', '唉', '要继续努力', '哎呀', '不开心']


# 删除所有控件
def clear_start():
    frame.destroy()
    frame_l.destroy()
    frame_r.destroy()


def rank_cards():
    global count_match, count_lose, count_grades, session, period, participant_record, rank_ID, names

    clear_start()
    frame_top = tk.Frame(deck1, bg='lightblue')
    frame_top.pack(side='top', expand='no', fill='x')

    frame_l = tk.Frame(deck1, bg='white')
    frame_l.pack(side='left', expand='yes', fill='y')

    frame_r = tk.Frame(deck1, bg="white")
    frame_r.pack(side='right', expand='yes', fill='y')

    label_1 = tk.Label(frame_top, bg='lightblue', text='请根据刚刚的互动过程猜测 Nao 对这些图片的喜爱度并按顺序点击', font=('微软雅黑', 24), fg='white', width=deck1.winfo_screenwidth(), height=4)
    label_1.pack()

    rank_l = tk.Label(frame_l, bg='white', text='Nao喜爱度排序', font=('微软雅黑', 18), fg='black', width=30, height=3)
    rank1_l = tk.Label(frame_l, bg='white',  text='第一位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank2_l = tk.Label(frame_l, bg='white',  text='第二位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank3_l = tk.Label(frame_l, bg='white',  text='第三位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank4_l = tk.Label(frame_l, bg='white',  text='第四位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank5_l = tk.Label(frame_l, bg='white',  text='第五位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank6_l = tk.Label(frame_l, bg='white',  text='第六位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank7_l = tk.Label(frame_l, bg='white',  text='第七位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank8_l = tk.Label(frame_l, bg='white',  text='第八位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)
    rank9_l = tk.Label(frame_l, bg='white',  text='第九位：？', font=('微软雅黑', 14), fg='black', width=30, height=2)

    rank_l.pack()
    rank1_l.pack()
    rank2_l.pack()
    rank3_l.pack()
    rank4_l.pack()
    rank5_l.pack()
    rank6_l.pack()
    rank7_l.pack()
    rank8_l.pack()
    rank9_l.pack()

    del cards[:]
    for x in range(11, 20):
        cards.append(ImageTk.PhotoImage(Image.open("images_%s/card_%s.png" % (str(session), str(x)))))
    random.shuffle(random_list)

    # 定义好9个button
    b_1 = tk.Button(frame_r, bg='white', image=cards[random_list[0]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(1, random_list[0], str(names[session][random_list[0]])): rank_record(j))
    b_2 = tk.Button(frame_r, bg='white', image=cards[random_list[1]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(2, random_list[1], names[session][random_list[1]]): rank_record(j))
    b_3 = tk.Button(frame_r, bg='white', image=cards[random_list[2]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(3, random_list[2], names[session][random_list[2]]): rank_record(j))
    b_4 = tk.Button(frame_r, bg='white', image=cards[random_list[3]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(4, random_list[3], names[session][random_list[3]]): rank_record(j))
    b_5 = tk.Button(frame_r, bg='white', image=cards[random_list[4]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(5, random_list[4], names[session][random_list[4]]): rank_record(j))
    b_6 = tk.Button(frame_r, bg='white', image=cards[random_list[5]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(6, random_list[5], names[session][random_list[5]]): rank_record(j))
    b_7 = tk.Button(frame_r, bg='white', image=cards[random_list[6]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(7, random_list[6], names[session][random_list[6]]): rank_record(j))
    b_8 = tk.Button(frame_r, bg='white', image=cards[random_list[7]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(8, random_list[7], names[session][random_list[7]]): rank_record(j))
    b_9 = tk.Button(frame_r, bg='white', image=cards[random_list[8]], width=250, height=250, borderwidth=0, padx=10, pady=10,
                    command=lambda j=(9, random_list[8], names[session][random_list[8]]): rank_record(j))

    # 排列button的位置
    b_1.grid(row=0, column=0)
    b_2.grid(row=0, column=1)
    b_3.grid(row=0, column=2)
    b_4.grid(row=1, column=0)
    b_5.grid(row=1, column=1)
    b_6.grid(row=1, column=2)
    b_7.grid(row=2, column=0)
    b_8.grid(row=2, column=1)
    b_9.grid(row=2, column=2)

    def rank_record(args):
        global count_match, count_lose, count_grades, session, period, rank_ID, names, participant_record_rankID, participant_record_buttonNum, participant_record_cardsNum

        rank_ID += 1
        button_num = args[0]
        cards_num = args[1]+1
        # cards_name = str(args[2])

        participant_record_rankID.append(rank_ID)
        participant_record_buttonNum.append(button_num)
        participant_record_cardsNum.append(cards_num)

        print (participant_record)
        # 用if语句
        if button_num == 1:
            b_1.config(state=tk.DISABLED)
        if button_num == 2:
            b_2.config(state=tk.DISABLED)
        if button_num == 3:
            b_3.config(state=tk.DISABLED)
        if button_num == 4:
            b_4.config(state=tk.DISABLED)
        if button_num == 5:
            b_5.config(state=tk.DISABLED)
        if button_num == 6:
            b_6.config(state=tk.DISABLED)
        if button_num == 7:
            b_7.config(state=tk.DISABLED)
        if button_num == 8:
            b_8.config(state=tk.DISABLED)
        if button_num == 9:
            b_9.config(state=tk.DISABLED)

        if rank_ID == 1:
            rank1_l.config(text='第一位：%s' % str(names[session][cards_num-1]))
        if rank_ID == 2:
            rank2_l.config(text='第二位：%s' % str(names[session][cards_num - 1]))
        if rank_ID == 3:
            rank3_l.config(text='第三位：%s' % str(names[session][cards_num-1]))
        if rank_ID == 4:
            rank4_l.config(text='第四位：%s' % str(names[session][cards_num - 1]))
        if rank_ID == 5:
            rank5_l.config(text='第五位：%s' % str(names[session][cards_num-1]))
        if rank_ID == 6:
            rank6_l.config(text='第六位：%s' % str(names[session][cards_num - 1]))
        if rank_ID == 7:
            rank7_l.config(text='第七位：%s' % str(names[session][cards_num-1]))
        if rank_ID == 8:
            rank8_l.config(text='第八位：%s' % str(names[session][cards_num - 1]))
        if rank_ID == 9:
            rank9_l.config(text='第九位：%s' % str(names[session][cards_num - 1]))
            dataframe = pd.DataFrame({'rank_ID': participant_record_rankID, 'button_num': participant_record_buttonNum,
                                      'cards_num': participant_record_cardsNum, 'count_match': count_match,
                                      'count_lose': count_lose})
            csv_name = time.time()
            dataframe.to_csv('cooperation2.csv', index=False, sep=',')
            tkMessageBox.showinfo('next', '进入下一主题', parent=deck1)
            import coo_2




# 定义函数refresh
def refresh():
    global random_list, session, period, count_match, count_lose, names, count_grades, participant_record_period, participant_record_left, participant_record_right, participant_record_choice
    print (period)
    random.shuffle(random_list)
    print('new random list:%s' % (str(random_list)))
    if period == 21:
        dataframe_choice = pd.DataFrame({'Period': participant_record_period, 'LeftCard': participant_record_left,
                                         'RightCard': participant_record_right, 'Choice': participant_record_choice})
        dataframe_choice.to_csv('cooperation2_choice.csv', index=False, sep=',')
        rank_cards()
    else:
        del cards[:]
        for x in range(1, 10):
            cards.append(ImageTk.PhotoImage(Image.open("images_%s/card_%s.png" % (str(session), str(x)))))
        b_1 = tk.Button(frame_r, bg='white', image=cards[random_list[0]], width=360, height=360, borderwidth=0, padx=10,
                        pady=10, command=lambda j=(1, random_list[0], random_list[1]): click(j))
        b_2 = tk.Button(frame_r, bg='white', image=cards[random_list[1]], width=360, height=360, borderwidth=0, padx=10,
                        pady=10, command=lambda j=(2, random_list[0], random_list[1]): click(j))
        mid = tk.Label(frame_r, bg='white', text=' ', width=15, font=('Arial', 14))
        right = tk.Label(frame_r, bg='white', text='', width=5)
        label_1 = tk.Label(frame_r, bg='white', text='', width=25, height=7)
        label_2 = tk.Label(frame_r, bg='white', text='', width=25, height=4)
        label_1.grid(row=0, column=0, columnspan=2)
        label_2.grid(row=1, column=0, columnspan=2)
        b_1.grid(row=2, column=0)
        mid.grid(row=2, column=1)
        b_2.grid(row=2, column=2)
        right.grid(row=2, column=3)


# 定义函数click
def click(args):
    global names, random_list, period, session, count_match, count_lose, cardback, count_grades, participant_record_period, participant_record_left, participant_record_right, participant_record_choice

    period += 1
    button_num = args[0]
    card_n1 = args[1]
    card_n2 = args[2]

    participant_record_period.append(period)
    participant_record_left.append(card_n1)
    participant_record_right.append(card_n2)
    participant_record_choice.append(button_num)

    # 判断用户选择的是图1还是图2，图1对应的是random_list[0]，图2对应的是random_list[1]
    if button_num == 1:
        if card_n1 < card_n2:
            count_match += 1
            count_grades = 1 * (count_match - count_lose)
            var_tmp = str('我更喜欢的是，%s' % str(names[session][card_n1]))
            tts.say(var_tmp)

            label_r.config(text='Nao选择的是：【%s】' % str(names[session][card_n1]), fg='darkred')
            button_r.config(image=cards[card_n1])
            tkMessageBox.showinfo('confirm', '匹配成功，恭喜你们：+1分', parent=deck1)

            leds.fadeRGB('FaceLeds', 256 * 256 * 255 + 256 * 255 + 0, 0.1)
            random.shuffle(result_match)
            tts.say(str(result_match[0])+str('，你选对了'))
            leds.fade('FaceLeds', 0.5, 1)

            tkMessageBox.showinfo('confirm', '下一轮', parent=deck1)
            count_match_l.config(text='猜对次数: %d' % count_match)
            count_grades_l.config(text='当前成绩： %d' % count_grades)
            button_r.config(image=cardback)
            label_r.config(text='希望你能选对！', fg='black')
            period_l.config(text='第%d轮/共21轮' % (period + 1))
            refresh()
        else:
            count_lose += 1
            count_grades = 1 * (count_match - count_lose)
            var_tmp = str('我更喜欢的是，%s' % str(names[session][card_n2]))
            tts.say(var_tmp)

            label_r.config(text='Nao选择的是：【%s】' % str(names[session][card_n2]), fg='black')
            button_r.config(image=cards[card_n2])
            tkMessageBox.showinfo('confirm', '匹配失败，真遗憾：-1分', parent=deck1)

            leds.fadeRGB('FaceLeds', 256 * 256 * 0 + 256*0 + 255, 0.1)
            random.shuffle(result_mismatch)
            tts.say(str(result_mismatch[0]) + str('，这次没有选对'))
            leds.fade('FaceLeds', 0.5, 1)

            tkMessageBox.showinfo('confirm', '下一轮', parent=deck1)
            count_lose_l.config(text='失败次数: %d' % count_lose)
            count_grades_l.config(text='当前成绩： %d' % count_grades)
            label_r.config(text='希望你能选对！', fg='black')
            button_r.config(image=cardback)
            period_l.config(text='第%d轮/共21轮' % (period + 1))
            refresh()
    else:
        if card_n1 < card_n2:
            count_lose += 1
            count_grades = 1 * (count_match - count_lose)
            var_tmp = str('我更喜欢的是，%s' % str(names[session][card_n1]))
            tts.say(var_tmp)

            label_r.config(text='Nao选择的是：【%s】' % str(names[session][card_n1]), fg='black')
            button_r.config(image=cards[card_n1])
            tkMessageBox.showinfo('confirm', '真遗憾：-1分', parent=deck1)

            leds.fadeRGB('FaceLeds', 256 * 256 * 0 + 256*0 + 255, 0.1)
            random.shuffle(result_mismatch)
            tts.say(str(result_mismatch[0]) + str('，这次没有选对'))
            leds.fade('FaceLeds', 0.5, 1)

            tkMessageBox.showinfo('confirm', '下一轮', parent=deck1)
            count_lose_l.config(text='失败次数: %d' % count_lose)
            count_grades_l.config(text='当前成绩： %d' % count_grades)
            label_r.config(text='希望你能选对！', fg='black')
            button_r.config(image=cardback)
            period_l.config(text='第%d轮/共21轮' % (period + 1))
            refresh()
        else:
            count_match += 1
            count_grades = 1 * (count_match - count_lose)
            var_tmp = str('我更喜欢的是，%s' % str(names[session][card_n2]))
            tts.say(var_tmp)

            label_r.config(text='Nao选择的是：【%s】' % str(names[session][card_n2]), fg='darkred')
            button_r.config(image=cards[card_n2])
            tkMessageBox.showinfo('confirm', '恭喜你们：+1分', parent=deck1)

            leds.fadeRGB('FaceLeds', 256 * 256 * 255 + 256*255 + 0, 0.1)
            random.shuffle(result_match)
            tts.say(str(result_match[0])+str('，你选对了'))
            leds.fade('FaceLeds', 0.5, 1)

            tkMessageBox.showinfo('confirm', '下一轮', parent=deck1)
            count_match_l.config(text='猜对次数: %d' % count_match)
            count_grades_l.config(text='当前成绩： %d' % count_grades)
            button_r.config(image=cardback)
            label_r.config(text='希望你能选对！', fg='black')
            period_l.config(text='第%d轮/共21轮' % (period + 1))
            refresh()


# 展示nao的照片和配对结果
for x in range(1, 10):
    cards.append(ImageTk.PhotoImage(Image.open("images_%s/card_%s.png" % (str(session), str(x)))))

topic = ['民族风情', '剪影星空', '太空探索', '西湖风光', '水果荟萃', '城市建筑']

name_1 = ['灯笼', '飞燕', '牛牛', '古楼', '荷花灯', '火车', '金鱼', '舞狮', '燕子']
name_2 = ['幽蓝星空', '湖边星空', '黄昏星空', '原野星空', '幻彩星空', '山野星空', '沙漠星空', '神秘星空', '幻影星空']
name_3 = ['天王星', '海王星', '木星', '火星', '太阳', '土星', '冥王星', '月球', '金星']
name_4 = ['断桥残雪', '花港观鱼', '雷峰夕照', '柳浪闻莺', '平湖秋月', '曲院风荷', '三潭映月', '双峰插云', '苏堤春晓']
name_5 = ['菠萝', '草莓', '橙子', '火龙果', '猕猴桃', '牛油果', '西瓜', '香蕉', '樱桃']
name_6 = ['深圳', '上海', '青岛', '广州', '北京', '成都', '苏州', '西安', '重庆']

names = [name_1, name_2, name_3, name_4, name_5, name_6]

tmp = deck1.winfo_screenwidth() / 70
session_l = tk.Label(frame, text='主题 2：%s' % str(topic[session]), bg='lightblue', font=("微软雅黑", 16), fg='black',
                     width=tmp, height=4)
period_l = tk.Label(frame, text='第%d轮/共21轮' % (period + 1), bg='lightblue', font=("微软雅黑", 16), fg='black', width=tmp,
                    height=4)
count_match_l = tk.Label(frame, text='猜中次数:   %d' % count_match, bg='lightblue', font=("微软雅黑", 16), width=tmp,
                         fg='black', height=4)
count_lose_l = tk.Label(frame, text='失败次数:   %d' % count_lose, bg='lightblue', font=("微软雅黑", 16), width=tmp, fg='black',
                        height=4)
count_grades_l = tk.Label(frame, text='当前成绩： %d' % count_grades, bg='lightblue', font=("微软雅黑", 16), width=tmp,
                          fg='black', height=4)

session_l.grid(row=0, column=0)
period_l.grid(row=0, column=1)
count_match_l.grid(row=0, column=2)
count_lose_l.grid(row=0, column=3)
count_grades_l.grid(row=0, column=4)

label_r = tk.Label(frame_l, bg='white', font=("微软雅黑", 14), fg='black', text='希望你能选对！', width=25, height=7)
label_r.pack()

button_r = tk.Button(frame_l, bg='white', image=cardback, width=450, height=450, borderwidth=0, padx=0, pady=0)
button_r.pack()

random.shuffle(random_list)

label_1 = tk.Label(frame_r, bg='white', text='', width=25, height=7)
label_2 = tk.Label(frame_r, bg='white', text='', width=25, height=4)
# 定义主页的两个button
b_1 = tk.Button(frame_r, bg='white', image=cards[random_list[0]], width=360, height=360, borderwidth=0, padx=10, pady=10,
                command=lambda j=(1, random_list[0], random_list[1]): click(j))
b_2 = tk.Button(frame_r, bg='white', image=cards[random_list[1]], width=360, height=360, borderwidth=0, padx=10, pady=10,
                command=lambda j=(2, random_list[0], random_list[1]): click(j))
mid = tk.Label(frame_r, bg='white', text=' ', width=15, font=('Arial', 14))
right = tk.Label(frame_r, bg='white', text='', width=5)

label_1.grid(row=0, column=0, columnspan=2)
label_2.grid(row=1, column=0, columnspan=2)
b_1.grid(row=2, column=0)
mid.grid(row=2, column=1)
b_2.grid(row=2, column=2)
right.grid(row=2, column=3)

tts.say('希望你都猜对了！准备开始新一组图片，我会好好表现的！')

deck1.mainloop()
