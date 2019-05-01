from flask import redirect, Blueprint, render_template
from domcek.sync.service import SyncService

blueprint = Blueprint('sync', __name__)
service = SyncService()

# This is endpoint which should download whole database users registered to event
@blueprint.route("/download", methods=['POST'])
def download():
    try:
        service.download()
        return redirect('/registration')
    except ConnectionError as e:
        return render_template('error.html', message=e.strerror)


# This is endpoint responsible for uploading changes to server after registration end
@blueprint.route("/upload", methods=['POST'])
def upload():
    service.upload()
    return redirect('/success')
