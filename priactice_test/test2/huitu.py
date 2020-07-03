# -*- coding: utf-8 -*-

# 使用turtle库绘制图形
# 画出 NUESOFT
# 导入turtle库，使用import+模块名 as相当于起别名t

import turtle as t

# 设置画笔大小10像素
t.pensize(10)
# 画笔颜色,第二个参数代表填充颜色
t.color("blue", "pink")
# 抬笔
t.penup()
# 指定坐标点
t.goto(-250, 0)
# 落笔,pd是pendown的简写
t.pd()
t.left(90)
t.forward(80)
t.right(145)
# forward的简写fd
t.fd(100)
t.lt(145)
t.fd(80)

# 抬笔
t.penup()
# 指定坐标点
t.goto(-100, 80)
# 落笔,pd是pendown的简写
t.pd()
t.lt(90)
t.fd(60)
t.lt(90)
t.fd(80)
t.lt(90)
t.fd(60)
# 抬笔
t.penup()
# 指定坐标点
t.goto(-161, 40)
# 落笔,pd是pendown的简写
t.pd()
t.fd(50)
# o
# 抬笔
t.penup()
# 指定坐标点
t.goto(0, 30)
# 落笔,pd是pendown的简写
t.pd()
# 开始填充
t.begin_fill()
t.circle(30)
t.end_fill()

# #S
#抬笔
t.penup()
#指定坐标点
t.goto(-25,60)
#落笔,pd是pendown的简写
t.pd()
t.lt(90)
t.circle(22,270)
#默认半径为正值时，以左侧为圆心
t.circle(-22,270)


t.done()

# 使用pyinstaller进行程序打包
# 安装pyinstaller
# 使用pip安装第三方模块
# pip install 模块名
# terminal 在命令行下安装
