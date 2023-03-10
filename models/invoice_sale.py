from odoo import models, fields, api


class InvoiceSale(models.Model):
    _name = 'invoice.sale'


class PurchaseApproval(models.Model):
    _inherit = 'account.move'

    related_so_ids = fields.Many2many('sale.order', string='Related SO',ondelete='cascade')

    @api.onchange('related_so_ids')
    def _onchange_related_so_ids(self):
        self.write({'invoice_line_ids': [(5, 0)]})
        vals=[]
        print('self.related_so_ids',self.related_so_ids)
        for rec in self.related_so_ids.order_line:
            print('rec',rec)


            value = {
                        'product_id': rec.product_id.product_tmpl_id.id,
                        'quantity': rec.product_uom_qty,
                        'price_unit': rec.price_unit,
                        'move_id': self._origin.id,
                        'move_type': 'out_invoice',
                    }

            vals.append((0,0,value))

            print(vals)
        self.update({
                'move_type': 'out_invoice',
                'invoice_line_ids': vals
            })
