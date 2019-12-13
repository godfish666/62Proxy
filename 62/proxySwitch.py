import winreg
import ctypes


class ProxySwitch(object):
    def __init__(self):

        # 如果从来没有开过代理 有可能健不存在 会报错
        self.INTERNET_SETTINGS = winreg.OpenKey(winreg.HKEY_CURRENT_USER,
                                           r'Software\Microsoft\Windows\CurrentVersion\Internet Settings',
                                           0, winreg.KEY_ALL_ACCESS)
        # 设置刷新
        self.INTERNET_OPTION_REFRESH = 37
        self.INTERNET_OPTION_SETTINGS_CHANGED = 39
        self.internet_set_option = ctypes.windll.Wininet.InternetSetOptionW


    def set_key(self, name, value):  # 修改键值

        _, reg_type = winreg.QueryValueEx(self.INTERNET_SETTINGS, name)

        winreg.SetValueEx(self.INTERNET_SETTINGS, name, 0, reg_type, value)

    def set_proxy_on(self, proxyURL):

        # 启用代理
        self.set_key('ProxyEnable', 1)  # 启用
        self.set_key('ProxyOverride', u'*.local;<local>')  # 绕过本地
        #self.set_key('ProxyServer', u'1.24.184.161:9999')  # 代理IP及端口
        self.set_key('ProxyServer', proxyURL)  # 代理IP及端口
        self.internet_set_option(0, self.INTERNET_OPTION_REFRESH, 0, 0)
        self.internet_set_option(0, self.INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
        print("set_proxy_on")

    def set_proxy_off(self):
        # 停用代理
        self.set_key('ProxyEnable', 0)  # 停用
        self.internet_set_option(0, self.INTERNET_OPTION_REFRESH, 0, 0)
        self.internet_set_option(0, self.INTERNET_OPTION_SETTINGS_CHANGED, 0, 0)
        print("set_proxy_off")

