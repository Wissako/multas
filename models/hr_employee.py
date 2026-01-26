from odoo import models, fields

class HREmployee(models.Model):
    _inherit = 'hr.employee'

    multas_ids = fields.One2many('gestion.multa', 'empleado_id', string="Multas")
