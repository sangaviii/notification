from odoo import models, fields, api
import datetime


class Event(models.Model):
    _inherit = 'birthday.celebration'

    @api.model
    def set_dob(self):
        today = fields.Date.today()
        partners = self.search([('birthdate', '=', today)])
        template = self.env.ref('notification.mail_template_birthday_event')

        for event in partners:
            template.send_mail(event.id, force_send=True)
    # @api.model
    # def set_email(self):
    #     today = fields.Date.today()
    #     anniversary_event = self.search([('event_date', '=', today)])
    #     template = self.env.ref('function.email_template_anniversary_mail')
    #
    #     for event in anniversary_event:
    #         template.send_mail(event.id, force_send=True)


