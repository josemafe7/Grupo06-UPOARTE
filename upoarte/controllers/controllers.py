# -*- coding: utf-8 -*-
from odoo import http

# class Upoarte(http.Controller):
#     @http.route('/upoarte/upoarte/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/upoarte/upoarte/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('upoarte.listing', {
#             'root': '/upoarte/upoarte',
#             'objects': http.request.env['upoarte.upoarte'].search([]),
#         })

#     @http.route('/upoarte/upoarte/objects/<model("upoarte.upoarte"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('upoarte.object', {
#             'object': obj
#         })