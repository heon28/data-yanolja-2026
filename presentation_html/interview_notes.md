# Interview Notes

Created: 2026-06-01

이 문서는 새 HTML 발표 스크립트 작성 전에 확정한 인터뷰 기반 결정사항입니다.
아직 최종 스크립트가 아니며, 이후 발표 구조안과 HTML 슬라이드 제작의 기준 입력으로 사용합니다.

## 1. 발표의 핵심 변화

청중이 발표 후 실제 업무에서 바꿔야 하는 판단은 다음입니다.

> 단순한 직감에 의해 A/B 테스트 후보를 반복해서 고르지 않고,
> 통계에 기반해 더 효율적으로 다음 실험 후보를 탐색함으로써
> 전체 실험 기간과 비용을 줄인다.

주장 수위는 강하게 가져갑니다.

- 모든 정책 후보를 충분히 실험할 수 없는 환경을 기본 전제로 둡니다.
- 트래픽, 시간, 비용 때문에 한 번에 평가할 수 있는 후보 수가 제한되어 있다고 봅니다.
- 순차적으로 A/B 테스트 후보를 직감으로 반복 선택하면 최적 정책에 도달하기까지 오래 걸릴 수 있습니다.
- Bayesian Optimization은 "다음에 무엇을 실험할지"를 통계적으로 선택해 전체 최적화 기간과 비용을 줄이는 방법으로 제시합니다.

단, 기술적 방어선도 명시합니다.

- 모든 후보를 충분히 실험할 수 없고, 한 점의 평가 비용이 큰 상황에서 유효한 주장입니다.
- 가까운 정책들이 완전히 무관한 결과를 내지 않는다는 구조적 가정이 필요합니다.
- 관측 노이즈를 모델링할 수 있어야 합니다.
- BO가 한 실험점의 표본 수 문제를 없애는 것은 아닙니다. 좋은 실험 설계를 대체하지 않고, 다음 후보 선택을 더 정보적으로 만드는 방법입니다.

## 2. 발표의 상위 프레이밍

발표는 CRM 전용 발표가 아닙니다.

핵심은 다음입니다.

> Bayesian Optimization은 다양한 black-box optimization 문제에서
> 비용과 실험을 아끼기 위한 방법론입니다.

CRM은 이 구조를 시각화하기 위한 예제입니다.

후반에는 다음 메시지를 짧게 연결합니다.

> 이 접근은 낯선 것이 아닙니다.
> ML/DL 하이퍼파라미터 튜닝에서는 이미 기본적으로 사용될 만큼 검증된
> black-box optimization 프레임워크입니다.
> 중요한 것은 대상이 모델 하이퍼파라미터인지 CRM 정책인지가 아니라,
> 문제가 `x -> f(x)` 형태이고 평가 비용이 크며 모든 후보를 다 실험할 수 없느냐입니다.

가격 최적화, 쿠폰 정책, 메시징 정책, 예산 배분 등도 같은 언어로 볼 수 있습니다.

## 3. 문제 제기 톤

A/B 테스트나 실무자의 직감을 공격하지 않습니다.

선호 톤:

> 직감은 실무에서 필요합니다.
> 다만 정책 후보가 많아지고 실험 기회가 제한되면,
> 직감만으로 다음 A/B 후보를 고르는 방식에는 한계가 있습니다.

즉, "A/B 테스트는 틀렸다"가 아니라
"A/B 테스트 후보를 고르는 문제를 더 잘 다룰 수 있다"가 중심입니다.

## 4. 메인 Surprise

청중에게 가장 강하게 남길 surprise는 다음입니다.

> Uncertainty는 피해야 할 것이 아니라,
> 다음 실험을 고르는 정보입니다.

조금 더 실무적으로 표현하면:

> 직감으로 A/B 후보를 반복해서 고르는 대신,
> uncertainty를 이용해 다음 실험점을 고르면
> 전체 실험 수와 기간을 줄일 수 있습니다.

보조 surprise는 후반에서만 사용합니다.

- 가장 높은 incremental profit 점이 opt-out constraint 때문에 최종 선택이 아닐 수 있습니다.
- 전체 평균 최적점보다 context별 최적점이 더 실무적일 수 있습니다.

## 5. 중심 예제

중심 예제는 장바구니 미구매 고객 대상 리마인드 CRM입니다.

좋은 프레이밍:

> 관심 신호가 있는 고객에게,
> 얼마나 빨리 얼마나 큰 혜택으로 개입해야
> 순증분 이익은 높이고 opt-out은 넘지 않을까?

구체적 시나리오:

- 기준 이벤트: 장바구니에 담았지만 아직 구매하지 않은 상태
- 정책 변수:
  - `discount_rate`: 할인율
  - `send_timing`: 장바구니 담은 후 리마인드/쿠폰 발송 시점
- 목적:
  - `incremental profit` 최대화
- 제약:
  - `opt_out_rate <= threshold`

이 예제는 기존의 단순한 "언제 쿠폰을 보내면 재구매가 잘 될까?"보다 강합니다.
너무 빠른 개입이나 큰 혜택은 단기 구매를 만들 수 있지만,
고객 입장에서는 압박으로 느껴져 opt-out/알림 차단률을 높일 수 있기 때문입니다.

## 6. Objective

화면과 말의 중심 objective는 `incremental profit`입니다.

해석:

> 쿠폰을 보냈기 때문에 추가로 생긴 구매 이익에서
> 쿠폰 비용과 발송 비용을 뺀 값입니다.
> 즉, "많이 팔렸나"가 아니라
> "이 개입이 실제로 돈을 더 벌었나"를 최적화합니다.

화면에는 간결하게 둡니다.

```text
incremental profit
```

필요하면 말로 다음을 보완합니다.

```text
incremental profit = uplifted purchase profit - coupon cost - send cost
```

## 7. Constraint

본문 constraint는 opt-out/알림 차단률 하나로 고정합니다.

문제 정의:

```text
maximize incremental profit
subject to opt_out_rate <= threshold
```

BO 설명상으로는 objective와 constraint를 별도의 black-box 함수로 제시합니다.

```text
f(x): incremental profit
g(x): opt-out risk
maximize f(x)
subject to g(x) <= threshold
```

다만 constrained BO의 수학을 깊게 설명하지는 않습니다.
목표는 다음 감각만 전달하는 것입니다.

> BO는 `f(x)`만 최적화하는 문제에서 끝나지 않고,
> `g(x) <= threshold` 같은 운영 제약이 있는 문제로도 확장할 수 있습니다.

시각화는 feasible region 중심으로 단순화합니다.

## 8. Context

context는 다음 조합으로 둡니다.

```text
상품 가격대 x 고객 구매 이력
```

예시 세그먼트:

- 저가 장바구니 x 신규 고객
- 저가 장바구니 x 기존 고객
- 고가 장바구니 x 신규 고객
- 고가 장바구니 x 기존 고객

이 선택은 연령/성별보다 더 적절합니다.

- 민감 속성처럼 보이지 않습니다.
- 정책 반응 차이가 자연스럽습니다.
- 고가 장바구니는 더 긴 고민 시간이 있을 수 있습니다.
- 신규 고객은 할인에 민감하지만 opt-out에도 민감할 수 있습니다.
- 기존 고객은 낮은 할인에도 반응할 수 있지만 과도한 쿠폰은 margin만 깎을 수 있습니다.

모델링 표현은 다음 정도만 사용합니다.

```text
f(x, c)
```

전달 목표:

> 정책 `x`가 같아도 context `c`가 다르면 반응 함수가 달라질 수 있습니다.
> 하지만 context마다 완전히 별도 문제로 풀 필요는 없고,
> 비슷한 context끼리는 정보를 공유할 수 있습니다.
> BO는 이런 방향으로도 확장할 수 있습니다.

context는 후반 확장 감각을 주는 역할입니다.
마지막 contribution 메시지에서는 제외합니다.

## 9. BO 직관 설명 깊이

기술 설명은 직관 중심입니다.
단, 그래픽을 적극 활용해 기술적 내용을 정확하게 전달합니다.

발표 시간 배분상 BO 직관 설명 블록은 약 8-10분입니다.

설명 목표:

- 수식 유도는 하지 않습니다.
- GP/GPR/acquisition을 한 줄 수식과 그래픽으로 설명합니다.
- 청중이 "함수도 확률분포를 가질 수 있다"를 직관적으로 이해하게 합니다.
- 청중이 "uncertainty를 다음 실험점 선택에 사용한다"를 기억하게 합니다.

## 10. BO 그래픽 요구사항

### 10.1 GP: 함수도 확률분포를 가질 수 있다

1D parameter 기준으로 설명합니다.

필요한 그래픽:

- 반투명한 함수 샘플들을 여러 개 누적해서 보여줍니다.
- 이를 통해 하나의 GP에서 함수가 확률적으로 샘플링될 수 있음을 보여줍니다.
- 서로 다른 GP 두 개를 비교해, 서로 다른 함수 분포가 생길 수 있음을 보여줍니다.

핵심 메시지:

> GP는 점 하나의 분포가 아니라 함수에 대한 분포입니다.

### 10.2 GPR: 데이터를 보면 함수 분포가 바뀐다

필요한 그래픽:

- prior `f ~ GP`에서 posterior `f | D ~ GP`로 이동합니다.
- 실제 데이터 포인트를 잘 보이게 표시합니다.
- 데이터 포인트가 주어진 뒤 반투명 함수 샘플들이 어떻게 달라지는지 보여줍니다.
- posterior mean line과 posterior variance band를 명확히 보여줍니다.

핵심 메시지:

> GPR은 관측 데이터를 본 뒤,
> 새로운 점들의 평균과 분산을 계산할 수 있게 해줍니다.

### 10.3 Acquisition Function

UCB 기준으로 설명합니다.

필요한 그래픽:

- 위에는 posterior mean과 variance band를 둡니다.
- 아래에는 acquisition function을 둡니다.
- x축과 평행한 선을 뒤에서 아래로 움직이며 acquisition function이 드러나는 식의 그래픽을 사용합니다.
- `mu(x) + beta sigma(x)`가 어떤 모양을 만드는지 시각적으로 보여줍니다.

핵심 메시지:

> 평균이 높은 곳과 아직 불확실한 곳을 함께 고려해 다음 실험점을 고릅니다.

### 10.4 Beta와 exploitation/exploration trade-off

필요한 그래픽:

- `beta = 1`과 `beta = 2`를 비교합니다.
- `beta`가 작을 때는 posterior mean이 높은 영역을 더 선호합니다.
- `beta`가 클 때는 uncertainty가 큰 영역도 더 강하게 고려합니다.

핵심 메시지:

> beta는 잘 될 것 같은 곳과 아직 모르는 곳 사이의 균형을 바꿉니다.

### 10.5 BO Loop

필요한 그래픽:

- acquisition으로 하나의 next point를 선택합니다.
- 그 점을 실제로 관측합니다.
- GPR에 새 점을 추가합니다.
- posterior가 업데이트됩니다.

표현:

```text
f | D_n ~ GP -> f | D_{n+1} ~ GP
```

핵심 메시지:

> BO는 이 과정을 반복하면서 전체 실험 수를 줄입니다.

## 11. 수식 표기

수식은 중간 수준으로 노출합니다.
LaTeX로 정확하게 렌더링해야 합니다.

HTML 구현 시 네트워크 의존성을 없애는 방향을 우선합니다.
CDN 기반 MathJax/KaTeX에 의존하지 않습니다.

후보 수식:

```tex
x^\* = \arg\max_x f(x)
```

```tex
f \sim \mathcal{GP}(m, k)
```

```tex
f \mid \mathcal{D}_n \sim \mathcal{GP}(m_n, k_n)
```

```tex
x_{n+1} = \arg\max_x \alpha(x)
```

```tex
\alpha_{\mathrm{UCB}}(x) = \mu_n(x) + \beta \sigma_n(x)
```

```tex
\max_x f(x) \quad \text{s.t.} \quad g(x) \le \tau
```

```tex
x^\*(c) = \arg\max_x f(x, c)
```

수식은 보이되, 설명은 그래픽이 담당해야 합니다.

## 12. 라이브러리 언급

Ax/BoTorch는 코드 스냅샷 2장으로 짧게 다룹니다.
합쳐서 약 2분 정도만 배정합니다.

### 12.1 Ax

목표:

> 생각보다 쉽게 시작할 수 있다.

보여줄 것:

- `parameters`
- `objective`
- `outcome_constraints`

메시지:

> 실무자가 정책 공간과 목적/제약을 정의하면,
> Ax가 BO loop를 감싸서 사용할 수 있게 해줍니다.

코드 스냅샷은 매우 간단해도 됩니다.

### 12.2 BoTorch

목표:

> 앞에서 본 개념이 코드에도 있다.

보여줄 것:

- GP prior
- posterior update
- acquisition function
- next candidate selection

BoTorch는 API 강의로 다루지 않습니다.
앞에서 배운 GP/GPR/acquisition이 실제 코드의 어느 부분에 대응되는지만 보여줍니다.

## 13. 발표 시간과 슬라이드 수

최종 발표 시간:

- 전체: Q&A 포함 30분
- 본문: 약 24-25분
- Q&A: 약 5분

슬라이드/scene 수:

- 18-22 scenes

BO 설명은 그래픽 애니메이션이 많으므로, "슬라이드 수"보다 "scene 수" 기준으로 설계합니다.

잠정 시간 배분:

- 오프닝/문제 제기: 4-5분
- BO 직관 그래픽 블록: 8-10분
- 장바구니 미구매 CRM 예제: 8-9분
- constraint/context/확장/코드: 4-5분
- 마무리: 1-2분

## 14. 시각 스타일

기본 배경은 사용자가 제공한 발표 포맷을 고정으로 사용합니다.

- 흰 배경
- 좌측 lime vertical bar
- 우상단 Dataya Nolja 로고
- Pretendard 폰트 사용

방향:

- 강의형
- 큰 수식
- 선명한 그래프
- 최소 장식

Patrick Winston 원칙에 따라, 제목은 항상 필요하지 않습니다.

- 모든 슬라이드에 제목을 넣지 않습니다.
- 필요한 장면에만 짧은 claim을 둡니다.
- 그래픽과 수식이 중심이 되는 장면에서는 제목을 과감히 생략할 수 있습니다.

## 15. Section Marker

section marker는 영어 키워드 중심의 발표 메시지형으로 사용합니다.

잠정 섹션:

```text
01 SEARCH
02 BELIEF
03 DECISION
04 CRM
05 EXTEND
06 CONTRIBUTIONS
```

의미:

- `SEARCH`: 직감 기반 A/B 후보 반복에서 정책 공간 탐색으로 전환
- `BELIEF`: GP/GPR로 함수에 대한 믿음과 업데이트를 시각화
- `DECISION`: acquisition과 beta로 다음 실험점 선택
- `CRM`: 장바구니 미구매 리마인드 CRM 예제
- `EXTEND`: constraint, context, hyperparameter tuning, Ax/BoTorch
- `CONTRIBUTIONS`: 발표가 남기는 사고방식

section marker는 장식이 아니라 복귀 표지판입니다.
고정 breadcrumb처럼 크게 쓰지 않고, 필요한 위치에 작게 둡니다.

## 16. 청중 질문 설계

질문은 단순 참여 장치가 아니라 기억 장치여야 합니다.
발표의 핵심 전환점에만 사용합니다.

질문 후보:

1. SEARCH 전환

   > 다음 A/B 후보를 고를 때,
   > 우리는 무엇을 근거로 그 후보를 고르고 있나요?

2. DECISION 전환

   > 불확실성이 큰 곳은 피해야 할 곳일까요,
   > 아니면 실험할 가치가 있는 곳일까요?

3. CRM/constraint 전환

   > 수익이 가장 높은 정책이 opt-out도 가장 높다면,
   > 그 정책은 최적 정책일까요?

질문 뒤에는 실제로 2-5초 정도 멈출 수 있어야 합니다.

## 17. 마지막 Contribution

마지막 contribution 메시지에서는 context를 제외합니다.
`f(x)`와 `g(x) <= c` 중심으로 닫습니다.

핵심 메시지:

> 대부분의 실제 의사결정은 결국 `f(x)`를 최대화하는 `x`를 찾는 일입니다.
> 그리고 복잡한 현실에서는 `g(x) <= c` 같은 제약이 붙는 경우도 많습니다.
> 모든 후보를 충분히 실험할 수 없다면,
> 오늘 본 Bayesian Optimization을 떠올려보시면 좋겠습니다.

화면 후보:

```text
Most decisions are search problems.

Find x that maximizes f(x).
Often, under g(x) <= c.
```

마지막은 `Thank you` 슬라이드로 끝내지 않습니다.
청중이 가져갈 사고방식을 남기는 contribution slide로 끝냅니다.

## 18. 아직 스크립트 작성 전 확인할 항목

아래는 다음 단계에서 구조안 작성 전에 점검할 수 있는 항목입니다.

- 18-22 scenes의 정확한 scene breakdown
- 각 scene의 animation 여부
- GP/GPR/acquisition 그래픽을 SVG/Canvas 중 무엇으로 구현할지
- LaTeX 로컬 렌더링 방식
- Ax/BoTorch 코드 스냅샷의 정확한 코드 수준
- Q&A backup을 HTML 안에 둘지 여부
