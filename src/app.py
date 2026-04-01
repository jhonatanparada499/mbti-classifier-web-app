from flask import Flask, request, redirect, url_for, render_template
from predict import predict_mbti

app = Flask(__name__)


@app.route("/", methods=["GET", "POST"])
def main_page():
    if request.method == "POST":
        text = request.form.get("user_text")
        return redirect(url_for("prediction", text=text))
    return render_template("index.html")


@app.route("/prediction")
def prediction():
    text = request.args.get("text")
    predictions = {
        "label": predict_mbti(text),
    }

    return render_template("predict.html", predictions=predictions)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
