import os, json, time
from flask import Flask, request
import ml_utils
import sqlite3 as sql
import run_backend



app = Flask(__name__)

def get_predictions():

    videos = []

    with sql.connect(run_backend.db_name) as conn:
        c = conn.cursor()
        for line in c.execute("SELECT * FROM videos"):
            #(title, video_id, score, upload_time)
            line_json  = {"title" : line[0], "video_id": line[1], "score": line[2], "upload_time": line[3]}
            videos.append(line_json)

    predictions = []

    for video in videos:
        predictions.append((video['video_id'], video['title'], float(video['score'])))

    predictions = sorted(predictions, key = lambda x: x[2], reverse = True)[:30]

    predictions_formatted = []

    for e in predictions:
        predictions_formatted.append("<tr><th><a href=\"{link}\">{title}</a></th><th>{score}</th></tr>".format(title = e[1], link = e[0], score = e[2]))

    return '\n'.join(predictions_formatted)



@app.route('/')
def main_page():
    preds = get_predictions()

    return """<head><h1>Youtube Videos Recommender</h1></head>
    <body>
    <table>
            {}
    </table>
    </body>""".format(preds)



@app.route('/predict')
def predict_api():
    yt_video_id = request.args.get("yt_video_id", default = '')

    ydl = ytdl.YoutubeDL({"ignoreerros": True})
    video_json_data = ydl.extract_info("https://youtube.com/watch?v={}".format(yt_video_id), download = False)

    if video_json_data is None:
        return "Not Found"

    p = ml_utils.compute_predictions(video_json_data)
    output = {"title": video_json_data['title'], "score": p}

    return json.dumps(output)



if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0')
