# -*- coding: utf-8 -*-

from odoo import models, fields, api

class empleado(models.Model):
     _name = 'upoarte.empleado'
     
     name = fields.Char('DNI', size=10, required=True)
     nombre = fields.Char('Nombre')
     apellidos = fields.Char('Apellidos')
     direccion = fields.Char('Dirección')
     telefono = fields.Integer('Teléfono', size=9)
     sueldo = fields.Float('Sueldo',(6,2))
     venta_ids = fields.One2many('upoarte.venta','empleado_id', 'Ventas realizadas')
     alquiler_ids = fields.One2many('upoarte.alquiler','empleado_id', 'Alquileres realizados')
     enmarcado_ids = fields.Many2many('upoarte.enmarcado',string='Enmarcados realizados')
     pedido_ids = fields.One2many('upoarte.pedido','empleado_id', 'Pedidos realizados')
    
     state = fields.Selection([('candidato','Candidato'),
                              ('contratado','Contratado'),
                              ('rechazado','Rechazado'),
                              ('despedido','Despedido'),],
                              'Estado',
                              default='candidato')
     
     _sql_constraints = [('empleado_name_unique','UNIQUE (name)','El DNI debe ser único')]
          
     @api.one
     def btn_submit_to_contratado(self):
        self.write({'state':'contratado'})
        
     @api.one
     def btn_submit_to_rechazado(self):
        self.write({'state':'rechazado'})
    
     @api.one
     def btn_submit_to_despedido(self):
        self.write({'state':'despedido'})
        
        
     @api.onchange('venta_ids','alquiler_ids','enmarcado_ids','pedido_ids')
     def onchange_empleado(self):
        if self.state == 'candidato' or self.state == 'rechazado' or self.state == 'despedido':
            raise models.ValidationError('El empleado tiene que estar contratado para poder realizar operaciones')
        
        
        
        