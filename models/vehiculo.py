# -*- coding: utf-8 -*-
from odoo import models, fields

class Vehiculo(models.Model):
    _name = 'gestion.vehiculo'
    _description = 'Gestión de Vehículos'

    name = fields.Char(string="Matrícula", required=True)
    marca = fields.Char(string="Marca", required=True)
    modelo = fields.Char(string="Modelo", required=True)
    kilometros = fields.Float(string="Kilómetros")
    
    
    conductor_id = fields.Many2one('hr.employee', string="Conductor Asignado")