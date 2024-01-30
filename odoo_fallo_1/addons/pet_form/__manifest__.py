# -*- coding: utf-8 -*-
{
    'name': 'Pets form',
    'version' : '1.2',
    'summary': 'probando',
    'sequence': 10,
    'depends': ['website'],
    'author': "Noel Alvarez",
    'category': 'Website',
    'description': """Probando formulario""",
    'license': 'LGPL-3',
    'data': [
              "views/template_main.xml",
              'views/snippets/pet_snippet.xml',
            ],
    'installable': True,
    'assets': {
        'web.assets_frontend': [
            'pet_form/static/src/js/*',
            'pet_form/static/src/libs/echarts/*',
        ],
    },
}