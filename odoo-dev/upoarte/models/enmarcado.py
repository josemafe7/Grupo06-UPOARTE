# -*- coding: utf-8 -*-

from odoo import models, fields, api

class enmarcado(models.Model):
     _name = 'upoarte.enmarcado'
     
     name = fields.Char('ID', size=10, required=True)
     cliente_id = fields.Many2one('upoarte.cliente', 'Cliente');
     cuadro_id = fields.Many2one('upoarte.cuadro', 'Cuadro a enmarcar');
     marco_id = fields.Many2one('upoarte.marco', 'Selección de marco');
     empleado_ids = fields.Many2many('upoarte.empleado',string='Empleados');
     precioTotalEnmarcado = fields.Float('Precio total enmarcado',(8,2))