# -*- coding: utf-8 -*-
{
    'name':
    "yds_security_rule",
    'summary':
    """
        Add otal paid amount for invoices made by employee to avialbe variables in security rule python code
    """,
    'author':
    "YDS",
    'website':
    "http://www.yds-int.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category':
    'Uncategorized',
    'version':
    '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr_payroll', 'account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
}
