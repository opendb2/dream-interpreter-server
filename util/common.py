import random
import time

# 文件名简陋生成策略
def rand_file_name():
    return '.'.join(['-'.join(['dream-img', str(random.randint(1, 10000)), str(int(time.time()))]), 'jpg'])

