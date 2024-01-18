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
              'views/script_layaut.xml',
              'views/snippets/pet_snippet.xml',
              'security/ir.model.access.csv'
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