from bottle import Bottle, request, response, run
import json


def str_unicode(str):
    n = len(str)
    s = [ord(str[i]) for i in range(n)]
    unicode = ['\\u%x' % x for x in s]
    return ''.join(unicode)

app = Bottle()

@app.post('/unicode')
@app.get('/unicode/<text>')
def unicode(text=None):
    text_unicode = ''
    if text is None:
        if request.content_type.find('application/json') == -1:
            return 'error: no input text'
        else:
            text_json = request.json
            if text_json is None:
                return 'error: no input text'
            else:
                text = text_json['content']
                text_unicode = str_unicode(text)
    else:
        text_unicode = str_unicode(text)
    return text_unicode

if __name__ == '__main__':
    run(app, host='0.0.0.0', port=8080, debug=True)
