from flask import Flask

app = Flask(__name__)

# route 데코레이터를 이용해 처리 가능한 URL
# - 고정 URL : 쿼리 스트링만 변함
# - 동적 URL : 쿼리 스트링과 URL의 일부분이 변함

# 다음 3가지 URL에 대한 뷰 함수는 두 개만 선언하면 된다.

@app.route('/board')
def board():
    return ''


# Flask에서 사용자가 요청하는 URL에서 동적으로 바뀌는 부분은 URL에 포함된 변수로 취급할 수 있다.
# URL에 변수를 추가하려면 변할 수 있는 주소의 부분을 산형 괄호(<>)로 감싸면 된다.
# URL이 동적으로 바뀌는 뷰 함수를 선언할 때 함수의 인자명은 route 데코레이터에 전달한 URL에서 변동되는 부분의 이름이 같아야 한다.
@app.route('/board/<article_idx>')
def board_view(article_idx):
    return ''


# URL 변수의 타입
# - route  데코레이터에 기록한 URL 변수는 컨버터 이름이 지정되지 않은 경우 값의 타입은 string으로 취급된다.
# - URL 변수명 앞에 컨버터 이름을 지정하면 Flask가 컨버터를 찾아 URL 변숫값을 먼저 받아 후처리를 하고 나서 후처리된 값을 뷰 함수에 전달한다.
# - Flask에서 기본으로 제공하는 route 데코레이터에 사용 가능한 컨버터 : int, float, path, string
#  - float 컨버터 : 슬래시를 포함한 주소로 URL 변숫값의 내용을 후처리된 값으로 변환하고 뷰 함수의 인자로 전달


# URL 변수 기본값 할당
# - route 데코레이터에 URL 변수를 포함한 URL을 전달하면, 웹 브라우저는 URL 변수를 포함해 URL을 호출해야만 오류가 발생하지 않는다.
# - URL 변수는 기본값을 할당할 수 있다.
# - 기본값이 할당된 URL은 웹 브라우저가 URL을 호출하면 URL 변수에 기본값을 제공한다.

# 브라우저가 '/board/'를 호출한 경우 route 데코레이터는 1행에서 지정한 것 처럼 default 인자로 page 변수에 index를 넣도록 지시한다.
# 그 결과 웹 애플리케이션은 최종적으로 '/board/index' 형태의 주소를 호출하는 것과 같은 효과를 지니게 된다.
@app.route('/board', defaults={'page': 'index'})
@app.route('/board/<page>')
def board_default():
    return ''

