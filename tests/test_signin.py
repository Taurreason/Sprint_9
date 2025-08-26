import allure


class TestSignin:

    @allure.title('Нажимаем кнопку Войти')
    def test_click_login_to_main(self, main_page, signin_page):
        with allure.step('Нажимаем на кнопку Войти'):
            main_page.click_on_login()
        with allure.step('Вводим почту'):
            signin_page.input_email()
        with allure.step('Вводим пароль'):
            signin_page.input_password()
        with allure.step('Нажимаем на кнопку Войти в форме авторизации'):
            signin_page.click_on_login_button_in_form()
        with allure.step('Проверяем переход на главную страницу'):
            assert main_page.wait_recipes_page_is_open()

    def test_click_login_check_button_exit(self, main_page, signin_page):
        with allure.step('Нажимаем на кнопку Войти'):
            main_page.click_on_login()
        with allure.step('Вводим почту'):
            signin_page.input_email()
        with allure.step('Вводим пароль'):
            signin_page.input_password()
        with allure.step('Нажимаем на кнопку Войти в форме авторизации'):
            signin_page.click_on_login_button_in_form()
        with allure.step('Проверяем отображение кнопки Выход'):
            assert main_page.check_exit_button()
