# <Team Name> — <Project Title>

> Replace this template with your own writeup. Keep it ≤ 2 pages.
> Delete every italicised instruction line before submitting.

*Tip: a judge reads dozens of these. Be specific. Be honest. Cut the fluff.*

---

## 1. What problem are you solving?

*One paragraph. Who's the customer? Why would they pay? What does success look like for them?*

*Bad: "We segment floods using AI."*
*Good: "An NDMA flood-response coordinator in Assam needs a binary flood mask + affected-area-in-km² number within 6 hours of an event. Today they wait 24–48 hours for manual analyst review of Sentinel-1 tiles. Our system collapses that to minutes."*

## 2. What did you build?

*One paragraph. Architecture, dataset, fine-tuning recipe.*

- **Base model:** TerraMind-1.0-small (or whatever you used)
- **Dataset:** Sen1Floods11 (or whatever you used)
- **Fine-tuning:** *e.g., frozen encoder, fine-tuned segmentation head, 10 epochs, AdamW, lr=1e-4*
- **Training compute:** *e.g., Colab T4, 45 min total*
- **Why TerraMind specifically?** *e.g., we used TiM mode to synthesize NDVI, which gave +2.4 mIoU vs. the same head without TiM.*

## 3. How did you measure it?

*Numbers vs. a baseline. Even a weak baseline counts. Examples: a published number on the same dataset, a trivial classifier, a UNet trained on the same data without TerraMind, the previous-tile baseline.*

| Method | Metric | Value |
|---|---|---|
| Baseline (e.g., random-init UNet, same data) | mIoU | 0.62 |
| **Ours (TerraMind-small + head)** | **mIoU** | **0.81** |
| Ours + TiM (NDVI-augmented) | mIoU | 0.84 |

*Note any caveats: "Evaluated on the held-out Sen1Floods11 test split, n=89 chips."*

## 4. What's the orbital-compute story?

*How does this fit on a satellite? Be specific.*

- **Model size on disk (FP16):** *e.g., 215 MB*
- **Inference latency per tile:** *e.g., 1.4 s/tile on a T4 GPU; we estimate ~3–4 s on Jetson Orin Nano based on a TOPS comparison*
- **Memory ceiling:** *e.g., < 2 GB peak VRAM at batch 1*
- **Bandwidth saved:** *e.g., one full Sentinel-1 GRD scene is ~1 GB; our flood mask output is ~5 KB. ~99.9% bandwidth saved per scene.*
- **Honest feasibility verdict:** *e.g., "Comfortably fits on the upcoming TM2Space Jetson payload at FP16. Quantization to INT8 would give us another 2–3× headroom but we didn't measure it."*

## 5. What doesn't work yet?

*The most useful section. Be honest.*

- *Limitation 1 (e.g., "Trained only on flooding events from 2017–2019; performance on a 2024 Pakistan flood test tile drops to 0.71 mIoU.")*
- *Limitation 2 (e.g., "Fails on urban floods — training data is mostly agricultural.")*
- *What you'd build with another week (e.g., "Active-learning loop with NDMA analysts to incorporate Indian flood events.")*

---

## How to run this

```bash
pip install -r requirements.txt
python infer.py --input sample_input/sample_tile.tif --output out_mask.tif
```

*Replace with your actual command. The judge should be able to run this in under 10 minutes on a Colab GPU.*

## Repo contents

```
.
├── README.md           # this file
├── requirements.txt    # pinned deps
├── infer.py            # demo entry point
├── train.py            # how we fine-tuned (optional but nice)
├── configs/            # TerraTorch configs we used
├── notebooks/          # exploration + eval
├── sample_input/       # ≤ 10 MB demo input
└── slides.pdf          # our 5-min presentation
```

## Team

- *Name 1 — role*
- *Name 2 — role*

## Acknowledgements

*Datasets, tutorials, prior art you built on. Be specific. (Generic "thanks to IBM" doesn't help judges; "we adapted IBM's Sen1Floods11 TerraTorch config from <link>" does.)*
