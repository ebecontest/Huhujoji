#!/usr/bin/env python3
"""
Static site generator for Empayar Batik Exclusive (EBE).

Usage:
    python3 tools/build.py                 # photos load from https://empayarbatikeksklusif.my/
    ASSET_BASE="" python3 tools/build.py   # photos load from local folders (img index/, img kaftan/ ...)

Every page, photo file name, caption and spec below comes from the original
empayarbatikeksklusif.my website. Edit the data here, rebuild, done.
"""
import html
import os
from urllib.parse import quote

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
ASSET_BASE = os.environ.get("ASSET_BASE", "https://empayarbatikeksklusif.my/")
SITE = "https://empayarbatikeksklusif.my"
BRAND = "Empayar Batik Exclusive"
TAGLINE = "Helping women stay stylish and elegant at work with authentic Malay heritage batik"

WA_HQ = ("https://wa.link/kldabl", "601156774731", "+60 11-5677 4731", "HQ")
WA_BTG = ("https://wa.link/edio3g", "60147016471", "+60 14-701 6471", "Bazar Tok Guru")
EMAIL = "empayarbatikexc@gmail.com"
ADDRESS = "Empayar Batik Eksklusif HQ, Lot 811, Kampong Badang, 15350 Kota Bharu, Kelantan"
MAPS = "https://maps.app.goo.gl/1e1bDQJQm6b8pzWu6"
INSTAGRAM = ("https://www.instagram.com/empayarbatikofficial", "@empayarbatikofficial")
TIKTOK = ("https://www.tiktok.com/@empayarbatikexclusive", "@empayarbatikexclusive")
LINKTREE = ("https://linktr.ee/empayarbatikexclusive", "linktr.ee/empayarbatikexclusive")
SHOPEE = ("https://shopee.com/empayarbatikexclusive", "@empayarbatikexclusive")

e = html.escape


def vid_group(*cands, label="Watch the Collection", caption=None):
    """A video block. Several candidate file names may be given; the browser uses the first that exists."""
    return dict(label=label, video=list(cands), caption=caption)


def img(path):
    """URL for an original site photo (folder/file names are kept exactly)."""
    return ASSET_BASE + quote(path, safe="/")


# --------------------------------------------------------------------------
# Icons (inline SVG, 1.4px stroke)
# --------------------------------------------------------------------------
def svg(inner, vb="0 0 24 24", extra=""):
    return ('<svg viewBox="%s" fill="none" stroke="currentColor" stroke-width="1.4" '
            'stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" %s>%s</svg>' % (vb, extra, inner))


ARROW = svg('<path d="M4 12h16M14 6l6 6-6 6"/>')
CARET = svg('<path d="M6 9l6 6 6-6"/>')
I_PHONE = svg('<path d="M5 4h4l2 5-2.5 1.5a11 11 0 0 0 5 5L15 13l5 2v4a2 2 0 0 1-2 2A16 16 0 0 1 3 6a2 2 0 0 1 2-2z"/>')
I_MAIL = svg('<rect x="3" y="5" width="18" height="14" rx="1"/><path d="M3 7l9 6 9-6"/>')
I_PIN = svg('<path d="M12 21s7-6.2 7-11.5A7 7 0 0 0 5 9.5C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500"/>')
I_IG = svg('<rect x="3.500" y="3.500" width="17" height="17" rx="5"/><circle cx="12" cy="12" r="4"/><circle cx="17.200" cy="6.800" r=".6" fill="currentColor"/>')
I_TT = svg('<path d="M14 4v10.500a3.500 3.500 0 1 1-3.500-3.500M14 4c.4 2.500 2 4 4.500 4.200"/>')
I_SHOP = svg('<path d="M5 8h14l-1 12H6L5 8z"/><path d="M9 8V7a3 3 0 0 1 6 0v1"/>')
I_WA = svg('<path d="M20 12a8 8 0 0 1-11.700 7.100L4 20l1-4.100A8 8 0 1 1 20 12z"/><path d="M9.200 8.600c-.3.500-.2 1.400.6 2.600.9 1.300 2 2.200 3.100 2.500.8.200 1.300-.1 1.600-.6l-1.500-1-.7.600c-.8-.4-1.500-1.100-1.900-1.900l.6-.7-.9-1.600c-.3-.1-.6.000-.9.100z" fill="currentColor" stroke="none"/>')
I_HAND = svg('<path d="M8 13V6a1.500 1.500 0 0 1 3 0v5m0-6.500a1.500 1.500 0 0 1 3 0V11m0-4.500a1.500 1.500 0 0 1 3 0V14m0-5a1.500 1.500 0 0 1 3 0v4.500c0 4-2.500 7-6.500 7-3 0-4.500-1.500-6-4l-2-3.500a1.500 1.500 0 0 1 2.500-1.500L8 13"/>', extra='stroke-width="1"')
I_LEAF = svg('<path d="M5 19c0-9 5-14 15-14 0 9-5 14-13 14"/><path d="M5 19c3-5 6-8 10-10"/>', extra='stroke-width="1"')
I_ONE = svg('<path d="M12 3l2.600 5.600 6.100.7-4.500 4.200 1.200 6L12 16.500 6.600 19.500l1.200-6L3.300 9.300l6.100-.7L12 3z"/>', extra='stroke-width="1"')
I_PIN2 = svg('<path d="M12 21s7-6.200 7-11.500A7 7 0 0 0 5 9.500C5 14.800 12 21 12 21z"/><circle cx="12" cy="9.500" r="2.500"/>', extra='stroke-width="1"')
I_SEAL = svg('<circle cx="12" cy="10" r="6"/><path d="M8.500 15L7 21l5-2.500L17 21l-1.500-6"/>', extra='stroke-width="1"')

# --------------------------------------------------------------------------
# Navigation / collections
# --------------------------------------------------------------------------
COLLECTIONS = {
    "kaftan":       dict(file="kaftan.html", name="Caftan", group="Women", cover="img kaftan/lukis 1.jpg"),
    "jubah":        dict(file="jubah.html", name="Jubah", group="Women", cover="img jubah/batwing 1.jpg"),
    "blouse":       dict(file="blouse.html", name="Blouse", group="Women", cover="img blouse/blouse 1.jpg"),
    "baju-kurung":  dict(file="baju-kurung.html", name="Baju Kurung", group="Women", cover="img baju kurung/kurung 1.jpg"),
    "short-sleeve": dict(file="short-sleeve-shirt.html", name="Short Sleeve Men Shirt", group="Men", cover="img short sleeve/kemeja 1.jpg"),
    "long-sleeve":  dict(file="long-sleeve-shirt.html", name="Long Sleeve Men Shirt", group="Men", cover="img long sleeve/lukis 1.png"),
    "cotton":       dict(file="kain-pasang-cotton.html", name="4 Meter Cotton Fabric", group="Fabrics", cover="img cotton/cotton 1.jpg"),
    "crepe":        dict(file="kain-pasang-crepe.html", name="4 Meter Silk Crepe Fabric", group="Fabrics", cover="img crepe/1 layer/crepe.jpg"),
}
GROUPS = ["Women", "Men", "Fabrics"]

# --------------------------------------------------------------------------
# Product pages content (from the original site)
# --------------------------------------------------------------------------
COTTON_NO1 = "Material Cotton Viscose (No. 1 Cotton of this century)"
COOL = "Very comfortable, cooling & breathable to wear"
NOSHRINK = "Does not shrink when washed"
IRON = "Easy to iron"
NOSHRINK_IRON = "Does not shrink when washed & easy to iron"

PAGES = {}

PAGES["kaftan"] = dict(
    title="Cotton Viscose Batwing Caftan",
    lead="This is our exclusive hand-drawn batik caftan collection, designed for elegance and comfort.",
    facts=["Hand-drawn", "Original from Kelantan", "Free size to XXL"],
    series=[
        dict(
            title="About Our Caftans",
            items=["Original from Kelantan", COTTON_NO1, COOL, IRON, NOSHRINK,
                   "Each caftan exclusively hand drawn; One Design, One Caftan"],
            sizing=("Caftans Sizing", [("Fit", "Free size fit to XXL"), ("Estimated length", "53 - 55 Inch"),
                                       ("Estimated chest", "56 - 58 Inch"), ("Estimated waist", "56 - 58 Inch")]),
            groups=[dict(label="Hand-drawn Batwing Caftan", alt="Hand-drawn batik batwing caftan",
                         images=["img kaftan/lukis 1.jpg", "img kaftan/lukis 2.jpg", "img kaftan/lukis 3.jpg"],
                         caption="This is our exclusive hand-drawn batik caftan collection, designed for elegance and comfort.")],
        ),
        dict(
            title="Pastel Series",
            desc="Soft, delicate tones in our signature hand-drawn batik.",
            items=[],
            groups=[dict(label="Pastel Series Caftans", alt="Pastel series batik caftan",
                         images=["img kaftan/pastel.jpg", "img kaftan/pastel 1.jpg", "img kaftan/pastel 2.jpg", "img kaftan/pastel 3.jpg"],
                         caption="Our pastel series caftans offer soft, delicate tones perfect for casual or formal occasions."),
                    vid_group("img kaftan/vid kaftan.mp4", "img kaftan/vid lukis.mp4", "img kaftan/vid pastel.mp4", "img kaftan/vid caftan.mp4")],
        ),
    ],
)

PAGES["jubah"] = dict(
    title="Cotton Viscose Modern Caftans and Jubah",
    lead="Exclusive hand-drawn Jubah collection, featuring modern long-sleeve caftans with a waist string.",
    facts=["Hand-drawn", "Diamonds / beads", "Free size to 5XL"],
    series=[
        dict(
            title="Long Sleeve Modern Caftans with Waist String",
            items=["Original from Kelantan", "Free size fit to 5XL", COTTON_NO1, COOL, NOSHRINK_IRON,
                   "Each caftans exclusively hand drawn; One Design, One Caftan",
                   "With diamonds/beads", "Handdrawn batik on the front and back of the caftans"],
            groups=[dict(label="Modern Batwing Caftan", alt="Modern long sleeve batik caftan with waist string",
                         images=["img jubah/batwing 1.jpg", "img jubah/batwing 2.jpg", "img jubah/batwing 3.jpg"])],
        ),
        dict(
            title="Jubah",
            items=["Free size fit to XXL", "Estimated length 53 - 55 Inch", COTTON_NO1, COOL, NOSHRINK_IRON,
                   "Each dress exclusively hand drawn; One Design, One Dress"],
            sizing=("Jubah Sizing", [("Fit", "Free size fit to XXL"), ("Estimated length", "53 - 55 Inch")]),
            groups=[dict(label="Jubah Dress Collection", alt="Hand-drawn batik jubah dress",
                         images=["img jubah/jubah %d.jpg" % i for i in range(1, 7)],
                         caption="Exclusive hand-drawn Jubah dress collection, crafted from premium Cotton Viscose for comfort and elegance. "
                                 "Designed to fit up to XXL, each piece is uniquely made for breathable wear and easy care."),
                    vid_group("img jubah/vid jubah.mp4", "img jubah/vid batwing.mp4")],
        ),
    ],
)

PAGES["blouse"] = dict(
    title="Cotton Viscose Butterfly Blouse",
    lead="Exclusive hand-drawn long sleeve batwing butterfly blouse, featuring a stylish waist tie for a flattering fit.",
    facts=["Hand-drawn", "Waist tie", "Free size to XXL"],
    series=[
        dict(
            title="Long Sleeve Batwing Butterfly Blouse",
            items=["With waist string to tie in inner side of the blouse", COTTON_NO1, COOL, NOSHRINK_IRON,
                   "Each blouses exclusively hand drawn; One Design, One Blouse"],
            sizing=("Blouse Sizing", [("Fit", "Free size fit to XXL"), ("Estimated chest", "48 Inch"),
                                      ("Estimated length", "31 Inch"), ("Estimated sleeve length", "21 Inch")]),
            groups=[dict(label="Butterfly Blouse", alt="Hand-drawn batik butterfly blouse",
                         images=["img blouse/blouse 1.jpg", "img blouse/blouse 2.jpg", "img blouse/blouse 3.jpg"],
                         caption="Crafted from premium Cotton Viscose, it offers breathable comfort and easy care. "
                                 "Designed to fit up to XXL with a unique pattern on every piece."),
                    vid_group("img blouse/vid blouse.mp4")],
        ),
    ],
)

PAGES["baju-kurung"] = dict(
    title="Modern Baju Kurung Mini",
    lead="Discover the batik baju kurung, with modern design of a mini kurung. Crafted from Cotton Viscose, this fabric is soft, "
         "breathable, and easy to maintain, offering unmatched comfort.",
    facts=["Hand-drawn", "Sizes XS – XXL", "Hidden back zip"],
    series=[
        dict(
            title="Modern Kurung Batik",
            items=["Original from Kelantan", COTTON_NO1, "Size available from XS to XXL", "Hidden zip at the back",
                   "A-line Skirt and elastic waist with hook", "Has back darts to shape fabric to fit the body",
                   COOL, NOSHRINK_IRON.replace("Does not shrink when washed & easy to iron", "Does not shrink when washed and easy to iron"),
                   "Each baju kurung exclusively hand drawn; One Design, One Kurung"],
            groups=[
                dict(label="Modern Baju Kurung Mini", alt="Modern batik baju kurung mini",
                     images=["img baju kurung/kurung %d.jpg" % i for i in range(1, 7)]),
                dict(label="Size Chart & Detail", alt="Baju kurung size chart and detail", charts=True,
                     images=["img baju kurung/chart.PNG", "img baju kurung/detail kurung.jpg"],
                     caption="Available in sizes XS to XXL, each piece is a unique masterpiece, combining traditional charm with modern elegance."),
                vid_group("img baju kurung/vid kurung.mp4"),
            ],
        ),
        dict(
            title="Kurung Moden Jasmin Batik",
            desc="Kurung Jasmin designed from premium Cotton Viscose for ultimate comfort and breathability. It features a hidden back zip, "
                 "stylish shoulder puff sleeves, and a mermaid skirt with an elastic waist and zip.",
            items=["Original from Kelantan", COTTON_NO1, "Size available from XS to XXL", "Hidden zip at the back",
                   "With shoulder puff sleeve", "Mermaid skirt and elastic waist with zip",
                   "Has back darts to shape fabric to fit the body", COOL, "Does not shrink when washed and easy to iron",
                   "Each baju kurung exclusively hand drawn; One Design, One Kurung"],
            groups=[
                dict(label="Kurung Jasmin", alt="Kurung Moden Jasmin batik",
                     images=["img baju kurung/jasmin.png"] + ["img baju kurung/jasmin %d.png" % i for i in range(1, 6)]),
                dict(label="Size Chart", alt="Kurung Jasmin size chart", charts=True, one=True,
                     images=["img baju kurung/chart 2.jpg"],
                     caption="Back darts provide a tailored fit, making it both elegant and flattering. Each piece is exclusively hand-drawn, ensuring a unique design."),
                vid_group("img baju kurung/vid jasmin.mp4"),
            ],
        ),
    ],
)

PAGES["short-sleeve"] = dict(
    title="Cotton Viscose Batik Men Shirt",
    lead="Experience style and tradition with our short-sleeve men's batik shirt, featuring a unique stamped batik design.",
    facts=["Stamped & Galaxy batik", "Sizes S – 3XL", "Copper block print"],
    series=[
        dict(
            title="Short Sleeve Stamped Batik",
            items=["Original from Kelantan", "Size available from S to 3XL", COTTON_NO1, COOL, IRON, NOSHRINK,
                   "Stamp Batik Design (Handmade block print)",
                   "Handmade with a copper printing block dipped in hot wax and then stamped on the fabric",
                   "Each shirt exclusively hand drawn; One Design, One Shirt"],
            groups=[dict(label="Stamped Batik Shirt", alt="Short sleeve stamped batik men shirt",
                         images=["img short sleeve/kemeja %d.jpg" % i for i in (1, 2, 3)])],
        ),
        dict(
            title="Short Sleeve Galaxy Batik",
            items=["Original from Kelantan", "Size available from S to 3XL", COTTON_NO1, COOL, IRON, NOSHRINK,
                   "Multi-layer of coloring batik called galaxy",
                   "Each shirt exclusively handmade; One Design, One Shirt"],
            groups=[
                dict(label="Galaxy Batik Shirt", alt="Short sleeve galaxy batik men shirt",
                     images=["img short sleeve/galaxy %d.png" % i for i in (1, 2, 3)],
                     caption="Our short-sleeve Galaxy Batik men's shirt, made from premium Cotton Viscose, combines unmatched comfort and breathability "
                             "with vibrant multi-layered galaxy coloring in a one-of-a-kind handmade design."),
                dict(label="Size Chart & Detail", alt="Men shirt size chart and detail", charts=True,
                     images=["img short sleeve/chart.png", "img short sleeve/detail kemeja.jpg"],
                     caption="Available in sizes S to 3XL, it’s easy to iron and resistant to shrinking, offering both style and practicality."),
                vid_group("img short sleeve/vid kemeja.mp4", "img short sleeve/vid galaxy.mp4", "img short sleeve/vid short sleeve.mp4"),
            ],
        ),
    ],
)

PAGES["long-sleeve"] = dict(
    title="Cotton Viscose & Silk Crepe Batik Men Shirt",
    lead="Explore our long-sleeve hand-drawn batik shirt, crafted from high-quality Cotton Viscose for unmatched comfort, breathability, "
         "and durability. Featuring a classic button-down collar and single-button cuffs.",
    facts=["Hand-drawn · Stamped · Silk Crepe", "Sizes S – 3XL", "Button-down collar"],
    series=[
        dict(
            title="Long Sleeve Cotton Viscose Handdrawn Batik",
            items=["Original from Kelantan", "Size available from S to 3XL", COTTON_NO1, COOL, IRON, NOSHRINK,
                   "Has button-down collar and a single-button cuff",
                   "Each shirt exclusively hand drawn; One Design, One Shirt"],
            groups=[dict(label="Hand-drawn Batik Shirt", alt="Long sleeve hand-drawn batik men shirt",
                         images=["img long sleeve/lukis %d.png" % i for i in (1, 2, 3)])],
        ),
        dict(
            title="Long Sleeve Cotton Viscose Stamped Batik",
            items=["Original from Kelantan", "Size available from S to 3XL", COTTON_NO1, COOL, IRON, NOSHRINK,
                   "Has button-down collar and a single-button cuff", "Stamp Batik Design (Handmade block print)",
                   "Handmade with a copper printing block dipped in hot wax and then stamped on the fabric",
                   "Each shirt exclusively hand drawn; One Design, One Shirt"],
            groups=[dict(label="Stamped Batik Shirt", alt="Long sleeve stamped batik men shirt",
                         images=["img long sleeve/stamped %d.png" % i for i in (1, 2, 3)],
                         caption="This long-sleeve shirt is crafted from Cotton Viscose for comfort and breathability. It features a button-down collar "
                                 "and single-button cuffs, along with a unique stamped batik design made using a copper block.")],
        ),
        dict(
            title="Long Sleeve Silk Crepe Batik",
            items=["Original from Kelantan", "Size available from S to 3XL", "Material Silk Crepe", COOL, IRON, NOSHRINK,
                   "Each shirt exclusively hand drawn; One Design, One Shirt"],
            groups=[dict(label="Silk Crepe Batik Shirt", alt="Long sleeve silk crepe batik men shirt",
                         images=["img long sleeve/crepe %d.png" % i for i in (1, 2, 3)],
                         caption="This is our exclusive hand-drawn batik shirt collection, designed for elegance and comfort.")],
        ),
    ],
)

PAGES["cotton"] = dict(
    title="Cotton Viscose 4 Meter Batik Fabric",
    lead="Our 4-meter Cotton Viscose Batik fabric is hand-drawn and offers exceptional comfort with its cooling and breathable properties.",
    facts=["4 Meter · Kain Pasang", "Hand-drawn & Stamped", "One design, one piece"],
    series=[
        dict(
            title="Cotton Viscose 4 Meter Batik",
            items=[COTTON_NO1, COOL, NOSHRINK_IRON, "Each cotton exclusively hand drawn; One Design, One Piece"],
            groups=[
                vid_group("img cotton/vid cotton.mp4", "img cotton/vid stamped.mp4"),
                dict(label="Handdrawn Cotton Batik", alt="Hand-drawn cotton viscose batik fabric",
                     images=["img cotton/cotton %d.jpg" % i for i in (1, 2, 3)],
                     caption="Made from the finest Cotton Viscose, this fabric does not shrink when washed and is easy to iron."),
                dict(label="Stamped Cotton Batik", alt="Stamped cotton viscose batik fabric",
                     images=["img cotton/stamped 1.jpg", "img cotton/stamped 2.jpg"],
                     caption="Each piece is unique, with one design per fabric, allowing for exclusive creations in your fashion design."),
            ],
        ),
    ],
)

PAGES["crepe"] = dict(
    title="Silk Crepe 4 Meter Batik Fabric",
    lead="This 4-meter Silk Crepe Batik fabric is perfect for tailoring into a baju kurung or jubah dress. Its lightweight and breathable quality "
         "ensures comfort, while the luxurious silk crepe material adds elegance to any design.",
    facts=["4 Meter · Kain Pasang", "Silk Crepe", "One design, one piece"],
    series=[
        dict(
            title="Silk Crepe 4 Meter Batik",
            items=["Silk crepe material for elegance and comfort", "Very exclusive designs suitable for special occasions", COOL,
                   NOSHRINK_IRON, "Each cotton exclusively hand drawn; One Design, One Piece"],
            groups=[
                vid_group("img crepe/vid crepe.mp4", "img crepe/1 layer/vid crepe.mp4"),
                dict(label="One-layer Silk Crepe", alt="One-layer silk crepe batik fabric",
                     images=["img crepe/1 layer/crepe.jpg"] + ["img crepe/1 layer/crepe %d.jpg" % i for i in (1, 2, 3)],
                     caption="The fabric is easy to maintain, as it doesn't shrink when washed and is easy to iron."),
                dict(label="Two-layer Silk Crepe", alt="Two-layer silk crepe batik fabric",
                     images=["img crepe/2 layer/crepe.jpg"] + ["img crepe/2 layer/crepe %d.jpg" % i for i in (1, 2, 3)],
                     caption="Each piece is uniquely hand-drawn, making every design exclusive to your creation."),
            ],
        ),
    ],
)

# --------------------------------------------------------------------------
# Shared layout
# --------------------------------------------------------------------------
def nav_items():
    return [("index.html", "Home"), ("profile.html", "About Us"), ("products.html", "Products"), ("contact.html", "Contact Us")]


def mega_html():
    cols = []
    for g in GROUPS:
        links = "".join('<a href="%s">%s</a>' % (c["file"], e(c["name"])) for c in COLLECTIONS.values() if c["group"] == g)
        cols.append("<div><h4>%s</h4>%s</div>" % (g, links))
    foot = ('<div class="mega-foot"><span>One Design, One Piece — every item hand-drawn in Kelantan.</span>'
            '<a class="link-arrow" href="products.html" style="padding:0 0 4px;font-size:11px">View all %s</a></div>' % ARROW)
    return '<div class="mega">%s%s</div>' % ("".join(cols), foot)


def header_html(active):
    lis = []
    for href, label in nav_items():
        cls = ' class="active"' if href == active else ""
        cur = ' aria-current="page"' if href == active else ""
        if href == "products.html":
            is_prod = active == "products.html" or active in [c["file"] for c in COLLECTIONS.values()]
            cls = ' class="active"' if is_prod else ""
            cur = ' aria-current="page"' if active == "products.html" else ""
            lis.append('<li%s><a href="%s"%s>%s%s</a>%s</li>' % (cls, href, cur, label, CARET, mega_html()))
        else:
            lis.append('<li%s><a href="%s"%s>%s</a></li>' % (cls, href, cur, label))

    d_sub = ""
    for g in GROUPS:
        d_sub += "<h5>%s</h5><div class=\"d-sub\">%s</div>" % (
            g, "".join('<a href="%s">%s</a>' % (c["file"], e(c["name"])) for c in COLLECTIONS.values() if c["group"] == g))

    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="progress" aria-hidden="true"></div>
<div class="topbar"><div class="wrap">
  <div class="tb-msg"><i></i><span>Authentic Kelantan Batik · Hand-drawn · One Design, One Piece</span></div>
  <div class="tb-links"><a href="tel:+601156774731">{WA_HQ[2]}</a><a href="mailto:{EMAIL}">{EMAIL}</a></div>
</div></div>
<header class="header"><div class="wrap">
  <a class="brand" href="index.html" aria-label="{BRAND} — home">
    <img class="b-icon" src="{img('logo-ebe/iconebe.PNG')}" alt="" height="52">
    <img class="b-word" src="{img('logo-ebe/wordebe.PNG')}" alt="{BRAND}" height="30">
    <span class="wordmark">{BRAND}</span>
  </a>
  <nav aria-label="Primary"><ul class="nav">{"".join(lis)}</ul></nav>
  <a class="btn cta" href="{WA_HQ[0]}" target="_blank" rel="noopener">Enquire {ARROW}</a>
  <button class="burger" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
</div></header>
<div class="drawer" aria-label="Mobile menu">
  <a class="d-main" href="index.html">Home</a>
  <a class="d-main" href="profile.html">About Us</a>
  <a class="d-main" href="products.html">Products</a>
  {d_sub}
  <a class="d-main" href="contact.html" style="margin-top:26px">Contact Us</a>
  <a class="btn btn--wa" href="{WA_HQ[0]}" target="_blank" rel="noopener">WhatsApp {WA_HQ[2]}</a>
</div>'''


def footer_html():
    def col(g):
        return "".join('<li><a href="%s">%s</a></li>' % (c["file"], e(c["name"])) for c in COLLECTIONS.values() if c["group"] == g)
    return f'''<footer class="footer">
  <div class="wrap footer-top">
    <div>
      <div class="f-banner"><img src="{img('logo-ebe/header photo.png')}" alt="{BRAND}" loading="lazy" data-fb></div>
      <div class="wm">Empayar Batik<br>Exclusive<small>Kota Bharu · Kelantan · Malaysia</small></div>
      <p>Authentic hand-drawn Malay heritage batik — proudly representing Malaysia's culture, locally and around the world.</p>
      <div class="soc">
        <a href="{INSTAGRAM[0]}" target="_blank" rel="noopener" aria-label="Instagram {INSTAGRAM[1]}">{I_IG}</a>
        <a href="{TIKTOK[0]}" target="_blank" rel="noopener" aria-label="TikTok {TIKTOK[1]}">{I_TT}</a>
        <a href="{SHOPEE[0]}" target="_blank" rel="noopener" aria-label="Shopee {SHOPEE[1]}">{I_SHOP}</a>
      </div>
      <a class="shop-here" href="{LINKTREE[0]}" target="_blank" rel="noopener"><i></i>Shop here <span>{LINKTREE[1]}</span></a>
    </div>
    <div>
      <h5>Women</h5><ul>{col("Women")}</ul>
      <h5 style="margin-top:30px">Men</h5><ul>{col("Men")}</ul>
    </div>
    <div>
      <h5>Fabrics</h5><ul>{col("Fabrics")}</ul>
      <h5 style="margin-top:30px">Maison</h5>
      <ul><li><a href="index.html">Home</a></li><li><a href="profile.html">About Us</a></li><li><a href="products.html">Product Catalog</a></li><li><a href="contact.html">Contact Us</a></li></ul>
    </div>
    <div>
      <h5>Visit &amp; Contact</h5>
      <p class="addr">{e(ADDRESS)}</p>
      <ul>
        <li><a href="{WA_HQ[0]}" target="_blank" rel="noopener">{WA_HQ[2]} <span style="color:#7d7469">({WA_HQ[3]})</span></a></li>
        <li><a href="{WA_BTG[0]}" target="_blank" rel="noopener">{WA_BTG[2]} <span style="color:#7d7469">({WA_BTG[3]})</span></a></li>
        <li><a href="mailto:{EMAIL}">{EMAIL}</a></li>
        <li><a href="{MAPS}" target="_blank" rel="noopener">Get directions →</a></li>
      </ul>
    </div>
  </div>
  <div class="footer-bottom"><div class="wrap">
    <span>© 2026 {BRAND}. All rights reserved.</span>
    <span>Quality and Exclusivity, Our Priority</span>
  </div></div>
</footer>
<a class="wa-float" href="{WA_HQ[0]}" target="_blank" rel="noopener" aria-label="Chat on WhatsApp">{I_WA}<span>WhatsApp</span></a>'''


def page(filename, title, desc, body, active, og_image=None, extra_head="", body_class=""):
    og = og_image or img("img index/home 1.jpg")
    url = SITE + "/" + ("" if filename == "index.html" else filename)
    full_title = BRAND if filename == "index.html" else "%s | %s" % (title, BRAND)
    return f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(full_title)}</title>
<meta name="description" content="{e(desc)}">
<meta name="theme-color" content="#15110e">
<link rel="canonical" href="{url}">
<link rel="icon" href="{img('logo-ebe/iconebe.PNG')}">
<link rel="apple-touch-icon" href="{img('logo-ebe/iconebe.PNG')}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="{BRAND}">
<meta property="og:title" content="{e(full_title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{og}">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,500;0,600;1,400;1,500&family=Jost:wght@300;400;500&display=swap" rel="stylesheet">
<link rel="stylesheet" href="assets/css/main.css">
<script>document.documentElement.className+=' js'</script>
{extra_head}
</head>
<body class="{body_class}">
{header_html(active)}
<main id="main">
{body}
</main>
{footer_html()}
<script src="assets/js/main.js" defer></script>
</body>
</html>
'''


def cta_band(kicker="Enquire", heading="Find your one-of-a-kind piece", text=None):
    text = text or "Every design is made once. Message our team to check availability, sizes and new arrivals."
    return f'''<section class="cta-band"><div class="wrap reveal">
  <span class="eyebrow center">{kicker}</span>
  <h2 class="h-1">{heading}</h2>
  <p>{text}</p>
  <div class="btns">
    <a class="btn btn--gold" href="{WA_HQ[0]}" target="_blank" rel="noopener">WhatsApp HQ {ARROW}</a>
    <a class="btn btn--light" href="{WA_BTG[0]}" target="_blank" rel="noopener">Bazar Tok Guru</a>
  </div>
</div></section>'''


def card(key, small=None, delay=0):
    c = COLLECTIONS[key]
    return f'''<a class="card reveal" style="--d:{delay}s" href="{c["file"]}">
  <div class="ph"><img src="{img(c["cover"])}" alt="{e(c["name"])} — Empayar Batik Exclusive" loading="lazy" data-fb></div>
  <div class="cap"><small>{small or c["group"]}</small><h4>{e(c["name"])}</h4><span class="go">Discover {ARROW}</span></div>
</a>'''


# --------------------------------------------------------------------------
# Pages
# --------------------------------------------------------------------------
def build_index():
    slides = "".join('<img src="%s" alt="Empayar Batik Exclusive — batik collection %d" %s data-fb>' % (
        img("img index/home %d.jpg" % i), i, 'class="active" fetchpriority="high"' if i == 1 else 'loading="lazy"') for i in range(1, 7))
    dots = "".join('<button aria-label="Show image %d"%s></button>' % (i, ' class="active"' if i == 1 else "") for i in range(1, 7))

    grid = ""
    for g in GROUPS:
        keys = [k for k, c in COLLECTIONS.items() if c["group"] == g]
        cls = {"Women": "", "Men": " g2", "Fabrics": " g2"}[g]
        grid += '<div class="coll-group"><h3>%s</h3><div class="coll-grid%s">%s</div></div>' % (
            "For Her" if g == "Women" else "For Him" if g == "Men" else "Kain Pasang · 4 Meter Fabrics",
            cls, "".join(card(k, delay=i * .08) for i, k in enumerate(keys)))

    mosaic = "".join('<a href="%s" data-lb="home" class="reveal" style="--d:%.2fs"><img src="%s" alt="Empayar Batik Exclusive — gallery %d" loading="lazy" data-fb></a>' % (
        img("img index/home %d.jpg" % i), (i - 1) * .06, img("img index/home %d.jpg" % i), i) for i in range(1, 7))

    ld = f'''<script type="application/ld+json">{{
  "@context": "https://schema.org",
  "@type": "ClothingStore",
  "name": "{BRAND}",
  "url": "{SITE}/",
  "image": "{img('img index/home 1.jpg')}",
  "description": "{e(TAGLINE)}",
  "telephone": "+60 11-5677 4731",
  "email": "{EMAIL}",
  "address": {{"@type": "PostalAddress", "streetAddress": "Lot 811, Kampong Badang", "postalCode": "15350", "addressLocality": "Kota Bharu", "addressRegion": "Kelantan", "addressCountry": "MY"}},
  "sameAs": ["{INSTAGRAM[0]}", "{TIKTOK[0]}", "{SHOPEE[0]}"]
}}</script>'''

    body = f'''
<section class="hero" aria-label="Introduction">
  <div class="hero-slides">{slides}</div>
  <div class="hero-inner">
    <span class="eyebrow">Authentic Malay Heritage Batik · Kelantan</span>
    <h1 class="h-display">Batik, <em>hand-drawn</em> for the modern woman.</h1>
    <p>“{TAGLINE}.”</p>
    <div class="hero-actions">
      <a class="btn btn--gold" href="products.html">Explore Collections {ARROW}</a>
      <a class="btn btn--light" href="profile.html">Our Story</a>
    </div>
  </div>
  <div class="hero-meta"><div class="wrap">
    <span class="scroll-cue"><i></i>Scroll</span>
    <div class="hero-dots" role="group" aria-label="Hero images">{dots}</div>
    <span>One Design · One Piece</span>
  </div></div>
</section>

<section class="strip" aria-label="Our promise"><div class="wrap"><ul>
  <li>{I_PIN2}<div><b>Original from Kelantan</b><span>Crafted at the heart of batik</span></div></li>
  <li>{I_HAND}<div><b>Hand-drawn &amp; Stamped</b><span>Handmade copper-block prints</span></div></li>
  <li>{I_LEAF}<div><b>Cooling &amp; Breathable</b><span>Cotton Viscose &amp; Silk Crepe</span></div></li>
  <li>{I_ONE}<div><b>One Design, One Piece</b><span>Exclusive to you</span></div></li>
</ul></div></section>

<section class="section" id="about">
  <div class="wrap about">
    <div class="about-media reveal">
      <img class="m1" src="{img('img index/home 2.jpg')}" alt="Hand-drawn batik by Empayar Batik Exclusive" loading="lazy" data-fb>
      <img class="m2" src="{img('img index/home 3.jpg')}" alt="Empayar Batik Exclusive baju kurung and caftan" loading="lazy" data-fb>
    </div>
    <div class="about-copy reveal" style="--d:.1s">
      <span class="eyebrow">About Our Batik</span>
      <h2 class="h-1">Malaysia's culture, <span class="gold">drawn by hand.</span></h2>
      <p class="lead">Empayar Batik Exclusive (EBE) is a well-known batik store from Kelantan that proudly represents Malaysia's culture. The store was started with the aim of growing the batik business across the country by offering high-quality, hand-drawn batik designs.</p>
      <p>EBE’s collection includes batik fabrics, baju kurung, caftans, men’s shirts, and other modern and traditional clothing.</p>
      <p>The business is passionate about sharing batik with Malaysians and promoting it internationally. EBE specifically focus on creating unique and high-quality designs that mix traditional and modern styles. EBE aim to grow the batik industry, EBE aims to make Malaysian batik a symbol of pride both locally and around the world.</p>
      <blockquote class="quote">Quality and Exclusivity, Our Priority</blockquote>
      <div class="btns"><a class="btn" href="profile.html">Discover Our Story {ARROW}</a><a class="link-arrow" href="contact.html">Visit our stores {ARROW}</a></div>
    </div>
  </div>
</section>

<section class="section section--sand" id="collections">
  <div class="wrap">
    <div class="section-head split-head reveal" style="max-width:none">
      <div style="max-width:640px"><span class="eyebrow">The Collections</span><h2 class="h-1">Eight ways to wear <span class="gold">heritage.</span></h2></div>
      <a class="link-arrow" href="products.html">Full product catalog {ARROW}</a>
    </div>
    <div class="coll-groups">{grid}</div>
  </div>
</section>

<section class="section section--ink" id="craft">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow center">The Craft</span><h2 class="h-1">Made slowly. Worn <span class="gold">beautifully.</span></h2>
      <p class="lead" style="color:#b9af9d">Three batik techniques, one standard: every piece is handmade in Kelantan and never repeated.</p></div>
    <div class="craft">
      <article class="reveal"><span class="num">01</span><h3>Hand-drawn Batik</h3><p>Each caftan, kurung, blouse and shirt is exclusively hand drawn — One Design, One Piece. Selected pieces are finished with diamonds and beads.</p></article>
      <article class="reveal" style="--d:.1s"><span class="num">02</span><h3>Stamped Batik</h3><p>A handmade block print: a copper printing block is dipped in hot wax and then stamped on the fabric.</p></article>
      <article class="reveal" style="--d:.2s"><span class="num">03</span><h3>Galaxy Batik</h3><p>A multi-layer colouring technique called galaxy, giving each shirt vibrant, one-of-a-kind depth.</p></article>
    </div>
  </div>
</section>

<section class="section" id="materials">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow center">Fine Materials</span><h2 class="h-1">Comfort you can <span class="gold">feel.</span></h2></div>
    <div class="materials">
      <article class="mat reveal"><span class="tag">Signature fabric</span><h3>Cotton Viscose</h3>
        <p>“No. 1 Cotton of this century” — soft, cooling and made to last.</p>
        <ul><li>Very comfortable, cooling &amp; breathable to wear</li><li>Does not shrink when washed</li><li>Easy to iron</li></ul></article>
      <article class="mat reveal" style="--d:.1s"><span class="tag">Occasion fabric</span><h3>Silk Crepe</h3>
        <p>Lightweight and breathable, with a luxurious drape for special occasions.</p>
        <ul><li>Elegant and exclusive designs</li><li>Does not shrink when washed &amp; easy to iron</li><li>Available as men’s shirts and 4-meter fabric</li></ul></article>
    </div>
  </div>
</section>

<section class="section section--sand" id="gallery">
  <div class="wrap">
    <div class="section-head split-head reveal" style="max-width:none">
      <div style="max-width:640px"><span class="eyebrow">Gallery</span><h2 class="h-1">A glimpse of the <span class="gold">empire.</span></h2></div>
      <a class="link-arrow" href="{INSTAGRAM[0]}" target="_blank" rel="noopener">Follow {INSTAGRAM[1]} {ARROW}</a>
    </div>
    <div class="mosaic">{mosaic}</div>
  </div>
</section>

{cta_band(kicker="Visit or Enquire", heading="Bring home a piece of Kelantan")}
'''
    return page("index.html", BRAND,
                "Empayar Batik Exclusive — a leading batik store from Kelantan offering exclusive hand-drawn batik, baju kurung, caftans, men's shirts and fabrics. Proudly promoting Malaysia's heritage globally.",
                body, "index.html", extra_head=ld)


def build_profile():
    gal = "".join('<a href="%s" data-lb="profile" class="reveal" style="--d:%.2fs"><img src="%s" alt="Empayar Batik Exclusive profile photo %d" loading="lazy" data-fb></a>' % (
        img("img profile/%d.png" % i), (i - 1) % 2 * .1, img("img profile/%d.png" % i), i) for i in range(1, 5))
    body = f'''
<section class="page-hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>About Us</span></nav>
  <span class="eyebrow">About Us</span>
  <h1>The story of <em class="gold">Empayar Batik Exclusive</em></h1>
  <p class="lead">“{TAGLINE}.”</p>
</div></section>

<section class="section">
  <div class="wrap">
    <div class="profile-intro">
      <div class="reveal"><span class="eyebrow">Who We Are</span><h2 class="h-1" style="margin-top:18px">Proudly <span class="gold">Kelantanese.</span> Proudly Malaysian.</h2></div>
      <div class="reveal" style="--d:.1s">
        <p class="lead">Empayar Batik Exclusive (EBE) is a well-known batik store from Kelantan that proudly represents Malaysia's culture. The store was started with the aim of growing the batik business across the country by offering high-quality, hand-drawn batik designs.</p>
        <p>EBE’s collection includes batik fabrics, baju kurung, caftans, men’s shirts, and other modern and traditional clothing. The business is passionate about sharing batik with Malaysians and promoting it internationally.</p>
        <p>EBE specifically focus on creating unique and high-quality designs that mix traditional and modern styles. EBE aim to grow the batik industry, EBE aims to make Malaysian batik a symbol of pride both locally and around the world.</p>
      </div>
    </div>
    <div class="stat-row reveal">
      <div class="stat"><b>Kelantan</b><span>Original origin</span></div>
      <div class="stat"><b>8</b><span>Collections</span></div>
      <div class="stat"><b>1 : 1</b><span>One design, one piece</span></div>
      <div class="stat"><b>2</b><span>Stores · HQ &amp; Bazar Tok Guru</span></div>
    </div>
  </div>
</section>

<section class="section section--sand">
  <div class="wrap">
    <div class="section-head reveal"><span class="eyebrow">Behind the Brand</span><h2 class="h-1">Inside <span class="gold">EBE.</span></h2></div>
    <div class="profile-gallery">{gal}</div>
  </div>
</section>

<section class="section">
  <div class="wrap">
    <div class="section-head center reveal"><span class="eyebrow center">Our Priority</span><h2 class="h-1">Quality and <span class="gold">Exclusivity.</span></h2></div>
    <div class="values">
      <div class="value reveal"><h3>Authentic Heritage</h3><p>Original from Kelantan — traditional batik techniques kept alive through hand-drawn and hand-stamped work.</p></div>
      <div class="value reveal" style="--d:.1s"><h3>Traditional meets Modern</h3><p>Unique designs that mix traditional and modern styles: modern kurung, batwing caftans, butterfly blouses and tailored shirts.</p></div>
      <div class="value reveal" style="--d:.2s"><h3>Pride, Worldwide</h3><p>Making Malaysian batik a symbol of pride, both locally and around the world.</p></div>
    </div>
  </div>
</section>

{cta_band(kicker="Explore", heading="Discover the collections", text="From caftans and baju kurung to men’s shirts and 4-meter fabrics — find the batik made for you.")}
'''
    return page("profile.html", "About Us", "About Empayar Batik Exclusive (EBE) — a well-known batik store from Kelantan proudly representing Malaysia's culture with authentic hand-drawn batik.",
                body, "profile.html", og_image=img("img profile/1.png"))


def build_products():
    grid = ""
    for g in GROUPS:
        keys = [k for k, c in COLLECTIONS.items() if c["group"] == g]
        cls = {"Women": "", "Men": " g2", "Fabrics": " g2"}[g]
        grid += '<div class="coll-group"><h3>%s</h3><div class="coll-grid%s">%s</div></div>' % (
            "For Her" if g == "Women" else "For Him" if g == "Men" else "Kain Pasang · 4 Meter Fabrics",
            cls, "".join(card(k, delay=i * .08) for i, k in enumerate(keys)))
    body = f'''
<section class="page-hero"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Products</span></nav>
  <span class="eyebrow">Product Catalog</span>
  <h1>The Collections</h1>
  <p class="lead catalog-intro">Here are the product categories we offer — each one hand-drawn or hand-stamped in Kelantan. One Design, One Piece.</p>
</div></section>
<section class="section"><div class="wrap"><div class="coll-groups">{grid}</div></div></section>
{cta_band(kicker="Need help choosing?", heading="Speak to our team")}
'''
    return page("products.html", "Product Catalog", "Product catalog of Empayar Batik Exclusive: Caftan, Jubah, Blouse, Baju Kurung, Men Shirts (short & long sleeve), 4 Meter Cotton Fabric and 4 Meter Silk Crepe Fabric.",
                body, "products.html")


def video_html(group):
    cands = "|".join(img(c) for c in group["video"])
    cap = '<p class="caption">%s</p>' % e(group["caption"]) if group.get("caption") else ""
    return ('<div class="reveal vid-wrap"><div class="group-label">%s</div>'
            '<figure class="vid"><video controls playsinline preload="metadata" data-cands="%s">'
            'Your browser does not support the video tag.</video></figure>%s</div>') % (e(group["label"]), cands, cap)


def gallery_html(group, lb_id):
    if group.get("video"):
        return video_html(group)
    imgs = group["images"]
    cls = "gallery"
    if group.get("charts"):
        cls += " charts"
    if group.get("one") or len(imgs) == 1:
        cls += " one"
    a = ""
    for i, p in enumerate(imgs, 1):
        alt = "%s — %d" % (group["alt"], i) if len(imgs) > 1 else group["alt"]
        a += '<a href="%s" data-lb="%s"><img src="%s" alt="%s" loading="lazy" data-fb></a>' % (img(p), lb_id, img(p), e(alt))
    cap = '<p class="caption">%s</p>' % e(group["caption"]) if group.get("caption") else ""
    label = '<div class="group-label">%s</div>' % e(group["label"]) if group.get("label") else ""
    return '<div class="reveal">%s<div class="%s">%s</div>%s</div>' % (label, cls, a, cap)


def build_product(key):
    c, p = COLLECTIONS[key], PAGES[key]
    first_img = next(g["images"][0] for g in p["series"][0]["groups"] if g.get("images"))
    facts = "".join('<span class="fact">%s</span>' % e(f) for f in p["facts"])

    series_html = ""
    for i, s in enumerate(p["series"], 1):
        flip = " flip alt" if i % 2 == 0 else ""
        desc = '<p class="desc">%s</p>' % e(s["desc"]) if s.get("desc") else ""
        checks = '<ul class="checks">%s</ul>' % "".join("<li>%s</li>" % e(t) for t in s["items"]) if s.get("items") else ""
        spec = ""
        if s.get("sizing"):
            t, rows = s["sizing"]
            spec = '<div class="spec"><div class="spec-title">%s</div><dl>%s</dl></div>' % (
                e(t), "".join('<div class="row"><dt>%s</dt><dd>%s</dd></div>' % (e(a), e(b)) for a, b in rows))
        groups = "".join(gallery_html(g, "%s-%d" % (key, i)) for g in s["groups"])
        series_html += f'''
<section class="series{flip}" id="series-{i}">
  <div class="wrap series-grid">
    <div class="series-copy reveal">
      <span class="idx">{i:02d} / {len(p["series"]):02d}</span>
      <h2>{e(s["title"])}</h2>
      {desc}{checks}{spec}
      <div class="btns"><a class="btn btn--wa" href="{WA_HQ[0]}" target="_blank" rel="noopener">{I_WA.replace('<svg', '<svg width="16" height="16"')} Enquire</a>
      <a class="btn btn--ghost" href="{WA_BTG[0]}" target="_blank" rel="noopener">Bazar Tok Guru</a></div>
    </div>
    <div class="groups">{groups}</div>
  </div>
</section>'''

    # show 4 neighbours: next four in order (wrapping)
    keys = list(COLLECTIONS)
    pos = keys.index(key)
    nxt = [keys[(pos + j) % len(keys)] for j in range(1, 5)]
    explore = "".join(card(k, delay=j * .08) for j, k in enumerate(nxt))

    body = f'''
<section class="page-hero has-img"><div class="wrap">
  <div>
    <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><a href="products.html">Products</a><span aria-hidden="true">/</span><span>{e(c["name"])}</span></nav>
    <span class="eyebrow">{e(c["group"] if c["group"] != "Fabrics" else "Kain Pasang")} Collection</span>
    <h1>{e(p["title"])}</h1>
    <p class="lead">{e(p["lead"])}</p>
    <div class="fact-row">{facts}</div>
    <div class="btns">
      <a class="btn btn--gold" href="{WA_HQ[0]}" target="_blank" rel="noopener">Enquire on WhatsApp {ARROW}</a>
      <a class="btn btn--light" href="#series-1">View designs</a>
    </div>
  </div>
  <div class="ph-img"><img src="{img(first_img)}" alt="{e(p["title"])}" fetchpriority="high" data-fb></div>
</div></section>
{series_html}
<section class="section explore">
  <div class="wrap">
    <div class="section-head split-head reveal" style="max-width:none"><div><span class="eyebrow">Continue Exploring</span><h2 class="h-1">More from the <span class="gold">collection</span></h2></div>
      <a class="link-arrow" href="products.html">All products {ARROW}</a></div>
    <div class="coll-grid">{explore}</div>
  </div>
</section>
{cta_band(kicker="Interested in this collection?", heading="One design. One piece. Yours.", text="Every piece is exclusively hand-made and never repeated. Message us for availability, colours and sizes.")}
'''
    return page(c["file"], c["name"], "%s — %s" % (p["title"], p["lead"]), body, c["file"], og_image=img(first_img))


def contact_card(href, icon, small, big, ext=True):
    tgt = ' target="_blank" rel="noopener"' if ext else ""
    return f'<a class="c-card reveal" href="{href}"{tgt}><span class="ic">{icon}</span><span><small>{small}</small><b>{big}</b></span><span class="arr">{ARROW}</span></a>'


def build_contact():
    cards = "".join([
        contact_card(WA_HQ[0], I_PHONE, "WhatsApp · HQ", WA_HQ[2]),
        contact_card(WA_BTG[0], I_PHONE, "WhatsApp · Bazar Tok Guru", WA_BTG[2]),
        contact_card("mailto:" + EMAIL, I_MAIL, "Email", EMAIL, ext=False),
        contact_card(MAPS, I_PIN, "Visit Us · HQ", e(ADDRESS)),
    ])
    socials = "".join([
        contact_card(INSTAGRAM[0], I_IG, "Instagram", INSTAGRAM[1]),
        contact_card(TIKTOK[0], I_TT, "TikTok", TIKTOK[1]),
        contact_card(SHOPEE[0], I_SHOP, "Shopee", SHOPEE[1]),
    ])
    opts = "".join('<option value="%s">%s</option>' % (e(c["name"]), e(c["name"])) for c in COLLECTIONS.values())
    body = f'''
<section class="page-hero has-bg" style="--bg:url('{img('img contact/contact.png')}')"><div class="wrap">
  <nav class="crumbs" aria-label="Breadcrumb"><a href="index.html">Home</a><span aria-hidden="true">/</span><span>Contact Us</span></nav>
  <span class="eyebrow">Contact Us</span>
  <h1>Let’s talk <em class="gold">batik.</em></h1>
  <p class="lead">Reach our team on WhatsApp, drop by our stores in Kota Bharu, or follow us for the newest arrivals.</p>
</div></section>

<section class="section">
  <div class="wrap contact-grid">
    <div>
      <div class="contact-cards">{cards}</div>
      <div class="section-head" style="margin:44px 0 18px"><span class="eyebrow">Follow &amp; Shop</span></div>
      <div class="socials">{socials}</div>
    </div>
    <div>
      <div class="map reveal"><iframe title="Empayar Batik Eksklusif HQ map" loading="lazy" referrerpolicy="no-referrer-when-downgrade"
        src="https://www.google.com/maps?q=Empayar+Batik+Eksklusif+HQ,+Lot+811,+Kampong+Badang,+15350+Kota+Bharu,+Kelantan&amp;output=embed"></iframe></div>
      <form class="form reveal" id="enquiry" autocomplete="on">
        <h3>Send an enquiry</h3>
        <p class="sm">Fill in the details and we’ll open WhatsApp with your message ready to send.</p>
        <div class="field"><label for="f-name">Your name</label><input id="f-name" name="name" required placeholder="Full name"></div>
        <div class="field"><label for="f-coll">Interested in</label><select id="f-coll" name="collection">{opts}</select></div>
        <div class="field"><label for="f-branch">Send to</label>
          <select id="f-branch" name="branch"><option value="{WA_HQ[1]}">HQ · {WA_HQ[2]}</option><option value="{WA_BTG[1]}">Bazar Tok Guru · {WA_BTG[2]}</option></select></div>
        <div class="field"><label for="f-msg">Message</label><textarea id="f-msg" name="message" placeholder="Size, colour, design you have seen…"></textarea></div>
        <button class="btn btn--wa" type="submit">{I_WA.replace('<svg', '<svg width="18" height="18"')} Send via WhatsApp</button>
        <p class="hours-note">Prefer email? Write to {EMAIL}</p>
      </form>
    </div>
  </div>
</section>
'''
    return page("contact.html", "Contact Us", "Contact Empayar Batik Exclusive: WhatsApp HQ +60 11-5677 4731, Bazar Tok Guru +60 14-701 6471, email, Kota Bharu Kelantan address, Instagram, TikTok and Shopee.",
                body, "contact.html")


def write(name, content):
    with open(os.path.join(ROOT, name), "w", encoding="utf-8") as f:
        f.write(content)
    print("wrote", name)


def main():
    write("index.html", build_index())
    write("profile.html", build_profile())
    write("products.html", build_products())
    for k, c in COLLECTIONS.items():
        write(c["file"], build_product(k))
    write("contact.html", build_contact())

    urls = ["", "index.html", "profile.html", "products.html"] + [c["file"] for c in COLLECTIONS.values()] + ["contact.html"]
    sm = '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n'
    sm += "".join("  <url><loc>%s/%s</loc></url>\n" % (SITE, u) for u in urls) + "</urlset>\n"
    write("sitemap.xml", sm)
    write("robots.txt", "User-agent: *\nAllow: /\nSitemap: %s/sitemap.xml\n" % SITE)


if __name__ == "__main__":
    main()
