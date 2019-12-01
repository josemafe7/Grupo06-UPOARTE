# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
     _name = 'upoarte.venta'
     
     name = fields.Char('ID', size=10, required=True)
     cliente_id = fields.Many2one('upoarte.cliente', 'Cliente');
     producto_ids = fields.Many2many('upoarte.producto',string='Productos');
     empleado_id = fields.Many2one('upoarte.empleado', 'Empleado');
     precioTotalVenta = fields.Float('Precio total venta',(8,2))
     