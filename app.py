from flask import Flask, render_template, request, send_file
import yt_dlp
import os

app = Flask(__name__)

# Home route
@app.route("/", methods=["GET", "POST"])
def index():
    filename = None
    if request.method == "POST":
        url = request.form["url"]
        try:
            ydl_opts = {
                "outtmpl": "downloads/%(title)s.%(ext)s",
                "format": "best"
            }
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info = ydl.extract_info(url, download=True)
                filename = ydl.prepare_filename(info)
                filename = os.path.basename(filename)
        except Exception as e:
            return render_template("index.html", error=str(e))
    return render_template("index.html", filename=filename)

# Download route
@app.route("/download/<path:filename>")
def download_file(filename):
    filepath = os.path.join("downloads", filename)
    return send_file(filepath, as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)
