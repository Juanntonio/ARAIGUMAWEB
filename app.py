from flask import Flask, render_template

app= Flask(__name__)


@app.route('/')

def template_primera():
    return render_template('ara.html')




if __name__ == '__main__':
    app.run()