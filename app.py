from flask import Flask, jsonify, request
app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route('/super_simple')
def super_simple():
    return "<h1>This is Super Simple boo</h1>", 200


@app.route('/super_simple_json')
def json_super_simple():
    return jsonify(message="This is Super Simple boo",
                   name="swetha")


@app.route('/not_found')
def not_found():
    return jsonify(message="The resource is not found"), 404


@app.route('/parameters')
def parameters():
    name = request.args.get('name')
    age = int(request.args.get('age'))
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough")


@app.route('/ur_variables/<string:name>/<int:age>')
def ur_variables(name: str, age: int):
    if age < 18:
        return jsonify(message="Sorry " + name + ", you are not old enough"), 401
    else:
        return jsonify(message="Welcome " + name + ", you are old enough")


if __name__ == '__main__':
    app.run()
