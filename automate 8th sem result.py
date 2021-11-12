from selenium import webdriver
import time
Reg_start=17104131001  #start Registration No
Reg_End=17104131056  #End Registration No
browser=webdriver.Chrome('chromedriver.exe')
#a=input("Input link")
a=('https://results.akuexam.net/BTechBPharm8thSemResults2021.aspx') #this is link for 8th sem
for rega in range(Reg_start,Reg_End):
    browser.get(a)
    reg_no=browser.find_element_by_xpath('//*[@id="ctl00_ContentPlaceHolder1_TextBox_RegNo"]')
    submit=browser.find_element_by_name('ctl00$ContentPlaceHolder1$Button_Show')
    reg_no.send_keys(rega)
    time.sleep(0.2)        
    submit.click()
    time.sleep(0.5)
    print("Submit >>",rega)
    
