from domcek.shared.abstract_service import Service


class OfflineService(Service):
    # Show table of all registered users
    def get_participants(self, filter_string):
        return self.participant_store.filter(filter_string)

    # Wrong payment table
    def wrong_payments(self, ):
        pass

    def get_participant_by_id(self, participant_id):
        pass