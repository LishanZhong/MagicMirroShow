import Client
import json
import Show

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
        message = msg['V']
        global msgListMain
        Show.msgList.append([message[0]['title'], message[0]['content']])
        msgListMain = Show.msgList


def onOffline():
    print("掉线了,尝试重新连接")
    initClient()



def initClient():
    c = Client.Client()
    c.connect()
    c.setCallback(onMessage, onOffline)

if __name__ == '__main__':
    initClient()
