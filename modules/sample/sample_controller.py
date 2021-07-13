from flask import Blueprint, request, jsonify
from flask.wrappers import Response
from modules.sample.services.pg_sample_service import PgSampleService
import logging

sample_api = Blueprint('sample_api', __name__)

sample_service = PgSampleService()

@sample_api.route('/sample', methods=['GET','POST'])
def get_or_create_sample_data():
    if request.method == 'GET':
        return jsonify(sample_service.get_sample_data())
    if request.method == 'POST':
        try:
            print(request.json)
            sample_service.add_sample_data(request.json)
            return Response({}, 200)
        except Exception as e:
            logging.error("Exception while adding new sample data %s" % e)
            return Response({}, 500)
