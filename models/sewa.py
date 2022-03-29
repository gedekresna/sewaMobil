from odoo import api, fields, models


class Sewa(models.Model):
    _name = 'mobil.sewa'
    _description = 'Form sewa mobil'

    name = fields.Char(string='Name')

    mobil_ids = fields.One2many(comodel_name='mobil.sewadetail', inverse_name='sewa_id', string='Pilih Tipe mobil')

    pemesan = fields.Many2one(comodel_name='res.partner', string='pemesanan', domain=[('is_customernya','=',True)],store=True)

    tgl_sewa = fields.Date(string='Tanggal Sewa')

    lama_sewa = fields.Integer(string='Lama Sewa')

    sudah_kembali = fields.Boolean(string='Sudah Dikembalikan', default=False)

    total = fields.Float(compute='_compute_total', string='Total')

    @api.depends('mobil_ids')
    def _compute_total(self):
        for record in self:
            record.total = record.mobil_ids.harga * record.lama_sewa
       
  
class SewaDetail(models.Model):
    _name = 'mobil.sewadetail'
    _description = 'New Description'

    sewa_id = fields.Many2one(comodel_name='mobil.sewa', string='Sewa')
    # mobil_id = fields.Many2one(comodel_name='mobil.list', string='Sewa Mobil')
    mobil_tipe_id = fields.Many2one(comodel_name='mobil.list', string='Tipe Mobil')

    name = fields.Char(string='Name')

    harga = fields.Float(compute='_compute_harga', string='harga')
    
    @api.depends('mobil_tipe_id')
    def _compute_harga(self):
        for record in self:
            record.harga = record.mobil_tipe_id.harga

    

  
    
    
   


   
    
    