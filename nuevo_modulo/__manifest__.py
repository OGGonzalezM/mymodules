# -*- coding: utf-8 -*-
{
    'name': "My first time",

    'summary': """Testing module""",

    'description': """
        Creacion del primer modulo en odoo:
            - pruebas de creacion
            - modulo inical
    """,

    'author': "Soluciones 4G",
    'website': "soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Test',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        #'templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        #'demo.xml',
    ],
    'auto_install':False,
    'installable':True,
}

