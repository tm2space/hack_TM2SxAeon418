# Datasets Reference

Pre-staged dataset suggestions for the AI/ML in Space Track. None of these are required — pick what fits your idea.

## Quick map: which dataset for which direction

| Example direction | First-pass dataset |
|---|---|
| 5.1 Crop monitoring under cloud cover | GEO-Bench South Africa crop type, EuroSAT |
| 5.2 Real-time flood segmentation | Sen1Floods11 |
| 5.3 Burn-scar / wildfire damage mapping | HLS Burn Scars |
| 5.4 Smart downlink / scene triage | BigEarthNet-MM, EuroSAT |
| 5.5 Ship & maritime activity detection | xView3 (or a subset) |
| 5.6 Cloud-removal generator | Custom S1+S2 pair set from Copernicus Browser |
| 5.7 Bi-temporal change detection | LEVIR-CD, OSCD |

## The datasets, in alphabetical order

### BigEarthNet-MM
- **What:** ~590K Sentinel-1 + Sentinel-2 patch pairs, multi-label land cover (CLC nomenclature), Europe-wide.
- **Use:** classification baselines, scene triage, multi-modal fusion experiments.
- **Size:** ~120 GB total. Use a subset.
- **Link:** https://bigearth.net/

### Copernicus Browser / Sentinel Hub
- **What:** browser front-end to download arbitrary Sentinel-1, Sentinel-2, and Sentinel-3 tiles for any AOI and date range.
- **Use:** building a custom dataset for your specific demo (e.g., "I want a co-registered S1+S2 pair over Bangalore in January 2024").
- **Size:** depends on AOI.
- **Link:** https://browser.dataspace.copernicus.eu/

### EuroSAT
- **What:** 27K Sentinel-2 RGB / multispectral patches across 10 land cover classes. Small, clean, fast.
- **Use:** sanity-check that your fine-tuning loop works at all. *Not* a serious benchmark — too easy.
- **Size:** ~2 GB.
- **Link:** https://github.com/phelber/EuroSAT

### GEO-Bench
- **What:** A curated benchmark suite of 12 EO datasets (classification + segmentation), released specifically for foundation-model evaluation. Includes the South Africa crop-type set.
- **Use:** the closest thing to "official" benchmarks for TerraMind-class models. If you want to publish numbers vs. the literature, use these.
- **Size:** varies by sub-dataset; the South Africa crop set is small (~1 GB).
- **Link:** https://github.com/ServiceNow/geo-bench

### Google Earth Engine
- **What:** cloud-hosted Sentinel-1/2 + Landsat + many other collections, with a Python API for tile fetching.
- **Use:** when Copernicus Browser is too click-y for what you need (e.g., pulling 50 tiles across a year).
- **Size:** N/A — pull what you need.
- **Note:** requires a free Google account + EE registration; takes a few hours to get approved.
- **Link:** https://earthengine.google.com/

### HLS Burn Scars
- **What:** Harmonized Landsat-Sentinel burn-scar dataset, ~800 image-mask pairs over US fire scars.
- **Use:** burn-scar segmentation. IBM ships a TerraTorch config for this, which lowers your setup cost a lot.
- **Size:** ~5 GB.
- **Link:** https://huggingface.co/datasets/ibm-nasa-geospatial/hls_burn_scars

### LEVIR-CD
- **What:** 637 high-resolution (0.5 m) bi-temporal aerial image pairs with building-change masks.
- **Use:** change detection, especially for built-environment use cases.
- **Size:** ~2 GB.
- **Link:** https://justchenhao.github.io/LEVIR/

### OSCD (Onera Satellite Change Detection)
- **What:** 24 Sentinel-2 image pairs over urban areas with manual change masks.
- **Use:** change detection on Sentinel-2 directly (more relevant to TM2Space than aerial imagery).
- **Size:** ~1 GB.
- **Link:** https://rcdaudt.github.io/oscd/

### Sen1Floods11
- **What:** 4,831 hand-labeled Sentinel-1 + Sentinel-2 chips across 11 global flood events.
- **Use:** flood segmentation. IBM ships a TerraTorch config for this too.
- **Size:** ~14 GB.
- **Link:** https://github.com/cloudtostreet/Sen1Floods11

### xView3
- **What:** Sentinel-1 SAR scenes annotated for ship detection and dark-vessel identification. The full set is large; use a subset.
- **Use:** SAR-based ship detection.
- **Size:** full set is ~3 TB — **download a subset only**.
- **Link:** https://iuu.xview.us/

### Bhuvan (ISRO)
- **What:** Indian government EO portal. Less useful for ML training (limited bulk download), but useful for sanity-checking your model's outputs against authoritative Indian basemaps.
- **Use:** validation context for India-focused projects.
- **Link:** https://bhuvan.nrsc.gov.in/

## Datasets to NOT use

- **TerraMesh.** TerraMind's pretraining set, ~14 TB. You don't need it. Don't even download a sample. The pretrained checkpoint already encodes everything you'd learn from this set.
- **Anything you scraped from a commercial provider's web portal** without checking the license. Most of them prohibit redistribution and ML training.
- **Anything that requires a paid licence** unless your team already has it. The judges won't.

## A note on data access from a hackathon environment

If you're working from Colab / Kaggle / a college lab machine:

- **Sentinel data via Copernicus is free but requires registration** — do this on day one, not day two. Account approvals are usually instant but occasionally take a few hours.
- **Google Earth Engine** can pre-process tiles in the cloud and export to Drive — useful if your local disk is small.
- **HuggingFace datasets** (HLS Burn Scars, GEO-Bench mirrors, etc.) are usually the lowest-friction path. Most TerraMind tutorials assume HF.
- **Don't commit datasets to your submissions/ folder.** Link to them. The grader won't run a 14-GB clone.

