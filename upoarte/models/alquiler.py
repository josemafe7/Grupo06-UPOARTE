# -*- coding: utf-8 -*-

from odoo import models, fields, api

class alquiler(models.Model):
     _name = 'upoarte.alquiler'
     
     name = fields.Char('ID',required=True)
     fechaInicioAlquiler = fields.Date('Fecha Inicio Alquiler')
     fechaFinAlquiler = fields.Date('Fecha Fin Alquiler')
     cliente_id = fields.Many2one('upoarte.cliente', 'Cliente')
     producto_ids = fields.Many2many('upoarte.producto',string='Productos')
     empleado_id = fields.Many2one('upoarte.empleado', 'Empleado')
     precioTotalAlquiler = fields.Float(compute='_calcularPrecioTotal',string='Precio total alquiler',store=True)
     
     _sql_constraints = [('alquiler_name_unique','UNIQUE (name)','El ID debe ser único')]
     
     @api.one
     @api.constrains('fechaFinAlquiler')
     def denegarFechaFinalPosterior(self):
         resultado = {}
         if(str(self.fechaInicioAlquiler) > str(self.fechaFinAlquiler)):
             raise models.ValidationError('La fecha fin de alquiler no puede ser antes que la de inicio')
         
     @api.one  
     @api.depends('producto_ids')  
     def _calcularPrecioTotal(self):
         precioTotal=0
         for productos in self.producto_ids:
             precioTotal = precioTotal + productos.precio
         
         self.precioTotalAlquiler = precioTotal
         
        
     @api.onchange('empleado_id')
     def denegarEmpleadosSinContrato(self):
        if self.empleado_id.state == 'candidato' or self.empleado_id.state == 'rechazado' or self.empleado_id.state == 'despedido':
            raise models.ValidationError('No se puede seleccionar un empleado sin contrato')
        
     def borrarProductos(self):
         self.write({'producto_ids':[ (5, ) ]})
         self.precioTotalAlquiler = 0
        
        
        
         