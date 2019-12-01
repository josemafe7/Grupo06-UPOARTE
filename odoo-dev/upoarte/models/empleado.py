# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empleado(models.Model):
     _name = 'upoarte.empleado'
     
     name = fields.Char('DNI', size=10, required=True)
     nombre = fields.Char('Nombre')
     apellidos = fields.Char('Apellidos')
     direccion = fields.Char('Dirección')
     telefono = fields.Integer('Teléfono', size=9)
     sueldo = fields.Float('Sueldo',(6,2))
     venta_ids = fields.One2many('upoarte.venta','empleado_id', 'Ventas realizadas');
     alquiler_ids = fields.One2many('upoarte.alquiler','empleado_id', 'Alquileres realizados');
     enmarcado_ids = fields.Many2many('upoarte.enmarcado',string='Enmarcados realizados');
     pedido_ids = fields.One2many('upoarte.pedido','empleado_id', 'Pedidos realizados');