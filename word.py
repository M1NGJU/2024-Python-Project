# word.py
from flask import Flask, render_template, request, redirect, url_for, session
import random
from datetime import datetime
import calendar

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'

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

@app.route('/setting', methods=['GET', 'POST'])
def setting():
    if request.method == 'POST':
        return redirect(url_for('calendar_view'))  # 새로운 라우트로 리다이렉트
        
    text = [
        "작은 변화가 큰 차이를 만든다.", "오늘의 노력이 내일의 성과를 만든다.",
        "포기하지 마라. 지금 포기하면 어제의 실패를 되풀이할 뿐이다.",
        "매일 조금씩, 꾸준히 나아가는 것이 중요하다.", "시작이 반이다. 이제 나머지 반을 채워보자.",
        "오늘도 최선을 다하자. 내일의 내가 고마워할 것이다."
    ]
    random_text = random.sample(text, 1)
    selected_keyword = session.get('selected_keyword', '선택된 키워드가 없습니다')
    
    # 현재 날짜 정보 가져오기
    now = datetime.now()
    last_day = calendar.monthrange(now.year, now.month)[1]
    date_range = f"{now.month}월 1일 ~ {now.month}월 {last_day}일"
    
    return render_template('setting.html', 
                         random_text=random_text, 
                         selected_keyword=selected_keyword,
                         date_range=date_range)

@app.route('/calendar')
def calendar_view():
    # 현재 날짜 가져오기
    current_date = datetime.now()
    
    # 월 이름을 한글로 변환하는 딕셔너리
    month_kr = {
        1: '1월', 2: '2월', 3: '3월', 4: '4월',
        5: '5월', 6: '6월', 7: '7월', 8: '8월',
        9: '9월', 10: '10월', 11: '11월', 12: '12월'
    }
    
    # 다양한 형식으로 날짜 표시
    formatted_date = {
        'full': current_date.strftime('%Y.%m.%d'),
        'year': current_date.year,
        'month': current_date.month,
        'day': current_date.day,
        'month_str': month_kr[current_date.month]
    }
    
    # word.py에서 설정된 선택된 키워드 가져오기
    selected_keyword = session.get('selected_keyword', None)
    
    return render_template('index.html', 
                         date=formatted_date, 
                         selected_keyword=selected_keyword)

if __name__ == '__main__':
    app.run(debug=True)