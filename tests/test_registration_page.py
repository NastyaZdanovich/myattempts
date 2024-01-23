import allure
from source_code.constants import Info
from source_code.pages.sign_in_page import SignInPage


class TestRegistration:
    def test_log_in_process(self, driver, main_page):
        with allure.step("1.Нажать кнопку 'Войти'"):
            main_page.click_by_xpath(main_page.sign_in_xpath)

        with allure.step("2. Войти с помощью своего профиля Mail.ru "):
            sign_in_page = SignInPage(driver)
            sign_in_page.click_by_xpath(sign_in_page.email_registration)

        with allure.step("3.Заполнить поля 'Электронная почта' и 'Пароль'"):
            sign_in_page.switch_handler(-1)
            sign_in_page.fill_in_a_form(sign_in_page.confirm_email_xpath, Info.EMAIL)
            sign_in_page.fill_in_a_form(sign_in_page.confirm_password_xpath, Info.PASSWORD)
            sign_in_page.click_by_xpath(sign_in_page.enter)

        with allure.step("4. Проверить, что вход в кабинет произошел "):

            main_page.switch_handler(0)
            main_page.refresh_page()
            text = main_page.get_a_text(main_page.my_oz_xpath)
            assert text == 'Мой OZ', f"Expected text 'Мой OZ', actual text {text}"

