{
    'name': 'Project Documents',
    'version': '1.0',
    'summary': 'Project Documentation Management',
    'description': """
        This modules allow the user to create or add a documentation related to the poecjt
        Features:
        - Create and organize projects
        - Upload documentation files
        - Categorize documents by type
        - Track document history
    """,
    'category': 'Tools',
    'author': 'Yasmin',
    'website': '',
    'depends': ['base', 'project'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/project_document_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'project_docs/static/src/css/custom_style.css',
        ],
    },
    'demo': [],
    'installable': True,
    'application': True,
    'auto_install': False,
    'uninstall_hook': 'uninstall_hook',
}
