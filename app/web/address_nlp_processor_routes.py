import os
from copy import copy
from flask import jsonify
from flask import make_response
from flask import request
from flask import abort
from flask import Blueprint
import Utils

demandware_routes = Blueprint('demandware_routes', __name__)
config = Utils.load_json_from_file(os.path.join("..", "samples", "config.json"))
dw_replacement_and_standard_singleserial_order = Utils.load_json_from_file(os.path.join("..", "samples", "Demandware_order.json"))

@demandware_routes.errorhandler(404)
def not_found(error):
    return make_response(jsonify({"error": "Not found", "error_description":error}), 404)

@demandware_routes.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({"error_description": "Bad request", "error": "invalid_request", "error_trace":error}), 403)


@demandware_routes.route('/s/<string:country>/dw/shop/v17_3/order_search', methods=['POST'])
def demandware_order_search(country):
    authorization_header = request.headers.get('Authorization')
    content_type_header = request.headers.get('Content-Type')
    country_code = country.replace('Sites-', '').replace('-Site', '')
    response = copy(dw_replacement_and_standard_singleserial_order)
    query = []
    for must in request.json["query"]["filtered_query"]["query"]["bool_query"]["must"]:
        query.append((must["term_query"]["fields"][0], must["term_query"]["values"][0]))

    if query:
        newhits = []

        for hit in response["hits"]:
            for field, value in query:
                if hit["data"].get(field) != value:
                    break
            else:
                newhits.append(hit)

        response["hits"] = newhits
        response["total"] = len(newhits)
        response["count"] = len(newhits)

    if None in (country_code, authorization_header, content_type_header):
        abort(400)
    elif country_code in config['demandware']['dw_order_search_endpoint'][0]['sites'] or config['demandware']['dw_order_search_endpoint'][1]['sites']:
        return jsonify(response), 200
    else:
        abort(404)

@demandware_routes.route('/')
def index():
    return "Server is alive !"
