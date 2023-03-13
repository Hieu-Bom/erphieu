# -*- coding: utf-8 -*-

from odoo import models, fields, api


class to_vuong(models.Model):
    _name = 'to_vuong.to_vuong'
    _description = 'to_vuong.to_vuong'

    section = fields.Selection([('relate', 'Relate'), ('vendor', 'Vendor')], string="Section")
    bl_no = fields.Char('B/L No')
    material_tool = fields.Char("MATERIAL OR TOOL")
    exporter = fields.Selection([('gn', 'GN'), ('vendor', 'Vendor')], string="Exporter")
    incoterms = fields.Selection([('cfr', 'CFR'), ('dap', 'DAP'), ('fob', 'FOB'), ('fca', 'FCA')], string="Incoterms")
    type = fields.Selection([('air', 'AIR'), ('lcl', 'LCL')], string="Type")
    country_id = fields.Many2one('res.country', "Country")
    country_id = fields.Char("Country")
    date = fields.Date("Date")
    freight = fields.Integer("Freight")
    handling_charge = fields.Integer("Handling Charge")
    customs_fee = fields.Integer("Customs fee")
    local_logistic_fee = fields.Integer("Local logistic fee")
    etc = fields.Char("ETC")
    total = fields.Integer("Total")
    vat_Of_surcharge = fields.Integer("VAT Of surcharge")
    total_included_vat = fields.Integer("Total included VAT")
    currency_id = fields.Many2one('res.currency', "CURRENCY")
    weight = fields.Integer("Weight")
    cbm_cont = fields.Char("CBM/Cont")
    forwarder = fields.Selection([('cj', 'CJ'), ('dhl', 'DHL'), ('skyways', 'SKYWAYS'), ('yusen', 'YUSEN')], string="Forwarder")
    cd_no = fields.Char("CD NO")
    cd_date = fields.Date("CD DATE")
    cd_fwd = fields.Selection([('kido', 'KIDO'), ('dsk', 'DSK')], string="CD FWD")
