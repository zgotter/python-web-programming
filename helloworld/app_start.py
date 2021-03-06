# 프로그램 기동 스크립트
#   - __init__.py에서 작성한 프로그램을 Flask 프레임워크에 포함되어 있는 내장 웹 서버를 이용해 가동시키는 프로그램

# helloworld 모듈로부터 app 이름을 가져옴
# 이 때 참조되는 이름은 파이썬이 가진 이름을 찾는 순서에 따라 자동으로 가져옴
# 실행 중인 파이썬 프로그램의 모든 네임스페이스에서 이름을 찾지 못 할 경우 NameError 예외 발생
from helloworld import app

# app_start.py 이 실행되는 네임스페이스 이름이 "__main__" 인 경우 테스트 서버를 실행
#   - 파이썬 모듈의 네임스페이스 이름이 "__main__" 이 되는 경우
#   -> 콘솔 창에서 python 명령어를 사용해 파이썬 모듈 파일을 인자로 제공할 때 뿐
if __name__ == "__main__":
    app.run(host="0.0.0.0")