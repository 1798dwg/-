import allure
import pytest

@allure.feature('搜索模块')
class TestSearch():
    def testcase1(self):
        print('case1')
    def testcase2(self):
        print('case2')
@allure.feature('登陆模块')
class TestLogin():
    @allure.story("登录成功")
    def test_login_success(self):
        print("这是登录：测试用例，登录成功")
        pass
    @allure.story('登录失败')
    def test_login_success_a(self):
        print("这是登录：测试用例，登陆失败")
        pass
    @allure.story('用户名确实')
    def test_login_success_b(self):
        print("这是登录：测试用例，登陆失败，用户名缺失")
        pass

    @allure.story('密码缺失')
    def test_login_success_c(self):
        print("这是登录：测试用例，登陆失败，密码缺失")
        pass

if __name__ == '__main__':
    pytest.main()


