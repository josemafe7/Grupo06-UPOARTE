# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedido(models.Model):
     _name = 'upoarte.pedido'
     
     idPedido = fields.Char('ID Pedido', size=9, required=True)
     fecha = fields.Date('Fecha Pedido', required=True)
     producto_ids = fields.Many2many('upoarte.producto',string='Productos');
     proveedor_id = fields.Many2one('upoarte.proveedor','Proveedor');
     empleado_id = fields.Many2one('upoarte.empleado','Empleado');