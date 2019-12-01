# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alquiler(models.Model):
     _name = 'upoarte.alquiler'
     
     name = fields.Char('ID',required=True)
     fechaInicioAlquiler = fields.Date('Fecha Inicio Alquiler')
     fechaFinAlquiler = fields.Date('Fecha Fin Alquiler')
     cliente_id = fields.Many2one('upoarte.cliente', 'Cliente');
     producto_ids = fields.Many2many('upoarte.producto',string='Productos');
     empleado_id = fields.Many2one('upoarte.empleado', 'Empleado');
     precioTotalAlquiler = fields.Float('Precio total alquiler',(8,2))