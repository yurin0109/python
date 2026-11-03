# Among the Stars · 수많은 별 속에서 나를 발견하는 시간

생년월일과 태어난 시간으로 **사주팔자를 직접 계산**하고, 오행 캐릭터(사슴·여우·곰·호랑이·수달)와 함께
나의 성향과 올해의 흐름을 읽어보는 사주 웹 서비스입니다.

> 운명을 맞히기보다, 나를 이해하는 시간으로.

## 기간 / 인원
2026.10.15 ~ 2026.11.06 / 1인

## 기술 스택
| 구분 | 사용 기술 |
|---|---|
| 백엔드 | Java 17, Spring Boot 3, Spring Data JPA |
| 프론트 | HTML, CSS, JavaScript (단일 페이지 + 탭 구성) |
| DB | MySQL 8 (배포), H2 (로컬 실행) |
| 테스트 | JUnit 5 |
| 디자인 | Figma |

## 주요 기능 (탭 7개)
1. **홈** — 서비스 소개, 이용 순서
2. **사주 입력** — 이름, 생년월일(양력), 태어난 시간(모름 가능), 출생 지역, 성별
3. **내 결과** — 사주팔자 8글자, 오행 비율, 일간으로 읽는 핵심 성향, 강한/보완할 기운, 오늘의 성찰 질문 + 답 적기
4. **올해 운세** — 올해 간지와 나의 일간 관계(비겁·식상·재성·관성·인성)로 읽는 흐름 + 풀이 근거 표시 + 올해 성찰 질문
5. **직장운** — 십성 분포(월지 2배)로 읽는 일하는 스타일 5종, 잘 맞는 분야, 올해 일의 흐름
6. **결혼운** — 배우자 별(여성 관성 · 남성 재성)의 양과 배우자 자리(일지)로 읽는 관계 스타일
7. **내 사주 목록** — 저장한 사주 조회 / 수정 / 삭제, **성찰 일기** (적은 답을 월별로 모아보기 · 프로필별 필터 · 수정 · 삭제)

### 성찰 질문 · 성찰 일기
- 질문 데이터 **610개** (`src/main/resources/reflection-questions.txt`)
  - 일간 오행별 60개 × 5 + 공통 60개 → 내 결과 탭
  - 올해와의 관계별 30개 × 5 → 올해 운세 탭
  - 직장 50개 → 직장운 탭 / 관계 50개 → 결혼운 탭
- 날짜와 프로필로 그날의 질문이 정해지고, "다른 질문"으로 다음 질문을 볼 수 있음
- 저장할 때 질문 문구는 화면에서 보낸 값이 아니라 서버의 질문 데이터에서 다시 찾아 저장 (조작 방지)
- 프로필을 삭제하면 그 프로필로 쓴 성찰 일기도 함께 삭제

## 구조
```
[브라우저 index.html]
   │  fetch (X-Client-Id 헤더)
   ▼
[ProfileController]        [ReflectionController]   REST API
   ▼                          ▼
[ProfileService] ◄──────── [ReflectionService] ──► [QuestionBank]  성찰 질문 315개
   │  └─► [SajuCalculator]  팔자 · 오행 · 올해 관계 계산 (직접 구현)
   │  └─► [Interpretation]  조건별 풀이 문구 템플릿
   ▼                          ▼
[ProfileRepository]        [ReflectionRepository] ──► DB (profile, reflection 테이블)
```
- **AI API 없이** 계산과 풀이 로직을 전부 직접 구현했습니다.
- 사주 결과는 DB에 저장하지 않고 조회할 때마다 계산합니다. (계산이 가볍고, 로직을 고치면 바로 반영)
- 로그인 대신 브라우저마다 발급한 고유 ID(UUID)로 "내 사주"를 구분합니다.

## API
| 메서드 | 주소 | 설명 |
|---|---|---|
| GET | /api/profiles | 내 사주 목록 |
| GET | /api/profiles/{id} | 사주 결과 |
| POST | /api/profiles | 사주 등록 |
| PUT | /api/profiles/{id} | 정보 수정 (사주 재계산) |
| DELETE | /api/profiles/{id} | 삭제 (성찰 일기 함께 삭제) |
| GET | /api/reflections/question?profileId=&type=core\|year\|career\|marriage&offset= | 오늘의 성찰 질문 |
| GET | /api/reflections?profileId= | 성찰 일기 목록 |
| POST | /api/reflections | 성찰 일기 저장 |
| PUT | /api/reflections/{id} | 답 수정 |
| DELETE | /api/reflections/{id} | 성찰 일기 삭제 |

## 핵심 구현: 사주 계산 정책
| 항목 | 정책 |
|---|---|
| 년주 | 1월 1일이 아니라 **입춘(2/4)** 기준으로 해가 바뀜 |
| 월주 | 음력 1일이 아니라 **12절기** 기준으로 달이 바뀜 |
| 일주 | 2000-01-01(무오일) 기준 날짜 차이 ÷ 60의 나머지 |
| 시주 | 한국 표준시 30분 보정 → 자시 23:30~01:29. 23:30 이후 출생은 다음 날 일주 |
| 오행 비율 | 태어난 계절을 나타내는 **월지에 가중치 3**, 나머지 글자 1. 합계 100% 보정 |

**알려진 한계:** 절기 날짜를 평균값으로 고정해서, 절기 당일 전후 출생자는 ±1일 오차가 날 수 있습니다.
(개선 계획: 한국천문연구원 절기 API 연동) 음력 입력은 아직 지원하지 않습니다.

## 테스트
`SajuCalculatorTest` — 경계 케이스 18개
- 입춘 전날/당일 년주, 1월 1일 출생
- 절기(한로) 전날/당일 월주, 1월 초 소한 전후
- 기준일 이전 날짜 일주, 60일 주기
- 13:29 / 13:30 시지 경계, 23:29 / 23:30 일주 변경
- 시간 모름 처리, 오행 비율 합계 100, 월지 가중치

`TenGodsTest` — 십성 6개
- 7글자 십성 분포(월지 2배), 시간 모름 처리, 배우자 별 · 배우자 자리, 점수 구간, 문구 누락 검사

`QuestionBankTest` — 성찰 질문 7개
- 600개 이상, 추가해도 기존 질문 코드 유지, 분류 11개 모두 존재, 문구 중복 없음
- 코드로 찾기, 같은 날 같은 질문 · 다른 질문 보기 동작, 탭별로 맞는 분류에서만 나오는지

## 실행 방법
```bash
# 로컬 실행 (H2 DB, 설치 필요 없음)
mvn spring-boot:run        # 또는 IntelliJ에서 SajuApplication 실행
# → http://localhost:8080

# 테스트
mvn test
```

## 배포 (Render + Neon PostgreSQL)
1. [Neon](https://neon.tech)에서 무료 PostgreSQL DB를 만들고 접속 정보를 확인
2. Render › Web Service › Environment 에 환경변수 등록 (코드에 비밀번호를 쓰지 않음)
```
SPRING_PROFILES_ACTIVE=prod
DB_URL=jdbc:postgresql://호스트/neondb?sslmode=require
DB_USERNAME=...
DB_PASSWORD=...
```
3. 저장하면 자동으로 다시 배포되고, 이후 서버가 재시작돼도 데이터가 유지됨
4. Health Check Path: `/api/version`

MySQL을 쓸 때는 `SPRING_PROFILES_ACTIVE=mysql` 과 `jdbc:mysql://...` 주소를 사용합니다. 테이블 구조는 `db/schema.sql` 참고.

## 캐릭터 이미지
오행 캐릭터 5종은 `src/main/resources/static/img/` 의 SVG 파일입니다.
`wood.svg`(사슴) · `fire.svg`(여우) · `earth.svg`(곰) · `metal.svg`(호랑이) · `water.svg`(수달)
같은 이름의 파일로 바꾸면 화면 전체에 반영됩니다.

## 트러블슈팅
<!-- 개발하면서 막혔던 문제 → 원인 → 해결을 여기에 기록하세요 -->
- 
