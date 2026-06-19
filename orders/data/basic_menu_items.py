KITCHEN_STATIONS = {
    "steam": {
        "name": "Steam Station",
        "description": "Momo steaming and dumpling preparation",
    },
    "grill": {
        "name": "Grill Station",
        "description": "Sekuwa, Choila, Sukuti and grilled items",
    },
    "main_kitchen": {
        "name": "Main Kitchen",
        "description": "Dal Bhat, Thakali, Dhido and curry dishes",
    },
    "breakfast": {
        "name": "Breakfast Station",
        "description": "Breakfast and morning specials",
    },
    "beverage": {
        "name": "Beverage Station",
        "description": "Tea, coffee and cold drinks",
    },
    "dessert": {
        "name": "Dessert Station",
        "description": "Desserts and sweets",
    },
}

RESTAURANT_MENU_ITEMS = {
    "snacks": [
        {
            "name": "Momo (Buff)",
            "price": 180,
            "priority": 3,
            "est_time": 15,
            "station": "steam",
        },
        {
            "name": "Momo (Chicken)",
            "price": 200,
            "priority": 3,
            "est_time": 15,
            "station": "steam",
        },
        {
            "name": "Momo (Veg)",
            "price": 160,
            "priority": 2,
            "est_time": 12,
            "station": "steam",
        },
        {
            "name": "Chatamari",
            "price": 150,
            "priority": 2,
            "est_time": 10,
            "station": "grill",
        },
        {
            "name": "Sekuwa",
            "price": 250,
            "priority": 3,
            "est_time": 18,
            "station": "grill",
        },
        {
            "name": "Choila",
            "price": 220,
            "priority": 3,
            "est_time": 12,
            "station": "grill",
        },
        {
            "name": "Aloo Tama",
            "price": 140,
            "priority": 1,
            "est_time": 8,
            "station": "main_kitchen",
        },
        {
            "name": "Wai Wai Sadeko",
            "price": 120,
            "priority": 1,
            "est_time": 5,
            "station": "main_kitchen",
        },
    ],

    "breakfast": [
        {
            "name": "Sel Roti with Aloo Tarkari",
            "price": 180,
            "priority": 3,
            "est_time": 15,
            "station": "breakfast",
        },
        {
            "name": "Chiura with Tarkari",
            "price": 160,
            "priority": 2,
            "est_time": 10,
            "station": "breakfast",
        },
        {
            "name": "Anda Paratha",
            "price": 150,
            "priority": 2,
            "est_time": 12,
            "station": "breakfast",
        },
        {
            "name": "Puri Tarkari",
            "price": 140,
            "priority": 1,
            "est_time": 10,
            "station": "breakfast",
        },
        {
            "name": "Jeri Swari",
            "price": 130,
            "priority": 1,
            "est_time": 5,
            "station": "breakfast",
        },
    ],

    "lunch": [
        {
            "name": "Dal Bhat Tarkari (Veg)",
            "price": 280,
            "priority": 3,
            "est_time": 15,
            "station": "main_kitchen",
        },
        {
            "name": "Dal Bhat Tarkari (Chicken)",
            "price": 380,
            "priority": 3,
            "est_time": 20,
            "station": "main_kitchen",
        },
        {
            "name": "Dal Bhat Tarkari (Mutton)",
            "price": 500,
            "priority": 2,
            "est_time": 25,
            "station": "main_kitchen",
        },
        {
            "name": "Thakali Khana Set",
            "price": 450,
            "priority": 3,
            "est_time": 20,
            "station": "main_kitchen",
        },
        {
            "name": "Gundruk Dhido Set",
            "price": 350,
            "priority": 2,
            "est_time": 18,
            "station": "main_kitchen",
        },
    ],

    # same pattern for dinner, drinks, desserts, specials...
}