import time
from classes.staff_parser import Staff_parser
from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup

from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from flask import Flask, render_template, request

 

app = Flask(__name__)
chromedriver = 'C:\\Users\\Divider\\source\\repos\\Repository_visual_code\\Python\\socet_parser\\chromedriver\\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')


@app.route("/pars/")
def home():

    try:
        
        stf_prsr = Staff_parser()
        browser = webdriver.Chrome(
            executable_path=chromedriver, chrome_options=options)
        browser.get('https://rozetka.com.ua/men_shoes/c721654/')
        browser.set_window_size(1500, 850)
        SCROLL_PAUSE_TIME = 2

        # Get scroll height
        last_height = browser.execute_script(
            "return document.body.scrollHeight")
        i = 0
        while True:
            # Scroll down to bottom
            browser.execute_script(
                "window.scrollTo(0, 15);")

            # Wait to load page
            time.sleep(SCROLL_PAUSE_TIME)

            # Calculate new scroll height and compare with last scroll height
            new_height = browser.execute_script(
                "return document.body.scrollHeight")
                
            if new_height == last_height:
                more = browser.find_element(By.CLASS_NAME, 'show-more')
                time.sleep(SCROLL_PAUSE_TIME)


                ActionChains(browser).move_to_element(more).click(more).perform()
                i+=1
                if i == 3 :
                    more = None 
                if more == None:
                    break
                more.click()
            last_height = new_height
        time.sleep(SCROLL_PAUSE_TIME)
        response = browser.page_source

  
    except Exception as ex:

        print('\n\n\n')
        print(ex)
        print('\n\n\n')

    finally:
        browser.close()
        browser.quit()
        
        
        return render_template("index.html", goods_staf = stf_prsr.take_goods_list(BeautifulSoup(response)))


@app.route("/")
def main_page():
    stf_prsr = Staff_parser()
    staff = stf_prsr.get_goods_list()

    return render_template("index.html", goods_staf = staff)


@app.route("/good/")
def hello_there():

        name = request.args.get('link')   
    #try:
        stf_prsr = Staff_parser()
        staff = stf_prsr.get_good_details(name)
  
        
        browser = webdriver.Chrome(
            executable_path=chromedriver, chrome_options=options)
   
        browser.get(staff.link)        
        SCROLL_PAUSE_TIME = 2
        
        # Wait to load page
        time.sleep(SCROLL_PAUSE_TIME)            
           
        response = browser.page_source

        browser.close()
        browser.quit()

        
        return render_template("buy.html", good_info = stf_prsr.take_good_details(BeautifulSoup(response), staff))

    # except Exception as ex:

    #     print('\n\n\n')
    #     print(ex)
    #     print('\n\n\n')


        
       
        
        

    


app.run(debug=True)





















# response = requests.get(
#     url="https://rozetka.com.ua/1162070/c1162070/segment=top-brendi/",
#     headers={"User-agent": "your bot 0.1"},
# )


# email = browser.find_element_by_id('email')
# password = browser.find_element_by_id('password')
# login = browser.find_element_by_id('submit')
# email.send_keys('my_mail')
# password.send_keys('my_pass')
# login.click()

# with open("info.txt", "w", encoding="utf-8") as file:
#     file.write(response.text)
# with open("market_goods.txt", "a", encoding="utf-8") as file:
#     for i in market_goods:
#         file.write(str(i))
