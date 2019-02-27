from flask import Flask, render_template, redirect, request
from services import SyncService

app = Flask(__name__)


# Show all users registered to event if local copy of database exist, other case show download button
@app.route("/", methods=['GET'])
def hello():
    return render_template('index.html')


# This is endpoint which should download whole database users registered to event
@app.route("/download", methods=['POST'])
def hello():
    SyncService.download()
    return redirect('/')


# This is endpoint responsible for uploading changes to server after registration end
@app.route("/upload", methods=['POST'])
def hello():
    SyncService.upload()
    return redirect('/')


@app.errorhandler(404)
def page_not_found(error):
    return render_template('page_not_found.html'), 404


@app.errorhandler(500)
def page_not_found(error):
    return render_template('error.html'), 500
