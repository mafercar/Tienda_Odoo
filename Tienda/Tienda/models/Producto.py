from odoo import models, fields, api

class Producto(models.Model):

    _name = 'producto'

    identificador = fields.Integer('Identificador', required = True)
    nombre = fields.Char('Nombre', required = True)
    precio = fields.Float('Precio', required = True)

    def name_get(self):

        res = []

        for record in self:

            name = record.nombre
            res.append((record.id, name))

        return res