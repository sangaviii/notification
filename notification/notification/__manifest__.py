{
    'name': 'My_cron',
    'version': '1.0',
    'summary': 'Custom module to set DOB using cron',
    'author': 'sangavi',
    'depends': ['base',],
    'data': [
        'security/ir.model.access.csv',
        'data/cron.xml',
        'views/birthday.xml',
        'views/template.xml',

    ],
    'installable': True,
    'application': True,
    'auto_install': False,
}
