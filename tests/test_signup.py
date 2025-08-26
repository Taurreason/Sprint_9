import allure


class TestSignup:

    @allure.title('Создание аккаунта')
    def test_create_account(self, main_page, signup_page, signin_page):
        with allure.step('Нажимаем на кнопку Создать аккаунт'):
            main_page.click_on_signup()
        with allure.step('Вводим имя'):
            signup_page.input_first_name()
        with allure.step('Вводим фамилию'):
            signup_page.input_second_name()
        with allure.step('Вводим никнейм пользователя'):
            signup_page.input_user_name()
        with allure.step('Вводим почту'):
            signup_page.input_email()
        with allure.step('Вводим пароль'):
            signup_page.input_password()
        with allure.step('Подтверждаем создание аккаунта'):
            signup_page.click_on_signup_down()
        with allure.step('Проверка перехода на страницу авторизации'):
            assert signin_page.check_user_is_authorized() and signin_page.check_visibility_signin_form()
            