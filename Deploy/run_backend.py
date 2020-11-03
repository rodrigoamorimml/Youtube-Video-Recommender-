from ml_utils import *
import time
import sqlite3 as sql
import youtube_dlc as ytdl

queries = ["machine+learning", "kaggle", "deep+learning"]
db_name = 'videos.db'

def update_db():
    ydl = ytdl.YoutubeDL({"ignoreerrors": True})

    with sql.connect(db_name) as conn:
        for query in queries:
            for page in range(1,2 ):
                r = ydl.extract_info("ytsearchdate20:{}".format(query), download = False)
                video_list  = r['entries']

                for video in video_list:
                    if video is None:
                        continue

                    p = compute_predictions(video)
                    video_id = video['webpage_url']
                    watch_title = video['title'].replace("'", "")
                    data_front = {"title": watch_title, "score": float(p), "video_id": video_id}
                    data_front['update_time'] = time.time_ns()

                    print(video_id, json.dumps(data_front))
                    c = conn.cursor()
                    c.execute("INSERT INTO videos VALUES ('{title}', '{video_id}', {score}, {update_time})".format(**data_front))
                    conn.commit()

    return True
