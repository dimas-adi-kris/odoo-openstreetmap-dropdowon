# -*- coding: utf-8 -*-
{
    'name': "Custom Purchase",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Odoo Dimas",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/16.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'web'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'report/purchase_analyse.xml',
        'views/stock_picking.xml',
        'views/origin.xml',
        'views/res_partner.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'custom_purchase/static/src/scss/*',
            'custom_purchase/static/src/js/*',
            'custom_purchase/static/src/xml/*',
        ],
    },
    'application': True,
    'installable': True,

}
