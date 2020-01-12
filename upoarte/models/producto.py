# -*- coding: utf-8 -*-

from odoo import models, fields, api

class producto(models.Model):
     _name = 'upoarte.producto'
     
     name = fields.Char('ID', size=10, required=True)
     nombre = fields.Char('Nombre')
     precio = fields.Float('Precio',(7,2),required=True)
     venta_ids = fields.Many2many('upoarte.venta',string='Ventas')
     alquiler_ids = fields.Many2many('upoarte.alquiler',string='Alquileres')
     pedido_ids = fields.Many2many('upoarte.pedido',string='Productos')
     
     _sql_constraints = [('producto_name_unique','UNIQUE (name)','El ID debe ser único')]
     