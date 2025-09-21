from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Ruta principal con HTML
@app.route("/")
def home():
    return render_template("index.html")

# Ruta API simple
@app.route("/api/hello")
def hello():
    return jsonify({"message": "Hola desde Flask en Azure 🚀"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8000, debug=True)