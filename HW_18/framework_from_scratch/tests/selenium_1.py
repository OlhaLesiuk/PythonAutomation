

def test_01(open_main_page):
    main_page = open_main_page
    assert main_page.is_login_button_displayed() is True, 'User is unable to see Main page'


def test_02(open_login_page):
    login_page = open_login_page.login('selo6est@gmail.com', 'qwerty123')
    assert login_page.is_enter_button_displayed() is True, "User was not logged in!"


def test_03(cabinet_page_view):
    cabinet_page = cabinet_page_view
    assert cabinet_page.is_logout_button_displayed() is True, 'User is unable to see cabinet functions'


def test_04(log_out_from_cabinet):
    log_out = log_out_from_cabinet
    assert log_out.is_logout2_button_displayed() is True, "User was not logged out!"
