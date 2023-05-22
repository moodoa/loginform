import pytest
import time
import threading


# 測試登錄表單在前端頁面上的正確顯示
def test_login_form_display():
    assert login_form.is_displayed() == True


# 測試 submit 按鈕在前端頁面上的功能
def test_submit_button_functionality():
    login_form.username_email = "example@example.com"
    login_form.password = "password"
    login_form.submit()
    assert login_form.is_logged_in() == True


# 測試錯誤訊息在前端頁面上的顯示
def test_error_message_display():
    login_form.username_email = "invalid_email"
    login_form.password = "invalid_password"
    login_form.submit()
    assert login_form.get_error_message() == "Invalid input"


# 測試輸入正確或錯誤時登錄 API 的功能
def test_login_endpoint():
    response = requests.post(
        "http://example.com/login", json={"username": "example", "password": "password"}
    )
    assert response.status_code == 200
    assert response.json()["success"] == True


def test_data_validation():
    response = requests.post(
        "http://example.com/login", json={"username": "", "password": ""}
    )
    assert response.status_code == 400
    assert "error" in response.json()


# 測試手機上的功能，
@pytest.mark.mobile
def test_mobile_functionality():
    # 這邊串接手機測試 API，例如點擊、滑動、其他特定手勢等等。
    result = login_form.test_mobile_api()
    assert result == True


# 測試效能
def test_performance():
    start_time = time.time()
    operate = login_form.test_performance()
    end_time = time.time()
    execution_time = end_time - start_time
    # 確保操作在一秒內完成
    assert execution_time < 1.0


# 測試密碼強度檢查功能
def test_password_strength():
    weak_password = "password"
    response = requests.post(
        "http://example.com/register",
        data={"username": "example", "password": weak_password},
    )
    assert response.status_code == 400
    assert "weak_password" in response.json()["error"]

    strong_password = "P@ssw0rd!123"
    response = requests.post(
        "http://example.com/register",
        data={"username": "example", "password": strong_password},
    )
    assert response.status_code == 200
    assert "success" in response.json()


# 測試多位使用者登錄
def login_user(username, password):
    response = requests.post(
        "http://example.com/login", data={"username": username, "password": password}
    )
    assert response.status_code == 200
    assert "success" in response.json()


def test_concurrent_login():
    num_users = 100
    usernames = ["user" + str(i) for i in range(num_users)]
    passwords = ["password" + str(i) for i in range(num_users)]

    threads = []
    for username, password in zip(usernames, passwords):
        thread = threading.Thread(target=login_user, args=(username, password))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()


# 測試系統的負載能力
def test_system_load():
    start_time = time.time()
    operate = login_form.test_heavyloading_performance()
    end_time = time.time()
    execution_time = end_time - start_time
    # 確保在十秒內完成大量請求
    assert execution_time < 10.0
