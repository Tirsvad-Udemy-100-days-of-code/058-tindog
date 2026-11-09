**English** · [Dansk](Lecture-2-Bootstrap-Components-da) · [Bahasa Malaysia](Lecture-2-Bootstrap-Components-ms)

# Lecture step 2: Bootstrap components

![Screenshot of the Move It page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/raw/branch/main/docs/images/lecture-2-bootstrap-components.png)

## What this step shows

A one-page website for a fictional start-up, Move It, built from Bootstrap components: a navbar with a dropdown and a search form, a hero, a features section with cards, a carousel and a footer.

## What we gained

- **Components save most of the work.** The navbar, cards, carousel and footer come from the documentation and only the text and colours change.
- **Some components need the JavaScript bundle.** The dropdown, the collapsing navbar and the carousel work because `bootstrap.bundle.min.js` is loaded at the end of the page.
- **Containers give a consistent layout.** `container` centres the content and sets a maximum width on every section.
- **Utility classes replace small CSS rules.** `py-5`, `mb-4`, `text-center` and `g-4` handle spacing and alignment.
- **Dark mode is one attribute.** Setting `data-bs-theme="dark"` on the `html` element switches the whole page; the "Dark mode" button in the navbar does this.
- **Themes exist.** Free and paid Bootstrap themes can be a starting point, and custom themes can be sold.

## Where to find it

| What | Where |
| --- | --- |
| The page | `src/tindog/site/lecture-2-bootstrap-components/index.html` |
| Address when served | `http://127.0.0.1:8058/lecture-2-bootstrap-components/index.html` |

Previous: [Lecture step 1](Lecture-1-Bootstrap-Introduction). Next: [Lecture step 3](Lecture-3-TinDog-Landing-Page).
