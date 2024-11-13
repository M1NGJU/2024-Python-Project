from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # session을 사용하기 위해 필요

# 키워드 리스트 정의
keywords = [
    "운동", "독서", "코딩", "1일 1커밋", "혼자 공부하는 파이썬", "요리", "SQL 공부", 
    "자격증 공부", "스프링 공부", "안드로이드 공부", "Node 공부하기", "WSM공부", "데이터 분석 공부"
]

# 홈 페이지 라우트
@app.route('/')
def home():
    return render_template("home.html")

# 키워드 선택 페이지 라우트
@app.route('/keyword', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        selected_keyword = request.form.get('selected_keyword')
        if selected_keyword:
            session['selected_keyword'] = selected_keyword
            return redirect(url_for('setting'))
    
    # 리스트에서 랜덤으로 5개의 키워드를 선택
    random_keywords = random.sample(keywords, 5)
    return render_template('keyword.html', random_keywords=random_keywords)

@app.route('/keywordtext', methods=['GET', 'POST'])
def keywordtext():
    if request.method == 'POST':
        keyword = request.form['keyword']
        session['selected_keyword'] = keyword
        return redirect(url_for('setting'))
    return render_template('keywordtext.html')

@app.route('/setting')
def setting():
    text = [
        "작은 변화가 큰 차이를 만든다.", "오늘의 노력이 내일의 성과를 만든다.",
        "포기하지 마라. 지금 포기하면 어제의 실패를 되풀이할 뿐이다.",
        "매일 조금씩, 꾸준히 나아가는 것이 중요하다.", "시작이 반이다. 이제 나머지 반을 채워보자.",
        "오늘도 최선을 다하자. 내일의 내가 고마워할 것이다."
    ]
    random_text = random.sample(text, 1)
    selected_keyword = session.get('selected_keyword', '선택된 키워드가 없습니다')
    
    return render_template('setting.html', random_text=random_text, selected_keyword=selected_keyword)

if __name__ == '__main__':
    app.run(debug=True)
