# todo.md — 오늘 할 일

> 이 파일은 체크리스트입니다. 작업 시작 시 확인하고, 끝나면 체크하세요.
> (CLAUDE.md 규칙 6번: 3단계 이상 작업은 여기 계획부터 적고 OK 받은 뒤 실행)

## 2026-08-02

- [x] `tasks/` 폴더 생성
- [x] `tasks/todo.md` 생성 (이 파일)
- [x] `tasks/progress.md` 생성
- [x] `SECURITY.md` 비상 매뉴얼 작성
- [x] `README.md` 폴더 구조 정리

---

## 2026-08-02 (추가) — 강남구 날씨·미세먼지 자동 저장 스크립트

**목표:** 매일 09:00에 서울 강남구 날씨 + 미세먼지 정보를 API 키 없이 가져와 `weather.txt`에 저장

**방식:** 네이버 날씨 검색 페이지(공개 웹페이지)를 스크래핑 — 미세먼지 공식 API(에어코리아)는 키가 필요해서 제외.
⚠️ 웹페이지 구조가 바뀌면 스크립트가 깨질 수 있음 (키 기반 API보다 안정성 낮음)

**변경 (tony 확인):** 스케줄러 등록은 하지 않음. 스크립트는 실행할 때마다 1회 동작.

**계획:**
1. [x] `requests`, `beautifulsoup4` 라이브러리 설치
2. [x] `scripts/weather_gangnam.py` 작성 — 네이버 날씨에서 기온/날씨상태/미세먼지/초미세먼지 추출
3. [x] 결과를 타임스탬프와 함께 `weather.txt`에 저장 (덮어쓰기 — 실행할 때마다 최신 정보로 갱신)
4. [x] 수동 실행 테스트 → `weather.txt` 내용 확인 (2026-08-02 18:38 실행, 정상 저장 확인)
5. ~~Windows 작업 스케줄러 등록~~ (제외)

---

## 2026-08-02 (추가) — GitHub 업로드 (private repo)

**목표:** claude-workspace 폴더를 GitHub private 레포로 업로드

**사전 확인 결과:**
- git 2.55.0, gh 2.97.0 설치됨, `kongbigy` 계정으로 로그인 완료
- 아직 git 저장소 아님 (`git init` 필요)
- 실제 `.env`/키/인증서 파일은 없음 (스캔 결과 0건)
- ⚠️ `docs/resume.pdf`, `portfolio.html`에 이름·이메일·전화번호 등 개인정보 포함 — private repo라도 포함 여부 확인 필요
- `weather.txt`는 스크립트 실행 시마다 덮어써지는 결과물 — 소스코드가 아니라 추적 제외 후보

**계획:**
1. [ ] `.gitignore` 작성 (.env, *.key, *.pem, id_rsa*, credentials, __pycache__, weather.txt 등)
2. [ ] `README.md`를 현재 실제 폴더 구조에 맞게 업데이트
3. [ ] `git init` → `git add` → `git commit -m "Initial setup"`
4. [ ] `gh repo create --private` 로 레포 생성 + push

**확인 필요 (tony님 답변 필요):** 레포 이름, resume.pdf/portfolio.html 포함 여부

---

## 새 작업 추가하는 법

```
- [ ] 할 일 내용
```

작업이 3단계 이상이면, 여기에 계획을 먼저 적고 나(tony)에게 보여준 뒤 OK를 받고 진행하세요.
