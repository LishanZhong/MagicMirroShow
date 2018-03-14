import Client
import json

def onMessage(msg):
    if msg['R'] == 'checkinok':
            print('Connected.')
    if msg['R'] == 'ping':
        Client.sendall(b'{\"M\":\"pong\"}\n')
    if msg['R'] == 'ok':
        print('操作成功完成.')

    if msg['R'] == 'weather':
        global weather
        weather = json.loads(msg['V'])
        print(weather)

    if msg['R'] == 'sensor':
        global sensor
        sensor = msg['V']
        print(sensor)

    if msg['R'] == 'message':
        global message
        message = msg['V']
        print(message)
        # for one in msg['V']:
        #     print('收到了消息：\n标题：' + one['title'] + "\n内容：" + one['content'] + "\n")


def onOffline():
    print("掉线了,尝试重新连接")
    initClient()



def initClient():
    c = Client.Client()
    c.connect()
    c.setCallback(onMessage, onOffline)

if __name__ == '__main__':
    initClient()
