from selenium.webdriver.common.by import By


class RecipePageLocators:

    MENU_BUTTON = By.CSS_SELECTOR, "div[class^='styles_menuButton__']"
    CREATE_RECIPE_LINK = By.CSS_SELECTOR, "a[href='/recipes/create']"

    RECIPE_TITLE_INPUT = By.XPATH, "//label[.//div[normalize-space()='Название рецепта']]//input[@type='text']"
    INGREDIENTS_INPUT_NAME = By.XPATH, "//label[.//div[normalize-space()='Ингредиенты']]//input[@type='text']"
    INGREDIENT_INPUT_ADDITIONAL_FIELD = By.XPATH, "//input[contains(@class,'styles_ingredientsInput__') and @type='text']"
    INGREDIENTS_INPUT_WEIGHT = By.XPATH, "//input[contains(@class,'styles_ingredientsAmountValue__')]"
    INGREDIENTS_INPUT_ADDITIONAL_WEIGHT = By.XPATH, "//input[contains(@class,'styles_ingredientsAmountValue__') and @type='text']"
    
    COOKING_TIME_INPUT = By.XPATH, "//label[.//div[normalize-space()='Время приготовления']]//input[@type='text']"
    RECIPE_DESCRIPTION_INPUT = By.CSS_SELECTOR, "textarea[class^='styles_textareaField__']"
    CHOOSE_FILE_BUTTON = By.XPATH, "//div[starts-with(@class,'styles_button__') and normalize-space(.)='Выбрать файл']"
    
    FILE_INPUT = By.CSS_SELECTOR, "input[type='file']"

    CREATE_RECIPE_BUTTON = By.XPATH, "//button[normalize-space(.)='Создать рецепт']"
    SUGGEST_LIST = By.CSS_SELECTOR, "div[class^='styles_container__']"
    SUGGEST_OPTIONS = By.XPATH, "//body//div[starts-with(@class,'styles_container__')]/div"

    MILK_OPTION  = By.XPATH, "//body//div[starts-with(@class,'styles_container__')]/div[normalize-space()='молоко']"
    FLOUR_OPTION = By.XPATH, "//body//div[starts-with(@class,'styles_container__')]/div[normalize-space()='мука']"

    CREATE_RECIPE_BUTTON = By.XPATH, "//button[normalize-space(.)='Создать рецепт']"

    ADD_INGREDIENT = By.XPATH, "//div[normalize-space(.)='Добавить ингредиент']"

    PANCAKES_TITLE = By.XPATH, "//h1[normalize-space(.)='Блинчики']"
    INGREDIENTS_TITLE = By.XPATH, "//h3[normalize-space(.)='Ингридиенты:']"
    INGREDIENTS_ITEMS = By.XPATH, "//p[contains(@class, 'styles_ingredients__list-item__')]"
    ADD_TO_CART_BUTTON = By.XPATH, "//button[normalize-space(text())='Добавить в покупки']"
           
                      