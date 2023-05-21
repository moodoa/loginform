import re


class LoginForm:
    def __init__(self):
        self._username_email = ""
        self._password = ""
        self._password_visible = False

    # username
    def username_email(self):
        return self._username_email

    def is_email_valid(self):
        if not self._username_email:
            return False
        if len(self._username_email) > 50 or len(self._username_email) < 7:
            return False
        email_regex = r"^[\w.-]+@[\w.-]+\.\w+$"
        return re.match(email_regex, self._username_email) is not None

    # password
    def password(self):
        return self._password

    def is_password_valid(self):
        if not self._password:
            return False
        if len(self._password) > 50 or len(self._password) < 7:
            return False
        return self._check_password_strength(self._password)

    def _check_password_strength(self, password):
        has_uppercase = re.search(r"[A-Z]", password) is not None
        has_lowercase = re.search(r"[a-z]", password) is not None
        has_digit = re.search(r"\d", password) is not None
        has_special = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is not None
        return has_uppercase and has_lowercase and has_digit and has_special

    def toggle_password_visibility(self):
        if self._password_visible == False:
            self._password_visible = True
        else:
            self._password_visible = False

    def is_password_visible(self):
        return self._password_visible

    # submit
    def is_submit_button_enabled(self):
        if not self._username_email or not self._password:
            return False
        if self.is_email_valid() and self.is_password_valid():
            return True
        else:
            return False

    # mobile
    def is_mobile_swipe_enable(self):
        test_result = True
        # 由此接檢測 API
        return test_result

    def is_mobile_touch_enable(self):
        test_result = True
        # 由此接檢測 API
        return test_result
