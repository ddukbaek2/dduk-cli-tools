# WEBNOTE

## 프로젝트 설치

### Blender 4.0.2 기본 경로에 설치.   
다운로드 경로 : `https://download.blender.org/release/Blender4.0/blender-4.0.2-windows-x64.msi`   
설치 경로 : `C:\Program Files\Blender Foundation\Blender 4.0`   

```
※ 블렌더 내장 파이썬 인터프리터의 버전은 3.10.13   
```

### Visual Studio Code 시스템 인스톨러 MSI버전 설치 및 실행 (포터블 및 관리자모드 필요없음).   
다운로드 경로 : `https://code.visualstudio.com/#alt-downloads`   
설치 경로 : `C:\Program Files\Microsoft VS Code\Code.exe`   

**기존에 남은 VSCode 확장 플러그인 제거 방법**   
`C:\Users\{계정명}\.vscode` 디렉토리 삭제.   
`C:\Users\{계정명}\AppData\Roaming\Code` 디렉토리 삭제.   

**VSCode 설치 시 추가 설정:**   
```
※ 설치시 최종적으로 마우스 우클릭시 나오는 컨텍스트 메뉴에 코드 항목 추가 체크.   
```

**VSCode 설치 시 추가 확장 설치:**   
```
Korean Language Pack for Visual Studio Code (Microsoft)   
Python (Microsoft)   
Pylance (Microsoft)   
Python Debugger (Microsoft)   
```

### VENV 설정
기본 설정된 파이썬 인터프리터 경로 : `C:\Program Files\Blender Foundation\Blender 4.0\4.0\python\bin\python.exe`   
프로젝트 루트에서 `venv-create` 입력시 알아서 생성됨.   


## 명령어
**OS 별 CLI 종류:**
```   
Windows OS : Command Prompt 사용. (.bat)   
Linux OS : Bash 사용. (.sh)   
Mac OS : Bash 사용. (.sh)   
```

**가상환경 명령어 (터미널로 루트에서 커맨드 입력하여 실행):**
```
venv-create.bat : 블렌더 기반 가상환경 생성 및 PIP 설치.   
venv-enable.bat : 생성된 가상환경 활성화.   
venv-pip.bat : 가상환경 내에서 PIP 설치.   
```

**실행 명령어 (터미널로 루트에서 커맨드 입력하여  실행):**
```
run-source.bat : 소스 기반 실행.
run-tests.bat : 단위 테스트 실행.
run-exe.bat : 빌드 된 바이너리 실행 파일 실행.
run-uitool.bat : QT5 UI TOOL (디자이너) 실행.
```

**프로젝트 설정 (VSCode로 파일을 열어서 내용 추가):**
```
project-prebuild.bat : 빌드에 필요한 사전 준비 처리.   
project-build.bat : 빌드.   
```


## 빌드 및 배포 (진행예정)
```
CI-Build : Jenkins   
CI-Deployment : 서버에 SSHServer 개발 혹은 OpenSSH 적용한 뒤 Jenkins로 SSH 접속 처리.
```