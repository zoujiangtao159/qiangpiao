#encoding:utf-8

import os
import requests
import json

import time

import sys


def search():
    search_url = 'https://api.showstart.com/app/activity/search.json?sysVersion=7.0&terminal=android&appVersion=3.9.3&sign=ab221cd4d69f7758078b04b6686e93c2&keyword=big%20boom&pageSize=20&uuid=83becea0d0734209b581de2167c56506&pageNo=1'
    #cookies = {"st_flpv":"20170913312018b07ae41f0523cefbd3e754be1a"}
    headers = {
        'Host':'api.showstart.com',
        'Connection':'Keep-Alive',
        'Accept-Encoding':'gzip',
        'User-Agent':'okhttp/3.9.0',
    }
    '''
    data ={
        'sysVersion': '7.0',
        'terminal': 'android',
        'appVersion': '3.9.3',
        'sign': 'd848a0ac3b9dbe21f9b4a2a9d1b058c7',
        'keyword': 'big boom',
        'pageSize': '20',
        'uuid': '83becea0d0734209b581de2167c52152',
        'pageNo': '1'
    }
    '''
    s = requests.session()
    reqq = s.get(search_url)
    #print(reqq.request)
    req_result = json.loads(reqq.content)
    #print(req_result)
    activity_result = req_result['result']['activityInfo']
    activity_list = []
    for activity in activity_result:
        if activity['showStartTime'] > 1506081600000 :
            activity_list.append(activity['activityId'])
    return activity_list



def bug_list_result(activity_id):
    bug_list_url = 'https://api.showstart.com/app/activity/ticket/list.json'
    data = {
        #'terminal': 'android',
        #'sysVersion': '7.0',
        #'sign': 'ab221cd4d69f7758078b04b7777e93c3',
        #'appVersion': '3.9.3',
        'activityId':activity_id ,
        #'uuid': '83becea0d0734209b581de2167c56506',
    }
    buy_piao = []
    bug_s = requests.session()
    bug_res = bug_s.post(bug_list_url,data = data)
    bug_result_list = json.loads(bug_res.content)
    #print(bug_result_list)
    for bug_l in bug_result_list['result']:
        if bug_l['remainTicket']  > 0 and bug_l['time'] != '售票结束':
            #print(bug_l)
            bug_piao = {}
            bug_piao['activityId'] = bug_l['activityId']
            bug_piao['ticketId'] = bug_l['ticketId']
            bug_piao['sellingPrice'] = bug_l['sellingPrice']
            bug_piao['limitBuyNum'] = bug_l['limitBuyNum']
            buy_piao.append(bug_piao)
    return buy_piao


#bug_list_result('59b60d280cf2628da8cd2d90')



def mai_piao(sellingPrice,activityId,ticketId,limitBuyNum):
    mai_url = 'https://api.showstart.com/app/order/order.json'
    if limitBuyNum == 0:
        limitBuyNum_r = 5
    else:
        limitBuyNum_r = limitBuyNum
    dataa = {
        'orderDetails[0].price': sellingPrice,
        'sysVersion': '7.0',
        'orderDetails[0].activityId': activityId,
        'sign': '9ee2b2e18b6953f9361206438cb38f5c',
        'longitude': '116.45973',
        'orderDetails[0].ticketType': '1',
        'uuid': '83becea0d0734209b581de2167c56506',
        'couponId': '3332974',
        'terminal': 'android',
        'orderDetails[0].goodsType': '1',
        'appVersion': '3.9.3',
        'orderDetails[0].num': limitBuyNum_r,
        'telephone': '15011159989',
        'latitude': '39.961182',
        'payPlatName': 'wxpaymobsc',
        'orderType': '1',
        'goodsType': '1',
        'orderDetails[0].ticketId': ticketId,
    }
    print(dataa)
    buy_ss = requests.session()
    bug_res = buy_ss.post(mai_url, data=dataa)
    bug_result_list = json.loads(bug_res.content)
    #print(bug_result_list)
    return bug_result_list


def duanxintongzhi():
    duanxin_url ='https://api.showstart.com/app/letter/sendcode.json'
    duanxin_data ={
        'terminal': 'android',
        'sysVersion': '7.0',
        'sign': '',
        'appVersion': '3.9.3',
        'type': '0',
        'mobile': '15011159989',
        'uuid': '83becea0d0734209b581de2167c56506',
    }
    duanxin_s =requests.session()
    duanxin_res = duanxin_s.post(duanxin_url,data=duanxin_data)
    duanxin_result = json.loads((duanxin_res.content))


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
    print(denglu_result)


def yuyin_tongzhi():
    yuyin_url ='http://www.baixing.com/oz/voice/?mobile=15011159989'
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

def restart_program():
  python = sys.executable
  os.execl(python, python, * sys.argv)



if __name__ == '__main__':
    deng_lu('18514509314')
    try:
        print(time.time())
        while time.time() < 1508644556:
            ssss = []
            search_res = search()
            for search_one in search_res:
                xinxi_list = bug_list_result(search_one)
                if xinxi_list != []:
                    ssss.append(xinxi_list)
            if len(ssss) == 0:
                print('没有可买任务', time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
            else:
                pass
            for ddd in ssss:
                for bug_ine in ddd:
                    #print(bug_ine)
                    mai_piao_result = mai_piao(sellingPrice=bug_ine['sellingPrice'], activityId=bug_ine['activityId'],
                                               ticketId=bug_ine['ticketId'], limitBuyNum=bug_ine['limitBuyNum'])
                    if mai_piao_result != None:
                        print('success')
                        duanxintongzhi()
                        yuyin_tongzhi()
                    else:
                        print('fail')
            time.sleep(3)
    except Exception as e:
        print('出现错误',e)
        restart_program()








