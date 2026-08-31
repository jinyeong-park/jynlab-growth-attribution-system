# Campaign context and keyword strategy

## Product

FirstHomeBayArea helps first-time Bay Area buyers evaluate condos — HOA financial health, true monthly cost including fees, comparable sales — instead of just aggregating listings like Zillow or Redfin. The core product primitive is an affordability calculator, and a secondary primitive ("My Price") lets a buyer record what they'd actually pay for a property versus its asking price.

Initial market: San Jose condos. Initial customer: someone seriously considering a purchase within ~12 months, not a casual browser. That last distinction matters for keyword selection below — I'm optimizing for buying intent, not real-estate curiosity.

## Primary conversion

**"Email My Results" request** — the user completes the affordability calculator and asks to have their result emailed. Not calculator-started, not a click. See [`attribution/README.md`](../attribution/README.md) for why that distinction is the whole point of this project.

## Keyword themes

I split targeting into three intent themes rather than one broad campaign, so I can compare cost-per-conversion across them and decide what to scale (see [`segmentation/`](../segmentation/)).

### Theme A — Calculation intent (highest priority)
Buyer is actively trying to answer "can I afford this."
- `how much condo can i afford san jose`
- `san jose home affordability calculator`
- `condo affordability calculator bay area`

### Theme B — Ownership-cost research intent
Buyer is past browsing and is digging into what condo ownership actually costs — HOA-specific research is a strong purchase-intent signal.
- `san jose condo hoa fees`
- `condo special assessment san jose`
- `hidden costs of buying a condo`

### Theme C — Broad buyer intent
Wider net, first-time-buyer language, more competitive and more likely to include lower-intent traffic — this theme is the control group for judging whether narrower intent (A/B) actually converts better per dollar.
- `first time home buyer san jose`
- `first time home buyer condo bay area`

## Negative keywords

Excluding rental and non-purchase intent so budget doesn't leak to the wrong searcher: `rent`, `apartment for rent`, `for rent near me`, `real estate agent jobs`, `real estate license`.

## Ad copy

[TODO — fill in once first two ad copy variants are written and approved. Each ad group gets 2 headlines/description sets so Theme performance isn't confounded by copy quality.]

## Budget and timeline

$[TODO] over [TODO] weeks, split evenly across the three themes for the first two weeks so I get a fair read before reallocating toward whichever theme has the lowest cost-per-"Email My Results."
