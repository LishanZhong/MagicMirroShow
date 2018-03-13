import Client

def onMessage(msg):
    if msg['R'] == 'checkinok':
            print('Connected.')
    if msg['R'] == 'ping':
        Client.sendall(b'{\"M\":\"pong\"}\n')
    if msg['R'] == 'ok':
        print('操作成功完成.')
    if msg['R'] == 'weather':
        print('天气：' + msg['V'])
    if msg['R'] == 'sensor':
        print('传感器数据' + str(msg['V']))

    if msg['R'] == 'message':
        for one in msg['V']:
            print('收到了消息：\n标题：' + one['title'] + "\n内容：" + one['content'] + "\n")


def onOffline():
    print("掉线了,尝试重新连接")
    initClient()



def initClient():
    c = Client.Client()
    c.connect()
    c.setCallback(onMessage, onOffline)


initClient()

