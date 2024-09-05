# from odoo import models, fields, api


# class Patient(models.Model):
#     _name = 'hms.patient'
#
#     first_name = fields.Char(string='First Name')
#     last_name = fields.Char(string='Last Name')
#     birth_date = fields.Date(string='Birth Date')
#     history = fields.Html(string='History')
#     cr_ratio = fields.Float(string='CR Ratio')
#     blood_type = fields.Selection([
#         ('a+', 'A+'),
#         ('b+', 'B+'),
#         ('ab+', 'AB+'),
#         ('o+', 'O+'),
#         ('a-', 'A-'),
#         ('b-', 'B-'),
#         ('ab-', 'AB-'),
#         ('o-', 'O-'),
#     ])
#     pcr = fields.Boolean(string='PCR')
#     image = fields.Binary(string='Image')
#     address = fields.Char(string='Address')
#     age = fields.Integer(string='Age')
#     department = fields.Many2one('hms.department', string='Department')


# class Department(models.Model):
#     _name = 'hms.department'
#
#     name = fields.Char(string='Name')
#     capacity = fields.Integer(string='Capacity')
#     is_open = fields.Boolean(string='Is Open')
#     # patients = fields.One2many('hms.patient', string='Patients')
#
#
# class Doctor(models.Model):
#     _name = 'hms.doctor'
#
#     first_name = fields.Char(string='First Name')
#     last_name = fields.Char(string='Last Name')
#     image = fields.Binary(string='Image')

# UncaughtPromiseError > OwlError
# Uncaught Promise > An error occured in the owl lifecycle (see this Error's "cause" property)
# OwlError: An error occured in the owl lifecycle (see this Error's "cause" property)
#     OwlError@http://localhost:8069/web/assets/debug/web.assets_web.js:7671:5
#     handleError@http://localhost:8069/web/assets/debug/web.assets_web.js:9163:35
#     handleError@http://localhost:8069/web/assets/debug/web.assets_web.js:13368:20
#     initiateRender@http://localhost:8069/web/assets/debug/web.assets_web.js:9959:26
#
#
# Caused by: TypeError: this.fields[name] is undefined
#     visitField@http://localhost:8069/web/assets/debug/web.assets_web.js:70671:31
#     parse/<@http://localhost:8069/web/assets/debug/web.assets_web.js:70623:26
#     visit@http://localhost:8069/web/assets/debug/web.assets_web.js:42214:49
#     visitChildren@http://localhost:8069/web/assets/debug/web.assets_web.js:42210:26
#     visitSearch@http://localhost:8069/web/assets/debug/web.assets_web.js:70812:9
#     parse/<@http://localhost:8069/web/assets/debug/web.assets_web.js:70612:26
#     visit@http://localhost:8069/web/assets/debug/web.assets_web.js:42214:49
#     visitXML@http://localhost:8069/web/assets/debug/web.assets_web.js:42221:10
#     parse@http://localhost:8069/web/assets/debug/web.assets_web.js:70609:17
#     load@http://localhost:8069/web/assets/debug/web.assets_web.js:72121:78
#     setup/<@http://localhost:8069/web/assets/debug/web.assets_web.js:75157:36
#     initiateRender/<@http://localhost:8069/web/assets/debug/web.assets_web.js:9956:63
#     initiateRender@http://localhost:8069/web/assets/debug/web.assets_web.js:9956:50
#     createComponent/<@http://localhost:8069/web/assets/debug/web.assets_web.js:13361:36
#     template@http://localhost:8069/web/assets/debug/web.assets_web.js line 13130 > Function:19:12
#     _render@http://localhost:8069/web/assets/debug/web.assets_web.js:9306:38
#     render@http://localhost:8069/web/assets/debug/web.assets_web.js:9298:18
#     initiateRender@http://localhost:8069/web/assets/debug/web.assets_web.js:9963:23
#