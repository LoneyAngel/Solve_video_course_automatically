from time import sleep
from lxml import etree
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from in_file import *

def element_exists(driver, by, value):
    """判断元素是否存在,返回true或false"""
    try:
        wait = WebDriverWait(driver, 5)  # 创建 WebDriverWait 对象，设置最长等待时间
        wait.until(EC.presence_of_element_located((by, value)))
        return True
    except Exception:
        return False

def get_video(text):
    """获取全部的视频url"""
    try:
        tree = etree.HTML(text)
        return tree.xpath('/html/body/div[3]/div[1]/div[2]/div[3]//h3/span[3]/a/@href')
    # xpath中//的使用方法
    except Exception as e:
        print(f"get_video_Error: {e}")

def get_progress(text):
    """获取全部的视频url"""
    try:
        tree = etree.HTML(text)
        return tree.xpath('/html/body/div[3]/div[1]/div[2]/div[3]//h3/span[1]/text()')
    # xpath中//的使用方法
    except Exception as e:
        print(f"get_video_Error: {e}")

def get_video_status(wait):
    """获取当前视频的状态"""
    if wait.until(EC.visibility_of_element_located((By.XPATH, '//*[@id="796427818"]/h3[1]/a/span[1]/em'))).text:
        return False  #未完成
    else:
        return True  #已经完成

def get_para(text):
    """判断视频是不是已经看过"""
    try:
        tree = etree.HTML(text)
        # print(tree.xpath('//*[@id="ext-gen1051"]/@aria-label')[0])
        return tree.xpath("//*[@id='ext-gen1051']/@aria-label")[0]
    except Exception as e:
        print(f"get_para_Error: {e}")