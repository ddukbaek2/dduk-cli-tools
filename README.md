# dduk-cli-tools

## 설치
- 1. 3.7 이상의 파이썬 인터프리터를 설치합니다.
- 2. 개발 작업을 할 수 있는 IDE를 설치합니다.
- 3. 배포중인 ppdk 파일을 다운로드하여 시스템폴더 등에 넣습니다.
    - (명령줄인터페이스에서 ppdk를 입력하여 사용할 수 있어야 합니다)
- 4. 작업 디렉토리로 이동하여 `ppdk new -d "프로젝트루트경로" -p "파이썬실행파일경로"`를 입력합니다.
- 5. 프로젝트루트경로에 프로젝트 템플릿이 생성됩니다.
- 6. 작업을 시작합니다.


## 지원 기능
- 프로젝트 템플릿 생성 기능 (venv 기반)
- 바이너리 애플리케이션 빌드 기능 (pyinstaller 기반)
- 아카이브 빌드 기능 (setuptools 기반)
- 디버그 기능 (debugpy 기반)


## 프로젝트 구조
- /root/
- /root/build/
- /root/hints/
- /root/hooks/
- /root/libs/
- /root/logs/
- /root/res/
- /root/src/
- /root/tests/
- /root/workingspace/
- /root/ppdk-project.yaml


## 명령 목록
- `ppdk new` `-p "{프로젝트루트경로}"` `-i "{파이썬실행파일경로}"`
- `ppdk update` `-p "{프로젝트루트경로}"`
- `ppdk build` `-p "{프로젝트루트경로}"`
- `ppdk archive` `-p "{프로젝트루트경로}"`
- `ppdk run` `-p "{프로젝트루트경로}"` `-a {인수1} {인수2} {인수3} ...`
- `ppdk debug` `-p "{프로젝트루트경로}"` `-a {인수1} {인수2} {인수3} ...`
- `ppdk service` `-p "{프로젝트루트경로}"` `-a {인수1} {인수2} {인수3} ...`
- -p : --project : 생략시 현재 디렉토리를 루트 디렉토리로 인식하고 처리.
- -i : --interperter : 생략시 현재 등록된 파이썬3 중 가장 우선 검색되는 것을 자동 선택.
- -a : --argument : 생략시 인자 없음.


## ppdk-project.yaml
- 내부 심볼 목록 정의.
- 로그 파일 자동 작성 기능.
- 