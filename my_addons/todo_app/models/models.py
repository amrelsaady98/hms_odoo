# Models: ticket (name, number, tag, state(new, doing and done), file, assign to(+),
# description)

from odoo import models, fields


class Ticket(models.Model):
    _name = 'todo.ticket'

    name = fields.Char(string='Ticket Name', required=True)
    number = fields.Integer(string='Ticket Number')
    tag = fields.Char(string='Ticket Tag')
    status = fields.Selection(
        [
            ('new', 'New'),
            ('is_doing', 'Is Doing'),
            ('done', 'Done')
        ],
        string='Status',
        default='new',
        required=True
    )
    file = fields.Binary(string='File')

    def action_done(self):
        for todo in self:
            todo.status = 'done'

    def action_new(self):
        for todo in self:
            todo.status = 'new'

    def action_is_doing(self):
        for todo in self:
            todo.status = 'is_doing'
