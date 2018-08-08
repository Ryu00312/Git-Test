from bottle import route, run, template, static_file

import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
STATIC_DIR = os.path.join(BASE_DIR, 'static')

@route('/sample')
def sample():
    return template('sample')
# Static Routes
@route('/static/css/<filename:path>')
def send_css(filename):
    return static_file(filename, root=f'{STATIC_DIR}/css')

@route('/static/js/<filename:path>')
def send_js(filename):
    return static_file(filename, root=f'{STATIC_DIR}/js')
    
run(host='localhost', port=8080,debug=True)