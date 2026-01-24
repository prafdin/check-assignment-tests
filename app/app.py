from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)


DEPLOY_DATE = datetime.now().strftime("%Y%m%d%H%M%S")


@app.route("/")
def index():
    return render_template(
        "index.html",
        deploydate=DEPLOY_DATE
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
