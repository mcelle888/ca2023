from flask import Flask, request

app = Flask(__name__)

message = 'Hello, world!'

@app.route('/')
def index():
    return f'<h3>{message}</h3>'

@app.route('/spam')
def spam():
    person = { 'name': 'John', 'age': 21 }
    return person

@app.route('/hello/<name>')
def hello(name):
    # name = (request.args.get('name'))
    # name = 'Jack'
    return { 'message': f'Hello, {name}!'}

@app.route('/add/<int:num1>/<int:num2>')
def add(num1, num2):
    # try:
        # num1 = request.args.get('num1', type = int)
        # num2 = request.args.get('num2', type = int)
        return { 'result': num1 + num2 }
    # except TypeError:
    #     return { 'error': 'num 1 and num 2 are required and must be integers'}, 400


# @app.errorhandler(TypeError)
# def type_error(error):
#     return { 'error' : str(error) }, 400


# error handling and has to be after all the routes, we use the decorator
@app.errorhandler(404)
def not_found(error):
    return { 'error' : str(error) }, 404

if __name__ == '__main__':
    app.run(debug=True)