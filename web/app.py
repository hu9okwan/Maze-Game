from flask import Flask, request, render_template
import os
from models.score_manager import ScoreManager
from models.scores import Score


app = Flask(__name__)
score_manager = ScoreManager()
score_manager.from_json("scores.json")


@app.route('/api/list')
def list_all_scores():
    return render_template("list.html", high_scores=score_manager.scores)

if __name__ == "__main__":
    print("Server running")
    app.run(debug=True)