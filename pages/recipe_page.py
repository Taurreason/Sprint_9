from locators.recipe_page_locators import RecipePageLocators
from pages.base_page import BasePage
from data import *

# from service import site


class RecipePage(BasePage):


    def __init__(self, *args):
        super().__init__(*args)

    def go_to_create_recipe_page(self):
        self.click(RecipePageLocators.CREATE_RECIPE_LINK)

    def input_recipe_title(self):
        self.find(RecipePageLocators.RECIPE_TITLE_INPUT).send_keys(TestData.RECIPE.title)

    def input_recipe_ingredient_name_1(self):
        self.find(RecipePageLocators.INGREDIENTS_INPUT_NAME).send_keys(TestData.RECIPE.ingredients[0].name)

    def input_recipe_ingredient_weight_1(self):
        self.find(RecipePageLocators.INGREDIENTS_INPUT_WEIGHT).send_keys(str(TestData.RECIPE.ingredients[0].weight_g))

    def input_recipe_ingredient_name_2(self):
        self.find(RecipePageLocators.INGREDIENT_INPUT_ADDITIONAL_FIELD).send_keys(TestData.RECIPE.ingredients[1].name)

    def input_recipe_ingredient_weight_2(self):
        self.find(RecipePageLocators.INGREDIENTS_INPUT_ADDITIONAL_WEIGHT).send_keys(str(TestData.RECIPE.ingredients[1].weight_g))

    def click_add_ingredient(self):
        self.click(RecipePageLocators.ADD_INGREDIENT)

    def input_cooking_time(self):
        self.find(RecipePageLocators.COOKING_TIME_INPUT).send_keys(str(TestData.RECIPE.cooking_time_min))

    def input_description_recipe(self):
        self.find(RecipePageLocators.RECIPE_DESCRIPTION_INPUT).send_keys(TestData.RECIPE.description)
  
    def pick_milk_from_suggest(self):
        self.choose_from_suggest(
            RecipePageLocators.SUGGEST_LIST,
            RecipePageLocators.MILK_OPTION
        )

    def pick_flour_from_suggest(self):
        self.choose_from_suggest(
            RecipePageLocators.SUGGEST_LIST,
            RecipePageLocators.FLOUR_OPTION
        )

    def upload_recipe_photo(self):
        self.upload_file(RecipePageLocators.FILE_INPUT, "pancakes.jpg")

    def click_to_create_recipe(self):
        btn = self.find_present(RecipePageLocators.CREATE_RECIPE_BUTTON)
        self.scroll_into_view(btn)
        self.click(RecipePageLocators.CREATE_RECIPE_BUTTON)

    def get_recipe_title_text(self) -> str:
        return self.find(RecipePageLocators.PANCAKES_TITLE).text.strip()
    
    def get_recipe_ingredients(self) -> str:
        self.find(RecipePageLocators.PANCAKES_TITLE)
        lines = self.find_all(RecipePageLocators.INGREDIENTS_ITEMS)
        return [e.text.strip() for e in lines if e.text.strip()]
    
    def is_add_to_list_visible(self):
        return bool(self.find(RecipePageLocators.ADD_TO_CART_BUTTON))
