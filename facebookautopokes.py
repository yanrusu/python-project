# 自動戳一下，每分鐘檢查

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


帳號 = input('請輸入 FB 帳號 : ')
密碼 = input('請輸入 FB 密碼 : ')
print('請輸入想戳的朋友，若超過一位請以 / 間隔，需為朋友帳號名稱，且須為以戳過之帳號，前後不可有空格')
flist = [x for x in input().split('/')]

driver = webdriver.Chrome()
driver.get("https://www.facebook.com/pokes")

chromeinput = driver.find_element(By.ID,'email')
chromeinput.send_keys(帳號)

chromeinput = driver.find_element(By.ID,'pass')
chromeinput.send_keys(密碼)

singbutton = driver.find_element(By.ID, 'loginbutton')
singbutton.send_keys(Keys.ENTER)


while True:
    elements = driver.find_elements(By.CSS_SELECTOR, ".x1i10hfl.x1qjc9v5.xjbqb8w.xjqpnuy.xa49m3k.xqeqjp1.x2hbi6w.x13fuv20.xu3j5b3.x1q0q8m5.x26u7qi.x972fbf.xcfux6l.x1qhh985.xm0m39n.x9f619.x1ypdohk.xdl72j9.x2lah0s.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.x2lwn1j.xeuugli.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x1n2onr6.x16tdsg8.x1hl2dhg.xggy1nq.x1ja2u2z.x1t137rt.x1q0g3np.x87ps6o.x1lku1pv.x1a2a7pz.x1lq5wgf.xgqcy7u.x30kzoy.x9jhf4c.x1lliihq")

    for element in elements:
        try:
            name=element.find_element(By.CSS_SELECTOR,".x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x9f619.x1ypdohk.xt0psk2.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1a2a7pz.xt0b8zv.xzsf02u.x1s688f")
            for fl in range(len(flist)):
                if name.text == flist[fl]:
                        print(name.text)
                        tf = element.find_element(By.CSS_SELECTOR,'.x1i10hfl.xjbqb8w.x6umtig.x1b1mbwd.xaqea5y.xav7gou.x1ypdohk.xe8uvvx.xdj266r.x11i5rnm.xat24cr.x1mh8g0r.xexx8yu.x4uap5.x18d9i69.xkhd6sd.x16tdsg8.x1hl2dhg.xggy1nq.x1o1ewxj.x3x9cwd.x1e5q0jg.x13rtm0m.x87ps6o.x1lku1pv.x1a2a7pz.x9f619.x3nfvp2.xdt5ytf.xl56j7k.x1n2onr6.xh8yej3')
                        tf.send_keys(Keys.ENTER)
        except:
            pass


    time.sleep(60)
    driver.refresh()