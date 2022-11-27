def test_01(open_main_page):
    main_page = open_main_page
    assert main_page.is_displayed() is True, 'User is unable to see Main page'


def test_02(open_login_page):
    login_page = open_login_page
    cabinet_page = login_page.login('selo6est@gmail.com', 'qwerty123')
    assert cabinet_page.is_displayed() is True, "User was not logged in!"


def test_03(log_out_from_cabinet):
    log_out = log_out_from_cabinet
    assert log_out.is_displayed() is True, "User was not logged out!"
