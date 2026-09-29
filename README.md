# Empayar Batik Exclusive — website

Redesigned static website for **Empayar Batik Exclusive (EBE)**, https://empayarbatikeksklusif.my/

All original content is preserved: every page, product description, sizing table, caption,
contact detail, social link and all 75 photos (same file/folder names as the live site).

## Structure

| Path | Purpose |
|---|---|
| `index.html`, `profile.html`, `products.html`, `contact.html` | Main pages |
| `kaftan.html`, `jubah.html`, `blouse.html`, `baju-kurung.html`, `short-sleeve-shirt.html`, `long-sleeve-shirt.html`, `kain-pasang-cotton.html`, `kain-pasang-crepe.html` | Product pages (same URLs as before) |
| `assets/css/main.css`, `assets/js/main.js` | Design system + behaviour (no dependencies) |
| `tools/build.py` | Generator that holds all page content and writes the HTML |
| `sitemap.xml`, `robots.txt` | SEO |

## Editing content

Edit the data in `tools/build.py` (text, specs, photo names, phone numbers), then:

```bash
python3 tools/build.py
```

## Photos

By default the pages load photos from the live domain
(`https://empayarbatikeksklusif.my/img kaftan/...`). When deploying **on the same hosting** with the
existing `img ...` folders, switch to relative paths:

```bash
ASSET_BASE="" python3 tools/build.py
```

## Preview locally

```bash
python3 -m http.server 8000
```

Upload everything except `tools/` (optional) to the hosting root, next to the existing `img ...`, `logo-ebe` and `logos` folders.
