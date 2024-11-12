from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# 키워드를 저장할 리스트 초기화
keywords = []

@app.route('/', methods=['GET', 'POST'])
def keywordtext():
    if request.method == 'POST':
        # 폼에서 입력된 키워드 가져오기
        keyword = request.form.get('keyword')
        if keyword:
            # 키워드를 리스트에 추가
            keywords.append(keyword)
            print("현재 키워드 리스트:", keywords)  # 터미널에 리스트 출력 (디버깅용)
        return redirect(url_for('keywordtext'))  # 페이지 새로고침
    return render_template('keywordtext.html')

if __name__ == "__main__":
    app.run(debug=True)