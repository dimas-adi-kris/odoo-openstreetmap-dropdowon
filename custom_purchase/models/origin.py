from odoo import api, models, fields, _


class OriginMove(models.Model):
    _name = 'stock.move.origin'
    _description = 'Stock Move origin'

    name = fields.Char(string="Nom")
    latitude = fields.Float(string="Latitude", digits=(16, 9))
    longitude = fields.Float(string="Longitude", digits=(16, 9))

    address = fields.Char(string="Rue")
