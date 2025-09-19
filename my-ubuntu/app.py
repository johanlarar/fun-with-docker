from flask import Flask
import os

app = Flask(__name__)


@app.route("/")
def hello():
    return {"message": "Hello, world!"}


@app.route("/health")
def health():
    return "OK"


@app.route("/passwd")
def read_passwd():
    try:
        if os.path.exists("/etc/passwd"):
            with open("/etc/passwd", "r") as f:
                content = f.read()
            return {
                "status": "success",
                "content": content,
                "lines": content.strip().split("\n"),
            }
        else:
            return {"status": "error", "message": "/etc/passwd not found"}, 404
    except PermissionError:
        return {"status": "error", "message": "Permission denied"}, 403
    except Exception as e:
        return {"status": "error", "message": str(e)}, 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=False)
