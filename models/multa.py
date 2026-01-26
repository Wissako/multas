from odoo import models, fields, api

class Multa(models.Model):
    _name="gestion.multa"
    _description="Modelo para gestionar multas de empleados"
    
    descripcion=fields.Text(string="Descripción)", required=True)
    tipo_multa_id=fields.Many2one('gestion.tipo_multa', string="Tipo de Multa",required=True)
    empleado_id=fields.Many2one('hr.employee', string="Empleado involucrado", required=True)
    importe=fields.Float(string="Importe de la multa")
    pagada=fields.Boolean(string="Pagada por la empresa", default=False)
    nombre_empleado=fields.Char(string="Nombre del Empleado", related="empleado_id.name", store=False)

