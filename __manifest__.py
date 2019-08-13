# Copyright 2019 Onestein
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'StatusBar Dynamic Visible',
    'summary': 'StatusBar Dynamic Visible',
    'category': 'Extra Tools',
    'version': '12.0.1.0.0',
    'development_status': 'Production/Stable',
    'author': 'Loney',
    'license': 'AGPL-3',
    'website': 'https://github.com/Alone-Tree',
    'depends': [
        'web'
    ],
    'data': [
        'templates/assets.xml',
        'security/approval_manger_security.xml',
        'security/ir.model.access.csv',
        'views/approval.xml',
    ],
    'js': ['static/src/js/*.js'],
    'installable': True,
    'application': True,
    'auto_install': False,
}
