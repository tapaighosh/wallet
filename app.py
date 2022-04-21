from pyexpat import model
from flask import Flask,jsonify
import json
from flask_cors import CORS
from pywallet import wallet
from flask_marshmallow import Marshmallow 
from flask_restx import Api, fields , Resource 


app=Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})


ma = Marshmallow(app)
api = Api()
api.init_app(app)

model=api.model('Model', {
  'Address': fields.String,
  "Private Key": fields.String,
  "Public Key": fields.String,
  "Seed": fields.String
})
@api.route('/home')
class home(Resource):
    @api.response(200, 'String')
    def get(self):
        return "Well Come"

@api.route('/api/createwallet')
class createWallet(Resource):
    @api.response(200, 'Success', model)
    def get(self):
        seed = wallet.generate_mnemonic()
        w = wallet.create_wallet(network="ETH", seed=seed, children=1)
        Account={'Private Key':w['private_key'],'Public Key':w['public_key'],'Seed':w['seed'],'Address':w['address']}
        return jsonify(Account)


if __name__=='__main__':
    app.run(debug=True)