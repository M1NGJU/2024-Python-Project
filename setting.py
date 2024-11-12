from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')
def home():
    text = [
        "작은 변화가 큰 차이를 만든다.", "오늘의 노력이 내일의 성과를 만든다.", "포기하지 마라. 지금 포기하면 어제의 실패를 되풀이할 뿐이다.", "매일 조금씩, 꾸준히 나아가는 것이 중요하다.","시작이 반이다. 이제 나머지 반을 채워보자.",
        "오늘도 최선을 다하자. 내일의 내가 고마워할 것이다.", "오늘도 최선을 다하자. 내일의 내가 고마워할 것이다."
    ]

    random_text = random.sample(text,1)

    return render_template('setting.html', random_text = random_text)

if __name__ == "__main__":
    app.run(debug=True)