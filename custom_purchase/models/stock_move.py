from odoo import api, models, fields, _


class StockMove(models.Model):
    _inherit = 'stock.move'

    # domain_origin = fields.Char(string="Origin Domain", compute="_compute_domain_origin")
    origin_id = fields.Many2one('stock.move.origin', "Origin")

    # @api.depends('product_id')
    # def _compute_domain_origin(self):
    #     for rec in self:
    #         for
    #     domain = {'origin_id': [('id', 'in', self.proudct_id.supplier_id.ids)]}