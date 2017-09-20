from bottle import route, run

@route('/hello')
def hello():
    return "Hello World"

def main():
    run(host='localhost',
        port=8080,
        debug=True)

if __name__ == '__main__':
    main()
