from flask import redirect, Blueprint, render_template, request
from domcek.sync.service import SyncService

blueprint = Blueprint('sync', __name__)
service = SyncService()

# This is endpoint which should download whole database users registered to event
@blueprint.route("/download", methods=['POST'])
def download():
    token = request.form.get('token', None)
    try:
        service.download(token)
        return redirect('/registration')
    except ConnectionError as e:
        return render_template('error.html', message=e.strerror)


# This is endpoint responsible for uploading changes to server after registration end
@blueprint.route("/upload", methods=['POST', 'GET'])
def upload():
    if request.method == 'POST':
        token = request.form.get('token', None)
        print(token)
        service.upload(token)
        return redirect('/success')
    else:
        return render_template('upload.html')


@blueprint.route("/success")
def success():
    return render_template('success.html')