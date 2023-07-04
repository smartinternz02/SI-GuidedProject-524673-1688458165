from flask import Flask, render_template

app = Flask(__name__,static_folder='C:/Users/Aditya/Downloads/Smartinternz/templates/assets', template_folder='C:/Users/Aditya/Downloads/Smartinternz/templates')


@app.route('/')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()