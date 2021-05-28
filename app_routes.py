from flask import jsonify, abort, request, make_response

from app import app, db
from .analytics import ContentBasedModel
from .models import RestnUserRating

base_url = '/api/v0.1'
model_content = ContentBasedModel()

# Recommend restaurants based on provided restaurant IDs
@app.route(base_url + '/recommend', methods=['GET', 'POST'])
def recommend():

    # pre-checks
    if not request.args.get('ids'):
        abort(404, description='Unable to locate ids')
    if (request.method == 'POST') & (not request.args.get('user_id')):
        abort(404, description='Unable to locate user_id')

    # recommendation
    reject_ids, scores, input_details = model_content.score(request.args.get('ids').split(','))

    # post-processing
    if request.args.get('prices'):
        prices = ['$'*int(p) for p in request.args.get('prices').split(',')]
        scores = [data for data in scores if data['price'] in prices]
    if request.args.get('zip_codes'):
        scores = [data for data in scores if data['zip_code'] in request.args.get('zip_codes').split(',')]

    # output
    scores = scores[:int(request.args.get('top', '5'))]
    output = {'total': len(scores), 'recommendations': scores, 'rejected_ids': reject_ids, 'input_ids': input_details}

    if request.method == 'GET':
        return jsonify(output)

    if request.method == 'POST':
        for input in output['input_ids']:
            rating = RestnUserRating(restn_id = input['id'], user_id = request.args.get('user_id'))
            db.session.add(rating)
        db.session.commit()
        return jsonify(output)

# A welcome message to test our server
@app.route('/')
def index():
    return jsonify({'message': 'Welcome to our server !!'})

# # Standard reply for errors
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': error.description}), 404)