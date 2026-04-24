# AI/ML in Space Track — Teams' Starter Kit

Setup walkthrough for getting TerraMind running on Colab / Kaggle / a local GPU box, plus the gotchas that will eat your day if you don't know about them.

> Unlike the Lost in Space track, this kit is **not** a local scorer. There is no automated grader for an open-ended challenge. This kit just gets you to "TerraMind loaded, dataset accessible, fine-tuning loop runs" as fast as possible — what you build from there is up to you.

## What you submit to the organizers

A folder under `submissions/<your_team_name>/` containing:

1. Your code (notebooks, scripts, configs)
2. A `README.md` writeup (≤ 2 pages)
3. A presentation (5 min, slides + demo)

Full spec: [`SUBMITTING.md`](../SUBMITTING.md).

## Quick start

```bash
# 1. Clone this repo and move into the starter kit
git clone <this-repo>
cd <repo>/teams_kit/

# 2. Install pinned dependencies
pip install -r requirements.txt

# 3. Verify TerraMind loads (this downloads ~500 MB)
python -c "from terratorch.models import TerraMindModel; \
  m = TerraMindModel.from_pretrained('ibm-esa-geospatial/TerraMind-1.0-small'); \
  print('OK, params:', sum(p.numel() for p in m.parameters())/1e6, 'M')"

# 4. Copy the example submission folder as your starting point
cp -r example_submissions/_template ../submissions/<your_team_name>/
```

If the third command prints a parameter count, you're set. If it crashes, see [Troubleshooting](#troubleshooting) below.

## Recommended environments

| Environment | Verdict |
|---|---|
| **Colab Pro (T4 / A100)** | Recommended. Most TerraMind tutorials assume Colab. T4 is enough for `tiny` / `small`. |
| **Kaggle (T4 ×2 / P100)** | Works. 30 hrs/week GPU quota — keep an eye on it. |
| **Local GPU (RTX 30/40-series, ≥ 12 GB VRAM)** | Best for iteration speed if you have it. |
| **Local CPU only** | Don't. Even tiny variants are too slow for fine-tuning. Use it for validation/inference only. |
| **Apple Silicon (MPS)** | Works for inference. **Fine-tuning has known UNetDecoder issues on MPS** — see [Troubleshooting](#troubleshooting). |

## Which TerraMind variant to use

| Variant | Params | When to use |
|---|---|---|
| **tiny**  | ~10 M  | Sanity-check your fine-tuning loop. Underpowered for most downstream tasks but trains in minutes. |
| **small** | ~100 M | **Default.** Best size/quality trade-off for a 48-hour build. Fits on Colab T4. |
| **base**  | ~300 M | Use if you have an A100 and want to push numbers. Will not fit on Colab free tier. |
| **large** | ~600 M | Don't. You don't have time. |

Default to `small` unless you have a specific reason. Almost all of the official IBM tutorials use `small`.

## What's in this folder

```
teams_kit/
├── README.md                        # you are here
├── requirements.txt                 # pinned versions — DO use these exact pins
└── example_submissions/
    ├── _template/                   # empty submission scaffold — copy this
    │   ├── README.md                # writeup template (the 5 questions)
    │   ├── requirements.txt         # your project's pins
    │   └── infer.py                 # placeholder entry point
    └── README.md                    # what each example is for
```

## Working starter notebooks (use IBM's, don't reinvent)

We deliberately don't ship a fine-tuning notebook in this repo, because IBM already publishes notebooks that work and are kept up to date. Use these as your starting point:

- **[TerraMind GitHub — official notebooks](https://github.com/IBM/terramind)** — has working examples for fine-tuning on Sen1Floods11, HLS Burn Scars, and a TiM showcase on the South Africa crop dataset. Read these before writing your own training loop.
- **[TerraTorch quickstart](https://github.com/IBM/terratorch)** — the underlying fine-tuning toolkit. Most TerraMind training is done by writing a TerraTorch YAML config and running `terratorch fit`.
- **[IBM Research blog post](https://research.ibm.com/blog/terramind-esa-earth-observation-model)** — the conceptual overview. Skim before coding.

If you want a starting point: clone IBM's notebook for the dataset closest to your idea, get it running end-to-end on a small subset, *then* start modifying. Trying to write the loop from scratch in 48 hours is a common way to lose 10 hours.

## Troubleshooting

### "ImportError: cannot import name X from terratorch"
You probably have an old TerraTorch. Pin to `>= 1.2.4`:
```bash
pip install "terratorch>=1.2.4" --upgrade
```

### "ImportError: cannot import ... from diffusers"
TerraMind's generative path uses a specific `diffusers` version. Pin to `0.30.0`:
```bash
pip install "diffusers==0.30.0"
```
Other versions break in interesting ways.

### "RuntimeError: MPS backend doesn't support ..." (Mac)
Known issue with the UNetDecoder on Apple Silicon. Two workarounds:
1. Switch to the FCN decoder in your config, *or*
2. Upgrade to TerraTorch ≥ 1.2.5 which has a partial MPS fix.

For fine-tuning specifically, you'll get much better mileage on Colab than on a Mac — borrow a Colab Pro subscription if you can.

### "OutOfMemoryError" on Colab T4
You're probably trying to use the `base` variant. Switch to `small`. If you're already on `small`, drop your batch size to 4 or use gradient accumulation.

### Model downloads are slow / failing
First-time download is ~500 MB for `small`. Mirror it to your Drive and load from there to avoid re-downloading on every Colab restart:
```python
from huggingface_hub import snapshot_download
snapshot_download(
    'ibm-esa-geospatial/TerraMind-1.0-small',
    local_dir='/content/drive/MyDrive/terramind-small',
)
```

### My fine-tuning loop runs but loss isn't going down
Three usual suspects:
1. Learning rate too high — TerraMind likes small LRs (`1e-5` to `1e-4`) for the encoder, larger for the head.
2. Encoder isn't frozen when it should be — for small datasets, freeze the encoder and only train the head first.
3. Dataset preprocessing doesn't match what TerraMind expects (band order, normalization, image size). Check IBM's notebook for the canonical preprocessing for your dataset.

### "I have 36 hours left and nothing works"
Cut scope. Pick the `small` variant, the smallest dataset that fits your idea, fine-tune *just the head* with the encoder frozen. A simpler thing that works beats an ambitious thing that doesn't.

## Compute budget tips

- Loading TerraMind-small fresh: ~30 sec on a T4
- One epoch of fine-tuning the head on Sen1Floods11 (small batch): ~5–10 min on a T4
- TiM-mode generation of one missing modality on a single tile: a few seconds on a T4

Plan your time accordingly. If you're doing TiM fine-tuning, expect roughly 2× the wall-clock time of vanilla fine-tuning — TiM adds an extra forward pass per step.

## Hardware reality-check for the rubric

The judging rubric has a 15% weight on **edge-inference feasibility** ([`JUDGING.md`](../docs/JUDGING.md)). You don't have to *prove* your model fits on a Jetson, but you should know roughly where you stand. Useful numbers:

- **Nvidia Jetson Orin Nano** (the class of compute on TM2Space's upcoming 6U): 8 GB shared RAM, ~40 TOPS INT8.
- **TerraMind-small** at FP16 inference: ~200 MB weights, runs comfortably in <2 GB RAM at batch 1.
- **TerraMind-base** at FP16: ~600 MB weights, fits but tighter.
- **A 17 km × 17 km Sentinel-2 tile** at 10 m/pixel is ~1700×1700 pixels — manageable, but for full inference you may want to tile it.

So if your project uses small + a small head, you're in good shape on feasibility. If you need base, mention quantization in your writeup. If you're doing real-time generation of full-resolution synthetic SAR tiles, be honest that it's an offline workload.

## Hard rules your submission must obey

- Single team folder under `submissions/<team_name>/`
- Pinned dependencies in `requirements.txt`
- Reproducible — a judge with your repo, your `requirements.txt`, and your README should be able to run inference
- TerraMind has to do real work (encoder, generator, TiM, fine-tuned head) — not a load-and-discard checkbox
- No keys, no large datasets in the folder, no weights > 200 MB

Full submission spec: [`../SUBMITTING.md`](../SUBMITTING.md).

Good luck.
