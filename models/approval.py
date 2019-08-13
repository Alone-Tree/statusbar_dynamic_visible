# -*- coding: utf-8 -*-

from odoo import models, fields, api, _


class Approval(models.Model):
    _name = 'approval'
    _description = 'Approval'

    name = fields.Char(string='姓名')
    date = fields.Date(string='日期', default=fields.Date.context_today, requird=True)
    title = fields.Char(string='标题')
    summary = fields.Text(string='内容')
    state = fields.Selection([
        ('draft', '草稿'),
        ('submit', '已提交'),
        ('captain_approval', '组长审批'),
        ('manager_approval', '经理审批'),
        ('boss_approval', '老板审批'),
        ('reject', '驳回'),
        ('agree', '同意'),
        ('dynamic_state', '待审批'),  # 动态显示，设置默认值为'待审批'
    ], string='单据状态', copy=False, index=True, track_visibility='onchange', track_sequence=3, default='draft')

    def button_submit(self):
        self.write({'state': 'submit'})

    def button_set_draft(self):
        self.write({'state': 'draft'})

    def button_captain_approval(self):
        self.write({'state': 'captain_approval'})

    def button_manager_approval(self):
        self.write({'state': 'manager_approval'})

    def button_boss_approval(self):
        self.write({'state': 'boss_approval'})

    def button_reject(self):
        self.write({'state': 'reject'})

    def button_agree(self):
        self.write({'state': 'agree'})

