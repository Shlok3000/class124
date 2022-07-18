from flask import Flask
#creating a flask object
app = Flask(__name__)

# use route() decorator to tell Flask what URL should trigger our function.
@app.route("/")
def HelloWorld():
    return("This is my home page")

@app.route("/intro")
def intro():
    return("Hey people")


if (__name__ == "__main__"):
     app.run(debug = True, port = 8000)