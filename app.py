from  flask import Flask, render_template, request
from web_sum import top10_sent
from vedio_sum import summarize_video
import requests
from bs4 import BeautifulSoup
from flask import current_app
from pdf_docx import Summuraize
from werkzeug.utils import secure_filename



app= Flask(__name__)

def get_wiki_content(url):
            req_obj= requests.get(url)
            text= req_obj.text
            soup=BeautifulSoup(text)
            all_paras=soup.find_all("p")
            wiki_text=''
            for para in all_paras:
                wiki_text+=para.text
            return wiki_text

@app.route("/")

def index():
    return render_template("index.html")


@app.route("/text-sum", methods=["GET", "POST"])

def sum():
    if request.method=="POST":
        url = request.form.get("url")
        video_file = request.files.get('file')
        doc_file=request.files.get('file1')
        if url:
            summary=top10_sent(get_wiki_content(url))
            return render_template("out.html", data={"summary": summary})
        else:
            #video_file = request.files.get('file')
            if video_file:
                # Save the video file locally
                video_path = 'input_video.mp4'
                video_file.save(video_path)
                summary= top10_sent(summarize_video(video_path))
                return render_template("out.html", data={"summary": summary})
            if doc_file:
                
                filename = secure_filename(doc_file.filename)
                #filepath = os.path.join(current_app.config['doc_file'], filename)

                summary=Summuraize(filename)
                return render_template("out.html", data={"summary": summary})



if __name__ == "__main__":
    app.run(debug=True)