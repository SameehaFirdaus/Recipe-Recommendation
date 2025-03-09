import streamlit as st

# Sample recipe data
recipes = {
    "Chicken Biryani": {
        "ingredients": ["chicken", "basmati rice", "onion", "yogurt", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken with spices, add rice and yogurt, and cook until done."
    },
    "Butter Chicken": {
        "ingredients": ["chicken", "butter", "cream", "tomato puree", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken in butter, add tomato puree and cream, and simmer."
    },
    "Fish Curry": {
        "ingredients": ["fish", "coconut milk", "onion", "tomato", "garlic", "ginger", "curry leaves", "spices"],
        "instructions": "Cook onion and spices, add fish and coconut milk, and simmer."
    },
    "Mutton Rogan Josh": {
        "ingredients": ["mutton", "yogurt", "onion", "garlic", "ginger", "spices"],
        "instructions": "Cook mutton with spices and yogurt until tender."
    },
    "Chicken Tikka Masala": {
        "ingredients": ["chicken", "yogurt", "tomato", "cream", "garlic", "ginger", "spices"],
        "instructions": "Marinate chicken in yogurt, grill, and then cook in a tomato cream sauce."
    },
    "Prawn Masala": {
        "ingredients": ["prawns", "onion", "tomato", "coconut milk", "garlic", "ginger", "spices"],
        "instructions": "Cook prawns with onion, tomato, and spices, then add coconut milk."
    },
    "Egg Curry": {
        "ingredients": ["eggs", "onion", "tomato", "garlic", "ginger", "spices"],
        "instructions": "Boil eggs, then cook with onion, tomato, and spices."
    },
    "Tandoori Chicken": {
        "ingredients": ["chicken", "yogurt", "lemon juice", "garlic", "ginger", "spices"],
        "instructions": "Marinate chicken in yogurt, lemon juice, and spices, then grill."
    },
    "Kadai Chicken": {
        "ingredients": ["chicken", "bell pepper", "onion", "tomato", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken with bell peppers, onion, and spices."
    },
    "Chettinad Chicken": {
        "ingredients": ["chicken", "coconut", "onion", "tomato", "garlic", "ginger", "spices"],
        "instructions": "Cook chicken with coconut and spices."
    },
    "Paneer Tikka": {
        "ingredients": ["paneer", "yogurt", "bell pepper", "onion", "spices"],
        "instructions": "Marinate paneer in yogurt and spices, then grill with vegetables."
    },
    "Hakka Noodles": {
        "ingredients": ["noodles", "chicken", "bell pepper", "soy sauce", "garlic", "ginger", "vegetables"],
        "instructions": "Stir-fry noodles with chicken and vegetables."
    },
    "Samosa": {
        "ingredients": ["potatoes", "peas", "spices", "flour", "oil"],
        "instructions": "Make a filling with potatoes and peas, wrap in dough, and fry."
    },
    "Aloo Tikki": {
        "ingredients": ["potatoes", "peas", "spices", "bread crumbs", "oil"],
        "instructions": "Mash potatoes and peas, form into patties, and fry."
    },
    "Chole Bhature": {
        "ingredients": ["chickpeas", "flour", "yogurt", "spices", "onion", "tomato"],
        "instructions": "Cook chickpeas with spices and serve with fried bread."
    },
    "Gulab Jamun": {
        "ingredients": ["milk powder", "flour", "sugar", "ghee", "cardamom"],
        "instructions": "Make dough, shape into balls, fry, and soak in sugar syrup."
    },
    "Jalebi": {
        "ingredients": ["maida", "sugar", "yogurt", "saffron", "ghee"],
        "instructions": "Make a batter, fry in spiral shapes, and soak in sugar syrup."
    },
    "Rasgulla": {
        "ingredients": ["chenna", "sugar", "water", "cardamom"],
        "instructions": "Make balls from chenna, boil in sugar syrup until spongy."
    },
    "Kheer": {
        "ingredients": ["rice", "milk", "sugar", "cardamom", "nuts"],
        "instructions": "Cook rice in milk, add sugar and cardamom, and garnish with nuts."
    },
    "Lassi": {
        "ingredients": ["yogurt", "sugar", "water", "cardamom"],
        "instructions": "Blend yogurt with sugar and water, and serve chilled."
    },
    "Mango Lassi": {
        "ingredients": ["yogurt", "mango", "sugar", "cardamom"],
        "instructions": "Blend yogurt with mango and sugar until smooth."
    },
    "Buttermilk": {
        "ingredients": ["yogurt", "water", "spices", "salt"],
        "instructions": "Whisk yogurt with water and spices, and serve chilled."
    },
    "Masala Chai": {
        "ingredients": ["tea leaves", "milk", "sugar", "spices"],
        "instructions": "Boil tea leaves with spices, add milk and
