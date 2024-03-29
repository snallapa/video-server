from flask import Flask
from flask import render_template, send_from_directory
import os
app = Flask(__name__)

content_dir = os.environ.get("CONTENT")
if not content_dir:
    raise Exception("Content dir environment variable not found")
if not content_dir.endswith("/"):
    content_dir = content_dir + "/"


@app.route('/video/<path:path>')
def video(path):
    return send_from_directory(content_dir, path)

@app.route('/text/<path:path>')
def text(path):
    return send_from_directory(content_dir, path)

@app.route("/", defaults={'path': ""})
@app.route('/<path:path>')
def home(path):
    resultPath = content_dir + path
    if os.path.isdir(resultPath):
        files = os.listdir(content_dir + path)
        if not path.endswith("/"):
            path =  path + "/"
        if not path.startswith("/"):
            path = "/" + path
        return render_template("files.html", files=files, length=len(files), path=path)
    else:
        subtitles = path[0 : path.rfind(".")] + ".vtt"
        print(subtitles)
        if (os.path.exists(content_dir + subtitles)):
            return render_template('video.html', src="/video/" + path, subtitle_src="/text/" + subtitles)
        return render_template('video.html', src="/video/" + path)

if __name__ == '__main__':
    app.run()
