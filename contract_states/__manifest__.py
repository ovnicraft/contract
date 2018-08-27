# -*- coding: utf-8 -*-
# Copyright 2018 PriseHub Cia. Ltda.
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

{
    'name': 'Contracts Sequence',
    'version': '10.0.1.0.0',
    'category': 'Contract Management',
    'license': 'AGPL-3',
    'author': "PriseHub, "
              "Odoo Community Association (OCA)",
    'website': 'https://github.com/oca/contract',
    'depends': ['contract'],
    'data': [
        'data/sequence.xml',
        'views/contract_view.xml',
    ],
    'installable': True,
}
