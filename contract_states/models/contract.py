# -*- coding: utf-8 -*-

from odoo import api, fields, models


class ContractTemplate(models.Model):
    _inherit = 'account.analytic.contract'

    generate_sequence = fields.Boolean('Generar secuencia ?', default=True)


class Contract(models.Model):
    _inherit = 'account.analytic.account'

    @api.one
    @api.depends('invoice_ids.state',
                 'amount_total')
    def _compute_totals(self):
        self.amount_invoiced = sum([i.amount_untaxed for i in self.invoice_ids if i.state != 'draft']) # noqa
        self.amount_to_invoice = self.amount_total - self.amount_invoiced

    STATES = [
        ('draft', 'Borrador'),
        ('run', 'En Proceso'),
        ('invoicing', 'Facturación'),
        ('stop', 'Detenido'),
        ('resciled', 'Resciliado'),
        ('changed', 'Modificado'),
        ('cancel', 'Anulado'),
        ('transfered', 'Transferido'),
        ('done', 'Finalizado')
    ]
    state = fields.Selection(STATES, string='Estado',
                             default='draft')
    amount_total = fields.Monetary(string='Total de Contrato')
    amount_invoiced = fields.Monetary(compute="_compute_totals",
                                      string="Facturado", store=True)
    amount_to_invoice = fields.Monetary(compute="_compute_totals",
                                        string="Por Facturar", store=True)
    invoice_ids = fields.One2many('account.invoice',
                                  'contract_id', string='Facturas')
    manager_id = fields.Many2one(
        'res.users',
        string="Vendedor"
    )

    @api.multi
    def action_cancel(self):
        self.write({'state': 'cancel'})

    @api.multi
    def action_start(self):
        self.write({'state': 'run'})
