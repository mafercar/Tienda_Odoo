from odoo import models, fields, api

class LineaFactura(models.Model):

    _name = 'linea_factura'

    identificador = fields.Integer('Identificador', required = True)
    identificadorFactura = fields.Integer('Identificador de factura', required = True)
    producto = fields.Many2one('producto', 'Producto')
    cantidad = fields.Integer('Cantidad', required = True)
    precio = fields.Float(

        compute = "get_precio",
        String = "Precio",
        required = True
    )

    def get_precio(self):

        for record in self:

            record.precio = record.producto.precio * record.cantidad

    def name_get(self):

        res = []

        for record in self:

            name = record.producto.nombre
            res.append((record.id, name))

        return res