# Data Yanolja 2026 Talk Proposal

데이터야놀자 2026 발표 제안과 발표 준비를 위한 공개 문서 저장소입니다.

## 발표 제목

`A/B 테스트만으로는 부족합니다: CRM 정책 최적화로 이해하는 베이지안 최적화`

## 한 줄 소개

베이지안 최적화는 딥러닝 하이퍼파라미터를 찾을 때만 쓰는 도구가 아니라, 상황에 따라 달라지는 비싼 의사결정 실험을 적은 시행착오로 최적화하는 방법입니다.

## Documents

- [실제 HTML 슬라이드 deck](./slides/index.html)
- [CFP 제출 문안](./docs/cfp/data-yanolja-2026/cfp-submission.md)
- [슬라이드 구성안](./docs/cfp/data-yanolja-2026/slide-outline.md)
- [슬라이드 본문 초안](./docs/cfp/data-yanolja-2026/slides-content.md)
- [슬라이드 화면용 압축 문구](./docs/cfp/data-yanolja-2026/slides-screen-copy.md)
- [프론트엔드 슬라이드 빌드 브리프](./docs/cfp/data-yanolja-2026/frontend-slides-brief.md)
- [데모 설계 문서](./docs/cfp/data-yanolja-2026/demo-spec.md)

## 발표에서 다루는 내용

- 왜 A/B 테스트만으로는 정책 탐색 문제를 충분히 설명하기 어려운가
- Gaussian Process와 Bayesian Optimization을 실무 문제 중심으로 쉽게 이해하는 방법
- CRM 정책 최적화 예제로 보는 `할인율 × 발송 시점` 최적화
- Constraint와 연령/성별별 정책 최적화 확장
- Ax / BoTorch로 실제 구현을 시작하는 관점

## Public / Private

- `docs/cfp/` 아래 문서는 공개 제출용 문서입니다.
- `slides/` 아래에는 실제 발표 deck 구현이 있습니다.
- 내부 브레인스토밍, 설계 메모, 실행 계획은 `docs/superpowers/`에서 별도로 관리하며 Git 추적 대상에서 제외합니다.
