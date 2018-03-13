# -*- coding: utf-8 -*-
from odoo import http

# class GoInside(http.Controller):
#     @http.route('/go_inside/go_inside/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/go_inside/go_inside/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('go_inside.listing', {
#             'root': '/go_inside/go_inside',
#             'objects': http.request.env['go_inside.go_inside'].search([]),
#         })

#     @http.route('/go_inside/go_inside/objects/<model("go_inside.go_inside"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('go_inside.object', {
#             'object': obj
#         })