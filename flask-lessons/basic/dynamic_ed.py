from flask import Flask, abort
import json

app = Flask(__name__)

# @app.route("/calculator/<int:num1>/add/<int:num2>")
# def add(num1, num2):
#     add_list = []
#     add_list.append({'operation': f'({num1} plus {num2})' })
#     add_list.append({'result': num1 + num2})
#     return json.dumps(add_list)

# if __name__ == '__main__':
#     app.run(debug=True)

# @app.route("/calculator/<int:num1>/subtract/<int:num2>")
# def subtract(num1, num2):
#     subtract_list = []
#     subtract_list.append({'operation': f'({num1} minus {num2})' })
#     subtract_list.append({'result': num1 - num2})
#     return json.dumps(subtract_list)
# here

@app.route("/calculator/<int:num1>/<foo>/<int:num2>")
def calculator(foo, num1, num2):
    add_list = {}
    if foo == "add":
        add_list['operation'] = (num1, 'plus', num2)
        add_list['result'] = (num1 + num2)
    elif foo == "subtract":
        add_list['operation'] = (num1, 'subtract', num2)
        add_list['result'] = (num1 - num2)
    elif foo == "divide":
        add_list['operation'] = (num1, 'divided by', num2)
        add_list['result'] = (num1 / num2)
    elif foo == "multiply":
        add_list['operation'] = (num1, 'multiplied by', num2)
        add_list['result'] = (num1 * num2)
    else:
        abort(404)
        
    return json.dumps(add_list)
    

 


if __name__ == '__main__':
    app.run(debug=True)