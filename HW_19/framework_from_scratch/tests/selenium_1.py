import pytest


@pytest.mark.smoke_test
def test_check_open_main_page(open_main_page):
    main_page = open_main_page
    assert main_page.is_login_button_displayed() is True, 'User is unable to see Main page'
    assert main_page.is_search_field_clickable() is True, "Search field is not clickable"
    assert main_page.is_ukrainian_language_default() is True, 'The Ukrainian language icon is not present on the site'


@pytest.mark.regression_test
def test_text_tittle(open_main_page):
    actual_title = open_main_page
    assert actual_title == 'MAKEUP - косметика і парфумерія в інтернет-магазині №1' is True, "Tittle is incorrect"


@pytest.mark.regression_test
def test_check_open_login_page(open_login_page, env):
    login_page = open_login_page.login(env.user_name, env.password)
    assert login_page.is_enter_button_displayed() is True, "User was not logged in!"
    assert login_page.is_forget_password_link_displayed() is True, 'The user is unable to recover a password'
    assert login_page.is_registration_button_displayed() is True, 'The user is unable to registration an account'
    assert login_page.is_password_field_displayed() is True, 'The user is unable to enter a password'
    assert login_page.is_email_field_displayed() is True, 'The user is unable to enter an email'


@pytest.mark.regression_test
def test_check_cabinet_page(cabinet_page, env):
    cabinet_page = cabinet_page.login(env.user_name, env.password)
    assert cabinet_page.is_basket_button_displayed() is True, 'User is unable to see cabinet functions'
    assert cabinet_page.is_feedback_button_displayed() is True, 'User is unable to write the feedback'
    assert cabinet_page.is_facebook_icon_displayed() is True, "The user is unable to redirect to the Facebook SDK"
    assert cabinet_page.is_subscribe_button_displayed() is True, 'The user is unable to subscribe on emails'


@pytest.mark.smoke_test
@pytest.mark.regression_test
def test_check_open_personal_cabinet_menu(personal_cabinet_menu, env):
    personal_cabinet = personal_cabinet_menu.login(env.user_name, env.password).click_cabinet_exit_button()
    assert personal_cabinet.is_cabinet_exit_button_displayed() is True, 'The user is unable to log out'
    assert personal_cabinet.is_parfume_tab_displayed() is True, 'The user is unable to choose Parfume tab'
    assert personal_cabinet.is_about_shop_button_displayed() is True, 'The user is unable to read info about shop'


def test_check_logout(log_out_from_cabinet, env):
    log_out = log_out_from_cabinet.login(env.user_name, env.password).click_cabinet_exit_button().logout()
    assert log_out.is_login_button_displayed() is True, "User was not logged out!"
