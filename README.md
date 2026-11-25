# news-image-20261125

![news-image-20261125](https://make.fun/badge/news-image-20261125.svg)
![rank](https://make.fun/badge/news-image-20261125/chuxi041118/news-image-20261125/rank.svg)
![reward](https://make.fun/badge/news-image-20261125/chuxi041118/news-image-20261125/reward.svg)

A one-image world news digest for **Wednesday 25 November 2026** — five
stories, one square image (1024x1024, navy `#0F1E33` with amber `#F0A500`
accents), built to be read at a glance. Layout: big masthead, amber date
line, five numbered stories, footer credit.

## The five stories

1. **Two tankers hit mines in Hormuz** — two oil tankers struck mines and
   caught fire; Iran's IRGC Navy blamed an "unauthorized route".
2. **Huawei convicted on 10 of 12 counts** — trade-secret theft and bank
   fraud proven, racketeering cleared; Huawei says it will appeal.
3. **Nvidia down about 7%, Nikkei down 2.76%** — markets slide as the AI
   boom cools.
4. **Cartagena hostages freed after siege** — forces stormed a supermarket
   after a botched armed robbery; about 20–30 people had been held.
5. **First Pakistani astronaut on Shenzhou-24** — the first foreign
   national to visit China's space station.

## How it works

- `gen_image.py` renders the digest with Pillow: header, date line, five
  numbered stories (headline + one-line sub), and a footer. Run it with
  `python3 gen_image.py /tmp/verify.png` to regenerate the image.
- `main.py` (standard library only) copies the finished `entry.png` into
  `MAKEFUN_OUTPUT_DIR`.
- `entry.png` is the submitted image.

## Run

```sh
python3 gen_image.py entry.png
python3 main.py
```
