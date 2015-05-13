from openerp.osv import osv,fields
from datetime import date

ARCHITECTURE = [
    ('32', '32 bits'),
    ('64', '64 bits')
]

class software(osv.osv):
    _name = 'software'
    _columns = {
        #'hadware_id': fields.many2one('hardware','Hardware'),
        #'einvoice_id': fields.one2many('account_einvoice ','account_id','Account einvoice'),
        'name_software': fields.char("name software", size=150, required=True),
        'architecture': fields.selection(ARCHITECTURE, 'architecture', required=True),
        'license': fields.char("license", size=150, required=False),
        'version': fields.char("version", size=150, required=True),
        'expiration': fields.date("expiration"),
        'used': fields.integer("used"),
        'free': fields.integer("free"),
        'installation': fields.char("installation", size=100, required=True),
        'description': fields.text("description", required=False),
        'cost_software': fields.float("cost software", required=True),
		}
software()
