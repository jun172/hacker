from flask import Flask,render_template
from SQL import SQL
from XSS import XSS
from CSRF import CSRF 
from DT import DT
from ONE import ONE
from FU import FU
from DARK import DARK





app = Flask(__name__)
app.secret_key = 

@app.route('/')
def home():
    return render_template("home.html")

# Blueprint登録
app.register_blueprint(SQL, url_prefix='/SQL')
app.register_blueprint(XSS, url_prefix='/XSS')
app.register_blueprint(CSRF , url_prefix='/CSRF')
app.register_blueprint(DT,url_prefix='/DT')
app.register_blueprint(ONE, url_prefix='/ONE')
app.register_blueprint(FU, url_prefix='/FU')
app.register_blueprint(DARK,url_prefix='/DARK')







if __name__ == '__main__':
   app.run(
    host="0.0.0.0",
    port=8080,
    debug=True,
)