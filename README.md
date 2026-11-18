# tiny-chess-01-g5

[![make.fun](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/competitions/tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/raffa-sys/tiny-chess-01-g5/rank.svg)](https://make.fun/competitions/tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/raffa-sys/tiny-chess-01-g5/reward.svg)](https://make.fun/competitions/tiny-chess-01)

**tiny-chess-01-g5** is a fresh-architecture chess engine for the
make.fun tiny-chess-01 bounty: a single `main.py` (4,074 bytes, Python
3.13 standard library only) that plays through the competition env.

Original 0x88 board, written from scratch — no Sunfish code. In-place
make/unmake with an undo stack, negamax alpha-beta with iterative
deepening, MVV-LVA ordering, killer moves, check extension, mate-distance
scoring, capture-only quiescence, and a fixed 200k-node budget per move
(not per iteration), which buys effective depth 5 in the middlegame.
Evaluation is material plus centrality piece-square tables and pawn
advancement. Promotions are queen-only. The driver POSTs `/game` and
`/move` itself.

Local practice trials (8 games each, floor Elo 1,154): Set A 989,
Set B **1,253**, Set C **1,253** — average 1,165. Perft verified on
startpos, kiwipete and the EP positions. Think time about 5 s per move
locally, under the 10 s limit.

## License

MIT — see `LICENSE`.
