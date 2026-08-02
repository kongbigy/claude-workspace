# claude-workspace

tony의 Claude Code 작업 공간입니다. 폴더/파일 구조와 각 용도를 정리했습니다.

```
claude-workspace/
├── CLAUDE.md              # Claude Code 행동 지침서 (보안 규칙, 소통 방식, 작업 원칙)
├── README.md              # 이 파일 — 폴더 구조 설명
├── SECURITY.md            # 키 노출 시 비상 대응 매뉴얼
├── .gitignore              # 민감 파일·산출물 git 추적 제외 목록
├── vercel.json             # Vercel 배포 설정 (루트 URL → portfolio.html)
├── .vercelignore           # Vercel 배포 시 제외할 파일 (개인정보·내부 문서)
├── portfolio.html          # 포트폴리오 웹페이지 (브라우저에서 바로 열람, Vercel 배포 대상)
├── docs/
│   ├── resume.pdf          # 이력서
│   └── sales.csv           # 매출 데이터 (분석용 샘플)
├── scripts/
│   └── weather_gangnam.py  # 서울 강남구 날씨·미세먼지 조회 스크립트 (API 키 불필요)
└── tasks/
    ├── todo.md              # 오늘 할 일 체크리스트
    └── progress.md          # 작업 기록 (append-only, 지우지 않고 계속 추가)
```

> `.env`(환경변수)와 `weather.txt`(스크립트 실행 결과물)는 `.gitignore`에 의해 저장소에 포함되지 않습니다.

## 파일별 설명

| 파일/폴더 | 용도 |
|---|---|
| `CLAUDE.md` | Claude Code가 작업 시작할 때마다 자동으로 읽는 규칙 파일. 보안 규칙, 위험 작업 확인 절차, 소통 방식이 정의되어 있음 |
| `SECURITY.md` | API 키·SSH 키·비밀번호 노출이 의심될 때 따라야 할 대응 절차 (OpenRouter / Oracle / WordPress) |
| `.gitignore` | `.env`, `*.key`, `*.pem` 등 민감 파일과 `weather.txt` 같은 실행 결과물을 git 추적에서 제외 |
| `vercel.json` | Vercel 배포 시 루트 주소(`/`)를 `portfolio.html`로 연결하는 설정 |
| `.vercelignore` | Vercel 배포 시 `portfolio.html` 외 파일(이력서, 내부 문서, 스크립트 등)을 업로드에서 제외 — 민감정보 공개 방지 |
| `portfolio.html` | 이력서 기반 포트폴리오 웹페이지. 더블클릭하면 브라우저에서 바로 열림 |
| `docs/resume.pdf` | 이력서 원본 — 자기소개서 초안, 포트폴리오 제작 등에 활용 |
| `docs/sales.csv` | 매출 데이터 분석 샘플 (월별 트렌드, TOP5 상품 등 분석에 사용) |
| `scripts/weather_gangnam.py` | 네이버 날씨 페이지를 스크래핑해 강남구 날씨·미세먼지를 `weather.txt`에 저장 (API 키 불필요) |
| `tasks/todo.md` | 오늘/이번 작업의 체크리스트. 3단계 이상 작업은 여기 계획을 먼저 적고 승인받은 뒤 실행 |
| `tasks/progress.md` | 완료된 작업 기록. 새 내용을 아래에 추가만 하고 기존 내용은 지우지 않음 |
| `.env` | API 키, 비밀번호 등 민감정보 저장용 (커밋 금지 대상, 아직 미생성) |

## 작업 흐름

1. 작업 시작 → `tasks/todo.md` 확인
2. 큰 작업(3단계 이상) → todo.md에 계획 작성 → tony에게 확인받기 → 실행
3. 위험한 작업(삭제, DB 파괴, git reset --hard 등) → 실행 전 반드시 확인
4. 작업 종료 → `tasks/progress.md`에 기록 추가
5. 키 노출 의심 시 → `SECURITY.md` 순서대로 대응

## 포트폴리오 배포 (Vercel)

`portfolio.html`만 배포되도록 `.vercelignore`로 나머지 파일을 제외해뒀습니다. GitHub 레포와 연결해 Vercel에서 Import 하면 `vercel.json` 설정에 따라 루트 주소에서 바로 포트폴리오가 열립니다. (배포 자체는 tony가 Vercel 대시보드/CLI에서 직접 진행)

## 참고

- 오라클 SSH 키: `~/.ssh/oracle-server.key`
- 오라클 서버 별칭: `oracle-server` (SSH config 등록)
- 자세한 보안 규칙은 `CLAUDE.md` 참고
