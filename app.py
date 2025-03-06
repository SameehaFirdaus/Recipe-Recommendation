import streamlit as st
from recipe_recommender import recommend_recipes

def main():
    st.title("Recipe Recommendation System")
    st.write("Enter the ingredients you have:")

    ingredients = st.text_input("Ingredients (comma-separated):")
    if st.button("Recommend Recipes"):
        if ingredients:
            recommended_recipes = recommend_recipes(ingredients.split(","))
            if recommended_recipes:
                st.subheader("Recommended Recipes:")
                for recipe in recommended_recipes:
                    st.write(f"- {recipe}")
            else:
                st.write("No recipes found for the given ingredients.")
        else:
            st.write("Please enter some ingredients.")

if __name__ == "__main__":
    main()
