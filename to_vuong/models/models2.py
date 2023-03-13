# -*- coding: utf-8 -*-

from odoo import models, fields, api


class to_vuong(models.Model):
    _name = 'to_vuong.to_vuong2'
    _description = 'to_vuong.to_vuong2'

    bill_fee = fields.Integer("BILL FWD FEE")
    customs_fee = fields.Integer("Customs fee")
    local_charge = fields.Integer("Local charge")
    over_time = fields.Integer("Over time")
    basic_fee = fields.Integer("BASIC FEE")
    handlin = fields.Integer("HANDLIN G CD FWD")
    red_inv = fields.Char("RED INV")
    port_charge = fields.Integer("PORT CHARGE")
    cd_fwd_fee = fields.Char("CD FWD FEE")
    note = fields.Char("Note")
    sum = fields.Integer("Sum")
    compare = fields.Char("Compare")
