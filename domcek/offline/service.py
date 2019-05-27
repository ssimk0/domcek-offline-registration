from domcek.shared.abstract_service import Service


class OfflineService(Service):
    # Show table of all registered users
    def get_participants(self, filter_string, only_participants=False):
        return self.participant_store.filter(only_participants, filter_string)

    # Wrong payment table
    def wrong_payments(self, filter_string):
        return self.wrong_payments_store.filter(filter_string)

    # Get participant by id
    def get_participant_by_id(self, user_id):
        return self.participant_store.find_by(user_id, 'user_id')

    # Get participant by email
    def get_participant_by_email(self, email):
        return self.participant_store.find_by(email, 'email')

    # Save participants to file
    def save(self):
        return self.participant_store.store()

    # Save payments
    def save_payments(self):
        return self.wrong_payments_store.store()

    def get_wrong_payments_by_payment_id(self, payment_id):
        return self.wrong_payments_store.find_by(payment_id, 'id')
