# -*- coding: utf-8 -*-
from odoo import api, fields, models

class PetModel(models.Model):
    _name = "pet_model"
    _description = "modelo de mascotas"
    
    name = fields.Char(string='name', required=True)
    age = fields.Integer(string='age')
    color = fields.Char(string='color')
    type = fields.Selection([('small', 'Small'),
                             ('medium', 'Medium'),
                             ('big', 'Big')], string='type', default="small", required=True)

 
