# Speaker Script

Title: `A/B 테스트만으로는 부족합니다: CRM 정책 최적화로 이해하는 베이지안 최적화`

Created: 2026-06-01

Source of truth:

- `presentation_html/interview_notes.md`
- `presentation_html/presentation_principles.md`
- `docs/how_to_speak/patrick_winston_analysis.md`

Format assumptions:

- HTML presentation under `presentation_html/`
- Pretendard loaded from `../fonts/Pretendard-1.3.9/`
- Local LaTeX rendering only; no CDN dependency
- Official-like white canvas, left lime bar, top-right Dataya Nolja logo
- 23 scenes total
- Main talk target: about 25-26 minutes
- Q&A target: about 5 minutes

## Global Speaking Rules

- Do not read the screen.
- Do not apologize for simplifying the math.
- Use questions only where they reinforce the core memory.
- After each designed question, pause for 2-5 seconds.
- `감사합니다` 슬라이드로 끝내지 말고, 마지막 Contributions 메시지에서 멈춘다.
- Keep A/B testing criticism soft: intuition is useful, but limited under many candidates and limited experiment budget.

## Scene 01. Title Page

Section: `00 TITLE`

Target time: 0:20

On screen:

```text
A/B 테스트만으로는 부족합니다
CRM 정책 최적화로 이해하는 베이지안 최적화
```

Visual:

- Full title image: `presentation_html/format/title.png`.
- Do not add extra overlay text.

Script:

안녕하세요. AB180에서 데이터사이언티스트로 일하고 있는 이병헌입니다.
A/B 테스트만으로는 부족합니다...라는 다소 과격한 발언과 어떻게 보면 도발을 하게 된 것 같은데요.
이로 인해 이렇게 많은 분들이 참여해주신 것 같아서, 송구스러우면서도 제목을 잘 지은 것 같다는 생각이 듭니다.

Transition:

## Scene 02. A/B 테스트는 비교입니다

Section: `00 A/B`

Target time: 1:10

On screen:

```text
장바구니 -> 미구매 -> CRM 개입

Q. 장바구니에 담은 상품을 미구매한 경우, 어떤 형태로 고객에게 알리는 것이 좋을까?
A: 리마인드 푸시
B: 6시간 뒤 10% 쿠폰
```

Visual:

- 상단에는 간단한 상황 흐름:
  `장바구니` -> `미구매` -> `CRM 개입`.
- 가운데에는 질문:
  `Q. 장바구니에 담은 상품을 미구매한 경우, 어떤 형태로 고객에게 알리는 것이 좋을까?`
- 아래에는 카드가 아니라 줄글 형태의 후보:
  `A: 리마인드 푸시`
  `B: 6시간 뒤 10% 쿠폰`.
- 이 장면은 A/B 테스트를 긍정적으로 보여줘야 한다.
  핵심은 “A/B 테스트는 좋은 비교 도구”라는 점이다.

Script:
사실은요... A/B 테스트가 막 그렇게 크게 부족하지는 않습니다. 오히려 매우 훌륭한 도구입니다.
예를 들어, 어떤 고객이 쇼핑 앱에서 결제 직전까지 갔지만 구매를 하지 않았다고 가정해보겠습니다.
이 때, 쇼핑 앱에서는 해당 고객이 구매를 유도하도록 푸시나 쿠폰을 보내고 싶을 텐데요.
하지만, 사실 푸시나 쿠폰 중 더 좋은 정책이 있을텐데... 이 때, A/B 테스트라는 실험을 통해서 어떤 것이 더 좋은지 평가할 수 있습니다.

A/B 테스트를 진행하는 방법은 이미 다 아시겠지만,
두 집단을 랜덤하게 나누어서 서로 비슷한 집단이 되게 하구요.
이 두 집단을 같은 기간 동안 관측함으로써 나오는 결과를 통계적 비교하여 평가하는 방법입니다.

## Scene 03. 후보 선택 문제

Section: `00 A/B`

Target time: 1:20

On screen:

```text
Q. 다음 A/B 후보는 무엇으로 고를까요?

쿠폰
  coupon 할인율: 3 ~ 15%
  발송시점: 1 ~ 48시간

대상
  신규고객 기존고객
  고가상품 저가상품

제약
  앱 삭제, 수신거부율(opt-out)
```

Visual:

- 화면 상단에는 질문:
  `Q. 다음 A/B 후보는 무엇으로 고를까요?`
- 아래에는 세 개의 블록:
  `쿠폰`, `대상`, `제약`.
- `쿠폰` 블록:
  `coupon 할인율: 3 ~ 15%`, `발송시점: 1 ~ 48시간`.
- `대상` 블록:
  `신규고객 / 기존고객`, `고가상품 / 저가상품`.
- `제약` 블록:
  `앱 삭제`, `수신거부율(opt-out)`.

Script:
그런데, 실무의 질문은 보통 이렇게 단순하지 않을 수도 있습니다.

쿠폰만 보더라도 할인율은 3%~15%가 있을 수 있고,
발송 시점 또한 1시간~48시간까지 굉장히 다양한 경우가 있을 수 있겠죠.

또한, 해당 고객이 신규고객인지 기존고객인지,
구매하려던 상품이 고가 상품인지 저가상품인지에 따라서도 적용해야하는 정책이 다를 수 있습니다.
이뿐만이 아닙니다. 해당 쿠폰을 발송함으로써 생기는 앱 삭제 또는 수신 거부율이 일정 비율 이상을 넘지 않는 제약 조건도 함께 봐야할 수도 있습니다.

만약, 쿠폰의 할인율과 발송시점만 따로 떼내서 모든 경우의 수를 실험하더라도 총 13 x 48 = 624개의 실험이 필요할 수도 있습니다.
하지만, 베이지안 최적화는 이를 효과적으로 Search할 수 있게 도와주어 아래의 질문에 대하여 답변을 해줍니다.

"다음에는 어떤 후보를 A/B 테스트로 올릴 것인가?"

## Scene 04. 목차

Section: `00 ROADMAP`

Target time: 0:45

On screen:

```text
목차

01 Search
02 Belief
03 Decision
04 CRM
05 Extend
06 Contributions
```

Visual:

- 간결한 2열 목차.
- Section marker는 영어 키워드를 유지한다.
- Each item has a short Korean explanation.

Script:

지금까지 A/B 테스트가 훌륭한 비교 도구라는 점,
그리고 실무에서는 후보 선택 문제가 따로 생긴다는 점을 봤습니다.

이제 오늘의 흐름을 잡겠습니다.

목차는 여섯 단계입니다.

먼저 후보 선택을 Search 문제로 다시 보겠습니다.

그 다음 가우시안 프로세스, 즉 GP로
모르는 함수에 대한 belief를 어떻게 표현하는지 보겠습니다.

세 번째로는 그 belief에서
다음 실험점을 어떻게 고르는지 보겠습니다.

그리고 이 구조를 장바구니 미구매 CRM 예제로 내린 뒤,
마지막에는 CRM 밖의 블랙박스 최적화 문제로 넓히겠습니다.

Transition:

먼저 오해를 막고, 이 발표가 다루는 문제의 모양부터 잡겠습니다.

## Scene 05. 비교에서 탐색으로

Section: `01 SEARCH`

Target time: 0:45

On screen:

```text
A/B 테스트
비교

베이지안 최적화
탐색

핵심은 다음 A/B 후보를 잘 선택하는 것입니다.
```

Visual:

- A/B 테스트는 `비교`, 베이지안 최적화는 `탐색`으로 크게 대비한다.
- 오른쪽에는 두 후보 비교와 `할인율 x 발송시점` 정책 공간을 함께 보여준다.
- 마지막 메시지는 `다음 A/B 후보를 잘 선택하는 것`.

Script:

오해를 먼저 막겠습니다.

베이지안 최적화는 A/B 테스트를 대체하는 것이 아닙니다.

어떤 정책 후보를 실제 유저에게 평가하려면,
여전히 실험 설계가 필요합니다.
무작위 배정도 필요하고,
표본 수도 필요하고,
측정 품질도 중요합니다.

BO가 바꾸는 지점은 그 앞입니다.

어떤 후보를 다음 A/B 테스트에 올릴 것인가.

방금 본 예시로 말하면,
수많은 할인율과 발송 시점 조합 중에서
이번 주에 실제로 테스트할 조합을 무엇으로 정할 것인가입니다.

왼쪽은 A/B 테스트가 잘하는 일입니다.

A와 B가 있고,
둘 중 무엇이 좋은지 비교합니다.

오른쪽은 오늘 다룰 일입니다.
policy search입니다.

앞에서 본 것처럼,
후보는 두 개가 아니라 정책 공간 전체에 놓여 있습니다.

모든 후보를 충분히 실험할 수 있다면 문제는 쉽습니다.
그냥 다 해보면 됩니다.

하지만 보통은 그렇지 않습니다.
트래픽은 제한되어 있고,
실험 기간도 제한되어 있고,
한 번의 실험에도 비용이 있습니다.

그래서 질문은 이렇게 바뀝니다.

> 모든 점을 다 찍을 수 없다면, 다음 점은 어디에 찍어야 할까?

Transition:

이 문제를 수식으로 쓰면 매우 짧습니다.

## Scene 06. 블랙박스 최적화

Section: `01 SEARCH`

Target time: 1:20

On screen:

```tex
x^\* = \arg\max_x f(x)
```

Small text:

```text
x: 정책 후보
f(x): 우리가 키우고 싶은 성과
```

Visual:

- 1D or 2D hidden response surface.
- The peak is visually suggested, not fully revealed.

Script:

우리가 푸는 문제는 이 한 줄입니다.

`x`는 우리가 고를 수 있는 정책 후보입니다.

오늘 예제에서는
할인율과 발송 시점의 조합입니다.

조금 더 일반화하면,
가격일 수도 있고,
예산 배분일 수도 있고,
모델 하이퍼파라미터일 수도 있습니다.

`f(x)`는 그 정책을 실행했을 때 우리가 얻고 싶은 성과입니다.

오늘은 그 성과를 순증분 이익으로 보겠습니다.

그리고 우리는 `f(x)`를 가장 크게 만드는 `x`를 찾고 싶습니다.

그런데 여기서 중요한 조건이 있습니다.

`f(x)`를 미리 알 수 없습니다.
정책을 실제로 실행해봐야 관측됩니다.

그리고 한 번 관측하는 데 비용이 듭니다.
시간이 들고, 유저가 필요하고, 실험 기회가 소모됩니다.

이런 문제를 블랙박스 최적화 문제라고 볼 수 있습니다.

입력 `x`를 넣으면 결과 `f(x)`가 나오지만,
그 안쪽 함수 모양은 모릅니다.

Transition:

그럼 모르는 함수를 어떻게 다룰까요? 여기서 두 번째 장으로 넘어갑니다.

## Scene 07. 함수에 대한 Belief

Section: `02 BELIEF`

Target time: 1:30

On screen:

```tex
f \sim \mathcal{GP}(m, k)
```

Claim:

```text
Gaussian Process
함수를 확률적으로 추출합니다.
```

Visual:

- A 1D axis.
- Many semi-transparent function samples accumulate.
- No data points yet.

Script:

베이지안 최적화의 첫 번째 핵심은
모르는 함수에 대한 belief를 명시적으로 가진다는 점입니다.

잠시 2차원 정책 공간을 1차원으로 줄여서 보겠습니다.
예를 들어 발송 시점은 고정하고,
할인율을 바꿨을 때 성과가 어떻게 움직일지만 본다고 생각하시면 됩니다.

Gaussian Process를 아주 직관적으로 말하면,
함수에 대한 확률분포입니다.

우리는 보통 확률분포라고 하면 점 하나를 떠올립니다.
키나 몸무게처럼 값 하나가 흔들리는 분포입니다.

여기서는 조금 다릅니다.

점 하나가 아니라,
함수 전체가 이렇게도 생길 수 있고,
저렇게도 생길 수 있다고 봅니다.

화면에 보이는 반투명한 선 하나하나가
가능한 함수 하나입니다.

아직 데이터를 보지 않았기 때문에,
여러 함수가 가능하다고 열어두는 겁니다.

오늘은 GP를 증명하지 않겠습니다.
가져갈 직관은 하나입니다.

> 함수도 확률분포를 가질 수 있다.

Transition:

그리고 어떤 belief를 갖느냐에 따라 가능한 함수 모양도 달라집니다.

## Scene 08. 서로 다른 prior

Section: `02 BELIEF`

Target time: 1:10

On screen:

```text
다른 belief는
다른 함수를 만듭니다.
```

Visual:

- Two side-by-side GP sample panels.
- Left: smoother functions.
- Right: more wiggly functions or larger variation.
- Keep labels minimal: `GP(m_1, k_1)`, `GP(m_2, k_2)`.

Script:

같은 GP라고 해도,
우리가 어떤 함수 모양을 그럴듯하다고 생각하느냐에 따라
샘플되는 함수의 모양이 달라집니다.

왼쪽은 가까운 `x`에서 결과도 비슷할 것이라는 belief가 강한 경우입니다.
함수가 부드럽습니다.

오른쪽은 조금 더 빠르게 변할 수 있다고 보는 경우입니다.
함수가 더 많이 흔들립니다.

이 지점이 실무적으로 중요합니다.

베이지안 최적화가 실험 기간을 줄일 수 있으려면,
가까운 정책들이 완전히 무관한 결과를 내지 않는다는 가정이 필요합니다.

예를 들어 할인율 10%와 11%가 완전히 아무 상관없는 결과를 낸다면,
우리는 주변 정보를 활용할 수 없습니다.

하지만 많은 정책 문제에서는
가까운 정책들이 어느 정도 비슷한 반응을 냅니다.

그 구조를 활용하는 것이 BO의 출발점입니다.

Transition:

이제 데이터를 보면 이 belief가 어떻게 바뀌는지 보겠습니다.

## Scene 09. prior에서 posterior로

Section: `02 BELIEF`

Target time: 1:40

On screen:

```tex
f \mid \mathcal{D}_n \sim \mathcal{GP}(m_n, k_n)
```

Claim:

```text
데이터가 함수 분포를 바꿉니다.
```

Visual:

- prior에서 샘플된 함수들로 시작한다.
- Add visible observed points.
- 관측점을 추가하면 posterior 샘플들이 관측점 주변으로 좁아진다.
- prior와 posterior 그래프는 크게 보여주고, 중간 화살표는 쓰지 않는다.
- `데이터`, `posterior`, `미지 영역` 라벨은 크게 보이게 둔다.

Script:

이제 몇 개의 실험 결과를 관측했다고 해보겠습니다.

우리는 어떤 `x`에서 실험했습니다.
예를 들어 5% 쿠폰을 6시간 뒤에 보냈고,
10% 쿠폰을 하루 뒤에 보냈습니다.

그리고 각 실험에서 결과 `y`를 봤습니다.

그러면 가능한 함수의 모양이 줄어듭니다.

방금까지 가능하다고 생각했던 함수들 중에서,
관측된 데이터와 너무 맞지 않는 함수들은 덜 그럴듯해집니다.

이게 가우시안 프로세스 회귀의 직관입니다.

prior는 데이터를 보기 전의 함수 분포입니다.
posterior는 데이터를 본 뒤의 함수 분포입니다.

수식은 이렇게 쓰지만,
핵심은 화면입니다.

데이터 포인트 근처에서는 가능한 함수들이 좁아집니다.
데이터가 없는 영역에서는 여전히 불확실성이 큽니다.

즉, 실험을 한 곳과 하지 않은 곳의 차이가
함수 분포 안에 남습니다.

Transition:

이 posterior에서 우리는 두 가지를 얻습니다.

## Scene 10. 평균과 불확실성

Section: `02 BELIEF`

Target time: 1:20

On screen:

```text
평균 + 불확실성
```

Visual:

- Posterior mean line.
- Posterior variance band.
- Observed points clearly visible.

Script:

posterior에서 우리가 특히 보는 것은 두 가지입니다.

첫 번째는 평균입니다.

지금까지 데이터를 봤을 때,
각 할인율과 발송 시점 후보에서
기대되는 순증분 이익이 어느 정도인가.

두 번째는 분산, 또는 불확실성입니다.

각 `x`에서 우리가 얼마나 모르는가.

여기서 중요한 점은,
불확실성이 단순히 나쁜 것이 아니라는 겁니다.

이 예제에서는 일부러 두 영역을 분리해서 보겠습니다.

왼쪽에는 평균이 높은 영역이 있고,
오른쪽에는 평균은 낮지만 uncertainty band가 훨씬 넓은 영역이 있습니다.

모르는 곳이 있다는 것은 불편하지만,
동시에 그곳이 다음 실험의 후보가 될 수 있다는 뜻입니다.

이제 오늘 발표의 가장 중요한 질문으로 갑니다.

Transition:

세 번째 장입니다. Belief에서 Decision으로 갑니다.

## Scene 11. 핵심 질문

Section: `03 DECISION`

Target time: 0:50

On screen:

```text
불확실성은 위험인가,
정보인가?
```

Visual:

- 제목은 앞 장의 제목 위치와 맞춘다.
- posterior 곡선을 크게 중앙에 두고, 평균이 높은 영역과 불확실성이 높은 영역을 함께 보여준다.
- Do not show answer immediately.

Script:

여기서 질문 하나를 드리겠습니다.

> 불확실성이 큰 곳은 피해야 할 곳일까요,
> 아니면 실험할 가치가 있는 곳일까요?

잠깐 멈춤.

일반적인 보고서에서는 불확실성이 불편한 요소처럼 보입니다.

하지만 Search 문제에서는 다릅니다.

불확실성은 다음 실험을 고르는 정보입니다.

잘 될 것 같은 곳도 중요하지만,
아직 몰라서 가치가 있는 곳도 있습니다.

Transition:

이 둘을 합쳐서 다음 점을 고르는 함수가 획득 함수입니다.

## Scene 12. 획득 함수

Section: `03 DECISION`

Target time: 1:40

On screen:

```tex
x_{n+1} = \arg\max_x \alpha(x)
```

Then:

```tex
\alpha_{\mathrm{UCB}}(x) = \mu_n(x) + \beta \sigma_n(x)
```

Visual:

- 위 패널: 사후 평균과 분산 범위.
- 아래 패널: UCB 획득 함수 곡선.
- posterior와 획득 함수 패널 모두에서 y축과 평행한 세로 축이 같은 속도로 좌에서 우로 이동한다.
- 이 축이 posterior의 band를 훑고, 동시에 아래의 `alpha(x)` 위치도 같이 훑는다.

Script:

획득 함수는 다음 실험점을 고르기 위한 점수 함수입니다.

오늘은 UCB라는 형태로 보겠습니다.

수식은 복잡하지 않습니다.

평균 `mu`가 있습니다.
지금까지 봤을 때 잘 될 것 같은 정도입니다.

그리고 표준편차 `sigma`가 있습니다.
아직 잘 모르는 정도입니다.

UCB는 이 둘을 더합니다.

잘 될 것 같은 곳과
아직 모르는 곳을 함께 점수화합니다.

아래 그래프가 획득 함수입니다.
이 값이 가장 큰 곳이 다음 실험 후보가 됩니다.

여기서 BO가 하는 일은 감으로 찍는 것이 아닙니다.

지금까지의 실험 결과로 만든 belief,
그리고 그 belief의 불확실성을 이용해서
다음에 가장 정보적인 점을 고릅니다.

Transition:

그런데 평균과 불확실성의 균형은 조절할 수 있습니다.

## Scene 13. 베타가 선택을 바꿉니다

Section: `03 DECISION`

Target time: 1:20

On screen:

```tex
\alpha_{\mathrm{UCB}}(x) = \mu_n(x) + \beta \sigma_n(x)
```

Small labels:

```text
beta = 0.4
beta = 2.3
```

Visual:

- Side-by-side or toggle animation.
- beta = 0.4 selects the higher-mean region.
- beta = 2.3 moves to the high-uncertainty region.

Script:

여기서 `beta`는 균형을 바꾸는 값입니다.

`beta`가 작으면 평균이 높은 곳을 더 선호합니다.
이미 좋아 보이는 곳을 더 파는 쪽입니다.

`beta`가 커지면 불확실성이 큰 곳도 더 중요하게 봅니다.
아직 모르는 영역을 확인하려는 힘이 커집니다.

이걸 흔히 exploitation과 exploration의 균형이라고 부릅니다.

하지만 용어보다 중요한 것은 직관입니다.

좋아 보이는 곳만 계속 가면,
더 좋은 영역을 놓칠 수 있습니다.

모르는 곳만 계속 가면,
실험 비용을 낭비할 수 있습니다.

BO는 이 균형을 명시적으로 계산합니다.

Transition:

이제 한 점을 고른 뒤 무슨 일이 일어나는지 보겠습니다.

## Scene 14. 베이지안 최적화 반복

Section: `03 DECISION`

Target time: 1:20

On screen:

```text
posterior
평균 + 불확실성
획득 함수
다음 A/B 후보
```

Visual:

- Step 1: posterior.
- Step 2: 평균과 불확실성 `mu(x), sigma(x)`.
- Step 3: 획득 함수 `alpha(x)=mu+beta sigma`.
- Step 4: 가장 점수가 높은 `x`를 다음 A/B 후보로 선택.
- Loop arrow.

Script:

베이지안 최적화는 이 과정을 반복합니다.

지금까지의 데이터로 posterior를 만듭니다.

posterior에서 평균과 불확실성을 계산합니다.

그 둘을 합쳐서 획득 함수를 만듭니다.

획득 함수 점수가 가장 큰 `x`를 다음 A/B 후보로 선택합니다.

그 후보는 다시 실제 A/B 테스트에 올라갑니다.
예를 들어 12% 쿠폰을 6시간 뒤에 보내는 정책일 수 있습니다.

그 점을 실제로 실험합니다.

새로운 관측값을 데이터에 추가합니다.

그러면 posterior가 다시 바뀝니다.

이 반복을 통해서,
모든 후보를 다 실험하지 않고도
좋은 영역으로 빠르게 좁혀갑니다.

다시 말하지만,
BO가 한 실험점의 표본 수 문제를 없애는 것은 아닙니다.

하지만 제한된 실험 기회 안에서
무엇을 먼저 실험할지에 대한 선택을 훨씬 정보적으로 만듭니다.

Transition:

이제 이 구조를 실제 정책 문제처럼 보이는 예제로 내리겠습니다.

## Scene 15. CRM 예시

Section: `04 CRM`

Target time: 1:20

On screen:

```text
장바구니 미구매 리마인드

결제 직전에 이탈한 미구매 고객에게 보낼 CRM
고가/저가 상품 & 기존/신규 고객
할인율 x 발송 시점
```

Visual:

- 중앙에 `쿠폰 발송 / 정책 x`.
- 오른쪽 같은 열 위아래에 `구매이익 f(x)`, `수신거부 g(x)`.
- 정책 x에서 두 결과로 양 갈래 화살표.
- `고가 상품(장바구니 신호)`, `결제 이탈(미구매)` 카드는 쓰지 않는다.

Script:

처음에 던진 예시를 다시 가져오되,
이번에는 설명을 반복하지 않고 최적화 문제로만 놓겠습니다.

오늘의 예제는 결제 직전에 이탈한 미구매 고객입니다.

이 고객에게 리마인드 메시지나 쿠폰을 보낼 수 있습니다.

정책 변수는 두 개로 단순화하겠습니다.

첫 번째는 할인율입니다.
5%, 10%, 15%처럼 혜택의 크기를 바꾸는 축입니다.

두 번째는 발송 시점입니다.
장바구니에 담은 직후 보낼지,
몇 시간 뒤 보낼지,
하루나 이틀 뒤 보낼지입니다.

좋은 질문은 이렇게 표현할 수 있습니다.

고가/저가 상품,
기존/신규 고객 같은 맥락을 보면서
얼마나 빨리,
얼마나 큰 혜택으로 개입해야 하는지를 묻습니다.

하나의 정책은 두 가지 결과를 동시에 만듭니다.

구매이익,
그리고 수신거부입니다.

그래서 좋은 질문은 이렇게 표현할 수 있습니다.

관심 신호가 있는 고객에게
얼마나 빨리,
얼마나 큰 혜택으로 개입해야
순증분 이익은 높이고
수신 거부율은 넘지 않을까?

여기서 CRM은 주제가 아니라 렌즈입니다.

우리가 보고 싶은 것은
비싼 블랙박스 실험에서 다음 후보를 고르는 구조입니다.

Transition:

이제 할인율과 발송 시점의 2차원 정책 공간을 보겠습니다.

## Scene 16. Policy Search Surface

Section: `04 CRM`

Target time: 1:30

On screen:

```tex
x^\* = \arg\max_x f(x)
```

Visual:

- 2D 히트맵: x축 할인율, y축 발송 시점.
- BO가 선택해온 점들의 이동 경로.
- 현재까지 관측된 좋은 점 또는 추천점을 표시한다.

Script:

이제 다시 처음 수식으로 돌아옵니다.

`x`는 할인율과 발송 시점의 조합입니다.

`f(x)`는 순증분 이익입니다.

우리는 이 히트맵의 가장 좋은 영역을 찾고 싶습니다.

히트맵의 한 점은
하나의 실제 CRM 정책 후보입니다.

모든 조합을 다 실험할 수 있으면 쉽습니다.
하지만 우리는 그럴 수 없다고 가정합니다.

그래서 몇 개의 초기 점에서 시작합니다.

각 점은 하나의 정책 실험입니다.

결과가 들어오면 posterior가 바뀌고,
획득 함수가 다음 점을 고릅니다.

이 과정을 반복하면서
유망한 영역으로 좁혀갑니다.

여기서 강조하고 싶은 것은
BO가 정답을 한 번에 맞히는 도구가 아니라는 점입니다.

BO는 다음 실험 후보를 더 잘 고르는 도구입니다.

Transition:

그런데 실무에서는 profit만 보면 안 됩니다.

## Scene 17. 제약조건 질문

Section: `04 CRM`

Target time: 0:45

On screen:

```text
수익이 가장 높은 정책이
수신 거부도 가장 많이 만든다면,
그 정책은 최적일까요?
```

Visual:

- Three compact boxes:
  `최고 수익` + `최고 수신 거부` -> `최적인가?`
- No formula yet.

Script:

그런데 실무에서는 profit만 보면 안 됩니다.

여기서 질문을 하나 더 드리겠습니다.

> 수익이 가장 높은 정책이 수신 거부도 가장 높다면,
> 그 정책은 최적 정책일까요?

잠깐 멈춤. 3초.

이 질문이 중요한 이유는,
장바구니 미구매 고객에게 너무 강한 쿠폰을 너무 빠르게 보내면
단기 구매는 늘어날 수 있지만
장기적으로는 고객 접점을 잃게 만들 수 있기 때문입니다.

Transition:

이제 답을 제약조건으로 표현하겠습니다.

## Scene 18. 제약조건: 실행 가능한 최적점

Section: `04 CRM`

Target time: 1:25

On screen:

```tex
\max_x f(x)
\quad \text{s.t.} \quad
g(x) \le \tau
```

Small labels:

```text
f(x): 순증분 이익
g(x): 수신 거부 위험
tau: 허용 가능한 최대 수신 거부율
```

Visual:

- 같은 2D 히트맵.
- Feasible region overlay.
- 제약 없는 최적점과 실행 가능한 최적점을 따로 표시한다.

Script:

실무에서는 보통 아닙니다.

단기 순증분 이익이 높더라도,
알림 차단이나 수신 거부를 너무 많이 만든다면
운영 가능한 정책이 아닙니다.

그래서 두 번째 블랙박스 함수를 생각합니다.

`f(x)`는 순증분 이익입니다.

`g(x)`는 수신 거부 위험입니다.

우리는 `f(x)`를 최대화하고 싶지만,
`g(x)`는 임계값 `tau`를 넘으면 안 됩니다.

오늘 제약조건이 있는 BO를 수학적으로 깊게 들어가지는 않겠습니다.

가져갈 직관은 하나입니다.

BO는 단순히 가장 높은 점을 찾는 문제에서 끝나지 않고,
운영 가능한 영역 안에서 좋은 점을 찾는 문제로 넓어질 수 있습니다.

이 그림에서 제약 없는 최적점은 수익만 보면 좋은 점입니다.

하지만 실행 가능한 최적점은 수신 거부 제약을 넘지 않는 영역 안에서
가장 좋은 점입니다.

Transition:

여기서 한 번 더 현실에 가까워져 보겠습니다.

## Scene 19. 맥락 질문

Section: `04 CRM`

Target time: 0:35

On screen:

```text
모든 맥락에
같은 정책을 쓸 수 있을까요?
```

Small text:

```text
상품 가격대 x 구매 이력
```

Visual:

- Question-only slide.
- No formula and no maps yet.

Script:

질문을 하나 더 드리겠습니다.

같은 장바구니 미구매 상황이어도,
고가 상품을 담은 재방문 고객과
저가 상품을 처음 담은 신규 고객에게
같은 정책이 최적일까요?

잠깐 멈춤. 2초.

여기서 맥락은 복잡하게 잡지 않고 두 가지만 보겠습니다.

상품 가격대,
그리고 고객 구매 이력입니다.

Transition:

맥락이 달라지면 같은 정책 공간에서도 최적점이 달라질 수 있습니다.

## Scene 20. 맥락에 따른 다른 반응 함수

Section: `04 CRM`

Target time: 1:25

On screen:

```text
맥락이 바뀌면
최적점도 바뀝니다.
```

Optional formula:

```tex
x^\*(c) = \arg\max_x f(x, c)
```

Visual:

- Four small contour maps:
  저가 상품 / 신규 고객,
  저가 상품 / 재방문 고객,
  고가 상품 / 신규 고객,
  고가 상품 / 재방문 고객.
- Different optima.
- 수식과 `상품 가격대 x 구매 이력` 라벨은 중앙 배치.
- 네 개 지도와 라벨은 크게 보여준다.

Script:

화면의 네 개 지도는 모두 같은 정책 공간입니다.

각 지도는 할인율과 발송 시점의 조합을 보여줍니다.

저가 상품을 담은 신규 고객과
고가 상품을 담은 기존 고객은
같은 할인율과 같은 발송 시점에 다르게 반응할 수 있습니다.

수식으로 쓰면 `f(x)`가 아니라 `f(x, c)`입니다.

정책 `x`가 같아도
맥락 `c`가 달라지면 반응 함수가 달라질 수 있습니다.

다만 이 말이
맥락마다 완전히 따로 문제를 풀어야 한다는 뜻은 아닙니다.

비슷한 맥락끼리는 정보를 공유할 수 있습니다.

오늘은 맥락을 반영한 BO의 모델링 디테일로 들어가지 않겠습니다.

목표는 이 감각만 남기는 것입니다.

BO는 목적함수 하나만 보는 문제에서 시작하지만,
제약조건과 맥락이 있는 실무 문제로도 넓어질 수 있습니다.

Transition:

이제 CRM 밖으로 시야를 넓히겠습니다.

## Scene 21. CRM을 넘어서

Section: `05 EXTEND`

Target time: 1:30

On screen:

```text
비용이 큰 모든 블랙박스 실험
```

Visual:

- Small examples around one central formula `x -> f(x)`:
  `하이퍼파라미터`, `가격`, `쿠폰 정책`, `예산 배분`, `메시징`.

Script:

CRM은 오늘의 예제일 뿐입니다.

이 구조는 훨씬 넓습니다.

이미 ML/DL 하이퍼파라미터 튜닝에서는
베이지안 최적화가 기본적으로 사용할 만한
블랙박스 최적화 프레임워크로 자리 잡았습니다.

거기서 `x`는 학습률이나 배치 크기일 수 있습니다.
`f(x)`는 검증 점수일 수 있습니다.

하지만 꼭 모델 학습일 필요는 없습니다.

가격 정책도 될 수 있고,
쿠폰 정책도 될 수 있고,
메시징 빈도나 예산 배분도 될 수 있습니다.

중요한 것은 대상이 무엇이냐가 아닙니다.

문제가 `x -> f(x)` 형태인지,
한 번 평가하는 데 비용이 큰지,
모든 후보를 다 실험할 수 없는지입니다.

그렇다면 베이지안 최적화를 떠올릴 수 있습니다.

Transition:

그럼 실제 구현은 얼마나 멀리 있을까요? 아주 짧게 구조만 보겠습니다.

## Scene 22. 구현 구조

Section: `05 EXTEND`

Target time: 0:55

On screen:

```text
Ax
BoTorch
```

Visual:

- 좌측에는 Ax 코드 스냅샷.
  Search space, objective, outcome constraint, next trial이 보이게 한다.
- 우측에는 BoTorch 코드 스냅샷.
  SingleTaskGP, marginal likelihood fitting, UCB acquisition, optimize_acqf가 보이게 한다.
- 파라미터, Gaussian Process, Gaussian Process modeling, Acquisition 부분은 서로 다른 색상으로 하이라이트한다.
- 코드는 전체를 읽히려는 목적이 아니라, 앞에서 배운 구조가 실제 코드 이름으로도 남아 있음을 보여주는 목적이다.

Script:

실제로 구현할 때도 구조는 크게 다르지 않습니다.

오늘은 코드를 읽는 장으로 만들지 않겠습니다.

대신 아주 작은 코드 스냅샷만 보겠습니다.

왼쪽은 Ax입니다.

Ax에서는 우리가 앞에서 말한 문제 정의를 높은 수준의 인터페이스로 적습니다.

Search space는 할인율과 발송 시점입니다.
objective는 profit입니다.
outcome constraint는 opt_out이 임계값을 넘지 않는다는 조건입니다.
그리고 get_next_trials를 호출하면 다음에 실험할 후보를 받습니다.

오른쪽은 BoTorch입니다.

여기로 내려가면 앞에서 본 구성요소가 조금 더 직접적으로 보입니다.

SingleTaskGP가 GP 모델입니다.
fit_gpytorch_mll이 데이터를 본 뒤 모델을 맞추는 부분입니다.
UpperConfidenceBound가 획득 함수입니다.
optimize_acqf가 그 획득 함수를 가장 크게 만드는 다음 후보를 찾는 부분입니다.

중요한 것은 라이브러리 이름이 아닙니다.

문제를 Search space, 목적함수, 제약조건으로 정확히 정의해야
최적화가 의미를 갖습니다.

Transition:

이제 마지막입니다. 오늘의 기여만 남기겠습니다.

## Scene 23. Contributions

Section: `06 CONTRIBUTIONS`

Target time: 1:30

On screen:

```text
Contributions

1. A/B 테스트는 비교하고, BO는 다음 후보를 고릅니다.
2. 불확실성은 다음 실험을 고르는 정보입니다.
3. 실무 decision making은 제약 안에서 f(x)를 최대화하는 문제입니다.
```

Visual:

- 매우 간결하게 둔다.
- 원래의 `x -> f(x)` 구조를 다시 보여주고, `g(x) <= c`를 덧붙일 수 있다.
- 별도의 감사 슬라이드는 만들지 않는다.

Script:

오늘 이야기의 기여는 CRM 캠페인 하나가 아닙니다.

대부분의 실제 decision making은 결국
`f(x)`를 최대화하는 `x`를 찾는 일입니다.

가격을 얼마로 할지.
쿠폰을 얼마나 줄지.
언제 메시지를 보낼지.
예산을 어디에 배분할지.

그리고 복잡한 현실에서는
`g(x) <= c` 같은 제약이 붙는 경우도 많습니다.

비용,
리스크,
수신 거부,
마진,
운영 가능성.

모든 후보를 충분히 실험할 수 있다면
그냥 다 해보면 됩니다.

하지만 그렇지 않다면,
다음 후보를 어떻게 고를지가 중요해집니다.

그때 오늘 본 베이지안 최적화를 떠올려보시면 좋겠습니다.

오늘의 핵심 단어는 세 개입니다.

Search,
불확실성,
제약조건.

이 세 가지가 정의되면,
우리는 더 이상 후보를 감으로만 고르지 않고
다음 실험점을 Search할 수 있습니다.

마지막으로 한 문장만 남기겠습니다.

불확실성은 피해야 할 것이 아니라,
다음 실험을 고르는 정보입니다.

End:

여기서 멈춘다. 박수가 시작된 뒤에만 짧게 인사한다.

## Q&A Backup Prompts

These are not part of the timed main talk.

### A/B 테스트와 BO는 대체 관계인가요?

아닙니다. 역할이 다릅니다.

A/B 테스트는 후보를 평가하는 실험 설계입니다.
BO는 다음에 평가할 후보를 고르는 search strategy입니다.

실무에서는 BO가 후보를 제안하고,
그 후보는 여전히 좋은 A/B 테스트로 평가해야 합니다.

### BO가 표본 수 문제도 해결하나요?

아닙니다.

BO는 어떤 후보를 평가할지 줄이는 데 도움을 줍니다.
하지만 한 후보의 성과를 믿기 위한 표본 수와 실험 품질 문제는 그대로 남습니다.

그래서 BO는 좋은 실험 설계를 대체하지 않습니다.
좋은 실험 설계 위에서 다음 후보를 더 정보적으로 선택하는 방법입니다.

### 왜 수신 거부를 제약조건으로 두나요?

CRM에서는 단기 성과가 높아도 고객이 알림을 끄거나 수신을 거부하면
장기적으로 운영 가능한 정책이 아닐 수 있습니다.

수신 거부는 우리가 직접 정하는 입력값이 아니라,
정책을 실행했을 때 관측되는 고객 반응입니다.
그래서 `g(x)`라는 별도의 블랙박스 함수로 볼 수 있습니다.

### 맥락은 왜 넣나요?

같은 정책이라도 상품 가격대와 고객 구매 이력에 따라 반응이 달라질 수 있습니다.

다만 맥락별로 완전히 별도 문제를 풀자는 뜻은 아닙니다.
비슷한 맥락끼리는 정보를 공유할 수 있고,
BO는 그런 방향으로도 넓어질 수 있습니다.

### 왜 hyperparameter tuning 이야기를 후반에 넣나요?

이 발표의 중심은 ML 모델 튜닝이 아니라 실무 decision making입니다.

다만 BO가 낯선 도구가 아니라,
이미 하이퍼파라미터 튜닝에서 검증된 블랙박스 최적화 프레임워크라는 점을
후반에 연결하기 위해 짧게 언급합니다.
