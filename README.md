# Simple Calculator API
🚀 간단한 사칙연산을 제공하는 API 입니다.  
➕➖✖️➗  FastAPI와 SQLite를 사용하여 구현했습니다.


## 폴더 구조
```
calculator_api/
├── main.py
├── app/
│   ├── __init__.py
│   ├── routers/
│   │   └── calculator.py
│   └── models.py
├── db.sqlite
└── requirements.txt
```

## 파일 별 설명
- main.py : FastAPI 애플리케이션을 실행하는 메인 파일입니다.
- app/__init__.py : app 패키지 초기화 파일입니다.
- app/routers/calculator.py : 계산기 API 라우터를 정의하는 파일입니다.
- app/models.py : Pydantic 모델을 정의하는 파일입니다.
- db.sqlite : 계산 결과를 저장하는 SQLite 데이터베이스 파일입니다. (선택적)
- requirements.txt : 필요한 패키지 목록을 정의하는 파일입니다.


## 배포 작업 순서 설명
1. `pip install -r requirements.txt` 명령어를 사용하여 필요한 패키지를 설치합니다.
2. `uvicorn main:app --reload` 명령어를 사용하여 FastAPI 애플리케이션을 실행합니다.
3. API 문서(Swagger UI)를 확인하여 API를 테스트합니다.  (http://127.0.0.1:8000/docs)