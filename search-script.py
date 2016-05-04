#!/usr/bin/env python
#ecoding=utf-8

from selenium import webdriver
from time import sleep

def find_elem(driver):
    #定位结果：世界排名
    web_shijiepaiming = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[1]/div[2]/div[1]/a/a/font").text

    #整站流量排名
    web_llpm = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/ \
                                            div/ul/li[1]/div[2]/div[2]/a/a/font").text
    #整站日均ip
    web_rjip = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[1]/\
                                            div[2]/div[3]/a/a/font").text
    #整站日均pv
    web_rjpv = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[1]\
                                            /div[2]/div[4]/a/a/font").text
    #百度权重
    qz = driver.find_element_by_xpath("/html/body/div[4]/div/div[1]/div/ul/li[2]/div[2]/\
                                               div[1]/p/a/img").get_attribute("src")
    #url = "http://seo.chinaz.com/template/default/images/public/baiduapp/500.gif",截取图片的名称
    web_baiduqz = qz[qz.index("baiduapp")+9:qz.index("gif")-1]

    return web_shijiepaiming, web_llpm, web_rjpv, web_rjip, web_baiduqz

driver = webdriver.Chrome()

#读取文件内容到db_list中
file_object = open("20160303.txt","r") # TODO 判断出错情况
db_list = []
for i in file_object.readlines():
    i = i.replace("\n","").split(",")
    db_list.append(i)
    print i
file_object.close()

for j in db_list:
    url ="http://seo.chinaz.com/?m=&host=" + j[0]
    db_shijiepaiming = j[1]
    driver.get(url)
    print driver.current_url
    web_shijiepaiming, web_llpm, web_rjpv, web_rjip, web_baiduqz = find_elem(driver)
    print j[0], ":"
    print u"    世界排名： %s" % web_shijiepaiming
    print u"    流量排名： %s" % web_llpm
    print u"    日均排名： %s" % web_rjip
    print u"    日均排名： %s" % web_rjip
    print u"    百度权重： %s" % web_baiduqz

    if db_shijiepaiming == web_shijiepaiming.replace(",", ""):
        print "    ", db_shijiepaiming, web_shijiepaiming, "ok"
    else:
        print "    ", db_shijiepaiming, web_shijiepaiming, "NG"

    sleep(1)

driver.quit()

