import allure

from data import *


class TestRecipePage:

    def test_create_recipe(self, recipe_page):
        with allure.step('Переходим на страницу создания рецепта'):
            recipe_page.go_to_create_recipe_page()
        with allure.step('Вводим название рецепта'):
            recipe_page.input_recipe_title()
        with allure.step('Вводим название первого ингридиента'):
            recipe_page.input_recipe_ingredient_name_1()
            recipe_page.pick_milk_from_suggest()
        with allure.step('Вводим вес первого ингридиента'):
            recipe_page.input_recipe_ingredient_weight_1()
            recipe_page.click_add_ingredient()
        with allure.step('Вводим название второго ингридиента'):
            recipe_page.input_recipe_ingredient_name_2()
            recipe_page.pick_flour_from_suggest()
        with allure.step('Вводим вес второго ингридиента'):
            recipe_page.input_recipe_ingredient_weight_2()
            recipe_page.click_add_ingredient()

        with allure.step('Вводим время приготовления'):
            recipe_page.input_cooking_time()
        with allure.step('Вводим описание рецепта'):
            recipe_page.input_description_recipe()
        with allure.step('Загружаем фото'):
            recipe_page.upload_recipe_photo()
        with allure.step('Скроллим вниз страницы и нажимаем на кнопку создания рецепта'):
            recipe_page.click_to_create_recipe()
        with allure.step('Проверяем название рецепта, список ингридиентов, наличие кнопки Добавить в покупки'):
            ingredients = recipe_page.get_recipe_ingredients()
            assert recipe_page.get_recipe_title_text() == TestData.RECIPE.title and TestData.RECIPE.ingredient_displays == ingredients and recipe_page.is_add_to_list_visible()
