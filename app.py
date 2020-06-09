
from flask import Flask, render_template, request
import eliza
app = Flask(__name__)


@app.route("/")
def home():    
    return render_template("home.html") 
@app.route("/get")
def get_bot_response():    
    userText = request.args.get('msg')
    eliz = eliza.Eliza()
    eliz.load('doctor.txt')
    response = eliz.respond(userText)
    return str(response) 
if __name__ == "__main__":    
    app.run()