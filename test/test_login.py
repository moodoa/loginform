import pytest
import time

from app.login import LoginForm


def test_username_email_field():
    login_form = LoginForm()

    # 測試使用者名稱/信箱欄位是否可輸入文字
    login_form._username_email = "example@example.com"
    assert login_form._username_email == "example@example.com"

    # 測試使用者名稱/信箱欄位是否接受無效的電子郵件格式
    login_form._username_email = "invalid_email"
    assert login_form.is_email_valid() == False

    # 測試使用者名稱/信箱欄位是否接受有效的電子郵件格式
    login_form._username_email = "example@example.com"
    assert login_form.is_email_valid() == True

    # 測試使用者名稱/信箱欄位符合字數限制
    login_form._username_email = f"{'a'*255}@example.com"
    assert login_form.is_email_valid() == False

    # 測試使用者名稱/信箱欄位是否能夠處理空字串
    login_form._username_email = ""
    assert login_form._username_email == ""
    assert login_form.is_email_valid() == False


def test_password_field():
    login_form = LoginForm()

    # 測試密碼欄位是否可輸入文字
    login_form._password = "password"
    assert login_form._password == "password"

    # 測試密碼欄位輸入字數限制
    login_form._password = "a" * 50 + "@Aa123"
    assert login_form.is_password_valid() == False

    # 測試密碼是否包含至少一個大寫/小寫英文、數字和特殊字元。
    login_form._password = "pass@WORD123"
    assert login_form.is_password_valid() == True

    # 測試密碼欄位是否可以切換隱藏或顯示字元
    login_form.toggle_password_visibility()
    assert login_form.is_password_visible() == True

    login_form.toggle_password_visibility()
    assert login_form.is_password_visible() == False

    # 測試密碼欄位是否可以多次切換隱藏或顯示字元
    for t in range(1000):
        assert login_form.is_password_visible() == False


def test_submit_button():
    login_form = LoginForm()

    # 測試在未填寫使用者名稱/信箱和密碼時，送出按鈕是否禁用
    assert login_form.is_submit_button_enabled() == False

    # 測試在只填寫使用者名稱/信箱時，送出按鈕是否禁用
    login_form.username_email = "example@example.com"
    assert login_form.is_submit_button_enabled() == False

    # 測試在只填寫密碼時，送出按鈕是否禁用
    login_form._username_email = ""
    login_form._password = "pass@WORD123"
    assert login_form.is_submit_button_enabled() == False

    # 測試在填寫有效的使用者名稱/信箱和密碼時，送出按鈕是否可用
    login_form._username_email = "example@example.com"
    assert login_form.is_submit_button_enabled() == True

    # 測試可否多次檢查使用者名稱/信箱和密碼
    for t in range(1000):
        assert login_form.is_submit_button_enabled() == True

    # 測試在填寫無效的使用者名稱/信箱時，送出按鈕是否禁用
    login_form._username_email = "invalid_email"
    login_form._password = "pass@WORD123"
    assert login_form.is_submit_button_enabled() == False

    # 測試在填寫無效的密碼時，送出按鈕是否禁用
    login_form._username_email = "example@example.com"
    login_form._password = "password"
    assert login_form.is_submit_button_enabled() == False


@pytest.mark.mobile
def test_mobile_interaction():
    login_form = LoginForm()

    # 測試手機滑動手勢功能是否正常
    assert login_form.is_mobile_swipe_enable() == True

    # 測試手機點擊手勢功能是否正常
    assert login_form.is_mobile_touch_enable() == True
