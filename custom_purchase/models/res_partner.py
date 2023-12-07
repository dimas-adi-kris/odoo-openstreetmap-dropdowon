from odoo import api, fields, models, _


class ResPartner(models.Model):
    _inherit = 'res.partner'

    def action_view_purchase_analyse_report(self):
        self.ensure_one()
        action = self.env['ir.actions.actions']._for_xml_id("custom_purchase.action_purchase_analyse_report_view")
        action['domain'] = [('partner_id', '=', self.id)]
        return action