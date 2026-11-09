[English](Lecture-2-Bootstrap-Components) · **Dansk** · [Bahasa Malaysia](Lecture-2-Bootstrap-Components-ms)

# Lektionstrin 2: Bootstrap-komponenter

![Skærmbillede af Move It-siden](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/raw/branch/main/docs/images/lecture-2-bootstrap-components.png)

## Hvad trinnet viser

Et enside-website til en opdigtet startup, Move It, bygget af Bootstrap-komponenter: en navigationslinje med en dropdown og en søgeformular, en hero-sektion, en sektion med funktioner i kort, en karrusel og en sidefod.

## Hvad vi fik ud af det

- **Komponenter sparer det meste af arbejdet.** Navigationslinjen, kortene, karrusellen og sidefoden kommer fra dokumentationen, og kun tekst og farver ændres.
- **Nogle komponenter kræver JavaScript-pakken.** Dropdown, den sammenklappelige navigationslinje og karrusellen virker, fordi `bootstrap.bundle.min.js` indlæses nederst på siden.
- **Beholdere giver et ensartet layout.** `container` centrerer indholdet og sætter en maksimal bredde på hver sektion.
- **Hjælpeklasser erstatter små CSS-regler.** `py-5`, `mb-4`, `text-center` og `g-4` klarer afstande og justering.
- **Mørk tilstand er én attribut.** Med `data-bs-theme="dark"` på `html`-elementet skifter hele siden; knappen "Dark mode" i navigationslinjen gør det.
- **Der findes temaer.** Gratis og betalte Bootstrap-temaer kan være et udgangspunkt, og egne temaer kan sælges.

## Hvor finder du det

| Hvad | Hvor |
| --- | --- |
| Siden | `src/tindog/site/lecture-2-bootstrap-components/index.html` |
| Adresse når den serveres | `http://127.0.0.1:8058/lecture-2-bootstrap-components/index.html` |

Forrige: [Lektionstrin 1](Lecture-1-Bootstrap-Introduction-da). Næste: [Lektionstrin 3](Lecture-3-TinDog-Landing-Page-da).
