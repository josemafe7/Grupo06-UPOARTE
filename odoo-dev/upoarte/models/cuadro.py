# -*- coding: utf-8 -*-

from odoo import models, fields, api

class cuadro(models.Model):
     _inherit = 'upoarte.producto'
     _name = 'upoarte.cuadro'
     
     estilo = fields.Char('Estilo')
     autor = fields.Char('Autor')
     medidas = fields.Float('Medidas')
     enmarcado_ids = fields.One2many('upoarte.enmarcado','cuadro_id', 'Enmarcados');