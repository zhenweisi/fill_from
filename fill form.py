import concurrent.futures
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time

# 创建一个无头 Chrome 浏览器实例
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无头模式

XW_01 = ['xxxx@gmail.com','xxxx1@gmail']#这就写邮箱了，无论几十个 格式是‘邮箱’，就可以了

def fill_input_field(email):
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://www.lombard.finance/")  # 替换为你要填写的网站地址
        time.sleep(5)  # 等待页面加载完成

        input_element = driver.find_element(By.XPATH, 'Xpath')#填写表单的地方 右键  找到xpath就行
        input_element.send_keys(email)
        print(f"已经填写: {email}")

        submit_button = driver.find_element(By.XPATH, 'Xpath')#点击按钮的地方 找到XPATH
        submit_button.click()
        print(f"已经完成：{email}")

        time.sleep(2)  # 等待提交完成
    except Exception as e:
        print(f"Error for email {email}: {str(e)}")
    finally:
        driver.quit()

def main():
    with concurrent.futures.ThreadPoolExecutor(max_workers=5) as executor:  # 使用5个线程并发处理
        executor.map(fill_input_field, XW_01)

if __name__ == "__main__":
    main()
