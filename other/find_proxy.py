import re
import os
import sys
import request
from urllib import request, parse
import random
from bs4 import BeautifulSoup

# content = request.urlopen("http://www.proxynova.com/proxy-server-list/country-cn/").read()
# soup = BeautifulSoup(content, 'lxml')

# print(soup)

import _dummy_thread

import itchat
from itchat.content import *
import time



@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def group_reply(msg):
    # # global replyToGroupChat
    # # global result.functionStatus

    if msg['isAt']:
        itchat.send('@%s\u2005I received: %s' % (msg['ActualNickName'], msg['Content']), msg['FromUserName'])   
    # # reply = get_response(msg['Text'])
    # if replyToGroupChat != result.functionStatus:
    #     if replyToGroupChat:
    #         @itchat.msg_register(TEXT, isGroupChat=True)
    #         def group_text_reply(msg):
    #             if u'关闭' in msg['Text']:
    #                 replyToGroupChat = False
    #                 return u'已关闭'
    #             elif u'开启' in msg['Text']:
    #                 return u'已经在运行'
    #             return u'输入"关闭"或者"开启"测试功能'
    #     else:
    #         @itchat.msg_register(TEXT, isGroupChat=True)
    #         def group_text_reply(msg):
    #             if u'开启' in msg['Text']:
    #                 replyToGroupChat = True
    #                 return u'重新开启成功'
    #     result.functionStatus = replyToGroupChat

    # return itchat.send_msg('已经收到%s的文本消息，消息内容为%s'%(user, msg['Text']),toUserName=msg['FromUserName'])

    # return reply or default_reply
result= {"replyToGroupChat": True, 
"functionStatus" : False}

@itchat.msg_register(itchat.content.TEXT,isGroupChat=True)
def change_function(msg):

    if result.get('replyToGroupChat') != result.get('functionStatus'):
        if result.get('replyToGroupChat'):
            print(result.get('replyToGroupChat'))
            @itchat.msg_register(itchat.content.TEXT, isGroupChat = True)
            
            def group_text_reply(msg):
                if '关闭' in msg['Text']:
                    print(msg.Text, end=",")
                    result['replyToGroupChat']= False
                    print(result.get('replyToGroupChat'), result['functionStatus'])
                    return '已关闭'

                elif '开启' in msg['Text']:
                    print(msg.Text, end =",")
                    result['replyToGroupChat']= True
                    print(result.get('replyToGroupChat'), result['functionStatus'])
                    return '已经在运行'
                return '输入"关闭"或者"开启"测试功能'

    else:
        @itchat.msg_register(itchat.content.TEXT, isGroupChat = True)
        def group_text_reply(msg):
            if '开启' in msg['Text']:
                print(msg.Text)
                result['replyToGroupChat'] = True
                print(result.get('replyToGroupChat'), result['functionStatus'])
                return '重新开启成功'
            return '输入"关闭"或者"开启"测试功能'

itchat.auto_login(hotReload=True)

_dummy_thread.start_new_thread(itchat.run, ())

# while 1:
#     # change_function()
#     time.sleep(.1)

