import json
import socket

import requests
import time


def mai_piao(name,sellingPrice,activityId,ticketId,limitBuyNum,sign):
    mai_url = 'https://api.showstart.com/app/order/order.json'
    if limitBuyNum == 0:
        limitBuyNum_r = 5
    else:
        limitBuyNum_r = limitBuyNum
    dataa = {
        'orderDetails[0].price': sellingPrice,
        'sysVersion': '7.0',
        'orderDetails[0].activityId': activityId,
        'sign': sign,
        'longitude': '116.45973',
        'orderDetails[0].ticketType': '1',
        'uuid': '83becea0d0734209b581de2167c56506',
        'couponId': '3332974',
        'terminal': 'android',
        'orderDetails[0].goodsType': '1',
        'appVersion': '3.9.3',
        'orderDetails[0].num': limitBuyNum_r,
        'telephone': name,
        'latitude': '39.961182',
        'payPlatName': 'wxpaymobsc',
        'orderType': '1',
        'goodsType': '1',
        'orderDetails[0].ticketId': ticketId,
    }
    #print(dataa)
    buy_ss = requests.session()
    bug_res = buy_ss.post(mai_url, data=dataa)
    bug_result_list = json.loads(bug_res.content)
    print(bug_result_list)
    return bug_result_list


def deng_lu(name,password='woaini521'):
    denglu_url = 'https://api.showstart.com/app/user/login.json'
    denglu_data ={
        'password': password,
        'sysVersion': '7.0',
        'sign': '',
        'longitude': '116.459152',
        'deviceType': '4',
        'uuid': '83becea0d0734209b581de2167c56506',
        'cityCode': '10',
        'terminal': 'android',
        'appVersion': '3.9.3',
        'loginIp': '192.168.3.113',
        'name': name,
        'latitude': '39.961306',
        'jsessionId': '95e2c4eb81b344a39679e320ff67c458',
    }
    denglu_cookies = {
        'st_flpv':'20170913312018b07ae41f0523cefbd3e754be1a'
    }
    denglu_s = requests.session()
    denglu_req = denglu_s.post(denglu_url,data =denglu_data,cookies = denglu_cookies)
    denglu_result = json.loads(denglu_req.content)
    try:
        sign = denglu_result['result']['sign']
        return sign
    except:
        print('账户名密码不对~请核实后重新运行！')
        return


def yuyin_tongzhi(name):
    yuyin_url ='http://www.baixing.com/oz/voice/?mobile='+name
    print(yuyin_url)
    cookies_yuyin ={
        '__trackId': '150580077035987',
        '__city': 'beijing',
        '_auth_redirect': 'http%3A%2F%2Fbeijing.baixing.com%2F',
        '__uuid': '115058007742982.3a073',
        'login_on_tab': '0',
        '_auth_action_type': 'reg',
        '__sense_session_pv': '2',
        'Hm_lvt_5a727f1b4acc5725516637e03b07d3d2': '1505800772',
        'Hm_lpvt_5a727f1b4acc5725516637e03b07d3d2': '1505800784',
        '_ga': 'GA1.2.1824894605.1505800772',
        '_gid': 'GA1.2.196617102.1505800772',
    }
    yuyin_header = {
        'Host': 'www.baixing.com',
        'Accept': 'application/json, text/javascript, image/webp, */*; q=0.01',
        'X-Requested-With': 'XMLHttpRequest',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.91 Safari/537.36',
        'Referer': 'http://www.baixing.com/oz/verify/reg?mobile=15011159989',
        'Accept-Encoding': 'gzip, deflate',
        'Accept-Language': 'zh-CN,zh;q=0.8,ja;q=0.6',

    }
    yuyin_s = requests.session()
    yuyin_res = yuyin_s.get(yuyin_url,cookies = cookies_yuyin,headers = yuyin_header)
    yuyin_result = json.loads(yuyin_res.content)
    print(yuyin_result)

def get_out_ip():
    url = 'http://ip.taobao.com/service/getIpInfo2.php'
    headers={
        'Host': 'ip.taobao.com',
        'Content - Length': '7',
        'Origin':'http://ip.taobao.com',
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
        'Accept':'*/*',
        'X-Requested-With':'XMLHttpRequest',
        'Referer':'http://ip.taobao.com/ipSearch.php',
        'Accept-Encoding':'gzip, deflate',
        'Accept-Language':'zh-CN,zh;q=0.8,ja;q=0.6',
        'Cookie':'t=f7c0ab27cfbcefda5f877f9117af52b7; cookie2=12a4d43bb0f75002d8df93e8d466baaf; v=0; _tb_token_=e337e833e3a3d; PHPSESSID=1f1n2v4qs60ck7so7hcforja67',
        'Content-Type':'application/x-www-form-urlencoded',
    }
    r = requests.post(url,headers=headers,data='ip=myip')
    pspm_result = json.loads(r.content)
    ip = pspm_result['data']['ip']
    print('ip='+ip)
    # 获取外网IP
    return ip

if __name__ == '__main__':
    get_out_ip()
    print('黄牛使用本脚本抢票！死全家！')
    print(
        '用户名必须是手机号，输入用户名密码后，进入抢票环节，抢到票后，手机会收到一个电话，告诉你验证码是XXXXX，不用管，用手机打开你的客户端，看未付订单，如果订单正确，付款就行了！然后可以改自己账户的名字和密码。抢票时间为14.00，建议13.57/58打开~，因为不知道人家服务器有没有请求订单次数限制，每秒3次的请求量，有点太多，人家可能会封号')
    name = input('用户名（手机号）：')
    password = input('密码：')
    sign = deng_lu(name, password)
    i = 0
    while time.time() < 1506491443:

        print('开始抢票时间：2017/9/27 13:50:43')
        time.sleep(30)
    while time.time() > 1506491443:

        while time.time() < 1506494452:
            time.sleep(0.3)
            maipiao_result = mai_piao(name=name, sellingPrice='260', activityId='59c9c1890cf277cc1aa25c38',
                                      ticketId='082979e2d5064a7e91cf9b0ab502070e', limitBuyNum='2', sign=sign)
            i = i + 1
            # print(i)1
            if i % 10 == 0:
                print('已经抢票次数:',i)
                print(time.strftime('结束抢票：2017/9/27 14:40:52'))
                if i % 180 == 0:
                    sign = deng_lu(name, password)
                    print('重新登录')
            if maipiao_result['state'] != '1':
                print(maipiao_result['msg'], '请重新运行程序')
                sign = deng_lu(name, password)
            elif maipiao_result['state'] == '1':
                #yuyin_tongzhi(name)
                #print('买票成功，请使用客户端查看未付订单，查看结果~，确认后修改账户密码，修改密码后支付订单，保证安全')
                break
        if maipiao_result['state'] == '1':
            yuyin_tongzhi(name)
            print('买票成功，请使用客户端查看未付订单，查看结果~，确认后修改账户密码，修改密码后支付订单，保证安全')
            break




