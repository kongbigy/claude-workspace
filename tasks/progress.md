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
