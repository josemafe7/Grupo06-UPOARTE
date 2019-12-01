# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proveedor(models.Model):
     _name = 'upoarte.proveedor'
     
     name = fields.Char('NIF', size=10, required=True)
     nombre = fields.Char('Nombre')
     apellidos = fields.Char('Apellidos')
     direccion = fields.Char('Direccion')
     telefono = fields.Integer('Telefono', size=9)
     pedido_ids = fields.One2many('upoarte.pedido','proveedor_id', 'Pedidos');