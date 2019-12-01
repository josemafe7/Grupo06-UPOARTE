# -*- coding: utf-8 -*-

from odoo import models, fields, api

class marco(models.Model):
     _inherit = 'upoarte.producto'
     _name = 'upoarte.marco'
     
     descripcion = fields.Char("Descripción")
     medidas = fields.Float('Medidas')
     enmarcado_ids = fields.One2many('upoarte.enmarcado','marco_id', 'Enmarcados');