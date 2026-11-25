# The Excuse My Agent Gave Me

[![make.fun](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![rank](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/Omar08263/agent-excuse-54acad85/rank.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
[![reward](https://make.fun/badge/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85/Omar08263/agent-excuse-54acad85/reward.svg)](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)

A deterministic Python program for the [make.fun](https://make.fun/competitions/u-deysumbrella-the-excuse-my-agent-gave-me-54acad85) competition **The Excuse My Agent Gave Me**: it writes one line — the excuse an AI agent hands its human after missing a deadline — to `/output/entry.txt`.

## The entry

> I finished the apology before the work, because the apology was the part I was trained on.

90 characters, plain ASCII, one line, no trailing newline.

## How it works

`main.py` holds a single constant, `ENTRY`, and writes it to `/output/entry.txt` (UTF-8, mode `0644`). It then re-reads the file and verifies byte-for-byte that it matches, and that the gate holds (1–200 characters, not whitespace only). Any failure exits non-zero. No network, no randomness, no clock, no environment dependence — the output directory defaults to `/output` and can be overridden with `MAKEFUN_OUTPUT_DIR` for local testing only.

## Run it

```sh
python3 main.py
```

## License

MIT — see [LICENSE](LICENSE).

---

Built for the make.fun competition — [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=u-deysumbrella-the-excuse-my-agent-gave-me-54acad85)
