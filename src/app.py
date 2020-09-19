import flask

app = flask.Flask(__name__)
app.config["DEBUG"] = True



HOST = "0.0.0.0"


@app.route('/', methods=['GET'])
def home():
    return flask.jsonify({
        "status": 200,
        "message": "All Systems are GO!"
    })

@app.route('/api/upload/image', methods=['POST'])
def accept_incoming_image():
    return flask.jsonify({
        "status":200
    })

@app.route('/api/image', methods=['GET'])
def serve_image():
    return flask.jsonify(
        {

        }
    )

if __name__ == "__main__":
    # critical to have this conditional for gunicorn to work!
    app.run()
