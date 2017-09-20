from bottle import Bottle, run, template

app = Bottle()

@app.route('/hello')
def hello():
    return "Hello world"

@app.route('/')
@app.route('/hello/<name>')
def greet(name='Stranger'):
    return template('Hello {{name}}, how are you?', name=name)

if __name__ == '__main__':
    run(app, host='127.0.0.1', port=8080, debug=True)
