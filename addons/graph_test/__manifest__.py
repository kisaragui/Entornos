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
              'views/snippets/graph_content.xml',
            ],
    'assets': {
        'web.assets_qweb': [
            'graph_test/static/src/components/**/*.xml',
        ],
        'web.assets_frontend': [
            'graph_test/static/src/components/**/*.js',
        ],
    },
    'installable': True,
    'application': True,
}