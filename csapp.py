#!/usr/bin/env python3
'''
Created on 20190207
Update on 20190207
@author: Eduardo Pagotto
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913

import sys
import logging
import signal

from csapp.web.ws import application

def handler_app(signal, frame):
    '''[crt-c detector]
    Arguments:
        signal {[type]} -- [description]
        frame {[type]} -- [description]
    '''
    logging.info('crt-c detectado, aplicacao encerrada:%d', signal)
    sys.exit()

def main():
    '''[Entry Point]
    '''
    signal.signal(signal.SIGINT, handler_app)
    application.run(host='0.0.0.0', port=5191, debug=True)

if __name__ == '__main__':
    main()
