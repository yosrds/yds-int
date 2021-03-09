# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import UserError, ValidationError
from odoo.tools.safe_eval import safe_eval


class Users(models.Model):
    _inherit = 'res.users'

    invoices = fields.One2many("account.move",
                               string='Invoices',
                               inverse_name='invoice_user_id')


class HrSalaryRule(models.Model):
    _inherit = 'hr.salary.rule'

    condition_python = fields.Text(default='''
# Available variables:
#----------------------
# payslip: object containing the payslips
# employee: hr.employee object
# contract: hr.contract object
# rules: object containing the rules code (previously computed)
# categories: object containing the computed salary rule categories (sum of amount of all rules belonging to that category).
# worked_days: object containing the computed worked days
# inputs: object containing the computed inputs.
# employee_invoices_total_amount: integer containing the total paid amount for invoices made by employee

# Note: returned value have to be set in the variable 'result'

result = rules.NET > categories.NET * 0.10''')

    amount_python_compute = fields.Text(default='''
# Available variables:
#----------------------
# payslip: object containing the payslips
# employee: hr.employee object
# contract: hr.contract object
# rules: object containing the rules code (previously computed)
# categories: object containing the computed salary rule categories (sum of amount of all rules belonging to that category).
# worked_days: object containing the computed worked days.
# inputs: object containing the computed inputs.
# employee_invoices_total_amount: integer containing the total paid amount for invoices made by employee

# Note: returned value have to be set in the variable 'result'

result = contract.wage * 0.10''')

    def _compute_rule(self, localdict):
        """
        :param localdict: dictionary containing the current computation environment
        :return: returns a tuple (amount, qty, rate)
        :rtype: (float, float, float)
        """
        localdict['employee_invoices_total_amount'] = localdict[
            'employee'].user_id.invoices.search([('payment_state', '=', 'paid')
                                                 ]).amount_total_signed
        return super(HrSalaryRule, self)._compute_rule(localdict)
