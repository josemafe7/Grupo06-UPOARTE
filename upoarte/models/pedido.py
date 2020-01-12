# -*- coding: utf-8 -*-

from odoo import models, fields, api

class pedido(models.Model):
     _name = 'upoarte.pedido'
     
     idPedido = fields.Char('ID Pedido', size=9, required=True)
     fecha = fields.Date('Fecha Pedido', required=True)
     producto_ids = fields.Many2many('upoarte.producto',string='Productos')
     proveedor_id = fields.Many2one('upoarte.proveedor','Proveedor')
     empleado_id = fields.Many2one('upoarte.empleado','Empleado')
     precioTotalPedido = fields.Float(compute='_calcularPrecioTotal',string='Precio total pedido',store=True)
     
     state = fields.Selection([('borrador','Borrador'),
                              ('confirmado','Confirmado'),
                              ('enviado','Enviado'),
                              ('rechazado','Rechazado'),],
                              'Estado',
                              default='borrador')
     
     _sql_constraints = [('pedido_idPedido_unique','UNIQUE (idPedido)','El ID Pedido debe ser único')]
     
     @api.one
     def btn_submit_to_confirmado(self):
        self.write({'state':'confirmado'})
    
     @api.one
     def btn_submit_to_enviado(self):
        self.write({'state':'enviado'})
     
     @api.one
     def btn_submit_to_rechazado(self):
        self.write({'state':'rechazado'})
    
     @api.onchange('idPedido','fecha','producto_ids','proveedor_id','empleado_id')
     def onchange_pedido(self):
        if self.state == 'rechazado':
            raise models.ValidationError('El pedido está rechazado')
    
     @api.one  
     @api.depends('producto_ids')  
     def _calcularPrecioTotal(self):
         precioTotal=0
         for productos in self.producto_ids:
             precioTotal = precioTotal + productos.precio
         
         self.precioTotalPedido = precioTotal
        
        
        