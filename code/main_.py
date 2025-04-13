from middle import *
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium import webdriver

if __name__ == '__main__':
    service = Service(EdgeChromiumDriverManager().install())
    options = Options()
    # options.add_argument('--headless')  # 如果需要无头模式可以取消注释
    driver = webdriver.Edge(service=service, options=options)
    wait = WebDriverWait(driver, 10)  # 创建 WebDriverWait 对象，设置最长等待时间
    # 进行分割

    a=input("输入1重置选择或开始第一次，否则将接着上次的继续:")
    if  a==1 or read_jihe()[0]=="":
        write_zhizhen("0\1")
        write_jihe([""])

        print("输入个人账号（输入个人账号后更新account.txt信息为输入的账号）")
        phone = input("账号：")
        password = input("密码：")
        ke = input("序号：")

        driver.get(
            "http://xuexi365.net/login?null"
        )
        text = denglu(driver, phone, password, wait)
        while text:
            phone = input("账号：")
            password = input("密码：")
            # 登录
            text = denglu(driver, phone, password, wait)
        # 将账号写入文件进行保存，减少重复输入
        write_account(phone, password)
        print("成功登入")
        # 开始刷
        start(wait, driver, ke)

    else:
        # 进度保存
        jihe=read_jihe()
        bofang(driver, jihe,wait)
    # 让窗口不会因为报错立即关闭
    input("程序运行结束")
