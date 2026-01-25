import os
import json
from flask import Flask, render_template, request, jsonify
from datetime import datetime

app = Flask(__name__)

DATA_DIR = '/data'
COMMENTS_FILE = os.path.join(DATA_DIR, 'comments.json')


def load_comments():
    if not os.path.exists(DATA_DIR):
        os.makedirs(DATA_DIR)
    if not os.path.exists(COMMENTS_FILE):
        return []
    with open(COMMENTS_FILE, 'r') as f:
        return json.load(f)


def save_comments(comments):
    with open(COMMENTS_FILE, 'w') as f:
        json.dump(comments, f, indent=4)


DEPLOY_REF = os.getenv("DEPLOY_REF", "NA")


@app.route("/")
def index():
    return render_template("index.html", deployref=DEPLOY_REF)


@app.route("/api/comments", methods=['GET'])
def get_comments():
    comments = load_comments()
    return jsonify(comments)


@app.route("/api/comments", methods=['POST'])
def add_comment():
    comments = load_comments()
    new_comment = {
        'content': request.json['content'],
        'timestamp': datetime.utcnow().isoformat()
    }
    comments.append(new_comment)
    save_comments(comments)
    return jsonify(new_comment), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
