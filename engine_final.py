import random

SKIN_PROFILES = {"Medium_Warm": {}, "Deep_Cool": {}}

def load_master_colors():
    return {
        "White": {"hex": "#FFFFFF"},
        "Black": {"hex": "#000000"},
        "Navy": {"hex": "#001F5B"},
        "Olive": {"hex": "#708238"},
        "Beige": {"hex": "#F5F5DC"},
        "Grey": {"hex": "#808080"},
        "Rust": {"hex": "#B7410E"},
        "Mustard": {"hex": "#FFDB58"},
        "Sky Blue": {"hex": "#87CEEB"},
        "Forest Green": {"hex": "#228B22"},
    }

def generate_recommendations(input_data):
    colors = load_master_colors()
    items = list(colors.keys())
    def build(n):
        return [{"color": c, "hex": colors[c]["hex"]} for c in random.sample(items, n)]
    return {
        "smart_shirts": build(5),
        "smart_pants": build(4),
        "all_season_neutrals": build(5)
    }
