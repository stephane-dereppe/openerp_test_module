from osv import osv
from osv import fields

class test_class(osv.osv):
    _name = 'test.players'
    _columns = {
            'player_name': fields.char('Name', size = 30,required= True),
            'experience' : fields.integer('Experience')
            }
    _order = 'player_name' 
    _defaults = {  
        'player_name': 'default_name',
        'experience' : '0'
        }
    _sql_constraints = [     ('PLAYER_UK', 'unique (player_name)', 'The name of the player must be unique !'),      ]