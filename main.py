from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/api/", methods=["GET","POST"])
def qa():
    if request.method == "POST":
        data = {"result":"thank uh im machine learning"}
        return jsonify(data)
        
 data = {"result":"thank uh im machine learning"}
 return jsonify(data)


app.run(debug=True)