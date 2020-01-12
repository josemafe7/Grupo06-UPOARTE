# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cliente(models.Model):
     _name = 'upoarte.cliente'
     
     name = fields.Char('DNI', size=10, required=True)
     nombre = fields.Char('Nombre')
     apellidos = fields.Char('Apellidos')
     direccion = fields.Char('Dirección')
     telefono = fields.Integer('Teléfono', size=9)
     venta_ids = fields.One2many('upoarte.venta','cliente_id', 'Ventas')
     alquiler_ids = fields.One2many('upoarte.alquiler','cliente_id', 'Alquileres')
     enmarcado_ids = fields.One2many('upoarte.enmarcado','cliente_id', 'Enmarcados')
     
     _sql_constraints = [('cliente_name_unique','UNIQUE (name)','El DNI debe ser único')]
     