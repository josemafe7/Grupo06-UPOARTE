# -*- coding: utf-8 -*-

from odoo import models, fields, api

class proveedor(models.Model):
     _name = 'upoarte.proveedor'
     
     name = fields.Char('NIF', size=10, required=True)
     nombre = fields.Char('Nombre')
     apellidos = fields.Char('Apellidos')
     direccion = fields.Char('Direccion')
     telefono = fields.Integer('Telefono', size=9)
     pedido_ids = fields.One2many('upoarte.pedido','proveedor_id', 'Pedidos')
     
     _sql_constraints = [('proveedor_name_unique','UNIQUE (name)','El NIF debe ser único')]
     
     def borrarPedidos(self):
         self.write({'pedido_ids':[ (5, ) ]})