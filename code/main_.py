from middle import *
from selenium.webdriver.edge.service import Service
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.edge.options import Options
from selenium import webdriver

if __name__ == '__main__':
    service = Service(EdgeChromiumDriverManager().install())
    options = Options()
    options.add_argument('--headless')  # 如果需要无头模式可以取消注释
    driver = webdriver.Edge(service=service, options=options)
    wait = WebDriverWait(driver, 10)  # 创建 WebDriverWait 对象，设置最长等待时间
    # 进行分割

    a=int(input("输入1来重置你的选择，否则将接着上次的继续:"))
    if  read_jihe()[0]=="" or a==1:
        write_zhizhen("0\1")
        write_jihe([""])
        print("先选择默认的尝试程序能不能正常使用，enm。。。。。")
        ke = input("序号：")
        account=read_account()
        phone = account[0]
        mima = account[1]
        print("2：默认账号(此时默认账号是测试账号)；\n1：个人账号（输入个人账号后更新默认账号为输入的账号）")
        if input("请选择：") == 1:
            phone = input("账号：")
            mima = input("密码：")
        driver.get(
            "http://xuexi365.net/login?null"
        )
        text = denglu(driver, phone, mima, wait)
        while text:
            phone = input("账号：")
            mima = input("密码：")
            text = denglu(driver, phone, mima, wait)
        write_account(phone, mima)
        print("成功登入")
        start(wait, driver, ke)

    else:
        jihe=read_jihe()
        bofang(driver, jihe,wait)

    input("程序运行结束")
