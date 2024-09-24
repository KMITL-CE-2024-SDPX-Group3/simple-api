from flask import Flask, jsonify, abort

app = Flask(__name__)


@app.route('/')
def index():
    return "Index!"


@app.route('/hello/<name>', methods=['GET'])
def hello(name):
    return "Hello, " + str(name)


@app.route("/getcode", methods=['GET'])
def get_code():
    return f"FEATURE => This function: {get_code.__name__}"


@app.route("/plus/<number_1>/<number_2>", methods=['GET'])
def plus(number_1: str, number_2: str):
    try:
        number_1: float = float(number_1)
        number_2: float = float(number_2)
        result = number_1 + number_2

        if result.is_integer():
            result = int(result)

        return jsonify({
            "result": result
        })
    except ValueError:
        # If the conversion fails, return a 400 Bad Request
        abort(400, description="Invalid input: both parameters must be numbers")
        return None  # This line is required for the type hint when abort is called


@app.errorhandler(400)
def bad_request(error):
    return jsonify({'error': error.description}), 400


if __name__ == '__main__':
    # app.run()
    app.run(debug=True)
