

# 直接pip install pyHook是找不到相关包的，不知道是不是因为这个库可以被用于一些比较邪恶的目的。。 
# 于是就要去网上下，可以下源码编译安装。 
# 在https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyhook这里可以直接下载到.whl文件。 
# pip install xxx.whl即可。


# pip install PyUserInput


from pymouse import PyMouse
from pykeyboard import PyKeyboard
import time
m = PyMouse()
k = PyKeyboard()


# x_dim, y_dim = m.screen_size()
# m.click(640, 360, 1)
# k.type_string('Hello, World!')

print(m.position()) #显示鼠标坐标
n=631

# 创建(269, 142) 
# 地址名称坐标 (417, 183)
# ip坐标 (400, 254)
# 确认按钮坐标 (1000, 376)


# 循环读取ip
for line in open("ip.txt"):  
    #print line,  #python2 用法
    m.click(269, 142, 1)
    time.sleep( 1 )
    m.click(417, 183, 1)
    time.sleep( 1 )
    k.type_string('eyip'+str(n))
    time.sleep( 1 )
    m.click(400, 254, 1)
    time.sleep( 1 )
    k.type_string(line.strip())
    m.click(1000, 376, 1)
    n=n+1
    time.sleep( 1 )
    # print(line)


    # for line in open("ip.txt"):  
    # #print line,  #python2 用法
    # m.click(269, 142, 1)
    # time.sleep( 1 )
    # m.click(417, 183, 1)
    # time.sleep( 1 )
    # k.type_string('ey1ip')
    # time.sleep( 1 )
    # k.type_string('ip')
    # k.tap_key(k.enter_key)
    # time.sleep( 1 )
    # k.type_string(str(n))
    # # time.sleep( 1 )
    # # m.click(400, 254, 1)
    # # time.sleep( 1 )
    # # k.type_string(line)
    # # time.sleep( 1 )
    # # m.click(1000, 376, 1)
    # # n=n+1
    # # time.sleep( 1 )
    # # print(line)
