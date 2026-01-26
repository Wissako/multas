# from odoo import http


# class Multas(http.Controller):
#     @http.route('/multas/multas', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/multas/multas/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('multas.listing', {
#             'root': '/multas/multas',
#             'objects': http.request.env['multas.multas'].search([]),
#         })

#     @http.route('/multas/multas/objects/<model("multas.multas"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('multas.object', {
#             'object': obj
#         })

