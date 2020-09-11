from flask import Flask, session

from checker import check_logged_in

app = Flask(__name__)

app.secret_key = 'YouWillNeverGuessMySecretKey'

@app.route('/')
def hello() -> str:
    return 'Hello from the simple webapp.'

@app.route('/page1')
@check_logged_in # tự động pass tham số func??? không cần () ???
def page1() -> str:
    return 'This is page 1.'

@app.route('/page2')
@check_logged_in
def page2() -> str:
    return 'This is page 2.'

@app.route('/page3')
@check_logged_in
def page3() -> str:
    return 'This is page 3.'

@app.route('/login')
def do_login() -> str:
    session['logged_in'] = True
    return 'You are now logged in.'

# thực tế thì sẽ không xảy ra việc truy cập /logout trước /login, song với code này thì có thể, và xảy ra Key Error
@app.route('/logout')  
def do_logout() -> str:
    session.pop('logged_in')
    return 'You are now logged out.'


if __name__ == '__main__':
    app.run(debug=True)