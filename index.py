import json
import requests
import datetime
import re
import random
'''

2022/8/23
Locustdy
有问题请联系QQ：1424305473

'''

appID = "" #微信测试平台appID
appsecret = "" #微信测试平台appsecret
User = '' #微信测试平台用户列表微信号
Message_id = '' #微信测试平台模板消息接口ID
string='' #计算时间差时间
nanbirthday='' #你的生日 格式 mm-dd 例如 12-29
nvbirthday='' #女朋友的生日
city='' #天气显示城市
mss='' #你想说的话
week_list = ["星期一","星期二","星期三","星期四","星期五","星期六","星期日"]
#下边不用动了
def Accesstoken():
    url = f"https://api.weixin.qq.com/cgi-bin/token?grant_type=client_credential&appid={appID}&secret={appsecret}"
    resp = requests.get(url)
    result = resp.json()
    if 'access_token' in result:
        return result['access_token']
    else:
        return result

def send_message():
    url=f"https://api.weixin.qq.com/cgi-bin/message/template/send?access_token={Accesstoken()}"
    data=json.dumps(message())
    resp= requests.post(url,data=data)
    result=resp.json()
    if result["errcode"]==0:
        return("发送成功")
    else:
        return("发送失败")


def tz():
    url=f"https://api.uomg.com/api/rand.qinghua"
#    url=f"https://v2.alapi.cn/api/dog?token=uRvtwvbA7IuS2zBB"
    resp=requests.get(url)
    result=resp.json()
    return result['content']
def lovets():
    a=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    a=datetime.datetime.strptime(a,'%Y-%m-%d %H:%M:%S')
    b=datetime.datetime.strptime(string,'%Y-%m-%d %H:%M:%S')
    a=a-b
    s=a.seconds
    m,s=divmod(s,60)
    h,m=divmod(m,60)
    time=str(a.days)+"天"+str(h)+"小时"+str(m)+"分"+str(s)+"秒"
#    print(a.days,"天%02d小时%02d分%02d秒" % (h, m, s),sep='')
    return time
def birthday(number):
    current=datetime.datetime.now().strftime('%m-%d')
    current=datetime.datetime.strptime(current,'%m-%d')
    data=datetime.datetime.strptime(number,'%m-%d').strftime('%m-%d')
    data=datetime.datetime.strptime(data,'%m-%d')
    if  current>data:
        data=data.replace(year = data.year + 1)
        time=data-current
    else:
        time=data-current
    return str(time.days)+"天"
def tqtest():
    url=f"https://api.wpbom.com/api/weather.php?city={city}"
    resp=requests.get(url)
    resulttq=resp.json()
    return resulttq


def randomcolor():
    colorarr =['1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    color = ""
    for i in range(6):
        color+=colorarr[random.randint(0,14)]
    return "#"+color


resulttq=tqtest()
json_data = {"first": mss, "word1": resulttq['data']['city']+","+resulttq['data']['forecast'][0]['type'],"word2":resulttq['data']['wendu']+"度","mss":tz(),"word4":birthday(nvbirthday),"word5":re.sub("\D", "",resulttq['data']['forecast'][0]['high'])+"度","word6":re.sub("\D", "",resulttq['data']['forecast'][0]['low'])+"度","word7":resulttq['data']['ganmao'],"word8":birthday(nanbirthday),"date":str(datetime.datetime.now().strftime('%Y-%m-%d'))+' '+week_list[datetime.datetime.now().weekday()],"color":randomcolor()}
def message():
    return {
        "touser": User,
        "template_id": Message_id,
        "topcolor": "#FF0000",
        # json数据对应模板
        "data": {
            "first": {
                "value": mss,
                # 字体颜色
                "color": randomcolor()
            },
            "word1": {
                "value": resulttq['data']['city']+","+resulttq['data']['forecast'][0]['type'],
                "color": randomcolor()
            },
            "word2": {
                "value": resulttq['data']['wendu']+"度",
                "color": randomcolor()
            },
            "word3":{
                "value": lovets(),
                "color": randomcolor()
            },
            "word4":{
                "value": birthday(nvbirthday),
                "color": randomcolor()
            },
            "word5":{
                "value": re.sub("\D", "",resulttq['data']['forecast'][0]['high'])+"度",
                "color": randomcolor()
            },
            "word6":{
                "value": re.sub("\D", "",resulttq['data']['forecast'][0]['low'])+"度",
                "color": randomcolor()
            },
            "word7":{
                "value": resulttq['data']['ganmao'],
                "color": "#173177"
            },
            "mss":{
                "value": tz(),
                "color": randomcolor()
            },
            "data":{
                "value": str(datetime.datetime.now().strftime('%Y-%m-%d'))+' '+week_list[datetime.datetime.now().weekday()],
                "color": "#173177"
            },
            "word8":{
                "value": birthday(nanbirthday),
                "color": randomcolor()
            },
        }
    }

def main_handler(a,b):
    print(json_data)
    
    return send_message()