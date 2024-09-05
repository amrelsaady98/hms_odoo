from odoo import fields, models


class Department(models.Model):
    _name = 'hms.department'

    name = fields.Char(string='Name')
    capacity = fields.Integer(string='Capacity')
    is_open = fields.Boolean(string='Is Open')