#!/usr/bin/env python3
'''
Created on 20190207
Update on 20190208
@author: Eduardo Pagotto
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913

import sys
import logging
import signal

from web.ws import application

def main():
    '''[Entry Point]
    '''
    application.run(host='0.0.0.0', port=5191, debug=True)

if __name__ == '__main__':
    main()
