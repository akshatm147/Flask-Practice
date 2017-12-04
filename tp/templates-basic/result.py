from flask import *
app = Flask(__name__)

@app.route('/result')
def result():
    dict = {'phy':50, 'chem':60, 'maths':70}
    return render_template('result.html', result=dict)

if __name__ == '__main__':
    app.run(debug=True)
