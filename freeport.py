# coding: utf-8
#

import socket


class FreePort(object):
    def __init__(self):
        self._start = 20000
        self._end = 40000
        self._now = self._start-1

    def get(self,default = None):
        while True:
            if default and not self.is_port_in_use(default):
                return default

            self._now += 1
            if self._now > self._end:
                self._now = self._start
            if not self.is_port_in_use(self._now):
                return self._now

    def is_port_in_use(self, port):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            ret = s.connect_ex(('localhost', port)) == 0
            if ret:
                print('%d is using, create new port' %port)
            return ret

freeport = FreePort()


if __name__ == "__main__":
    for i in range(10):
        print(freeport.get())