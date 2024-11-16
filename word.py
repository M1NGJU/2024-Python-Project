from flask import Flask, render_template, request, redirect, url_for, session
import random
from datetime import datetime
import calendar

# Flask 애플리케이션 생성
app = Flask(__name__)

# 세션에 사용할 암호화 키 설정
app.secret_key = 'your_secret_key_here'

# 키워드 리스트 정의 (사용자에게 보여질 활동 선택 키워드)
keywords = [
    "운동", "독서", "코딩", "1일 1커밋", "혼자 공부하는 파이썬", "요리", "SQL 공부", 
    "자격증 공부", "스프링 공부", "안드로이드 공부", "Node 공부하기", "WSM공부", "데이터 분석 공부"
]

# 오늘 날짜 기준으로 고유한 랜덤 숫자를 세션에 저장하고 반환하는 함수
def get_daily_random_number():
    current_date = datetime.now().strftime('%Y-%m-%d')  # 오늘 날짜 문자열
    session_key = f'random_number_{current_date}'  # 날짜에 기반한 세션 키 생성
    
    # 세션에 오늘 날짜의 랜덤 숫자가 없으면 생성
    if session_key not in session:
        session[session_key] = random.randint(1, 10)  # 1~10 사이 랜덤 숫자 생성
    
    return session[session_key]  # 저장된 랜덤 숫자 반환

# 홈 페이지 라우트 (기본 경로)
@app.route('/')
def home():
    # `home.html` 템플릿 렌더링
    return render_template("home.html")

# 키워드 선택 페이지 라우트
@app.route('/keyword', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        # 사용자가 선택한 키워드를 세션에 저장
        selected_keyword = request.form.get('selected_keyword')
        if selected_keyword:
            session['selected_keyword'] = selected_keyword
            return redirect(url_for('setting'))  # 설정 페이지로 이동
    
    # 랜덤하게 5개의 키워드 선택
    random_keywords = random.sample(keywords, 5)
    return render_template('keyword.html', random_keywords=random_keywords)  # 키워드 페이지 렌더링

# 직접 입력한 키워드를 처리하는 라우트
@app.route('/keywordtext', methods=['GET', 'POST'])
def keywordtext():
    if request.method == 'POST':
        # 사용자가 입력한 키워드를 세션에 저장
        keyword = request.form['keyword']
        session['selected_keyword'] = keyword
        return redirect(url_for('setting'))  # 설정 페이지로 이동
    return render_template('keywordtext.html')  # 키워드 입력 페이지 렌더링

# 설정 페이지 라우트
@app.route('/setting', methods=['GET', 'POST'])
def setting():
    if request.method == 'POST':
        return redirect(url_for('calendar_view'))  # 달력 페이지로 이동
    
    # 동기부여 문구 리스트
    text = [
        "작은 변화가 큰 차이를 만든다.", "오늘의 노력이 내일의 성과를 만든다.",
        "포기하지 마라. 지금 포기하면 어제의 실패를 되풀이할 뿐이다.",
        "매일 조금씩, 꾸준히 나아가는 것이 중요하다.", "시작이 반이다. 이제 나머지 반을 채워보자.",
        "오늘도 최선을 다하자. 내일의 내가 고마워할 것이다."
    ]
    random_text = random.sample(text, 1)  # 랜덤한 문구 하나 선택
    selected_keyword = session.get('selected_keyword', '선택된 키워드가 없습니다')  # 세션에서 키워드 가져오기
    
    now = datetime.now()
    last_day = calendar.monthrange(now.year, now.month)[1]  # 현재 달의 마지막 날짜 계산
    date_range = f"{now.month}월 1일 ~ {now.month}월 {last_day}일"  # 현재 달의 날짜 범위 문자열 생성
    
    return render_template('setting.html', 
                           random_text=random_text, 
                           selected_keyword=selected_keyword,
                           date_range=date_range)  # 설정 페이지 렌더링

# 달력 페이지 라우트
@app.route('/calendar', methods=['GET', 'POST'])
def calendar_view():
    current_date = datetime.now()  # 현재 날짜 및 시간 가져오기
    
    # 월 이름을 한글로 매핑
    month_kr = {
        1: '1월', 2: '2월', 3: '3월', 4: '4월',
        5: '5월', 6: '6월', 7: '7월', 8: '8월',
        9: '9월', 10: '10월', 11: '11월', 12: '12월'
    }
    
    # 현재 날짜를 다양한 형식으로 저장
    formatted_date = {
        'full': current_date.strftime('%Y.%m.%d'),
        'year': current_date.year,
        'month': current_date.month,
        'day': current_date.day,
        'month_str': month_kr[current_date.month]
    }
    
    # 세션에서 선택된 키워드 가져오기
    selected_keyword = session.get('selected_keyword', None)
    
    # 오늘의 랜덤 숫자 가져오기
    daily_random_number = get_daily_random_number()
    
    if request.method == 'POST':
        return render_template('calendar.html', 
                               date=formatted_date, 
                               selected_keyword=selected_keyword)
    
    return render_template('index.html', 
                           date=formatted_date, 
                           selected_keyword=selected_keyword,
                           random_number=daily_random_number)  # 랜덤 숫자와 함께 메인 페이지 렌더링

# Flask 애플리케이션 실행
if __name__ == '__main__':
    app.run(debug=True)
