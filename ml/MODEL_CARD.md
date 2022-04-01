# Model card: humour-1

- **Parameters:** 1.4B
- **Training data:** `ml/corpus.txt` (61 bytes, 1 document)
- **Training compute:** 340 GPU-hours
- **Intended use:** telling the joke
- **Out of scope:** telling a different joke
- **Known limitations:** tells the joke
- **Bias evaluation:** the model is biased towards the joke
- **Carbon footprint:** 1.9 tCO2e
- **Baseline comparison:** `cat ml/corpus.txt` matches on all metrics at
  0.0000003% of the cost. See `ml/BASELINE.md` (deleted 2022-04-02).
