from odoo import models, fields
from odoo.exceptions import UserError


class AddPatientLogWizard(models.TransientModel):
    _name = 'hms.add.patient.log'

    description = fields.Char(string='Description')
    patient_id = fields.Many2one('hms.patient')

    def action_create_log(self):

        self.ensure_one()
        # if not record.description:
        #     raise UserError('Please enter a description.')

        # print(self.description)
        self.env['hms.patient_log'].create({
            'patient_id': self.patient_id.id,
            'created_by': self.env.user.id,
            'date': fields.Date.context_today(self),
            'description': self.description,
        })
        print(f'{self.patient_id.id}: {self.description}')
        return {'type': 'ir.actions.act_window_close'}


'''
RPC_ERROR
Odoo Server Error
Traceback (most recent call last):
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/http.py", line 1781, in _serve_db
    return service_model.retrying(self._serve_ir_http, self.env)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/service/model.py", line 133, in retrying
    result = func()
             ^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/http.py", line 1808, in _serve_ir_http
    response = self.dispatcher.dispatch(rule.endpoint, args)
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/http.py", line 2012, in dispatch
    result = self.request.registry['ir.http']._dispatch(endpoint)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/addons/base/models/ir_http.py", line 222, in _dispatch
    result = endpoint(**request.params)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/http.py", line 757, in route_wrapper
    result = endpoint(self, *args, **params_ok)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/addons/web/controllers/dataset.py", line 28, in call_button
    action = self._call_kw(model, method, args, kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/addons/web/controllers/dataset.py", line 20, in _call_kw
    return call_kw(request.env[model], method, args, kwargs)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/api.py", line 468, in call_kw
    result = _call_kw_multi(method, model, args, kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/api.py", line 453, in _call_kw_multi
    result = method(recs, *args, **kwargs)
             ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/my_addons/hospital_management_system/wizards/add_patient_log_wizard.py", line 15, in action_create_log
    self.env['hms.patient_log'].create({
  File "<decorator-gen-0>", line 2, in create
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/api.py", line 414, in _model_create_multi
    return create(self, [arg])
           ^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/models.py", line 4626, in create
    records = self._create(data_list)
              ^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/models.py", line 4814, in _create
    cr.execute(SQL(
  File "/home/amr-el-saady/PycharmProjects/odoo17/odoo/sql_db.py", line 332, in execute
    res = self._obj.execute(query, params)
          ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/amr-el-saady/PycharmProjects/odoo17/venv/lib/python3.12/site-packages/psycopg2/extensions.py", line 113, in getquoted
    pobjs = [adapt(o) for o in self._seq]
             ^^^^^^^^
psycopg2.ProgrammingError: can't adapt type 'hms.patient'

The above server error caused the following client error:
RPC_ERROR: Odoo Server Error
    RPCError@http://localhost:8069/web/assets/debug/web.assets_web.js:27887:9
    makeErrorFromResponse@http://localhost:8069/web/assets/debug/web.assets_web.js:27913:19
    jsonrpc/promise</<@http://localhost:8069/web/assets/debug/web.assets_web.js:27961:48
    
'''
