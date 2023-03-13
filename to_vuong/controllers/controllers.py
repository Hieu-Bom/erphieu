# -*- coding: utf-8 -*-
# from odoo import http


# class ToVuong(http.Controller):
#     @http.route('/to_vuong/to_vuong', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/to_vuong/to_vuong/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('to_vuong.listing', {
#             'root': '/to_vuong/to_vuong',
#             'objects': http.request.env['to_vuong.to_vuong'].search([]),
#         })

#     @http.route('/to_vuong/to_vuong/objects/<model("to_vuong.to_vuong"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('to_vuong.object', {
#             'object': obj
#         })
