# Frontend Slides Brief

이 문서는 `frontend-slides`로 실제 HTML 슬라이드를 만들 때 사용할 빌드 브리프입니다. 목표는 `slides-screen-copy.md`의 텍스트를 바로 시각화 가능한 화면 구조로 옮길 수 있게 하는 것입니다.

## Overall Direction

- 분위기: `editorial + technical`
- 인상: `실무 문제를 구조화하는 사람`, `차갑기보다 선명한 설명`, `연구 발표보다 제품/실험 이야기`
- 키워드:
  - signal
  - search
  - contour
  - experiment
  - decision surface

## Visual Tone

- 다크 테마에 과도하게 기대지 않는다
- 밝은 바탕 위에 진한 잉크색 텍스트를 사용한다
- 포인트 컬러는 탐색과 실험의 느낌이 나도록 `cobalt`, `vermilion`, `teal` 조합을 사용한다
- purple 계열은 피한다
- 배경은 완전 평면 흰색 대신 아주 옅은 warm gray 또는 paper tone을 사용한다

## Suggested Design Tokens

### Color

- Background: `#F5F2EA`
- Surface: `#FFFDF8`
- Ink: `#14213D`
- Muted Ink: `#4E5B73`
- Accent 1: `#2B59C3`
- Accent 2: `#E4572E`
- Accent 3: `#1B998B`
- Border: `#D9D3C7`

### Typography

- Headline:
  - `Space Grotesk` 또는 `Sora`
- Body:
  - `SUIT` 또는 `Pretendard`
- Formula / code:
  - `JetBrains Mono`

### Motion

- 페이지 전환은 짧고 선명하게
- 요소는 staggered reveal
- heatmap, contour, node-link는 fade + slight translate
- 과한 bounce나 glassmorphism 계열은 피한다

## Layout System

### Allowed Layouts

- `hero`
  - 타이틀 또는 마무리용
- `split`
  - 좌우 비교
- `formula-bullets`
  - 수식 1개 + 짧은 해석
- `heatmap`
  - contour / heatmap 중심
- `cards`
  - 짧은 예시 나열
- `node-link`
  - task 관계 설명

### Spacing Rule

- 슬라이드마다 시각적 주인공은 하나만 둔다
- 텍스트는 3단 이상 쌓지 않는다
- bullet은 4개를 넘기지 않는다
- 수식은 한 슬라이드에 1개만 둔다

## Slide-by-Slide Build Spec

### Slide 1

- Layout: `hero`
- Visual:
  - 좌측 상단 작은 eyebrow: `Data Yanolja 2026`
  - 중앙 대형 headline
  - 하단 얇은 흐름선: `A/B Test -> Policy Search -> Bayesian Optimization`
- Background:
  - 종이 질감 느낌의 밝은 배경
  - 얇은 contour line 패턴

### Slide 2

- Layout: `split`
- Left panel:
  - A/B 비교 카드
- Right panel:
  - `할인율 × 발송 시점` 격자
- Visual note:
  - 왼쪽은 깔끔한 binary comparison
  - 오른쪽은 조합 폭발이 직관적으로 보이게

### Slide 3

- Layout: `formula-bullets`
- Formula block:
  - `x* = argmax_x f(x)`
- Right bullets:
  - `x = 정책 파라미터`
  - `f(x) = 기대 성과`
  - `평가가 비싸고 noisy하다`
- Visual note:
  - 뒤에 아주 옅은 2D contour

### Slide 4

- Layout: `formula-bullets`
- Left:
  - GP 수식
- Right:
  - prior / posterior mini plot 2개
- Visual note:
  - uncertainty band는 cobalt
  - observed points는 vermilion

### Slide 5

- Layout: `split`
- Left:
  - noisy scatter
- Right:
  - 짧은 설명 bullets
- Visual note:
  - 동일 x에서 여러 점이 튀는 모양이 눈에 띄어야 함

### Slide 6

- Layout: `formula-bullets`
- Main visual:
  - mean / uncertainty / acquisition을 세로 스택
- Visual note:
  - 세 곡선 색을 분리
  - 마지막 행에서 next point를 크게 표시

### Slide 7

- Layout: `split`
- Left:
  - 파라미터 카드 2개
- Right:
  - objective 계산 흐름
- Visual note:
  - `incremental profit`
  - `coupon cost`
  - `send cost`
  - 세 요소가 분리되어 보여야 함

### Slide 8

- Layout: `heatmap`
- Main visual:
  - objective heatmap
  - BO trajectory overlay
- Caption:
  - `적은 실험으로 유망한 구간을 좁혀간다`
- Visual note:
  - trajectory는 vermilion
  - optimum mark는 cobalt ring

### Slide 9

- Layout: `heatmap`
- Main visual:
  - objective heatmap + feasible mask
- Secondary:
  - `g(x) = 7일 무접속 이탈률`
- Visual note:
  - infeasible 영역을 반투명 hatch로 처리
  - constrained optimum과 unconstrained optimum을 둘 다 찍는다

### Slide 10

- Layout: `split`
- Left:
  - `20대 여성` contour
- Right:
  - `30대 남성` contour
- Visual note:
  - 연령/성별 그룹의 optimal point가 분명히 다르게 보여야 함
  - 상단에 `Age and gender change the optimum`

### Slide 11

- Layout: `node-link`
- Main visual:
  - 연령/성별 그룹 노드 4개
  - 공유되는 relation
- Side copy:
  - `20대 여성`
  - `20대 남성`
  - `30대 여성`
  - `30대 남성`
- Visual note:
  - 그룹별 최적화를 하되 완전히 따로 보지 않는 느낌
  - node-link는 과도한 네트워크 그래프 느낌보다 단순한 관계도

### Slide 12

- Layout: `cards`
- Cards:
  - `할인율 × 쿠폰 유효기간`
  - `할인율 × 발송 비율`
  - `할인율 × uplift threshold`
  - `가격 정책 / 예산 배분 / 운영 파라미터`
- Visual note:
  - 2x2 카드 그리드

### Slide 13

- Layout: `cards`
- Left card:
  - `Ax = 빠른 시작`
- Right card:
  - `BoTorch = 유연한 확장`
- Bottom strip:
  - `코드보다 먼저 필요한 것은 문제 정의`

### Slide 14

- Layout: `hero`
- Headline:
  - `베이지안 최적화는 하이퍼파라미터 튜닝만의 도구가 아닙니다`
- Subheadline:
  - `A/B 테스트 이후의 정책 탐색 문제를 다루는 방법으로 볼 수 있습니다`
- Closing line:
  - `핵심은 objective, constraint, group context를 구조화하는 능력입니다`
- Visual note:
  - 마지막 슬라이드는 매우 정적이고 강하게

## Reusable Components

- eyebrow label
- formula card
- contour / heatmap panel
- metric chip
- policy parameter card
- comparison card
- closing statement block

## Avoid

- 보라색 메인 테마
- 과한 3D 효과
- 과도한 글래스모피즘
- 작은 글씨로 많은 내용을 우겨넣는 구성
- 복잡한 코드 스크린샷

## Build Priority

1. Slide 1, 2, 7, 8, 9, 10, 14부터 만든다
2. 수식 슬라이드는 동일한 component system으로 재사용한다
3. 실제 데모 결과가 나오면 Slide 8~10의 placeholder visual만 교체한다
