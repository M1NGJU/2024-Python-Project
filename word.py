from flask import Flask, render_template, request, redirect, url_for
import random

app = Flask(__name__)

# 기본 페이지 라우팅
@app.route('/')
def index():
    # 키워드 리스트 정의
    keywords = [
        "운동", "독서", "코딩", "1일 1커밋", "혼자 공부하는 파이썬", "요리", "SQL 공부", 
        "자격증 공부", "스프링 공부", "안드로이드 공부", "Node 공부하기", "WSM공부", "데이터 분석 공부"
    ]
    
    # 리스트에서 랜덤으로 5개의 키워드를 선택
    random_keywords = random.sample(keywords, 5)
    
    # 랜덤 키워드 리스트를 HTML 템플릿으로 전달
    return render_template('keyword.html', random_keywords=random_keywords)

# 새로운 키워드 입력 페이지 라우팅
@app.route('/keywordtext', methods=['GET', 'POST'])
def keywordtext():
    if request.method == 'POST':
        keyword = request.form['keyword']
        # 입력된 키워드에 대한 처리 로직을 추가
        # 예: 데이터베이스에 저장하거나, 다른 작업을 수행
        print("사용자가 입력한 키워드:", keyword)
        # 여기서 추가적으로 작업을 할 수 있습니다.
        # 예를 들어, 새로운 키워드를 저장하거나 처리 후 리디렉션

    return render_template('keywordtext.html')

if __name__ == '__main__':
    app.run(debug=True)