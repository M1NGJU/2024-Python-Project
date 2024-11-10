from flask import Flask, render_template

app = Flask(__name__)  # Flask 인스턴스 이름을 'app'으로 변경

@app.route('/')
def keywordtext():
    return render_template('keywordtext.html')

if __name__ == "__main__":
    app.run(debug=True)  # 'app'으로 변경하여 실행
