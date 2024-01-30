{
    'name': 'Pets form',
    'version' : '1.0',
    'summary': 'probanndo',
    'depends': ['website'],
    'author': "Noel Alvarez",
    'category': 'Website',
    'description': """Probando formulario""",
    'license': 'LGPL-3',
    'data': [
              'views/template_main.xml',
              'views/assets.xml',
              'views/snippets/pet_snippet.xml',
            ],
    'assets': {
        'web.assets_frontend': [
            'pet_form/static/src/xml/*.xml',
            'pet_form/static/src/js/*.js'
        ],
    },
    'installable': True,
    'application': True,
    'auto_install': False,
}