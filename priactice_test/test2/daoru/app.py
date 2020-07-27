# -*- coding: utf-8 -*-

import xlrd
from flask import request

from flask import Flask

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def hello_world():
    if request.method == 'POST':
        exec_file = request.files.get('file')
        success = import_file(exec_file)
        return success


def import_file(exec_file):
    table = ''
    nrows = 0
    success = u'导入成功!'
    try:
        file_res = exec_file.read()  # 读取file文件对象
        data = xlrd.open_workbook(file_contents=file_res)  # 生成xlrd对象
        table = data.sheets()[0]  # 顺序获取工作簿
        nrows = table.nrows  # 获取行数
    except Exception as e:
        print e
        print u'文件格式必须是execl'
    for n in range(0, nrows):
        account = table.row_values(n)  # 遍历获取每一单元格的数据
        if len(account) != 6:
            raise BaseException(u'数据错误,请检查列数')
        audit_time, role, user, ip, audit_type, audit_detail = account
        message = u'第{}行数据导入成功'.format(n)
        # row_values = table.row_values(rowx=2, start_colx=1, end_colx=3)  # 获取第一列到第三列的第二行数据
        # print row_values
        print message
        print audit_time, role, user, ip, audit_type, audit_detail
    return success


if __name__ == '__main__':
    app.run()
