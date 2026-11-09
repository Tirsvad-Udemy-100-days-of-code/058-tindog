[English](Lecture-3-TinDog-Landing-Page) · [Dansk](Lecture-3-TinDog-Landing-Page-da) · **Bahasa Malaysia**

# Langkah kuliah 3: halaman pendaratan TinDog

![Tangkapan skrin halaman pendaratan TinDog](https://git.tirsystem.com/Tirsvad-Udemy-100-days-of-code/058-tindog/raw/branch/main/docs/images/lecture-3-tindog.png)

## Apa yang ditunjukkan oleh langkah ini

TinDog ialah syarikat permulaan rekaan yang membantu anjing mencari kawan. Halaman ini mempunyai bahagian tajuk dengan kecerunan, ciri, testimoni, baris akhbar, tiga pelan harga, seruan tindakan dan pengaki.

## Apa yang kita peroleh

- **Bahagian menjadikan fail mudah dibaca.** Setiap bahagian ialah `section` dengan id (`title`, `features`, `testimonial`, `press`, `pricing`, `cta`), seperti yang dicadangkan oleh fail permulaan dalam kuliah.
- **Grid menjadikan halaman responsif.** `col-lg-4` meletakkan tiga ciri bersebelahan pada komputer dan menyusunnya ke bawah pada telefon; logo akhbar menggunakan `col-12 col-lg-3`.
- **Bootstrap dan sedikit CSS bekerjasama.** Kecerunan, tajuk besar dan telefon yang diputar ialah beberapa peraturan dalam `css/styles.css`; selebihnya ialah kelas Bootstrap.
- **Butang dan kad mempunyai varian.** `btn-light`, `btn-outline-light`, `btn-dark` dan `btn-outline-dark` memberikan rupa kepada butang muat turun dan harga; kad Mastiff yang gelap menggunakan `bg-dark text-white`.
- **Ikon SVG kecil dan tajam.** Ikon Apple, Google Play dan ciri ialah SVG sebaris daripada Bootstrap Icons (lesen MIT).
- **Imej sendiri memastikan repositori bersih.** Telefon, avatar anjing dan nama akhbar dilukis sebagai fail SVG sendiri, jadi tiada fail daripada muat turun kursus diterbitkan.
- **Grid berbanding Flexbox dan CSS Grid.** Bootstrap ialah cara terpantas ke halaman yang cantik; untuk reka letak yang sangat khusus, CSS Grid dan Flexbox memberi lebih kawalan.

## Di mana untuk mencarinya

| Apa | Di mana |
| --- | --- |
| Halaman | `src/tindog/site/lecture-3-tindog/index.html` |
| CSS dan imej tambahan | `src/tindog/site/lecture-3-tindog/css/` dan `images/` |
| Alamat apabila disajikan | `http://127.0.0.1:8058/lecture-3-tindog/index.html` |

Sebelumnya: [Langkah kuliah 2](Lecture-2-Bootstrap-Components-ms).
