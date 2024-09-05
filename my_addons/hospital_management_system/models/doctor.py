from odoo import models, fields, api


class Doctor(models.Model):
    _name = 'hms.doctor'

    name = fields.Char(string='Name', compute='_compute_name')
    doctor_id = fields.Many2one('hms.patient')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    image = fields.Binary(string='Image')

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for record in self:
            record.name = f"Dr. {record.first_name} {record.last_name}"
