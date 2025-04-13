from tools import *


def denglu(driver, phone, mima, wait):
    """登录"""
    error_text = ""
    try:
        wait.until(EC.visibility_of_element_located((By.ID, 'phone'))).send_keys(phone)
        wait.until(EC.visibility_of_element_located((By.ID, 'pwd'))).send_keys(mima)
        wait.until(EC.visibility_of_element_located((By.ID, 'loginBtn'))).click()
        # 必须等待页面的加载
        sleep(1)
        url = driver.current_url
        if url.find("passport"):
            driver.get(url)
            wait.until(EC.visibility_of_element_located((By.ID, 'phone'))).send_keys(phone)
            wait.until(EC.visibility_of_element_located((By.ID, 'pwd'))).send_keys(mima)
            wait.until(EC.visibility_of_element_located((By.ID, 'loginBtn'))).click()

    except Exception as e:
        print(f"denglu_ERROR：{e}")
    finally:
        return error_text


def start(wait, driver, number):
    """开始对网站进行操作"""
    try:
        sleep(1)
        # 选择课程
        driver.find_element(
            By.XPATH, '//*[@id="frame_content"]'
        )
        iframe = wait.until(
            EC.visibility_of_element_located((By.XPATH, f'//*[@id="frame_content"]'))
        )
        driver.switch_to.frame(iframe)
        wait.until(
            EC.visibility_of_element_located(
                (By.XPATH, f'/html/body/div/div[2]/div[3]/ul/li[{number}]/div[2]/h3/a')
            )).click()
        # 跳转到选择具体的课的页面

        original_window = driver.current_window_handle
        # 等待新窗口打开
        wait.until(EC.number_of_windows_to_be(2))

        # 切换到新窗口
        for window_handle in driver.window_handles:
            if window_handle != original_window:
                driver.switch_to.window(window_handle)
                break
        sleep(2)  #必须进行等待操作
        url_j = driver.page_source
        jihe = ["https://mooc1-2.chaoxing.com" + i for i in get_video(url_j)]
        write_jihe(jihe)
        if len(jihe) == 0:
            print("视频链接获取出错，无视频链接")
        else:
            print(f'总共{len(jihe)}个视频')
            bofang(driver, jihe, wait)
    except Exception as e:
        print(f"start_Error: {e}")


def bofang(driver, jihe, wait):
    """视频播放的相关的操作"""
    quan = 1
    count = read_zhizhen()-1
    judge = True
    # 对每一个视频进行操作
    while judge:

        print(f"***********************第{quan}次：***********************")
        try:
            # 播放视频
            while count!=len(jihe):
                count += 1
                print(f"{count}/{len(jihe)}")
                sleep(1)
                driver.get(jihe[count-1])

                # 若非视频对象或者已经看完，结束本次循环
                try:
                    # 两次切换iframe，转到播放所在的部分
                    iframe = wait.until(EC.visibility_of_element_located((By.ID, 'iframe')))
                    driver.switch_to.frame(iframe)
                    sleep(1)
                    wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ext-gen1051"]')))
                    text = driver.page_source
                    if get_para(text) == "任务点已完成":
                        write_zhizhen(f"{count}/{len(jihe)}")
                        print("任务点已完成\n")
                        continue
                    iframe = wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="ext-gen1050"]/iframe')))
                    driver.switch_to.frame(iframe)
                    sleep(1)
                except Exception:
                    write_zhizhen(f"{count}/{len(jihe)}")
                    print("非视频链接。\n")
                    continue

                # 正常的情况
                # 定位播放按钮
                wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="video"]/button'))).click()
                sleep(1)
                start_status = wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="video"]/div[6]/button/span[2]'))).text

                if start_status == "播放":  #处理异常的情况
                    wait.until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="video"]/div[6]/button'))).click()

                wait.until(
                    EC.visibility_of_element_located((By.XPATH, '//*[@id="video"]/div[6]/div[4]/span[2]')))

                sleep(2)
                # 5秒判断1次 视频是否播放完毕
                while True:
                    start_status = wait.until(
                        EC.visibility_of_element_located((By.XPATH, '//*[@id="video"]/div[6]/button/span[2]'))).text
                    if start_status == "重播":
                        print(f"结束播放{count}/{len(jihe)}视频")
                        # 进行进度写入
                        write_zhizhen(f"{count}/{len(jihe)}")
                        break
                    elif start_status == "播放":
                        print("注意：视频已被暂停")
                    sleep(5)

        except Exception as e:
            print(f"bofang_Error: {e}")
            print('''出现错误，您可以选择输入1结束程序，
                     输入其他
                     接着上次的进度重新进行尝试''')
            if int(input()) == 1:
                driver.quit()
                print("结束")
                break
            else:
                quan += 1
                print("祝您此次成功\n")
