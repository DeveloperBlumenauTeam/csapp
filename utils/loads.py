#!/usr/bin/env python3
'''
Created on 20190207
Update on 20190207
@author: Eduardo Pagotto
'''

# pylint: disable=C0301
# pylint: disable=C0103
# pylint: disable=W0703

import logging
import logging.config
import yaml

def set_config_yaml(texto, app_name, config_file):
    """
    Carrega arquivo de configuração e loggin predefinido (obrigatorio)
        :param texto: Texto a ser exibido primeiro
        :param app_name: nome do logger principal
        :param config_file: arquivo formato .yaml a ser carregado
    """
    try:
        with open(config_file, 'r') as stream:
            global_config = yaml.load(stream)
            logging.config.dictConfig(global_config['loggin'])
            log = logging.getLogger(app_name)
            log.info('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
            log.info(texto)
            log.info('Load config: %s', config_file)
            return global_config, log

    except yaml.YAMLError as exc:
        print('Arquivo: {0}, Erro: {1}'.format(config_file, repr(exc)))

    except Exception as exp:
        print('Arquivo: {0}, Erro Geral: {1}'.format(config_file, repr(exp)))

    quit()
