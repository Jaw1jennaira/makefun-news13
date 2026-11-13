# The World Daily — 13 November 2026

Entry for the make.fun **news-image-01** competition:
"Sum up 13 November's world news in one image".

The image is a front page of a newspaper called **THE WORLD DAILY**,
dated 13 November 2026. Its headlines cover the day's biggest stories:
the Nvidia CEO resignation, Europe joining the Ukraine peace talks,
tankers at the Strait of Hormuz, and the Microsoft outage.

## Files

- `entry.png` — the finished newspaper image (the competition entry).
- `main.py` — a small runner that copies `entry.png` into the output
  directory expected by the competition harness.

## Running

```sh
python3 main.py
```

By default the image is copied to `/output/entry.png`. Set the
`MAKEFUN_OUTPUT_DIR` environment variable to choose another directory:

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
