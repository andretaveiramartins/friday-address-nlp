import sys,os
sys.path.append(os.path.dirname(sys.modules[__name__].__file__))
from flask import Flask
import web.address_nlp_processor_routes as address_nlp_processor_routes

if __name__ == '__main__':
    mock_server = Flask(__name__)
    mock_server.register_blueprint(address_nlp_processor_routes.demandware_routes)
    mock_server.run(host='0.0.0.0', debug=True)
    