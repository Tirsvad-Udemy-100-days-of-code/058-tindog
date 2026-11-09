[English](Lecture-3-TinDog-Landing-Page) · **Dansk** · [Bahasa Malaysia](Lecture-3-TinDog-Landing-Page-ms)

# Lektionstrin 3: TinDog-landingssiden

![Skærmbillede af TinDog-landingssiden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/raw/branch/main/docs/images/lecture-3-tindog.png)

## Hvad trinnet viser

TinDog er en opdigtet startup, der hjælper hunde med at finde venner. Siden har en titelsektion med en farveovergang, funktioner, en udtalelse, en presserække, tre prisplaner, en opfordring til handling og en sidefod.

## Hvad vi fik ud af det

- **Sektioner gør filen læsbar.** Hver del er en `section` med et id (`title`, `features`, `testimonial`, `press`, `pricing`, `cta`), som startfilen i lektionen foreslår.
- **Rutenettet gør siden responsiv.** `col-lg-4` stiller tre funktioner side om side på en computer og stabler dem på en telefon; pressens logoer bruger `col-12 col-lg-3`.
- **Bootstrap og lidt CSS arbejder sammen.** Farveovergangene, den store overskrift og den drejede telefon er få regler i `css/styles.css`; alt andet er Bootstrap-klasser.
- **Knapper og kort findes i varianter.** `btn-light`, `btn-outline-light`, `btn-dark` og `btn-outline-dark` giver download- og priseknapperne deres udseende; det mørke Mastiff-kort bruger `bg-dark text-white`.
- **SVG-ikoner er små og skarpe.** Apple-, Google Play- og funktionsikonerne er indlejret SVG fra Bootstrap Icons (MIT-licens).
- **Egne billeder holder repositoryet rent.** Telefonen, hundens avatar og pressens navne er tegnet som egne SVG-filer, så ingen fil fra kursets download udgives.
- **Rutenet kontra Flexbox og CSS Grid.** Bootstrap er den hurtigste vej til en flot side; til et meget særligt layout giver CSS Grid og Flexbox mere kontrol.

## Hvor finder du det

| Hvad | Hvor |
| --- | --- |
| Siden | `src/tindog/site/lecture-3-tindog/index.html` |
| Ekstra CSS og billeder | `src/tindog/site/lecture-3-tindog/css/` og `images/` |
| Adresse når den serveres | `http://127.0.0.1:8058/lecture-3-tindog/index.html` |

Forrige: [Lektionstrin 2](Lecture-2-Bootstrap-Components-da).
