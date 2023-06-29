import sys
sys.path.append('./UnitTest')
from Solution import spiralOrder
from flask import Flask, render_template, request, jsonify

app = Flask(__name__, template_folder='WebUI', static_folder='WebUI/static')
@app.route('/')
def index():
    return render_template('index.html', name="Spiral Matrix")

@app.route('/solve', methods=['POST'])
def solve():
    matrix_str = request.form['matrix'].strip().replace('; ', ',').replace(', ', ',').replace(' ', ',')
    #Insertion after 1st Bug
    if matrix_str == '':
        return (jsonify([]))
    matrix = [[int(num) for num in row.split(',')] for row in matrix_str.split('\n')]
    result = spiralOrder(matrix)
    return jsonify(result=result)

if __name__ == '__main__':
    app.run(debug=True)
