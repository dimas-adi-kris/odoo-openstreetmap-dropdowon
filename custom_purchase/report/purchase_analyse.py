from odoo import api, models, fields, tools


class PurchaseAnalyseReport(models.Model):
    _name = "purchase.analyse.report"
    _description = "to analyse the purchase based on product"
    _auto = False

    receipt_date = fields.Datetime(string="Receipt Date")
    partner_id = fields.Many2one('res.partner', string="Supplier")
    product_id = fields.Many2one('product.product', string="Product")
    currency_id = fields.Many2one('res.currency', string="Currency")
    product_uom_qty = fields.Float(string="Qty Purchased")
    qty_received = fields.Float(string="Qty Received")
    product_uom = fields.Many2one('uom.uom', string="UoM")
    difference = fields.Float(string="Difference")

    qty_invoice = fields.Float(string="Qty Invoiced")
    picking_name = fields.Char(string="GRN")
    difference_percentage = fields.Float(string="Difference Percentage", group_operator="avg")

    unit_received_price = fields.Monetary(string="Unit Received Price")
    price_unit = fields.Monetary(string="Price")

    def init(self):
        tools.drop_view_if_exists(self.env.cr, 'purchase_analyse_report')
        query = """
            CREATE OR REPLACE VIEW purchase_analyse_report AS (
            SELECT ROW_NUMBER() OVER () AS id,
                po.effective_date AS receipt_date,
                po.partner_id,
                po.currency_id,
                pol.product_id,
                pol.product_uom_qty,
                pol.product_uom,
                pol.qty_received,
                sp.name AS picking_name,
                aml.quantity AS qty_invoice,
                pol.qty_received - pol.product_uom_qty AS difference,
                abs((pol.qty_received - pol.product_uom_qty)/pol.product_uom_qty) AS difference_percentage,
                (pol.price_unit * pol.product_uom_qty)/pol.qty_received AS unit_received_price,
                pol.price_unit
            FROM purchase_order_line pol 
            LEFT JOIN purchase_order po ON po.id = pol.order_id
            LEFT JOIN
                stock_move sm ON sm.purchase_line_id = pol.id
            LEFT JOIN 
                stock_picking sp ON sp.id = sm.picking_id
            LEFT JOIN
                account_move_line aml ON aml.purchase_line_id = pol.id
            WHERE pol.product_id IS NOT NULL AND po.effective_date IS NOT NULL and sm.state='done'
            );
        """
        self.env.cr.execute(query)
