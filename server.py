from flask import Flask, request
app = Flask(__name__)

def respond_missing_param(name: str):
    return "Missing valid parameter value for '%s' (number)" % name, 400

@app.route('/triangle')
def respond_to_triangle():
    a = request.args.get('a', None, int)
    b = request.args.get('b', None, int)
    c = request.args.get('c', None, int)

    if a is None:
        return respond_missing_param('a')
    elif b is None:
        return respond_missing_param('b')
    elif c is None:
        return respond_missing_param('c')

    uniques = []

    for x in [a, b, c]:
        if x not in uniques:
            uniques.append(x)
    
    if len(uniques) == 1:
        return 'EQUILATERAL'
    elif len(uniques) == 2:
        return 'ISOSCELES'
    else:
        return 'SCALENE'
