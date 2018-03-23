#!/usr/bin/env python
# _*_ coding:utf-8 _*_
# __author__ = 'cosmic'

import SocketServer

class SockHandler(SocketServer.BaseRequestHandler):

    def handle(self):
        print "接收到客户端的一个连接:", self.client_address
        data = 'start'

        while len(data):
            data = self.request.recv(2048)
            self.request.send("返回:" + data)

        print "客户端关闭。。。 。。。"

serAddr = ("0.0.0.0", 8888)
print "wait......"

server = SocketServer.TCPServer(serAddr, SockHandler)
server.serve_forever()