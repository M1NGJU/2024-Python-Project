from flask import Flask, render_template, request, redirect, url_for, session
import random

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # session을 사용하기 위해 필요

@app.route('/keywordtext', methods=['GET', 'POST'])
def keywordtext():
    if request.method == 'POST':
        # 폼에서 입력된 키워드 가져오기
        keyword = request.form.get('keyword')
        if keyword:
            # 키워드를 세션에 저장
            session['selected_keyword'] = keyword
            # setting 페이지로 리다이렉트
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

# 다른 라우트들은 그대로 유지...

if __name__ == '__main__':
    app.run(debug=True)