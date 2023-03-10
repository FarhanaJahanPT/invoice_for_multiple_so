
{
    'name': 'Invoice',
    'sequence': 1,
    'category': 'Account',
    'depends': ['base', 'account','sale'],
    'data': [
        'views/invoice_sale.xml',
    ],
    'installable': True,
    'auto_install': False,
}
