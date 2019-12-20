from flask import Flask
app = Flask('app')

@app.route('/')
def hello_world():
  return 'Hello, World!'

app.run(host='0.0.0.0', port=8080)

if hello_world() == False:
  print('hello world!')
  else:
    def hello_world():
      return 'Hello, World!'