from flask import Flask
app = Flask(__name__)

@app.get("/")
def home():
    return "Deploy automático OK: GitHub Actions -> ECR -> ECS Fargate"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
