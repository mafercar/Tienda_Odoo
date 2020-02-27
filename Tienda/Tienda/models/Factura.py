from odoo import models, fields, api

class Factura(models.Model):

    _name = 'factura'

    identificador = fields.Integer('Identificador', required = True)
    lineas_factura = fields.One2many('linea_factura', "identificadorFactura", 'Lineas')
    precio = fields.Float(

        compute = "get_precio",
        String = "Precio",
        required = True
    )

    def get_precio(self):

        for record in self:

            precio = 0

            for record_2 in record.lineas_factura:

                precio += record_2.precio

            record.precio = precio