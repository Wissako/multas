{
    'name': "multas",

    'summary': "Modulo para gestionar multas de usuarios y utilizar herencia de modelos",

    'description': """
    Modulo para gestionar multas de usuarios y utilizar herencia de modelos en Odoo 19
    para la practica de Sistemas de gestion empresarial: "Herencia en Odoo"

    """,

    'author': "Luis Alfonso",
    'website': "https://youtu.be/xvFZjo5PgG0?si=nVEphf_9zFc4or9b",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'hr'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',                
        'views/menus.xml',
        'views/hr_employee_views.xml',   
        'views/vehiculo_view.xml',
        'views/multa_views.xml',
        'reports/report_actions.xml',
        'reports/report_templates.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}

