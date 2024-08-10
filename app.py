from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from api.chat import get_response

app = Flask(__name__, static_folder='static')
CORS(app)  

@app.get("/")
def index_get():
    return render_template("index.html", active_page='beranda')

@app.get("/blog")
def blog_get():
    return render_template("blog.html", active_page='blog')

@app.get("/blog/blog-details-gangguan-kecemasan")
def blog_details_gangguan_kecemasan():
    return render_template("blog-details.html", active_page='blog')

@app.get("/blog/blog-details-highlight-kecemasan")
def blog_details_highlight_kecemasan():
    return render_template("blog-details-short.html", active_page='blog')

@app.get("/blog/blog-details-highlight-depresi")
def blog_details_highlight_depresi():
    return render_template("blog-details-short-2.html", active_page='blog')

@app.get("/blog/blog-details-highlight-stress")
def blog_details_highlight_stress():
    return render_template("blog-details-short-3.html", active_page='blog')

@app.get("/blog/blog-details-gangguan-depresi")
def blog_details_gangguan_depresi():
    return render_template("blog-details-2.html", active_page='blog')

@app.get("/blog/blog-details-gangguan-stress")
def blog_details_gangguan_stress():
    return render_template("blog-details-3.html", active_page='blog')

@app.get("/blog/blog-details-gangguan-stress-pasca-trauma")
def blog_details_gangguan_stress_pasca_trauma():
    return render_template("blog-details-4.html", active_page='blog')

@app.get("/blog/blog-details-skizofrenia")
def blog_details_skizofrenia():
    return render_template("blog-details-5.html", active_page='blog')

@app.get("/blog/blog-details-bipolar")
def blog_details_bipolar():
    return render_template("blog-details-6.html", active_page='blog')

@app.get("/chatbot")
def chatbot_get():
    return render_template("chatbot.html", active_page='chatbot')

@app.post("/predict")
def predict():
    text = request.get_json().get("message")
    if not text:
        return jsonify({"answer": "Please provide a message."}), 400
    
    response = get_response(text)
    return jsonify({"answer": response})

if __name__ == "__main__":
    app.run(debug=True)
