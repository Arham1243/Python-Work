info = [
    {"img_path": "1379358706_content_10_SM.jpg", "title": " Cafe Vienna"},
    {"img_path": "IMG_13262_SM.jpg", "title": " Chiavari Chair"},
    {"img_path": "DSC02039_SM.JPG", "title": " Wood Folding Chairs"},
    {"img_path": "Plastic_Folding_Chairs_SM.JPG", "title": " Plastic Folding Chairs"},
    {"img_path": "Spandex_Cocktail_Table_White_SM.JPG", "title": " Bar Stools"},
    {"img_path": "High_Chairs_SM.jpg", "title": " High Chairs"},
    {
        "img_path": "Resin_folding_chair_for_ceremony_SM.jpg",
        "title": " Resin folding chair",
    },
    {
        "img_path": "Crossback_Vineyard_Chairs-lights-in-a-clear-top-tent_SM.jpg",
        "title": " Crossback Vineyard Chairs",
    },
    {"img_path": "King_Throne_Chair__Gold_on_White_SM.jpg", "title": " Special chair"},
    {
        "img_path": "All_Occasion_Rentals_Tolix-Chair-Rusty_SM.jpg",
        "title": " TOLIX CHAIR",
    },
    {"img_path": "Farm_Bench_1_SM.jpg", "title": " Farm Bench"},
    {"img_path": "Dance%20Floor%20(2).jpg", "title": " DANCE FLOOR COLOR OAK"},
    {
        "img_path": "All%20Occasion%20Rentals%20Black-and-White-Dance-Floor-5.jpg",
        "title": " DANCE FLOOR BLACK, WHITE & CHECK",
    },
    {"img_path": "0001_SM.jpg", "title": " Wedding Bouquets"},
    {"img_path": "001_SM.jpg", "title": " Center Pieces"},
    {"img_path": "IMG_8422_SM.jpg", "title": " Cake Flower"},
    {"img_path": "IMG_2533_SM.JPG", "title": " Ceremony Flowers"},
    {"img_path": "Chair%20Covers.jpg", "title": " Chair Covers"},
    {"img_path": "Pictures111_192_SM.jpg", "title": " Polyester"},
    {
        "img_path": "All%20Occasion%20Rentals%20Wooden%20Swings.jpg",
        "title": " Wooden Swings",
    },
    {
        "img_path": "ivory-table-linens-round_4_SM.jpg",
        "title": " 90 Round Polyester Tablecloth",
    },
    {"img_path": "Linen_Skirtingv2_SM.jpg", "title": " 120'Round Polyester Tablecloth"},
    {"img_path": "IMG_1326.jpg", "title": " 132 Round Polyester Tablecloth"},
    {
        "img_path": "90_x_132_inch_Rectangular_Red_Tablecloth_Polyester_SM.jpg",
        "title": " 6 ft Polyester Table Drape",
    },
    {
        "img_path": "90_x_156_inch_Rectangular_Burgundy_Tablecloth_Polyester_SM.jpg",
        "title": " 8 ft Polyester Table Drape",
    },
    {
        "img_path": "10_ft_banquet_table_linen_ivory_SM.jpg",
        "title": " 10 ft banquet table linen",
    },
    {"img_path": "black-table-skirt_2_SM.jpg", "title": " Polyester Table Skirt"},
    {"img_path": "Spandex_Tablecloth_SM.jpg", "title": " Spandex Tablecloth"},
    {"img_path": "NAPKIN_POLYESTER_v2_SM.jpg", "title": " Polyester Napkins"},
    {"img_path": "IMG_1379_SM.jpg", "title": " Satin Napkins"},
    {"img_path": "add2.jpg", "title": " Chair Covers"},
    {"img_path": "P1010063v2.JPG", "title": " Organza Sashes"},
    {"img_path": "DSCN0444v2.jpg", "title": " Round Tablecloths Satin"},
    {"img_path": "01_(476x490)_SM.jpg", "title": " Wedding Arch and Chuppah"},
    {"img_path": "Columns_SM.jpg", "title": " Wedding Columns"},
    {"img_path": "Red-Carpet-Runner_SM.jpg", "title": " Ground Covering"},
    {"img_path": "Portable_Crowd_Fence_SM.gif", "title": " Portable Crowd Fence"},
    {"img_path": "Boxwood_hedges_SM.jpg", "title": " Boxwood Hedge Panels"},
    {"img_path": "Umbrella_SM.jpg", "title": " Umbrella"},
    {"img_path": "Bike_Rack_All_Occasion_Rentals_SM.jpg", "title": " Bike Rack"},
    {"img_path": "Tent_Bener_30x60_SM.jpg", "title": " Tent Rentals"},
    {
        "img_path": "High-Peak-Tent-20x40_v2_SM.jpg",
        "title": " Quick Peak style frame tent",
    },
    {
        "img_path": "Clearspan_Structure_Tents_SM.jpg",
        "title": " Clearspan Structure Tents",
    },
    {"img_path": "Tent_Sidewalls_SM.jpg", "title": " Tent Sidewall"},
    {"img_path": "EZ_Up_Canopy_SM.jpg", "title": " EZ Up Canopy"},
    {"img_path": "Tent_Bener_SM.jpg", "title": " Tent Lighting"},
    {"img_path": "DSC04862v3_SM.jpg", "title": " Tent Accessories"},
    {"img_path": "All_Occasion_Rentals_SM.jpg", "title": " Tent Liners"},
    {"img_path": "2-pole_tent_SM.jpg", "title": " Pole Tents"},
    {
        "img_path": "building-under-construction-site-free-vector_SM.jpg",
        "title": " Test Tent",
    },
    {
        "img_path": "building-under-construction-site-free-vector_SM.jpg",
        "title": " Test Tent #2",
    },
    {"img_path": "Serving%20Equipments%20-%20V2.JPG", "title": " Charger Plates"},
    {
        "img_path": "Chocolate%20Fountain%20-%2031-%20Copy.jpg",
        "title": " Chocolate Fountain",
    },
    {"img_path": "Beverage%20%20Dispensers-v2.jpg", "title": " Popcorn Machine"},
]


import os
from slugify import slugify

new_data = []

for data in info:
    try:
        folder_name = "images"
        img_path = data["img_path"]
        title = data["title"]
        files = os.listdir(folder_name)
        slug = slugify(title)
        ext = img_path.split(".")[-1]
        new_img_path = f"{slug}.{ext}"
        new_info = {}
        new_info['title'] = title
        new_info['img_path'] = new_img_path
        new_data.append(new_info)
        os.rename(os.path.join(folder_name, img_path), os.path.join(folder_name, new_img_path))
    except Exception as e:
        print(e)