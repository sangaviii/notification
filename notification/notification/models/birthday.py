from odoo import api, fields, models
import datetime


class MyBirthday(models.Model):
    _name = 'birthday.celebration'

    name = fields.Char(string='Name')
    birthdate = fields.Date(string='Date of Birth')
    email = fields.Char(string='Email')

    # @api.model
    # def set_dob(self):
    #     today = fields.Date.today()
    #     partners = self.search([('birthdate', '=', today)])
    #     template = self.env.ref('notification.mail_template_birthday_event')
    #
    #     for event in partners:
    #         template.send_mail(event.id, force_send=True)


