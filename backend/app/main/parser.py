from selenium import webdriver
from app import db
from flask import current_app
from sqlalchemy import create_engine
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from app.models import Map
import re

engine = create_engine("sqlite:///Map.db")
for id in range(593, 594):
    from backend.main import app
    chrome_options = Options()
    driver = webdriver.Chrome(options=chrome_options)
    driver.get("https://egrp365.org/reestr?egrp=40:25:000237:"+str(id))
    kadastr_number = driver.find_element(By.XPATH, "//*[contains(text(), 'Кадастровый номер')]")
    square = driver.find_element(By.XPATH, "//*[contains(text(), 'Плoщадь')]")
    kadastr_number = kadastr_number.text.strip("Кадастровый номер")
    sep = '\n'
    square = square.text.split(sep, 1)[0]
    square = square.split("м",1)[0]
    square = re.sub('\D', '', square)

    new_map = Map(kadastr_number=kadastr_number, square=int(float(square)), kadastr_id=id)
    print(new_map)
    with app.app_context():
        db.session.add(new_map)
        db.session.commit()

