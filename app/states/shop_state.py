import reflex as rx
from typing import TypedDict


class ShopProduct(TypedDict):
    id: int
    name: str
    category: str
    price: float
    old_price: float
    image: str
    images: list[str]
    rating: float
    reviews_count: int
    badge: str
    colors: list[str]
    sizes: list[str]
    in_stock: bool
    is_new: bool
    popularity: int
    description: str
    materials: str
    care: str


class Review(TypedDict):
    author: str
    avatar: str
    rating: int
    date: str
    title: str
    body: str


# ---------- Seed data ----------

_WOMEN_IMGS = [
    "https://images.unsplash.com/photo-1594633312681-425c7b97ccd1?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1594633313593-bab3825d0caf?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1483985988355-763728e1935b?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1490481651871-ab68de25d43d?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1539109136881-3be0616acf4b?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1551232864-3f0890e580d9?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1572804013309-59a88b7e92f1?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1585487000160-6ebcfceb0d03?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1520975916090-3105956dac38?w=900&auto=format&fit=crop",
]
_MEN_IMGS = [
    "https://images.unsplash.com/photo-1591047139829-d91aecb6caea?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1490578474895-699cd4e2cf59?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1638289661650-53d2a1922eea?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1533867617858-e7b97e060509?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1516826957135-700dedea698c?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1552374196-1ab2a1c593e8?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1617137968427-85924c800a22?w=900&auto=format&fit=crop",
]
_HOME_IMGS = [
    "https://images.unsplash.com/photo-1578500494198-246f612d3b3d?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1513694203232-719a280e022f?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1524758631624-e2822e304c36?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1616486338812-3dadae4b4ace?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1567016432779-094069958ea5?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1592078615290-033ee584e267?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1519710164239-da123dc03ef4?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1519455953755-af066f52f1a6?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1493663284031-b7e3aefcae8e?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1615529182904-14819c35db37?w=900&auto=format&fit=crop",
]
_BEAUTY_IMGS = [
    "https://images.unsplash.com/photo-1608248543803-ba4f8c70ae0b?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1522337360788-8b13dee7a37e?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1631730359585-38a4935cbec4?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1596462502278-27bfdc403348?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1571781926291-c477ebfd024b?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1556228720-195a672e8a03?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1570194065650-d99fb4bedf0a?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1512207855439-e6bcbca25da2?w=900&auto=format&fit=crop",
]
_ACC_IMGS = [
    "https://images.unsplash.com/photo-1509631179647-0177331693ae?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1553062407-98eeb64c6a62?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1523170335258-f5ed11844a49?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1611085583191-a3b181a88401?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1590874103328-eac38a683ce7?w=900&auto=format&fit=crop",
    "https://images.unsplash.com/photo-1608042314453-ae338d80c427?w=900&auto=format&fit=crop",
]


def _mk(
    pid: int,
    name: str,
    cat: str,
    price: float,
    old: float,
    imgs: list[str],
    rating: float,
    reviews: int,
    badge: str,
    colors: list[str],
    sizes: list[str],
    stock: bool,
    new: bool,
    pop: int,
    desc: str,
    materials: str,
    care: str,
) -> ShopProduct:
    return {
        "id": pid,
        "name": name,
        "category": cat,
        "price": price,
        "old_price": old,
        "image": imgs[0],
        "images": imgs,
        "rating": rating,
        "reviews_count": reviews,
        "badge": badge,
        "colors": colors,
        "sizes": sizes,
        "in_stock": stock,
        "is_new": new,
        "popularity": pop,
        "description": desc,
        "materials": materials,
        "care": care,
    }


APPAREL_SIZES = ["XS", "S", "M", "L", "XL"]
ONE_SIZE = ["One Size"]

_WOMEN = [
    _mk(
        1,
        "Linen Wrap Blouse",
        "Women",
        128.00,
        168.00,
        [_WOMEN_IMGS[0], _WOMEN_IMGS[3], _WOMEN_IMGS[4]],
        4.8,
        214,
        "Bestseller",
        ["Cream", "Sage", "Charcoal"],
        APPAREL_SIZES,
        True,
        False,
        940,
        "A softly draped wrap blouse in washed European linen — an effortless layer for warm afternoons.",
        "100% washed linen",
        "Machine wash cold, line dry",
    ),
    _mk(
        2,
        "Silk Slip Dress",
        "Women",
        198.00,
        0.0,
        [_WOMEN_IMGS[1], _WOMEN_IMGS[5], _WOMEN_IMGS[8]],
        4.8,
        41,
        "New",
        ["Blush", "Ivory", "Sage"],
        APPAREL_SIZES,
        True,
        True,
        620,
        "Bias-cut silk slip with delicate spaghetti straps and a whisper-light finish.",
        "100% mulberry silk",
        "Dry clean only",
    ),
    _mk(
        3,
        "Wide-Leg Trousers",
        "Women",
        148.00,
        0.0,
        [_WOMEN_IMGS[2], _WOMEN_IMGS[6], _WOMEN_IMGS[0]],
        4.7,
        96,
        "Trending",
        ["Charcoal", "Sand", "Forest"],
        APPAREL_SIZES,
        True,
        False,
        810,
        "Fluid wide-leg trouser cut from soft cupro-viscose blend, tailored to fall beautifully.",
        "78% cupro, 22% viscose",
        "Dry clean recommended",
    ),
    _mk(
        4,
        "Merino Cardigan",
        "Women",
        168.00,
        210.00,
        [_WOMEN_IMGS[9], _WOMEN_IMGS[4], _WOMEN_IMGS[7]],
        4.9,
        158,
        "Bestseller",
        ["Cream", "Sage", "Blush"],
        APPAREL_SIZES,
        True,
        False,
        890,
        "A soft, cropped cardigan knit from ultra-fine merino wool with mother-of-pearl buttons.",
        "100% Italian merino wool",
        "Hand wash cool",
    ),
    _mk(
        5,
        "Cotton Poplin Shirt",
        "Women",
        118.00,
        0.0,
        [_WOMEN_IMGS[7], _WOMEN_IMGS[0], _WOMEN_IMGS[3]],
        4.6,
        73,
        "",
        ["Ivory", "Sage", "Blush"],
        APPAREL_SIZES,
        True,
        False,
        540,
        "The relaxed everyday shirt — crisp cotton poplin with a soft, lived-in finish.",
        "100% organic cotton poplin",
        "Machine wash cold",
    ),
    _mk(
        6,
        "Pleated Midi Skirt",
        "Women",
        158.00,
        0.0,
        [_WOMEN_IMGS[5], _WOMEN_IMGS[8], _WOMEN_IMGS[9]],
        4.7,
        62,
        "New",
        ["Sand", "Forest"],
        APPAREL_SIZES,
        True,
        True,
        480,
        "Sunray-pleated midi skirt with a soft elastic waist and gentle movement.",
        "Recycled polyester",
        "Machine wash cool",
    ),
    _mk(
        7,
        "Wool Overcoat",
        "Women",
        428.00,
        520.00,
        [_WOMEN_IMGS[3], _WOMEN_IMGS[4], _WOMEN_IMGS[9]],
        4.9,
        132,
        "Editor's Pick",
        ["Camel", "Charcoal"],
        APPAREL_SIZES,
        True,
        False,
        960,
        "A timeless double-breasted overcoat woven from a soft Italian wool-cashmere blend.",
        "80% wool, 20% cashmere",
        "Dry clean only",
    ),
    _mk(
        8,
        "Silk Neck Scarf",
        "Women",
        78.00,
        0.0,
        [_WOMEN_IMGS[6], _WOMEN_IMGS[1], _WOMEN_IMGS[7]],
        4.6,
        88,
        "",
        ["Blush", "Sage", "Ivory"],
        ONE_SIZE,
        True,
        False,
        420,
        "Hand-rolled silk twill scarf in a soft botanical print.",
        "100% silk twill",
        "Dry clean",
    ),
    _mk(
        9,
        "Linen Jumpsuit",
        "Women",
        218.00,
        0.0,
        [_WOMEN_IMGS[8], _WOMEN_IMGS[2], _WOMEN_IMGS[0]],
        4.7,
        51,
        "New",
        ["Cream", "Sage"],
        APPAREL_SIZES,
        True,
        True,
        510,
        "A relaxed wide-leg jumpsuit in washed linen with a tie waist.",
        "100% washed linen",
        "Machine wash cold, line dry",
    ),
    _mk(
        10,
        "Cashmere Knit",
        "Women",
        268.00,
        0.0,
        [_WOMEN_IMGS[4], _WOMEN_IMGS[9], _WOMEN_IMGS[3]],
        4.9,
        174,
        "Bestseller",
        ["Cream", "Blush", "Charcoal"],
        APPAREL_SIZES,
        False,
        False,
        900,
        "Whisper-soft cashmere pullover in a relaxed silhouette with dropped shoulders.",
        "100% Grade-A cashmere",
        "Hand wash cool",
    ),
]

_MEN = [
    _mk(
        11,
        "Cashmere Overcoat",
        "Men",
        348.00,
        420.00,
        [_MEN_IMGS[0], _MEN_IMGS[3], _MEN_IMGS[4]],
        4.7,
        132,
        "Bestseller",
        ["Camel", "Charcoal", "Navy"],
        APPAREL_SIZES,
        True,
        False,
        870,
        "A refined overcoat cut from Italian wool-cashmere, softly tailored for everyday elegance.",
        "80% wool, 20% cashmere",
        "Dry clean only",
    ),
    _mk(
        12,
        "Merino Knit Sweater",
        "Men",
        168.00,
        0.0,
        [_MEN_IMGS[2], _MEN_IMGS[1], _MEN_IMGS[5]],
        4.7,
        55,
        "New",
        ["Sage", "Charcoal", "Cream"],
        APPAREL_SIZES,
        True,
        True,
        620,
        "A finely knit crewneck in ultra-soft merino, made to layer through the seasons.",
        "100% Italian merino wool",
        "Hand wash cool",
    ),
    _mk(
        13,
        "Oxford Cotton Shirt",
        "Men",
        128.00,
        0.0,
        [_MEN_IMGS[1], _MEN_IMGS[6], _MEN_IMGS[0]],
        4.6,
        92,
        "",
        ["Ivory", "Sky", "Sand"],
        APPAREL_SIZES,
        True,
        False,
        540,
        "The heritage oxford — soft brushed cotton with a relaxed collar and pearl buttons.",
        "100% organic cotton",
        "Machine wash cold",
    ),
    _mk(
        14,
        "Suede Loafers",
        "Men",
        224.00,
        0.0,
        [_MEN_IMGS[3], _MEN_IMGS[7], _MEN_IMGS[4]],
        4.8,
        143,
        "Trending",
        ["Camel", "Charcoal"],
        ["40", "41", "42", "43", "44", "45"],
        True,
        False,
        730,
        "Hand-finished suede loafers on a soft leather sole — Italian craftsmanship, quietly done.",
        "Italian suede, leather sole",
        "Wipe clean, use suede brush",
    ),
    _mk(
        15,
        "Linen Trousers",
        "Men",
        158.00,
        0.0,
        [_MEN_IMGS[6], _MEN_IMGS[2], _MEN_IMGS[1]],
        4.6,
        68,
        "",
        ["Sand", "Cream", "Forest"],
        APPAREL_SIZES,
        True,
        False,
        470,
        "A relaxed straight-leg linen trouser with soft pleats and a natural drape.",
        "100% washed linen",
        "Machine wash cool",
    ),
    _mk(
        16,
        "Wool Blazer",
        "Men",
        398.00,
        480.00,
        [_MEN_IMGS[7], _MEN_IMGS[0], _MEN_IMGS[3]],
        4.8,
        84,
        "Editor's Pick",
        ["Charcoal", "Navy"],
        APPAREL_SIZES,
        True,
        False,
        800,
        "An unstructured wool blazer with hand-finished lapels — softly tailored, easily worn.",
        "100% Italian wool",
        "Dry clean only",
    ),
    _mk(
        17,
        "Selvedge Denim",
        "Men",
        178.00,
        0.0,
        [_MEN_IMGS[4], _MEN_IMGS[5], _MEN_IMGS[6]],
        4.7,
        121,
        "New",
        ["Indigo", "Charcoal"],
        APPAREL_SIZES,
        True,
        True,
        640,
        "Japanese selvedge denim, cut to a slim straight leg with a natural mid-rise.",
        "100% selvedge cotton denim",
        "Machine wash cold, inside out",
    ),
    _mk(
        18,
        "Cotton Crew Tee",
        "Men",
        58.00,
        0.0,
        [_MEN_IMGS[5], _MEN_IMGS[1], _MEN_IMGS[2]],
        4.5,
        189,
        "",
        ["Cream", "Sage", "Charcoal", "Blush"],
        APPAREL_SIZES,
        True,
        False,
        720,
        "The essential everyday tee — heavyweight organic cotton with a boxy fit.",
        "100% organic cotton",
        "Machine wash cool",
    ),
]

_HOME = [
    _mk(
        19,
        "Oak Ceramic Vase",
        "Home & Living",
        64.00,
        0.0,
        [_HOME_IMGS[0], _HOME_IMGS[3], _HOME_IMGS[9]],
        4.9,
        88,
        "Editor's Pick",
        ["Sand", "Cream"],
        ONE_SIZE,
        True,
        False,
        830,
        "Hand-thrown stoneware vase with a soft matte glaze — designed to hold seasonal branches.",
        "Stoneware ceramic",
        "Wipe clean with a damp cloth",
    ),
    _mk(
        20,
        "Terracotta Table Lamp",
        "Home & Living",
        142.00,
        0.0,
        [_HOME_IMGS[1], _HOME_IMGS[4], _HOME_IMGS[0]],
        4.6,
        27,
        "New",
        ["Terracotta", "Sand"],
        ONE_SIZE,
        True,
        True,
        380,
        "Sculpted terracotta base with a warm linen shade — a soft glow for quiet evenings.",
        "Terracotta, linen shade",
        "Dust gently, avoid moisture",
    ),
    _mk(
        21,
        "Rattan Pendant Light",
        "Home & Living",
        189.00,
        220.00,
        [_HOME_IMGS[2], _HOME_IMGS[5], _HOME_IMGS[3]],
        4.8,
        178,
        "Trending",
        ["Natural"],
        ONE_SIZE,
        True,
        False,
        910,
        "Hand-woven rattan pendant that casts a soft, patterned light — made in a family workshop.",
        "Natural rattan, brass fittings",
        "Dust with a soft brush",
    ),
    _mk(
        22,
        "Linen Throw Blanket",
        "Home & Living",
        128.00,
        0.0,
        [_HOME_IMGS[6], _HOME_IMGS[9], _HOME_IMGS[3]],
        4.8,
        156,
        "Bestseller",
        ["Cream", "Sage", "Blush"],
        ONE_SIZE,
        True,
        False,
        780,
        "Softly washed linen throw with a subtle fringed edge — the perfect weight for any season.",
        "100% French linen",
        "Machine wash cold, line dry",
    ),
    _mk(
        23,
        "Soy Wax Candle",
        "Home & Living",
        48.00,
        0.0,
        [_HOME_IMGS[4], _HOME_IMGS[8], _HOME_IMGS[0]],
        4.7,
        302,
        "Bestseller",
        ["Sand"],
        ONE_SIZE,
        True,
        False,
        850,
        "Hand-poured soy wax candle scented with fig, cedar, and orange blossom.",
        "Soy wax, cotton wick",
        "Trim wick to 5mm before each burn",
    ),
    _mk(
        24,
        "Stoneware Bowl Set",
        "Home & Living",
        98.00,
        128.00,
        [_HOME_IMGS[7], _HOME_IMGS[0], _HOME_IMGS[3]],
        4.9,
        64,
        "",
        ["Cream", "Sage"],
        ONE_SIZE,
        True,
        False,
        490,
        "A set of four hand-glazed stoneware bowls — no two are exactly alike.",
        "Stoneware ceramic",
        "Dishwasher safe, avoid microwave",
    ),
    _mk(
        25,
        "Linen Cushion Cover",
        "Home & Living",
        58.00,
        0.0,
        [_HOME_IMGS[9], _HOME_IMGS[6], _HOME_IMGS[3]],
        4.6,
        112,
        "",
        ["Cream", "Sage", "Blush", "Charcoal"],
        ONE_SIZE,
        True,
        False,
        460,
        "Softly textured linen cushion cover with a hidden zip closure.",
        "100% linen",
        "Machine wash cool",
    ),
    _mk(
        26,
        "Brass Wall Mirror",
        "Home & Living",
        218.00,
        0.0,
        [_HOME_IMGS[8], _HOME_IMGS[5], _HOME_IMGS[2]],
        4.7,
        42,
        "New",
        ["Brass"],
        ONE_SIZE,
        True,
        True,
        320,
        "A softly arched wall mirror framed in hand-finished brushed brass.",
        "Brass frame, glass",
        "Polish gently with a soft cloth",
    ),
    _mk(
        27,
        "Ceramic Planter",
        "Home & Living",
        78.00,
        0.0,
        [_HOME_IMGS[5], _HOME_IMGS[0], _HOME_IMGS[7]],
        4.6,
        89,
        "",
        ["Cream", "Terracotta"],
        ONE_SIZE,
        True,
        False,
        410,
        "A generously scaled indoor planter with a soft matte finish and drainage tray.",
        "Stoneware ceramic",
        "Wipe clean",
    ),
    _mk(
        28,
        "Wooden Serving Tray",
        "Home & Living",
        88.00,
        0.0,
        [_HOME_IMGS[3], _HOME_IMGS[7], _HOME_IMGS[9]],
        4.7,
        76,
        "",
        ["Natural"],
        ONE_SIZE,
        False,
        False,
        380,
        "Hand-turned oak serving tray with soft rounded edges and forged brass handles.",
        "Solid oak, brass handles",
        "Wipe clean, oil occasionally",
    ),
]

_BEAUTY = [
    _mk(
        29,
        "Botanical Facial Oil",
        "Beauty",
        58.00,
        0.0,
        [_BEAUTY_IMGS[0], _BEAUTY_IMGS[3], _BEAUTY_IMGS[4]],
        4.9,
        302,
        "Bestseller",
        ["30ml"],
        ONE_SIZE,
        True,
        False,
        940,
        "A weightless botanical facial oil that leaves skin softly luminous — rosehip, jojoba and squalane.",
        "Rosehip, jojoba, squalane",
        "Apply 3–4 drops morning and night",
    ),
    _mk(
        30,
        "Rose Quartz Roller",
        "Beauty",
        42.00,
        58.00,
        [_BEAUTY_IMGS[2], _BEAUTY_IMGS[0], _BEAUTY_IMGS[5]],
        4.9,
        421,
        "Trending",
        ["Rose"],
        ONE_SIZE,
        True,
        False,
        970,
        "Cool rose quartz face roller — a five-minute ritual to soothe and sculpt.",
        "Rose quartz, brass fittings",
        "Store in a cool place, wipe clean",
    ),
    _mk(
        31,
        "Cleansing Balm",
        "Beauty",
        48.00,
        0.0,
        [_BEAUTY_IMGS[3], _BEAUTY_IMGS[1], _BEAUTY_IMGS[0]],
        4.8,
        217,
        "",
        ["100ml"],
        ONE_SIZE,
        True,
        False,
        780,
        "Melt-in balm cleanser that dissolves the day gently — with camellia, oat and chamomile.",
        "Camellia oil, oat, chamomile",
        "Massage into dry skin, rinse warm",
    ),
    _mk(
        32,
        "Hand & Body Cream",
        "Beauty",
        38.00,
        0.0,
        [_BEAUTY_IMGS[1], _BEAUTY_IMGS[4], _BEAUTY_IMGS[6]],
        4.7,
        168,
        "New",
        ["Fig", "Neroli"],
        ONE_SIZE,
        True,
        True,
        690,
        "A cocooning cream in a naturally derived base of shea and almond oils.",
        "Shea butter, almond oil",
        "Massage in as often as loved",
    ),
    _mk(
        33,
        "Silk Sleep Mask",
        "Beauty",
        42.00,
        0.0,
        [_BEAUTY_IMGS[5], _BEAUTY_IMGS[2], _BEAUTY_IMGS[7]],
        4.6,
        94,
        "",
        ["Blush", "Ivory", "Sage"],
        ONE_SIZE,
        True,
        False,
        420,
        "Adjustable silk sleep mask with a soft mulberry-silk lining for gentler rest.",
        "100% mulberry silk",
        "Hand wash cool",
    ),
    _mk(
        34,
        "Bath Salts",
        "Beauty",
        34.00,
        0.0,
        [_BEAUTY_IMGS[4], _BEAUTY_IMGS[6], _BEAUTY_IMGS[0]],
        4.7,
        122,
        "",
        ["Lavender", "Cedar"],
        ONE_SIZE,
        True,
        False,
        460,
        "Mineral-rich bath salts blended with pure essential oils for a slow, quiet soak.",
        "Sea salt, essential oils",
        "Dissolve two handfuls in warm water",
    ),
    _mk(
        35,
        "Botanical Perfume",
        "Beauty",
        88.00,
        0.0,
        [_BEAUTY_IMGS[7], _BEAUTY_IMGS[3], _BEAUTY_IMGS[5]],
        4.8,
        148,
        "Editor's Pick",
        ["50ml"],
        ONE_SIZE,
        True,
        False,
        810,
        "A softly grounded scent of fig leaf, cedar and warm amber — quietly present.",
        "Alcohol denat., natural extracts",
        "Spray onto pulse points",
    ),
    _mk(
        36,
        "Overnight Serum",
        "Beauty",
        78.00,
        0.0,
        [_BEAUTY_IMGS[6], _BEAUTY_IMGS[1], _BEAUTY_IMGS[3]],
        4.8,
        189,
        "New",
        ["30ml"],
        ONE_SIZE,
        True,
        True,
        720,
        "A gentle bakuchiol and niacinamide serum that helps skin wake softer, brighter.",
        "Bakuchiol, niacinamide, squalane",
        "Apply nightly to clean skin",
    ),
]

_ACC = [
    _mk(
        37,
        "Leather Weekender",
        "Accessories",
        289.00,
        0.0,
        [_ACC_IMGS[1], _ACC_IMGS[3], _ACC_IMGS[0]],
        4.9,
        63,
        "New",
        ["Camel", "Charcoal"],
        ONE_SIZE,
        True,
        True,
        640,
        "Hand-finished leather weekender with brass hardware and a soft cotton lining.",
        "Vegetable-tanned leather",
        "Wipe clean, condition annually",
    ),
    _mk(
        38,
        "Woven Straw Hat",
        "Accessories",
        118.00,
        0.0,
        [_ACC_IMGS[0], _ACC_IMGS[4], _ACC_IMGS[2]],
        4.7,
        82,
        "",
        ["Natural"],
        ONE_SIZE,
        True,
        False,
        520,
        "A wide-brimmed woven hat with a soft leather band — for softer, sunlit days.",
        "Natural straw, leather band",
        "Store flat, avoid moisture",
    ),
    _mk(
        39,
        "Acetate Sunglasses",
        "Accessories",
        168.00,
        210.00,
        [_ACC_IMGS[4], _ACC_IMGS[5], _ACC_IMGS[1]],
        4.8,
        141,
        "Bestseller",
        ["Tortoise", "Charcoal", "Cream"],
        ONE_SIZE,
        True,
        False,
        760,
        "Italian-made acetate frames with UV400 lenses — a softly rounded silhouette.",
        "Italian acetate, UV400 lenses",
        "Store in the included case",
    ),
    _mk(
        40,
        "Gold Signet Ring",
        "Accessories",
        148.00,
        0.0,
        [_ACC_IMGS[2], _ACC_IMGS[3], _ACC_IMGS[5]],
        4.9,
        96,
        "",
        ["Gold"],
        ["6", "7", "8", "9"],
        True,
        False,
        610,
        "A softly domed signet ring in recycled 14k gold vermeil.",
        "14k gold vermeil on sterling silver",
        "Polish with a soft jewellery cloth",
    ),
    _mk(
        41,
        "Leather Card Wallet",
        "Accessories",
        88.00,
        0.0,
        [_ACC_IMGS[5], _ACC_IMGS[0], _ACC_IMGS[3]],
        4.6,
        118,
        "",
        ["Camel", "Charcoal", "Forest"],
        ONE_SIZE,
        True,
        False,
        480,
        "Slim vegetable-tanned leather card wallet — softens beautifully over time.",
        "Vegetable-tanned leather",
        "Wipe clean, condition annually",
    ),
    _mk(
        42,
        "Woven Belt",
        "Accessories",
        78.00,
        0.0,
        [_ACC_IMGS[3], _ACC_IMGS[1], _ACC_IMGS[0]],
        4.5,
        74,
        "",
        ["Cream", "Charcoal", "Camel"],
        ["S", "M", "L"],
        False,
        False,
        340,
        "A soft woven belt with a hand-finished leather tab and antique brass buckle.",
        "Woven cotton, leather, brass",
        "Wipe clean",
    ),
]

ALL_PRODUCTS: list[ShopProduct] = _WOMEN + _MEN + _HOME + _BEAUTY + _ACC


_REVIEW_POOL: list[Review] = [
    {
        "author": "Amelia L.",
        "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=amelia",
        "rating": 5,
        "date": "2 weeks ago",
        "title": "Beautifully made",
        "body": "The quality is extraordinary — softer and more elegant than I expected. Wearing it feels like a small ritual.",
    },
    {
        "author": "Jonah R.",
        "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=jonah",
        "rating": 5,
        "date": "1 month ago",
        "title": "Everyday favourite",
        "body": "I reach for this constantly. It looks considered every time and only feels better with wear.",
    },
    {
        "author": "Priya A.",
        "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=priya",
        "rating": 4,
        "date": "3 weeks ago",
        "title": "A quiet luxury",
        "body": "The materials feel thoughtful and lasting. Runs slightly generous — size down if between sizes.",
    },
    {
        "author": "Marcus D.",
        "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=marcus",
        "rating": 5,
        "date": "5 days ago",
        "title": "Perfect weight",
        "body": "The finish is beautiful and the packaging arrived like a gift. Highly recommend to a friend.",
    },
    {
        "author": "Ines K.",
        "avatar": "https://api.dicebear.com/9.x/notionists/svg?seed=ines",
        "rating": 4,
        "date": "2 months ago",
        "title": "Timeless piece",
        "body": "Exactly the kind of piece I hoped for — quietly beautiful, and made to be worn for years.",
    },
]


_CATEGORY_ROUTE = {
    "women": "Women",
    "men": "Men",
    "home-living": "Home & Living",
    "beauty": "Beauty",
    "accessories": "Accessories",
}


DEFAULT_PRODUCT: ShopProduct = {
    "id": 0,
    "name": "",
    "category": "",
    "price": 0.0,
    "old_price": 0.0,
    "image": "",
    "images": [],
    "rating": 0.0,
    "reviews_count": 0,
    "badge": "",
    "colors": [],
    "sizes": [],
    "in_stock": True,
    "is_new": False,
    "popularity": 0,
    "description": "",
    "materials": "",
    "care": "",
}


class ShopState(rx.State):
    products: list[ShopProduct] = ALL_PRODUCTS

    # ----- filters -----
    active_category: str = ""  # "" means all
    min_price: int = 0
    max_price: int = 500
    selected_colors: list[str] = []
    selected_sizes: list[str] = []
    min_rating: int = 0
    in_stock_only: bool = False
    search_q: str = ""

    # ----- sort + pagination -----
    sort_by: str = (
        "popular"  # latest | price_low | price_high | popular | best_rated
    )
    page: int = 1
    per_page: int = 12

    # ----- product detail -----
    current_product_id: int = 0
    active_image_index: int = 0
    detail_selected_size: str = ""
    detail_selected_color: str = ""
    detail_quantity: int = 1

    # ----- wishlist / cart -----
    wishlist_ids: list[int] = []

    # ----- filter panel (mobile) -----
    filters_open: bool = False

    all_colors: list[str] = [
        "Cream",
        "Ivory",
        "Sand",
        "Sage",
        "Forest",
        "Blush",
        "Charcoal",
        "Camel",
        "Navy",
        "Terracotta",
        "Natural",
        "Brass",
        "Gold",
        "Tortoise",
        "Indigo",
        "Sky",
    ]
    all_sizes: list[str] = [
        "XS",
        "S",
        "M",
        "L",
        "XL",
        "One Size",
        "40",
        "41",
        "42",
        "43",
        "44",
        "45",
        "6",
        "7",
        "8",
        "9",
    ]
    all_categories: list[str] = [
        "Women",
        "Men",
        "Home & Living",
        "Beauty",
        "Accessories",
    ]

    sort_options: list[dict[str, str]] = [
        {"key": "popular", "label": "Most popular"},
        {"key": "latest", "label": "Latest arrivals"},
        {"key": "best_rated", "label": "Best rated"},
        {"key": "price_low", "label": "Price: low to high"},
        {"key": "price_high", "label": "Price: high to low"},
    ]

    # ---------- computed ----------
    @rx.var
    def filtered_products(self) -> list[ShopProduct]:
        results: list[ShopProduct] = []
        q = self.search_q.strip().lower()
        for p in self.products:
            if self.active_category and p["category"] != self.active_category:
                continue
            if p["price"] < self.min_price or p["price"] > self.max_price:
                continue
            if self.min_rating > 0 and p["rating"] < self.min_rating:
                continue
            if self.in_stock_only and not p["in_stock"]:
                continue
            if self.selected_colors:
                if not any(c in p["colors"] for c in self.selected_colors):
                    continue
            if self.selected_sizes:
                if not any(s in p["sizes"] for s in self.selected_sizes):
                    continue
            if q:
                hay = f"{p['name']} {p['category']} {p['description']}".lower()
                if q not in hay:
                    continue
            results.append(p)
        # sort
        if self.sort_by == "price_low":
            results.sort(key=lambda x: x["price"])
        elif self.sort_by == "price_high":
            results.sort(key=lambda x: x["price"], reverse=True)
        elif self.sort_by == "best_rated":
            results.sort(key=lambda x: x["rating"], reverse=True)
        elif self.sort_by == "latest":
            results.sort(key=lambda x: (x["is_new"], x["id"]), reverse=True)
        else:  # popular
            results.sort(key=lambda x: x["popularity"], reverse=True)
        return results

    @rx.var
    def total_results(self) -> int:
        return len(self.filtered_products)

    @rx.var
    def total_pages(self) -> int:
        n = self.total_results
        if n == 0:
            return 1
        return (n + self.per_page - 1) // self.per_page

    @rx.var
    def paginated_products(self) -> list[ShopProduct]:
        start = (self.page - 1) * self.per_page
        return self.filtered_products[start : start + self.per_page]

    @rx.var
    def page_numbers(self) -> list[int]:
        return list(range(1, self.total_pages + 1))

    @rx.var
    def has_active_filters(self) -> bool:
        return (
            bool(self.active_category)
            or self.min_price > 0
            or self.max_price < 500
            or bool(self.selected_colors)
            or bool(self.selected_sizes)
            or self.min_rating > 0
            or self.in_stock_only
            or bool(self.search_q)
        )

    @rx.var
    def category_heading(self) -> str:
        return self.active_category if self.active_category else "The Full Shop"

    @rx.var
    def category_subtitle(self) -> str:
        subtitles = {
            "Women": "Softly considered pieces for a slower rhythm of dressing.",
            "Men": "Quietly refined essentials, made to last a decade.",
            "Home & Living": "Objects for a calmer, more considered home.",
            "Beauty": "Botanical rituals for skin, body, and quiet moments.",
            "Accessories": "The finishing pieces — hand-finished, softly detailed.",
        }
        return subtitles.get(
            self.active_category,
            "A curated edit across the house — clothing, home, beauty and beyond.",
        )

    # ----- product detail computed -----
    @rx.var
    def current_product(self) -> ShopProduct:
        for p in self.products:
            if p["id"] == self.current_product_id:
                return p
        return DEFAULT_PRODUCT

    @rx.var
    def current_reviews(self) -> list[Review]:
        # cycle three reviews based on product id
        pid = max(self.current_product_id, 1)
        start = pid % len(_REVIEW_POOL)
        pool = _REVIEW_POOL + _REVIEW_POOL
        return pool[start : start + 3]

    @rx.var
    def rating_breakdown(self) -> list[dict[str, int]]:
        p = self.current_product
        total = max(p["reviews_count"], 1)
        # roughly weighted distribution
        r = p["rating"]
        buckets = [
            {"stars": 5, "pct": int(min(96, 40 + (r - 4) * 55))},
            {"stars": 4, "pct": int(max(4, 40 - (r - 4) * 20))},
            {"stars": 3, "pct": int(max(2, 12 - (r - 4) * 6))},
            {"stars": 2, "pct": 2},
            {"stars": 1, "pct": 1},
        ]
        _ = total
        return buckets

    @rx.var
    def related_products(self) -> list[ShopProduct]:
        cur = self.current_product
        out = [
            p
            for p in self.products
            if p["category"] == cur["category"] and p["id"] != cur["id"]
        ]
        return out[:4]

    @rx.var
    def current_main_image(self) -> str:
        p = self.current_product
        if not p["images"]:
            return p["image"]
        idx = self.active_image_index
        if idx < 0 or idx >= len(p["images"]):
            return p["images"][0]
        return p["images"][idx]

    @rx.var
    def wishlist_count(self) -> int:
        return len(self.wishlist_ids)

    @rx.var
    def wishlist_products(self) -> list[ShopProduct]:
        by_id = {p["id"]: p for p in self.products}
        out: list[ShopProduct] = []
        for pid in self.wishlist_ids:
            p = by_id.get(pid)
            if p is not None:
                out.append(p)
        return out

    # ---------- event handlers ----------
    def _reset_page(self):
        self.page = 1

    @rx.event
    def load_all(self):
        self.active_category = ""
        self.search_q = ""
        self._reset_page()

    @rx.event
    def load_category(self):
        slug = self.router.page.params.get("category", "")
        self.active_category = _CATEGORY_ROUTE.get(slug, "")
        self._reset_page()

    @rx.event
    def load_search(self):
        q = self.router.url.query_parameters.get("q", "")
        self.search_q = q
        self.active_category = ""
        self._reset_page()

    @rx.event
    def load_product(self):
        pid_str = self.router.page.params.get("product_id", "0")
        try:
            self.current_product_id = int(pid_str)
        except ValueError:
            self.current_product_id = 0
        self.active_image_index = 0
        p = self.current_product
        self.detail_selected_size = p["sizes"][0] if p["sizes"] else ""
        self.detail_selected_color = p["colors"][0] if p["colors"] else ""
        self.detail_quantity = 1

    @rx.event
    def set_category(self, cat: str):
        self.active_category = cat
        self._reset_page()

    @rx.event
    def set_sort(self, key: str):
        self.sort_by = key
        self._reset_page()

    @rx.event
    def set_min_price(self, v: str):
        try:
            self.min_price = max(0, int(float(v)))
        except ValueError:
            self.min_price = 0
        self._reset_page()

    @rx.event
    def set_max_price(self, v: str):
        try:
            self.max_price = min(500, int(float(v)))
        except ValueError:
            self.max_price = 500
        self._reset_page()

    @rx.event
    def toggle_color(self, color: str):
        if color in self.selected_colors:
            self.selected_colors.remove(color)
        else:
            self.selected_colors.append(color)
        self._reset_page()

    @rx.event
    def toggle_size(self, size: str):
        if size in self.selected_sizes:
            self.selected_sizes.remove(size)
        else:
            self.selected_sizes.append(size)
        self._reset_page()

    @rx.event
    def set_min_rating(self, r: int):
        self.min_rating = r if self.min_rating != r else 0
        self._reset_page()

    @rx.event
    def toggle_in_stock(self):
        self.in_stock_only = not self.in_stock_only
        self._reset_page()

    @rx.event
    def clear_filters(self):
        self.min_price = 0
        self.max_price = 500
        self.selected_colors = []
        self.selected_sizes = []
        self.min_rating = 0
        self.in_stock_only = False
        self.search_q = ""
        self._reset_page()

    @rx.event
    def set_search_q(self, v: str):
        self.search_q = v
        self._reset_page()

    @rx.event
    def submit_search(self, form_data: dict):
        q = form_data.get("q", "").strip()
        self.search_q = q
        self._reset_page()
        return rx.redirect(f"/search?q={q}")

    @rx.event
    def go_to_page(self, p: int):
        if 1 <= p <= self.total_pages:
            self.page = p

    @rx.event
    def next_page(self):
        if self.page < self.total_pages:
            self.page += 1

    @rx.event
    def prev_page(self):
        if self.page > 1:
            self.page -= 1

    @rx.event
    def toggle_filters(self):
        self.filters_open = not self.filters_open

    # ----- product detail actions -----
    @rx.event
    def set_active_image(self, index: int):
        self.active_image_index = index

    @rx.event
    def select_detail_size(self, s: str):
        self.detail_selected_size = s

    @rx.event
    def select_detail_color(self, c: str):
        self.detail_selected_color = c

    @rx.event
    def inc_quantity(self):
        if self.detail_quantity < 10:
            self.detail_quantity += 1

    @rx.event
    def dec_quantity(self):
        if self.detail_quantity > 1:
            self.detail_quantity -= 1

    # ----- wishlist / cart (sync to HomeState for navbar badge) -----
    @rx.event
    async def toggle_wishlist(self, product_id: int):
        from app.states.home_state import HomeState

        if product_id in self.wishlist_ids:
            self.wishlist_ids.remove(product_id)
            home = await self.get_state(HomeState)
            if home.wishlist_count > 0:
                home.wishlist_count -= 1
            return rx.toast("Removed from wishlist.")
        self.wishlist_ids.append(product_id)
        home = await self.get_state(HomeState)
        home.wishlist_count += 1
        return rx.toast.success("Saved to wishlist.")

    @rx.event
    async def add_to_cart(self, product_id: int):
        from app.states.cart_state import CartState

        product = None
        for p in self.products:
            if p["id"] == product_id:
                product = p
                break
        if product is None:
            return rx.toast.error("That piece is no longer available.")
        cart = await self.get_state(CartState)
        size = product["sizes"][0] if product["sizes"] else ""
        color = product["colors"][0] if product["colors"] else ""
        return await cart.add_item(
            product["id"],
            product["name"],
            product["category"],
            product["image"],
            product["price"],
            1,
            size,
            color,
        )

    @rx.event
    async def add_current_to_cart(self):
        from app.states.cart_state import CartState

        p = self.current_product
        if p["id"] == 0:
            return rx.toast.error("That piece is no longer available.")
        cart = await self.get_state(CartState)
        return await cart.add_item(
            p["id"],
            p["name"],
            p["category"],
            p["image"],
            p["price"],
            self.detail_quantity,
            self.detail_selected_size,
            self.detail_selected_color,
        )
