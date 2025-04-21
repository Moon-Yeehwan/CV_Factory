# CVFactory - 자소서 자동 생성기 ✨

AI 기반으로 자기소개서를 자동 생성하는 웹 애플리케이션입니다.  
Llama 기반 프롬프트를 활용하여 키워드 입력만으로 빠르게 자소서를 완성할 수 있습니다.

## 📌 주요 기능
- 키워드 기반 자소서 자동 생성
- Django 기반 백엔드 구조
- 사용자 커뮤니티 기능 포함 (자기소개서 공유, 피드백)
- 향후 GPT 연동 및 템플릿 자동화 기능 확장 예정

## 🛠 사용 기술

| 구분 | 기술 |
|------|------|
| Backend | Python, Django |
| Frontend | HTML/CSS (Bootstrap) |
| AI Model | Llama-3 기반 Prompt Engineering |
| DB | SQLite (개발용) |
| 배포 | GitHub (버전관리), 이후 Render/Supabase 예정 |

## 🖼 프로젝트 구조

CVFactory_project/
├── Main_Server-main/
│   ├── api/
│   ├── crawlers/
│   ├── cvfactory/
│   └── data_management/
├── bulletin_board-main/
│   └── board/
