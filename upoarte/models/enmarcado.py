# -*- coding: utf-8 -*-

from odoo import models, fields, api

class enmarcado(models.Model):
     _name = 'upoarte.enmarcado'
     
     name = fields.Char('ID', size=10, required=True)
     cliente_id = fields.Many2one('upoarte.cliente', 'Cliente')
     cuadro_id = fields.Many2one('upoarte.cuadro', 'Cuadro a enmarcar')
     marco_id = fields.Many2one('upoarte.marco', 'Selección de marco')
     empleado_ids = fields.Many2many('upoarte.empleado',string='Empleados')
     precioTotalEnmarcado = fields.Float(compute='_calcularPrecioTotal',string='Precio total enmarcado',store=True)
     
     _sql_constraints = [('enmarcado_name_unique','UNIQUE (name)','El ID debe ser único')]
     
     @api.onchange('empleado_ids')
     def denegarEmpleadosSinContrato(self):
        for empleado in self.empleado_ids:
            if self.empleado_id.state == 'candidato' or self.empleado_id.state == 'rechazado' or self.empleado_id.state == 'despedido':
                raise models.ValidationError('No se puede seleccionar un empleado sin contrato')
            
     @api.one  
     @api.depends('cuadro_id','marco_id')  
     def _calcularPrecioTotal(self):
         self.precioTotalEnmarcado = self.cuadro_id.precio + self.marco_id.precio
         
     def borrarEmpleados(self):
         self.write({'empleado_ids':[ (5, ) ]})