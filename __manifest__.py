# -*- coding: utf-8 -*-
{
    'name': "Modular",

    'summary': """Testing module""",

    'description': """
        Creacion del segundo modulo en odoo:
            - Creacion del modulo
            - modulo inicial
			-Modulo de pruebas
    """,

    'author': "OGGonzalezM",
    'website': "soluciones4g.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/$
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
        'demo/tmodule_course_demo.xml',
    ],
    'auto_install':False,
    'installable':True,
}

