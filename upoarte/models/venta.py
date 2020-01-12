# -*- coding: utf-8 -*-

from odoo import models, fields, api

class venta(models.Model):
     _name = 'upoarte.venta'
     
     name = fields.Char('ID', size=10, required=True)
     cliente_id = fields.Many2one('upoarte.cliente', 'Cliente')
     producto_ids = fields.Many2many('upoarte.producto',string='Productos')
     empleado_id = fields.Many2one('upoarte.empleado', 'Empleado')
     precioTotalVenta = fields.Float(compute='_calcularPrecioTotal',string='Precio total venta',store=True)
     
     _sql_constraints = [('venta_name_unique','UNIQUE (name)','El ID debe ser único')]
     
     @api.one  
     @api.depends('producto_ids')  
     def _calcularPrecioTotal(self):
         precioTotal=0
         for productos in self.producto_ids:
             precioTotal = precioTotal + productos.precio
         
         self.precioTotalVenta = precioTotal
         
     @api.onchange('empleado_id')
     def denegarEmpleadosSinContrato(self):
        if self.empleado_id.state == 'candidato' or self.empleado_id.state == 'rechazado' or self.empleado_id.state == 'despedido':
            raise models.ValidationError('No se puede seleccionar un empleado sin contrato')
        
     def borrarProductos(self):
         self.write({'producto_ids':[ (5, ) ]})
         self.precioTotalVenta = 0