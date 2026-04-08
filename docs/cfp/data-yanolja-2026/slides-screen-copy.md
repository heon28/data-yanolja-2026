# Slides Screen Copy

이 문서는 실제 슬라이드 화면에 올릴 텍스트를 압축한 버전입니다. `frontend-slides`로 옮길 때 바로 사용할 수 있도록, 각 슬라이드별 레이아웃과 온스크린 문구만 남겼습니다.

## Deck Rules

- 오프닝과 마무리는 1~2줄 중심으로 짧게 간다
- 개념/예제 슬라이드는 2~4개의 짧은 포인트만 둔다
- 한 슬라이드에 문장 2개 이상이 길게 들어가면 발표자 설명으로 내린다
- 수식은 1개만 두고, 그 아래 해석 포인트만 붙인다

## Slide 1

- Layout: hero
- Headline: `A/B 테스트만으로는 부족합니다`
- Subheadline: `CRM 정책 최적화로 이해하는 베이지안 최적화`
- Footer: `이병헌`

## Slide 2

- Layout: split
- Headline: `A/B 테스트는 강력합니다`
- On-screen copy:
  - `좋은 비교 도구입니다`
  - `하지만 정책 공간을 직접 최적화해주지는 않습니다`
  - `파라미터가 2개만 되어도 탐색 비용은 급격히 커집니다`

## Slide 3

- Layout: formula + bullets
- Headline: `우리가 실제로 푸는 문제`
- Formula:

```text
x* = argmax_x f(x)
```

- On-screen copy:
  - `x = 정책 파라미터 조합`
  - `f(x) = 기대 성과`
  - `문제는 f(x)를 모른다는 점입니다`

## Slide 4

- Layout: formula + visual
- Headline: `함수도 확률적으로 볼 수 있습니다`
- Formula:

```text
f ~ GP(m, k)
```

- On-screen copy:
  - `함수에 대한 분포`
  - `mean + uncertainty`

## Slide 5

- Layout: formula + short text
- Headline: `현실의 실험 결과는 noisy합니다`
- Formula:

```text
y = f(x) + ε
```

- On-screen copy:
  - `같은 정책도 결과는 흔들립니다`
  - `그래서 uncertainty를 같이 봐야 합니다`

## Slide 6

- Layout: formula + three points
- Headline: `다음 점은 어떻게 고를까`
- Formula:

```text
x_next = argmax_x [μ(x) + βσ(x)]
```

- On-screen copy:
  - `잘 될 것 같은 곳`
  - `아직 잘 모르는 곳`
  - `이 둘의 균형이 핵심입니다`

## Slide 7

- Layout: two-column
- Headline: `오늘의 예제는 CRM 정책 최적화입니다`
- On-screen copy:
  - `정책 파라미터 = 할인율 × 발송 시점`
  - `objective = incremental profit - coupon cost - send cost`
  - `완전 합성 시뮬레이터로 설명합니다`

## Slide 8

- Layout: heatmap
- Headline: `제약이 없으면 이렇게 찾을 수 있습니다`
- On-screen copy:
  - `적은 실험으로 유망한 구간을 좁혀갑니다`
  - `random / dense grid보다 더 효율적입니다`

## Slide 9

- Layout: formula + contour
- Headline: `하지만 실무에는 제약이 있습니다`
- Formula:

```text
max_x f(x)  subject to  g(x) <= 0
```

- On-screen copy:
  - `g(x) = 7일 무접속 이탈률`
  - `수익이 높아도 운영 불가능한 정책은 탈락합니다`
  - `우리가 찾는 것은 feasible optimum입니다`

## Slide 10

- Layout: two-panel comparison
- Headline: `연령과 성별이 달라지면 답도 달라집니다`
- Formula:

```text
x*(c) = argmax_x f(x, c)
```

- On-screen copy:
  - `모든 고객에게 같은 정책이 최적일 필요는 없습니다`
  - `20대 여성, 20대 남성, 30대 여성, 30대 남성`
  - `연령/성별마다 최적점이 달라질 수 있습니다`

## Slide 11

- Layout: node-link
- Headline: `그룹을 완전히 따로 볼 필요는 없습니다`
- Formula:

```text
x*(c) = argmax_x f(x, c)
```

- On-screen copy:
  - `연령/성별 그룹 간 유사성은 활용할 수 있습니다`
  - `데이터가 적어도 더 안정적으로 탐색할 수 있습니다`
  - `핵심은 그룹별 최적화 + 정보 공유입니다`

## Slide 12

- Layout: card grid
- Headline: `같은 프레임은 다른 정책 문제에도 연결됩니다`
- On-screen copy:
  - `할인율 × 쿠폰 유효기간`
  - `할인율 × 발송 비율`
  - `할인율 × uplift threshold`
  - `핵심은 파라미터화와 제약 정의입니다`

## Slide 13

- Layout: comparison cards
- Headline: `구현은 생각보다 가깝습니다`
- On-screen copy:
  - `Ax = 빠른 시작`
  - `BoTorch = 유연한 확장`
  - `진짜 어려운 건 코드보다 문제 정의입니다`

## Slide 14

- Layout: closing hero
- Headline: `베이지안 최적화는 하이퍼파라미터 튜닝만의 도구가 아닙니다`
- Subheadline: `A/B 테스트 이후의 정책 탐색 문제를 다루는 방법으로 볼 수 있습니다`
- Closing line: `핵심은 objective, constraint, group context를 구조화하는 능력입니다`

## Repeated Line

`예측만 잘한다고 의사결정이 자동으로 좋아지지는 않습니다.`
