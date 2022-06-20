from app import app


@app.route('/')
def hippie():
    return f'Oh shit, here we go again'


@app.route('/some/<string:some_shit>/')
def some_shit(some_):
    return f'what the shit named {some_} you pulling in the URL?'


@app.route('/about')
def about_route():
    return f'I dont mind what would you do there'


@app.route('/login')
def login_route():
    return
