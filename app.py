from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1 style='color:blue; text-align:center;'>Flask Docker App</h1><p>Running successfully!</p>"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
