from demo6.api.register_api import RegisterApi


class TestBase:

    def setup(self):
        self.login = RegisterApi().login(mobile="13812345670", pwd="12345678")
        return self.login
