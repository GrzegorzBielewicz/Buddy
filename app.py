from flask import Flask, render_template, url_for, request

app = Flask(__name__)


@app.route('/')
def index():
    return 'This is index'


@app.route('/introduction', methods=['GET', 'POST'])
def introduction():
    if request.method == 'GET':
        return render_template('introduction.html')
    else:
        nickname = 'Buddy'
        if 'nickname' in request.form:
            nickname = request.form['nickname']

        age = 25
        if 'age' in request.form:
            age = request.form['age']

        return render_template('/presentation.html', nickname=nickname, age=age)


if __name__ == '__main__':
    app.run()