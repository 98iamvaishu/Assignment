from selenium import webdriver
from itertools import zip_longest
import csv
image_url = []
num_cashless = []
anual_income = []
driver = webdriver.Chrome(executable_path=r'C:/Users/vaishnavi/Downloads/chromedriver_win32/chromedriver.exe')
driver.get(
    "https://health.policybazaar.com/quotes?tabel=4&enquiryid=MTQ0MjI1MjM0&profileid=35419148")
for image in driver.find_elements_by_xpath('//div[@class="quotes-box-inner1"]//img[@src]'):
    image_url.append(image.get_attribute('src'))
for elem in driver.find_elements_by_xpath('.//span[@class = "cash-hospital ng-binding ng-scope"]'):
    if elem.text != '':
        num_cashless.append(elem.text)
for elem in driver.find_elements_by_xpath('//div[@class="anual-text ng-binding ng-scope"]'):
    anual_income.append(elem.text)
d = [image_url, num_cashless, anual_income]
export_data = zip_longest(*d, fillvalue='')
with open('data.csv', 'w', encoding="ISO-8859-1", newline='') as file:
    wr = csv.writer(file)
    wr.writerow(("ImageURL", "Number of cashless hospitals", "Annual Premium"))
    wr.writerows(export_data)
file.close()
