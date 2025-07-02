from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

# Load model and known fruit names
model = pickle.load(open("model.pkl", "rb"))
known_fruits = pickle.load(open("known_fruits.pkl", "rb"))

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    if request.method == "POST":
        fruit_name = request.form["fruit"].strip().lower()
        if fruit_name not in known_fruits:
            prediction = "None"
        else:
            prediction = model.predict([fruit_name])[0]
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True, port=5001)
