**English** · [Dansk](Lecture-1-Bootstrap-Introduction-da) · [Bahasa Malaysia](Lecture-1-Bootstrap-Introduction-ms)

# Lecture step 1: Bootstrap introduction

![Screenshot of the Bootstrap introduction page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/raw/branch/main/docs/images/lecture-1-bootstrap-introduction.png)

## What this step shows

The page explains Bootstrap with Bootstrap itself: coloured buttons, a card and a demonstration of the 12-column grid.

## What we gained

- **Bootstrap is a set of ready-made CSS classes.** It was created at Twitter by Mark Otto and Jacob Thornton in 2010. Adding classes such as `btn btn-success` styles a plain element without writing CSS.
- **One CDN link is enough to start.** The stylesheet and the script bundle are loaded from a CDN; the project pins version 5.3.3 and checks the files with integrity hashes.
- **The grid has 12 columns and is mobile first.** `col-md-4` means four of twelve columns from the medium breakpoint upwards, and full width below it.
- **Components are copied and adjusted.** The card is taken from the documentation and changed to fit.
- **Trade-offs.** Bootstrap is fast, consistent and works in all common browsers, but elements collect many classes and heavy customisation is harder.

## Where to find it

| What | Where |
| --- | --- |
| The page | `src/tindog/site/lecture-1-bootstrap-introduction/index.html` |
| Address when served | `http://127.0.0.1:8058/lecture-1-bootstrap-introduction/index.html` |

Next: [Lecture step 2](Lecture-2-Bootstrap-Components).
