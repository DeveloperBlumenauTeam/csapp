#!/usr/bin/env python3
'''
Created on 20190209
Update on 20190209
@author: Eduardo Pagotto
'''

#pylint: disable=C0301
#pylint: disable=C0103
#pylint: disable=W0703
#pylint: disable=R0913

import logging
import subprocess

def execute_conversao(comando):
    separado = comando.split(' ')
    proc = subprocess.Popen(separado,
                            #shell=True,
                            #preexec_fn=os.setsid,
                            stdout=subprocess.PIPE,
                            stderr=subprocess.STDOUT)
    proc.wait()

    logging.debug('Comando: %s status: %d', comando, proc.returncode)

    if proc.returncode != 0: # saiu com erro
        msg_erro = ''
        if proc.stderr is not None:
            for line in iter(proc.stderr.readline, b''):
                linhaErro = line.decode('utf-8')
                msg_erro = msg_erro + str(linhaErro) + ' '

        raise Exception('Falha Comando: {0} Erro [{1}]'.format(comando, msg_erro))

    # Saiu de forma correta
    msg_ok = ''
    for line in iter(proc.stdout.readline, b''):
        linhaOk = line.decode('utf-8').replace('\n', '').replace('\r', '').replace('/', '\\')
        logging.debug('%s', linhaOk)
        msg_ok = msg_ok + linhaOk + ' '

    return msg_ok