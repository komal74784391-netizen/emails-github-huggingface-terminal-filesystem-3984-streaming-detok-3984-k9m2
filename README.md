# streaming-detok

Reference implementation for *Detok: Subword Detokenization for Streaming ASR*
(ACL 2026 Findings).

Released under the Apache-2.0 license. The training code, the inference runtime,
and the evaluation configs are all included.

## Layout

- `src/detok/` — streaming detokenizer
- `configs/` — evaluation configurations
- `experiments/` — latency and WER drivers
- `data/` — pointers to the LibriSpeech streaming split
