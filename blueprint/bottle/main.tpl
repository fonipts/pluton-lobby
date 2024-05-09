from bottle import route, run, template

@route('/health')
def health_name(name):
    return template('<b>Hello</b>!', name=name)

@route('/health/<name>')
def health(name):
    return template('<b>Hello {{name}}</b>!', name=name)

run(host='localhost', port=8080)
