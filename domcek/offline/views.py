from flask import render_template, Blueprint, request
from domcek.offline.service import OfflineService

blueprint = Blueprint('registration', __name__)
service = OfflineService()

# This is endpoint which should show all registered participants
@blueprint.route("/", methods=['GET'])
def index():
    filter = request.args.get('q', None)
    participants = service.get_participants(filter)
    return render_template('registration.html', participants=participants, filter=filter)


@blueprint.route('/participant/{}', methods=['GET'])
def detail(participant_id):
    participant = service.get_participant_by_id(participant_id)
    return render_template('participant_detail.html', participant=participant)

# This is endpoint responsible for show table with wrong payments
@blueprint.route("/wrong-payments", methods=['GET'])
def wrong_payments():
    payments = service.wrong_payments()
    return render_template('wrong_payments_table.html', payments=payments)
