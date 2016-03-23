from flask import Flask
#from app import app

@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Peyton'}  # fake user
    return '''
<html>
  <head>
    <title>Home Page</title>
  </head>
  <body>
    <h1>Hello, ''' + user['nickname'] + '''</h1>
  </body>
</html>
'''
if __name__ == "__main__":
    app.run(host='45.55.180.111')
