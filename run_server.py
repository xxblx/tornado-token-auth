#!/usr/bin/env python
import logging

import tornado.httpserver
import tornado.ioloop

from webapp.app import Application
from webapp.conf import HOST, PORT


def main():
    logging.basicConfig(level=logging.DEBUG)

    http_server = tornado.httpserver.HTTPServer(Application())
    http_server.listen(PORT, HOST)

    tornado.ioloop.IOLoop.current().start()


if __name__ == '__main__':
    main()
