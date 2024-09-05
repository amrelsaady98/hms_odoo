{
    'name': 'Hospital Management System',
    'version': '1.0',
    'summary': 'hospital management system',
    'description': '''
        Sysytem to manage hospitals and clinics processes and patients data
    ''',
    'author': 'Amr El-Saady',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/base_menus.xml',
        'views/patient_view.xml',
        'views/department_view.xml',
        'views/doctor_view.xml',
        'wizards/add_patient_log_wizard_view.xml',
        'reports/patient_report.xml',
    ],
    'installable': True,
    'application': True,
}