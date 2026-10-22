from flask import Flask, render_template

app= Flask(__name__)


@app.route('/')
def home():
    return "Hola muy buenas tardes"

@app.route('/elegante')
def elegante():
    return "<h1>Elegante</h1>"

@app.route('/primera')
def template_primera():
    return render_template('ara.html')

if __name__ == '__main__':
    app.run()