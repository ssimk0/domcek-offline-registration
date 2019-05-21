from domcek.shared.abstract_service import Service


class OfflineService(Service):
    # Show table of all registered users
    def get_participants(self, filter_string):
        return self.participant_store.filter(filter_string)

    # Wrong payment table
    def wrong_payments(self, filter_string):
        return self.wrong_payments_store.filter(filter_string)

    def get_participant_by_id(self, user_id):
        return self.participant_store.find_by(user_id, 'user_id')

    def save(self):
        return self.participant_store.store()
