{
    'name': 'graph testing',
    'version' : '1.3',
    'summary': 'testing graphic',
    'depends': ['web'],
    'author': "Noel Alvarez",
    'category': 'web',
    'description': """testing a bar graphic """,
    'license': 'LGPL-3',
    'data': [
              'views/container_template.xml',
              'views/snippets/graph_snippet.xml',
            ],
    'assets': {
        'web.assets_custom': [
            'graph_test/static/src/components/**/*',
        ],
    },
    'installable': True,
    'application': True,
}