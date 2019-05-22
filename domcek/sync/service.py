from domcek.shared.abstract_service import Service
import json


class SyncService(Service):
    # Login user and call rest-sync endpoint to download users and save it to file as json
    def download(self, token):
        response = self.make_request('GET', '/registration/events/participants/all-details/sync?token=' + token)
        if response.status_code == 200:
            response = json.loads(response.content)

            self.participant_store.store(response['participants'])
            self.wrong_payments_store.store(response['wrong-payments'])
        else:
            raise ConnectionError('Problem with connection to api server')

    # Login user and call rest-sync endpoint to sync changes to server from your local copy of database
    # in case of error send email with changes to admin
    def upload(self, token):
        pass
