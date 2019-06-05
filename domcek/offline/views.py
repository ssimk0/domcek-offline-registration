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

# Participants list
@blueprint.route("/participants", methods=['GET'])
def participants():
    filter = request.args.get('q', None)
    participants = service.get_participants(filter, True)
    paid = service.get_paid_amount()
    on_reg = service.get_on_reg_amount()
    return render_template('all-participants.html', participants=participants, filter=filter, on_reg=on_reg, paid=paid)

# Participant detail and register action
@blueprint.route('/participant/<int:user_id>', methods=['GET', 'POST'])
def detail(user_id):
    if request.method == 'POST':
        amount = request.form.get('amount', None)
        participant = service.get_participant_by_id(user_id)
        participant['on_registration'] = int(amount) if amount is not None and amount != '' else 0
        participant['was_on_event'] = 1
        participant['subscribed'] = 1
        participant['transport_out'] = '11:00' if request.form.get('bus', participant.get('transport_out', None)) == 'on' else ''
        service.save()
        return redirect('/registration')
    else:
        participant = service.get_participant_by_id(user_id)
        return render_template('register-participant.html', participant=participant)

# Payment detail
@blueprint.route('/wrong-payments/<int:payment_id>', methods=['GET', 'POST'])
def detailWrongPayments(payment_id):
    if request.method == 'POST':
        email = request.form.get('email', None)
        participant = service.get_participant_by_email(email)
        payment = service.get_wrong_payments_by_payment_id(payment_id)
        if participant:
            payment['user_id'] = participant['user_id']
            service.save_payments()
        return redirect('/registration/wrong-payments')
    else:
        payment = service.get_wrong_payments_by_payment_id(payment_id)
        return render_template('payment-detail.html', payment=payment)


# This is endpoint responsible for show table with wrong payments
@blueprint.route("/wrong-payments", methods=['GET'])
def wrong_payments():
    filter = request.args.get('q', None)
    payments = service.wrong_payments(filter)
    return render_template('wrong-payments.html', payments=payments)
