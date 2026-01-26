from odoo import models, fields

class TipoMulta(models.Model):
    _name="gestion.tipo_multa"
    _description="Tipos de multas"

    name=fields.Char(string="Tipo de sanción", required=True)
