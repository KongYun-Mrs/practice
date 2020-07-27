# -*- coding: utf-8 -*-
import sys
import time
import json
import base_64
import hashlib
import requests
import traceback
from requests.auth import HTTPBasicAuth


class Skylink(object):
    def __init__(self, cmd='', args_=''):
        self.cmd = cmd
        self.args_ = args_
        pass

    def args(self):
        devices_list = [
            {
                "linkage_url": "https://183.129.204.45:8443",  # ip 和端口
                "api_id": "admin",  # 账号
                "api_cert": "admin_default",  # 密码
            }
        ]
        return self.args_ if self.args_ else {
            "devices_list": str(devices_list),
            "sip": "1.1.1.1",  # 源ip
            "dip": "2.2.2.2",
            "protocol": "TCP",
            "src_port": "200",
            "dst_port": "100",
            "duration": "",
        }

    def command(self):
        # return 'DpTech_DenyNetwork'
        return self.cmd

    def results(self, *args, **kwargs):
        print("results: ", args, kwargs)


skylink = Skylink()

devices_list = skylink.args().get('devices_list', [])
try:
    devices_list = json.loads(devices_list)
    print(devices_list)
except:
    try:
        devices_list = eval(devices_list)
    except:
        devices_list = []
        print("#####Error: devices_list:%s is not type of list, type(devices_list)=%s" % (
            devices_list, type(devices_list)))

# ---------------------
PROTOCAL_MAPPING = {
    "ICMP": "1",
    "TCP": "6",
    "UDP": "17",
}


def http_request(method, url, headers=None, params=None, data=None, timeout=10, verify=False,
                 authorization=None):
    headers = headers if headers else {
        "Content-Type": "application/json",
        "Accept": "application/json",
        # "Authorization": authorization,
        "Accept - Encoding": "gzip, deflate, sdch",
        "Accept - Language": "zh_CN, en",
        "Cache - Control": "no-cache",
        "Connection": "keep-alive",
        "Content-Length": '348',
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36",
    }
    # print("{}, {}, {}, {}, {}".format(method, url, params, headers, data))
    try:
        r = requests.request(
            method,
            url,
            params=params,
            data=data,
            headers=headers,
            timeout=timeout,
            verify=verify,
            auth=authorization
        )
        print r.status_code
        return r.status_code, r.content
    except Exception as e:
        print(e)
    return 500, 'http/https error'


def get_user_authorization(username, password):
    s = username + ':' + password
    return "Basic {}".format(base64_str(s))


def base64_str(s):
    return base_64.encodestring(s)[:-1]


def hash_str(s):
    return s.replace('.', '').replace('-', '').replace('/', '')


def md5_str(s):
    m = hashlib.md5()
    m.update(s.encode("utf-8"))
    return m.hexdigest()


def denyService(oneDev):
    # IP封禁
    # dip = skylink.args().get('dip', "")
    host = oneDev.get("linkage_url", "")
    api_id = oneDev.get("api_id", "")
    # api_cert = oneDev.get("api_cert", "")
    api_cert = 'admin_default'
    authorization = get_user_authorization(api_id, api_cert)
    # 发起封禁请求
    url = host + "/func/web_main/api/maf/maf_addrfilter/maf_addrfilter/mafcustomv4wblist"
    print url
    data = {
        "mafcustomv4wblist":
            {
                "GroupStr": "abc",
                "IPStart": "1.1.1.1",
                "IPEnd": "1.1.1.1",
                "LeftAge": "300",
                "Action": "2"
            }
    }
    code, content = http_request(
        method='POST', url=url, data=data, authorization=authorization)
    print("IPv4封禁：{},{}".format(code, content))
    if code == 201:
        code = 200
        content = u"IP封禁成功"
    else:
        print u'IP封禁失败!'
    return code, content


def queryService(oneDev):
    # IP封禁查询
    global params
    offset = skylink.args().get('offset')
    count = skylink.args().get('count')
    action = skylink.args().get('action', '')
    dip = skylink.args().get('dip', '')

    host = oneDev.get("linkage_url", None)
    api_id = oneDev.get("api_id", "")
    api_cert = oneDev.get("api_cert", "")

    authorization = get_user_authorization(api_id, api_cert)
    url = host + "/func/web_main/api/maf/maf_addrfilter/maf_addrfilter/mafcustomv4wblist"
    if offset and count and count:
        params = {
            "Action": action,
            "offsert": offset,
            "count": count
        }
    # 查询符合action的数据条目数
    if not (offset or count) and action:
        params = {
            'Action': action
        }
    #  批量查询
    if dip and offset and count:
        params = {
            'dip': dip,
            "offsert": offset,
            "count": count
        }
    # 单个Ipv4查询
    if not (offset or count) and action:
        params = {
            'dip': dip,
        }

    code, content = http_request(
        url=url, method='GET', params=params, authorization=authorization)
    if code == 200:
        content = json.loads(content)
    else:
        print(u"查询错误，{}, {}".format(code, content))
        content = []
    return content


def deleteService(oneDev):
    # 解除封禁
    host = oneDev.get("linkage_url", "")
    api_id = oneDev.get("api_id", "")
    api_cert = oneDev.get("api_cert", "")
    DbId = skylink.args().get('DbId')

    authorization = get_user_authorization(api_id, api_cert)

    data = {
        "mafcustomv4wblist":
            {
                "DbId": DbId
            }
    }

    url = host + '/func/web_main/api/maf/maf_addrfilter/maf_addrfilter/mafcustomv4wblist'

    code, content = http_request(url=url, method='DELETE', data=data, authorization=authorization)
    if code == 204:
        content = u"解除封禁成功"
    return content


def modifyService(oneDev):
    # 修改封禁策略
    dip = skylink.args().get('dip')  # 封禁ip不可修改
    LeftAge = skylink.args().get('LeftAge')  # 策略的生存时间
    Action = skylink.args().get('Action')  # 策略的动作。1代表白名单，２代表黑名单。
    GroupStr = skylink.args().get('GroupStr')  # 设备分组名称
    host = oneDev.get('linkage_url', '')
    api_cert = oneDev.get('api_cert', '')
    api_id = oneDev.get('api_id', '')
    authorization = get_user_authorization(api_id, api_cert)
    url = host + '/func/web_main/api/maf/maf_addrfilter/maf_addrfilter/mafcustomv4wblist'
    data = {
        "mafcustomv4wblist":
            {
                "GroupStr": GroupStr,
                "IPAddr": dip,
                "LeftAge": LeftAge,
                "Action": Action
            }
    }
    code, content = http_request(url=url, method='PUT', data=data, authorization=authorization)
    if code == 200:
        print (u'修改策略成功')


def AddGroup(oneDev):
    # 创建分组
    host = oneDev.get("linkage_url", None)
    api_id = oneDev.get('api_cert', "")
    api_cert = oneDev.get('api_id', "")
    group_name = skylink.args().get('group_name')
    authorization = get_user_authorization(api_id, api_cert)
    data = {
        "mafgrouplist":
            {
                "State": "1",  # 分组状态 1表示开启 0表示关闭
                "GroupName": "abc",  # 分组名称
                "Descr": ""
            }
    }
    url = host + '/func/web_main/api/maf/maf_addrfilter/maf_addrfilter/mafgrouplist'
    print url
    code, content = http_request(url=url, method='POST', data=data,
                                 authorization=HTTPBasicAuth('admin', 'admin_default'))

    if code == 201:
        content = u"创建成功"
    return content


def Getipobj(oneDev):
    # 批量获取设备IP地址对象
    api_id = oneDev.get('api_cert', "")
    api_cert = oneDev.get('api_id', "")
    host = oneDev.get("linkage_url", "")
    authorization = get_user_authorization(api_id, api_cert)
    url = host + '/func/web_main/api/maf/maf_addrfilter/maf_addrfilter/mafgrouplist'
    code, content = http_request(url=url, method='POST', authorization=authorization)
    if code == 200:
        content = u"查询成功"
    else:
        print(u"查询错误，{}, {}".format(code, content))
        content = []
    return content


def dispatch(func):
    ret = []
    if not isinstance(devices_list, list):
        print(u"##没有相关设备,跳过该服务")
        skylink.results({"dptech_linkage_results": ret})
        return
    for dev in devices_list:
        request_id = dev.get("request_id", "")
        resp = {
            "msg_type": "response",
            "created": int(time.time() * 1000),
            "request_id": request_id,
            "status": 500,
            "status_text": u"内部执行错误"
        }
        try:
            code, content = func(dev)
            resp['status'] = code
            resp['status_text'] = content
        except Exception as exc:
            traceback.print_exc()
            print("antivirusVictim error:", str(exc))
            resp['status_text'] = exc

        ret.append(resp)
    skylink.results({"dptech_linkage_results": ret})


def dispatch2key(func, results_key):
    ret = []
    if not isinstance(devices_list, list):
        print(u"##没有相关设备,跳过该服务")
        skylink.results({"securitypolicylist": ret})
        return
    for dev in devices_list:
        try:
            resp = func(dev)
        except Exception as exc:
            traceback.print_exc()
            print(" error:", str(exc))
            resp = u"操作失败"

        ret.append(resp)
    skylink.results({results_key: ret})


''' EXECUTION CODE '''
if __name__ == "__main__":
    print('command is %s' % (skylink.command(),))
    c = {
        "DpTech_DenyNetwork_Std": {
            "devices_list": [
                {
                    "linkage_url": "http://127.0.0.1:8888",  # ip 和端口
                    "api_id": "admin",  # 账号
                    "api_cert": "123456",  # 密码
                }
            ]
        },
        "DpTech_QueryNetwork_Std": {
            "devices_list": [
                {
                    "linkage_url": "http://127.0.0.1:8888",  # ip 和端口
                    "api_id": "admin",  # 账号
                    "api_cert": "123456",  # 密码
                }
            ]
        },
        "DpTech_DeleteNetwork_Std": {
            "devices_list": [
                {
                    "linkage_url": "http://127.0.0.1:8888",  # ip 和端口
                    "api_id": "admin",  # 账号
                    "api_cert": "123456",  # 密码
                }
            ],
            "name": "",
            "delallEnable": "",
        },
        "DpTech_AddGroup_Std": {"devices_list": [
            {
                "linkage_url": "http://127.0.0.1:8888",  # ip 和端口
                "api_id": "admin",  # 账号
                "api_cert": "123456",  # 密码
            }
        ]
        },
        "DpTech_Getipobj_Std": {"devices_list": [
            {
                "linkage_url": "http://127.0.0.1:8888",  # ip 和端口
                "api_id": "admin",  # 账号
                "api_cert": "123456",  # 密码
            }
        ]
        },
        "DpTch_ModifyService_Std": {"devices_list": [
            {
                "linkage_url": "http://127.0.0.1:8888",  # ip 和端口
                "api_id": "admin",  # 账号
                "api_cert": "123456",  # 密码
            }
        ]
        },
        "DpTch_ServiceCount_Std": {"devices_list": [
            {
                "linkage_url": "http://127.0.0.1:8888",  # ip 和端口
                "api_id": "admin",  # 账号
                "api_cert": "123456",  # 密码
            }
        ]}
    }
    if len(sys.argv) >= 2 and sys.argv[1] in c:
        skylink.cmd = sys.argv[1]
    else:
        skylink.cmd = 'DpTech_DenyNetwork_Std'
    skylink.args_ = c[skylink.cmd]

    # if skylink.command() == 'DpTech_DenyNetwork_Std':
    # IP封禁
    # dispatch(denyService)
    # elif skylink.command() == 'DpTech_QueryNetwork_Std':
    #     # IP封禁查询
    #     dispatch2key(queryService, 'securitypolicylist')
    # elif skylink.command() == 'DpTech_DeleteNetwork_Std':
    #     # 解除IP封禁
    #     dispatch2key(deleteService, 'dptech_delete_results')
    # elif skylink.command() == 'DpTech_AddGroup_Std':
    #     # 添加设备分组
    dispatch2key(AddGroup, 'Group_list')
    # elif skylink.command() == 'DpTech_Getipobj_Std':
    #     # 查询设备分组IP对象
    #     dispatch2key(Getipobj, 'Ipobj_list')
    # elif skylink.command() == 'DpTch_ModifyService_Std':
    #     # 修改IP封禁策略
    #     dispatch2key(modifyService, 'modif_list')
