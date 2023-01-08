import pytest
import allure
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

@allure.testcase("http://www.baidu.com")
@allure.feature("百度搜索")
@pytest.mark.parametrize("test_data1",['allure','pytest','unittest'])
def test_steps_demo(test_data1):
    with allure.step("打开百度首页"):
        driver = webdriver.Firefox()
        driver.get("http://www.baidu.com")
        driver.maximize_window()

    with allure.step(f"输入搜索词：{test_data1}"):
        driver.find_element(By.ID,"kw").send_keys(test_data1)
        # time.sleep(1)
        driver.find_element(By.ID,"su").click()
        # time.sleep(1)

    with allure.step("保存图片"):
        driver.save_screenshot(f"./result/jietu_{test_data1}.png")
        allure.attach.file(f"./result/jietu_{test_data1}.png",attachment_type=allure.attachment_type.PNG)


    with allure.step("关闭浏览器"):
        driver.quit()

if __name__ == '__main__':
    pytest.main()


