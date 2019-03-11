from flask import render_template, redirect, Blueprint
from domcek.registration import service

blueprint = Blueprint('registration', __name__)


# Show all users registered to event if local copy of database exist, other case show download button
@blueprint.route("/", methods=['GET'])
def home():
    return render_template('index.html')


# This is endpoint which should download whole database users registered to event
@blueprint.route("/download", methods=['POST'])
def download():
    service.download()
    return redirect('/')


# This is endpoint responsible for uploading changes to server after registration end
@blueprint.route("/upload", methods=['POST'])
def upload():
    service.upload()
    return redirect('/')
