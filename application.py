from flask import Flask, render_template, request

application = Flask(__name__)

@application.route('/')
def main():
    return render_template('index.html')