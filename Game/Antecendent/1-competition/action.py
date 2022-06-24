# coding:utf-8

import sys

reload(sys)
sys.setdefaultencoding('utf8')

from naoqi import ALProxy

# 连接机器人，修改ip地址即可，设定语言为中文
tts = ALProxy("ALTextToSpeech", "192.168.1.107", 9559)
tts.setLanguage("Chinese")
postureProxy = ALProxy("ALRobotPosture", "192.168.1.107", 9559)
leds = ALProxy('ALLeds', '192.168.1.107', 9559)

motion = ALProxy("ALMotion", "192.168.1.107", 9559)

motion.openHand('Hand')

leds.fade('FaceLeds', 0.5, 1)

tts.say('hi')

leds.fadeRGB('FaceLeds', 256*256*255 + 256*97 + 0, 1)
leds.fade('FaceLeds', 0.5, 1)



leds.fadeRGB('FaceLeds', 256*256*0 + 256*0 + 255, 1)
leds.fade('FaceLeds', 0.5, 1)
