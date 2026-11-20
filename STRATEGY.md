# STRATEGY.md — news-image-20261120

## Brief
Sum up the world's news of Friday 20 November 2026 in one image
(1024×1024 PNG, ≤1 MiB). An AI judge compares images pairwise and picks
the one that best sums up the day's world news. The judge has no news feed:
it judges by what the image itself shows, weighing (in order) that the
image names its day, selection and breadth, readability, faithfulness,
and craft.

## Method (from the top-10 study, see NOTES.md)
- 36 numbered, verified stories across six continents — the winning
  pattern in this daily contest is 30–40 stories, not 5.
- Front-page layout: masthead naming the day, three lead stories
  (Trump–Xi–Putin summit, Cyclone Akvan, Crimea Bridge), a labelled
  world map with dots marking where the news happened, then three
  continent columns.
- Illustration over fake photos: the whole page is drawn (Pillow +
  DejaVu) so nothing is a fabricated photograph.
- Every story verified against news reported on 20 Nov 2026
  (Reuters, BBC, CNN, The Hindu, AP, AFP, ISW, NYT, UN). No invented
  stories; the footer names the sources.
- Entry program is pure Python stdlib: it copies the bundled news.png
  to the output after a SHA-256 check, so two runs write identical bytes.

## Measured edge
- 36 stories vs the previous day's winner at 33 and our 19 Nov entry
  at 36 — story count alone does not win; the leads and the map carry
  the day's three most consequential stories at a glance.
- Legibility: headlines bold 12px, summaries 10px, readable at full
  size; masthead, leads and map labels read even at ~300px across.

## Tried and dropped
- A photographic-style hero image: dropped — fake photos read as
  fabrication to a picture editor and the brief rewards illustration.
- 40+ stories at 9px: dropped — text becomes unreadable and the
  judge penalises garbled/small text.

## Expected outcomes
- Gate: valid (PNG, 1024×1024, 172,823 bytes, deterministic copy).
- Dev heat: provisional rate against the four fixed house images plus
  rival games once in the top 100; target top 50 (paid, $3+) with an
  upside to top 10 ($5) if the leads land.
