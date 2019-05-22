from flask import render_template, Blueprint, request, redirect
from domcek.offline.service import OfflineService

blueprint = Blueprint('registration', __name__)
service = OfflineService()

# This is endpoint which should show all registered participants
@blueprint.route("/", methods=['GET', 'POST'])
def index():
    filter = request.args.get('q', None)
    participants = service.get_participants(filter)
    return render_template('registration.html', participants=participants, filter=filter)


@blueprint.route('/participant/<int:user_id>', methods=['GET', 'POST'])
def detail(user_id):
    if request.method == 'POST':
        amount = request.form.get('amount', None)
        participant = service.get_participant_by_id(user_id)
        participant['on_registration'] = int(amount)
        participant['was_on_event'] = 1
        service.save()
        return redirect('/registration')
    else:
        participant = service.get_participant_by_id(user_id)
        return render_template('register-participant.html', participant=participant)

# This is endpoint responsible for show table with wrong payments
@blueprint.route("/wrong-payments", methods=['GET'])
def wrong_payments():
    filter = request.args.get('q', None)
    payments = service.wrong_payments(filter)
    return render_template('wrong-payments.html', payments=payments)
