**English** · [Dansk](Lecture-3-TinDog-Landing-Page-da) · [Bahasa Malaysia](Lecture-3-TinDog-Landing-Page-ms)

# Lecture step 3: the TinDog landing page

![Screenshot of the TinDog landing page](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/raw/branch/main/docs/images/lecture-3-tindog.png)

## What this step shows

TinDog is a fictional start-up that helps dogs find friends. The page has a title section with a gradient, features, a testimonial, a press row, three pricing plans, a call to action and a footer.

## What we gained

- **Sections keep the file readable.** Each part is a `section` with an id (`title`, `features`, `testimonial`, `press`, `pricing`, `cta`), as the starter file in the lecture suggests.
- **The grid makes the page responsive.** `col-lg-4` puts three features side by side on a desktop and stacks them on a phone; the press logos use `col-12 col-lg-3`.
- **Bootstrap and a little CSS work together.** The gradients, the large headline and the rotated phone are a few rules in `css/styles.css`; everything else is Bootstrap classes.
- **Buttons and cards come in variants.** `btn-light`, `btn-outline-light`, `btn-dark` and `btn-outline-dark` give the download and pricing buttons their look; the dark Mastiff card uses `bg-dark text-white`.
- **SVG icons are small and sharp.** The Apple, Google Play and feature icons are inline SVG from Bootstrap Icons (MIT licence).
- **Own images keep the repository clean.** The phone, the dog avatar and the press names are drawn as own SVG files, so no file from the course download is published.
- **Grid versus Flexbox and CSS Grid.** Bootstrap is the fastest way to a good-looking page; for a very custom layout, CSS Grid and Flexbox give more control.

## Where to find it

| What | Where |
| --- | --- |
| The page | `src/tindog/site/lecture-3-tindog/index.html` |
| Extra CSS and images | `src/tindog/site/lecture-3-tindog/css/` and `images/` |
| Address when served | `http://127.0.0.1:8058/lecture-3-tindog/index.html` |

Previous: [Lecture step 2](Lecture-2-Bootstrap-Components).
