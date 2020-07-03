# -*- coding: utf-8 -*-
import re

import ipaddress
from netaddr import IPAddress

net = ipaddress.ip_network('10.11.23.34'.decode('utf-8'), False)

# print net.version
#
# # 查看网络中独立地址个数
# print net.num_addresses
# # 获取网路掩码
# print net.netmask

ip_v4 = ipaddress.ip_address('10.11.23.34'.decode('utf-8'))
if isinstance(ip_v4, ipaddress.IPv4Address):
    print 'True'
else:
    print 'False'

if not isinstance(ip_v4, ipaddress.IPv6Address):
    print u'不是合法的IPV6'

# 判断是否是合法的掩码
mask = '255.255.255.0'
print IPAddress(mask).is_netmask()

if re.match('^[\d\.]+$', mask):
    print u'ip合法'

# ip_address 检验IP是否合法
# ip_test = ipaddress.ip_address('dasdas.133.12.41'.decode('utf-8'))
# ip_network 检验网段是否合法
# ip_network = ipaddress.ip_network('ADSZXCZ.254ASDSA.255.0/89')


def process_ui_msg(ctx):
    ui_sock = ctx.socket(zmq.REP)
    #ui_sock.bind('ipc:///dev/shm/config')
    ui_sock.bind('tcp://*:5555')
    #popen('chmod 777 /dev/shm/config')
    get_mgt_ifname()
    try:
        while True:
            req=request(ui_sock)
            debug_out('req :\n' + req)
            log.info('QQQQQ %s\n',req)
            rep = doit(req, ui_sock)
            debug_out('\nresponse :\n' + rep)
            log.info('AAAAA %s\n',rep)
            reponse(ui_sock, rep)
    except Exception,e:
        log.warn("[{0}:{1}] {2}".format('aaaaa', "guish", e), exc_info=1)
        print Exception,":",e
        print "req : " + req
