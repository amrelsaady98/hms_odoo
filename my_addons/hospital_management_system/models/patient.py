import re
from dateutil.relativedelta import relativedelta
from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Patient(models.Model):
    _name = 'hms.patient'

    name = fields.Char(string='Name' , compute='_compute_name')
    first_name = fields.Char(string='First Name')
    last_name = fields.Char(string='Last Name')
    email = fields.Char(
        string="Email",
        required=True,
        unique=True,
    )
    birth_date = fields.Date(string='Birth Date')
    status = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('Critical', 'Critical'),
    ], default='undetermined', string='Status')
    history = fields.Html(string='History')
    cr_ratio = fields.Float(string='CR Ratio')
    blood_type = fields.Selection([
        ('a+', 'A+'),
        ('b+', 'B+'),
        ('ab+', 'AB+'),
        ('o+', 'O+'),
        ('a-', 'A-'),
        ('b-', 'B-'),
        ('ab-', 'AB-'),
        ('o-', 'O-'),
    ])
    pcr = fields.Boolean(string='PCR', default=True)
    image = fields.Binary(string='Image')
    address = fields.Char(string='Address')
    age = fields.Integer(string='Age', compute='_compute_age')
    department = fields.Many2one('hms.department', string='Department', domain=[('is_open', '=', True)])
    doctor = fields.One2many('hms.doctor', 'doctor_id', string='Doctor', copy=False)
    patient_logs = fields.One2many('hms.patient_log', 'patient_id', string='Patient Log')

    _sql_constraints = [
        ('email_uniq', 'unique(email)', 'The email address must be unique.')
    ]

    @api.constrains('email')
    def _check_email(self):
        email_regex = r'^\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
        for record in self:
            if not re.match(email_regex, record.email):
                raise ValidationError("Invalid email address format.")

    @api.constrains('cr_ratio')
    def _validate_pcr(self):
        for rec in self:
            if rec.cr_ratio <= 0.0:
                raise ValidationError("Invalid CR value")

    @api.depends('first_name', 'last_name')
    def _compute_name(self):
        for record in self:
            record.name = f"{record.first_name} {record.last_name}"

    @api.depends('birth_date')
    def _compute_age(self):
        for rec in self:
            if rec.birth_date:
                rec.age = relativedelta(fields.Date.today(), rec.birth_date).years
            else:
                rec.age = 0

    def action_undetermined(self):
        for record in self:
            record.status = 'undetermined'

    def action_good(self):
        for record in self:
            record.status = 'good'

    def action_fair(self):
        for record in self:
            record.status = 'fair'

    def action_critical(self):
        for record in self:
            record.status = 'Critical'

    # @api.model --> no change
    def write(self, vals):
        if 'status' in vals:
            old_status = self.status
            new_status = vals.get('status')
            if old_status != new_status:
                self._create_log(f"Status Updated to {new_status}")
        return super(Patient, self).write(vals)

    def _create_log(self, description):
        self.env['hms.patient_log'].create({
            'patient_id': self.id,
            'created_by': self.env.user.id,
            'date': fields.Date.context_today(self),
            'description': description
        })

    @api.onchange('age')
    def _onchange_age(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': 'PCR Field Checked',
                    'message': 'The PCR field has been automatically checked because the age is below 30.',
                }
            }

    def action_add_log_wizard(self):
        action = self.env['ir.actions.actions']._for_xml_id('hospital_management_system.action_patient_log_wizard')
        action['context'] = {
            'default_patient_id': self.id
        }

        # self.env['lr.publisher'].print_hi()
        # self.env['hms.patient_log'].create(action)
        return action

    @api.model
    def _get_report_values(self, docids, data=None):
        docs = self.browse(docids)
        return {
            'docs': docs,
        }

    @api.model
    def action_print_patient_report(self, another):
        self.ensure_one()
        return self.env.ref('hospital_management_system.action_report_hms_patient_status').report_action(self)


class PatientLog(models.Model):
    _name = "hms.patient_log"

    patient_id = fields.Many2one('hms.patient')
    created_by = fields.Many2one('hms.doctor', string='Created By')
    date = fields.Date(string='Date')
    description = fields.Char(string='Description')
