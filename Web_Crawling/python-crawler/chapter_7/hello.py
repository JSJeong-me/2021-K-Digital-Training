from flask import Flask
app = Flask(__name__)  # 플라스크 인스턴스를 생성합니다.

# /에 접근할 때 호출됩니다.
@app.route("/")
def hello():  # 아무 이름으로 함수를 생성합니다.
    return "Hello World!"