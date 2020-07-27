#!/usr/bin/python
# -*-coding:utf-8-*-

import zmq
import sys

from Tools.scripts.treesync import raw_input

context = zmq.Context()
socket = context.socket(zmq.REQ)
socket.connect("tcp://localhost:5555")

while (True):
    socket.send('1111'.encode('utf-8'))
    response = socket.recv()
    print(response)
