from selenium import webdriver
from datetime import datetime
from bs4 import BeautifulSoup
from classes.good_details import Good_details
from models.good_model import Good_db
from classes.good import Good
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
from sqlalchemy import Column, Table, Integer, String, MetaData , any_, create_engine
from sqlalchemy.orm import sessionmaker


chromedriver = 'C:\\Users\\Divider\\source\\repos\\Repository_visual_code\\Python\\socet_parser\\chromedriver\\chromedriver.exe'

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('--ignore-certificate-errors-spki-list')


class Staff_parser:
    goods = []
    goods_details = []

    def __init__(self) -> None:
        pass
    
    def get_good_details(self, name):
        engine = create_engine('sqlite:///DB/orm.sqlite', echo=True) # connect to server
        Session = sessionmaker(bind=engine)
        session = Session()
       
        staff = session.query(Good_db).filter_by(name=name).first()
        session.close()
        return staff

    def get_goods_list(self ):
        engine = create_engine('sqlite:///DB/orm.sqlite', echo=True) # connect to server
        Session = sessionmaker(bind=engine)
        session = Session()
        staff = session.query(Good_db).order_by(Good_db.id)
        session.close()
        return staff


    def take_goods_list(self, soup):
        try:
            market_goods = soup.find_all("div", class_="goods-tile__inner")
            engine = create_engine('sqlite:///DB/orm.sqlite', echo=True) # connect to server
            Session = sessionmaker(bind=engine)
            session = Session()

            for i in market_goods:
                try:
                    good = Good_db(
                        len(self.goods),
                        i.find("a", class_="goods-tile__heading")["title"],
                        str(i.find("span", class_="goods-tile__price-value").get_text()),
                        i.find("img", class_="ng-lazyloaded")["src"],
                        i.find("a", class_="goods-tile__picture")["href"]
                    )
                    if(good.name != ''):
                        self.goods.append(good)
                        session.add(good)
                        session.commit()
                except Exception as ex:
                    pass
            
            
            session.close()
        except Exception as ex:

            print('\n\n\n')
            print(ex)
            print('\n\n\n')
        finally:
            
            return self.goods


    def take_goods_details_list(self, goods):
        try:
            browser = webdriver.Chrome(
                executable_path=chromedriver, chrome_options=options)
            browser.get('https://rozetka.com.ua/women_shoes/c721659/')
            browser.set_window_size(1500, 850)
            SCROLL_PAUSE_TIME = 3

            for good in goods:
                try:
                    browser.get(good.link)
                    time.sleep(SCROLL_PAUSE_TIME)
                    response = browser.page_source
                    self.goods_details.append(self.take_good_details(BeautifulSoup(response), good))
                except Exception as ex:
                    print('\n\n\n')
                    print(ex)
                    print('\n\n\n')

        except Exception as ex:

            print('\n\n\n')
            print(ex)
            print('\n\n\n')
        finally:
            return self.goods

    def take_good_details(self, soup, good):        
        try:
            photos = soup.find_all("img", class_="picture-container__picture")
            desc = soup.find("div", class_="product-about__description-content").get_text()
            charact = soup.find("div", class_="characteristics-full__group")
            sizes = soup.find("div", class_="var-options__wrapper").find_all("a", class_="stylelistrow")
        except Exception as ex:

            print('\n\n\n')
            print(ex)
            print('\n\n\n')
     
        try:
            imgs = []
            for i in photos:
                if 'изображение' in i['alt']:
                    imgs.append(i['src'])
                
                print('\n\n\n*****')
                print(i)
            print(len(imgs))
            print(len(imgs))
            print(len(imgs))
            print(len(imgs))
            print(len(imgs))
        except Exception as ex:

            print('\n\n\n')
            print(ex)
            print('\n\n\n')

        # try:
        #     imgs = []
        #     for i in photos:
        #         if 'var-options__block_cross_off' in i['class'] :
        #             imgs.append(i['src'])
                
        # except Exception as ex:

        #     print('\n\n\n')
        #     print(ex)
        #     print('\n\n\n')

        return Good_details(good.name,good.price,good.photo,good.link,imgs,desc,'')