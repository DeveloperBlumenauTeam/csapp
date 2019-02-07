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
import os
import logging

from flask import Flask, jsonify, json, request#, #g #render_template,

from csapp.utils.loads import set_config_yaml
from csapp.web.invalid import Invalid

application = Flask(__name__)

@application.errorhandler(Invalid)
def handle_invalid_usage(error):
    """[Handle de mensagem de erro que retorna ao cliente]
    Arguments:
        error {[json]} -- [Dados do erro detectado]
    Returns:
        [json] -- [dados do erro]
    """
    logging.error('ERRO: %s', str(error))
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response

@application.route('/')
def api_root():
    """[Entry point aplicação]
    Returns:
        [string] -- [mostra mensage de bem-vindo]
    """
    return 'Welcome'

@application.before_first_request
def execute_inicializacao():
    """[Inicaliza dos singleton]
    """
    try:
        config, log = set_config_yaml('CSAPP v-0.0.1', __name__, os.environ['CFG_CSAPP'] if 'CFG_CSAPP' in os.environ else './etc/setup.yaml')
        log.info('Config carregado com sucesso')

    except Exception as exp:
        import pathlib
        current_dir = pathlib.Path(__file__).parent
        current_file = pathlib.Path(__file__)
        print('Path Local:{0}, File: {1} motivo:{3}'.format(current_dir, current_file, str(exp)))

        sys.exit(1)

@application.route('/comandoA', methods=['GET', 'POST'])
def comandoA():
    '''[Primeiro Comando]
    Raises:
        Invalid -- [description]
        inv -- [description]
        Invalid -- [description]
    Returns:
        [type] -- [description]
    '''
    try:
        if (request.method == 'POST' or request.method == 'GET') is False:
            raise Invalid('Comando invalido', status_code=404)

        #auth = request.headers['Authorization']
        #host = request.headers['host']
        # FIXME: colocar um jwt para melhorar a seguranca

        payload = request.get_json(silent=True)
        logging.debug('Recebido: %s', str(payload))

        if request.method == 'POST':
            return "ok"
        else: # GET
            opp = {'teste':'ok', 'status':True}
            response = application.response_class(
                response=json.dumps(opp),
                status=200,
                mimetype='application/json'
            )
            return response

    except Invalid as inv:
        raise inv
    except Exception as exp:
        raise Invalid('Erro Report:{0}'.format(str(exp)), status_code=404)
