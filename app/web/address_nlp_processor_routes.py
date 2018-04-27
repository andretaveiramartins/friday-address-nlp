import os
import sys
sys.path.append('..')
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort
from flask import Blueprint
import address_nlp_providers.custom_address_nlp as nlp

address_nlp_routes = Blueprint('address_nlp_routes', __name__)

@address_nlp_routes.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "error_description":error}), 404)

@address_nlp_routes.errorhandler(500)
def bad_request(error):
    print (error) 
    return jsonify({"error_description": "Bad request", "error": "internal_server_error"}), 500


@address_nlp_routes.route('/address_nlp_process', methods=['GET','POST'])
def process_address_route():
    #authorization_header = request.headers.get('Authorization')
    #content_type_header = request.headers.get('Content-Type')
    response = None
    try:
        response = nlp.process_address(request.args.get('address'))
    except Exception as exc:
        print(exc)
        abort(500)
    return jsonify(response), 200
    

@address_nlp_routes.route('/')
def index():
    return "Server is alive !"
