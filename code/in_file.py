def write_zhizhen(progress):
    """写入进度指针"""
    try:
        with open(r'..\zhizhen.txt', 'w+') as f:
            f.write(progress)
    except Exception as e:
        print(f"write_zhizhen:{e}")

def read_zhizhen():
    with open(r'..\zhizhen.txt', 'r') as f:
        data=int(f.read().split('\\')[1])
        return data

def write_in3(text):
    """写入异常"""
    try:
        with open(r'..\abnormal_complication.txt', 'a+') as f:
            f.write(text)
    except Exception as e:
        print(f"write_in3:{e}")

# 作为开始和结束的链接提供
def read_jihe():
    with open(r'..\url.txt', 'r+') as f:
        return f.read().split("\n")

def write_jihe(jihe):
    with open(r'..\url.txt', 'w+') as f:
        for i in jihe:
            f.write(i+"\n")

def read_account():
    with open(r'..\account.txt', 'r+') as f:
        return f.read().split("\n")
def write_account(phone,mima):
    with open(r'..\account.txt', 'w+') as f:
        f.write(phone+"\n")
        f.write(mima)
