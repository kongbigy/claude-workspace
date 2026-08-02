# progress.md — 작업 기록 (append-only)

> 이 파일은 지우거나 수정하지 말고 **아래에 계속 추가만** 하세요.
> 형식: `## 날짜` → 한 일 요약

---

## 2026-08-02

- 작업 환경 초기 구축
  - `tasks/` 폴더 + `todo.md`, `progress.md` 생성
  - `SECURITY.md` 비상 매뉴얼 작성 (키 노출 대응 절차)
  - `README.md` 작성 (폴더 구조 정리)

- `C:\Users\sati3\sample` 폴더 정리
  - `images/`(jpg 5개), `docs/`(txt·docx·pptx 5개), `misc/`(emm 2개 + Word 잠금 파일 1개)로 분류 이동
  - `영어학습 일일 목표.docx`가 Word에서 열려있어 첫 시도 실패 → 파일 닫은 후 재시도로 이동 완료
  - 목적지 충돌 없어 `.bak` 백업은 발생하지 않음

- `D:\workspace\fils` 폴더 정리
  - `이미지/`(jpg 5개), `문서/`(txt·docx·pptx 5개), `기타/`(emm 2개)로 분류 이동
  - 목적지 충돌 없어 `.bak` 백업은 발생하지 않음

- 강남구 날씨·미세먼지 조회 스크립트 작성 (`scripts/weather_gangnam.py`)
  - API 키 없이 네이버 날씨 검색 페이지를 스크래핑하는 방식 채택 (에어코리아 공식 API는 키 필요해서 제외)
  - `requests`, `beautifulsoup4` 설치 후 구현, 실행할 때마다 `weather.txt`를 덮어쓰는 1회성 스크립트로 제작 (tony 요청에 따라 스케줄러 등록은 하지 않음)
  - 수동 실행으로 정상 동작 확인 (기온/날씨상태/미세먼지/초미세먼지 저장됨)

- 이력서 기반 포트폴리오 웹페이지 제작 (`portfolio.html`)
  - resume.pdf 정보로 경력 2개(테크노바, 리브랜드) + 대표 프로젝트 1개(AI 콘텐츠 자동화)를 경력 섹션 3개로 구성 (tony 확인 후 결정 — 없는 경력 지어내지 않음)
  - 반응형/다크모드 대응, 외부 CDN 없이 순수 HTML/CSS로 제작

- claude-workspace를 GitHub private 레포로 업로드 (https://github.com/kongbigy/claude-workspace)
  - 민감 파일 스캔 결과 실제 키/시크릿 파일 없음 확인 후 `.gitignore` 작성 (.env, *.key 등 패턴 + weather.txt 결과물 제외)
  - README.md를 실제 폴더 구조(docs/, scripts/, portfolio.html 등)에 맞게 갱신
  - resume.pdf/portfolio.html(개인정보 포함)은 tony 확인 후 포함, weather.txt는 제외
  - git user.name/email 미설정 상태였음 — CLAUDE.md 코드 "git config는 직접 건드리지 않음" 규칙에 따라 tony가 직접 설정
  - `gh repo create --private --source=. --push` 로 생성 + 첫 커밋 "Initial setup" 푸시 완료
