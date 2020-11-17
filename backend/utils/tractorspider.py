import re
import os
import argparse
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import urllib.request
from bs4 import BeautifulSoup
import json

SHORT_WAIT=1
MEDIUM_WAIT=10
LONG_WAIT=60

def main(destination):
    driver = webdriver.Firefox()

    # Open search page
    driver.get("https://www.hasznaltauto.hu/kereso/munkagep")

    # Select category
    category = WebDriverWait(driver, MEDIUM_WAIT).until(EC.presence_of_element_located((By.ID, "hirdetesmunkagepsearch-kivitel")))
    Select(category).select_by_visible_text("traktor")

    # Click submit button
    submit = WebDriverWait(driver, MEDIUM_WAIT).until(EC.presence_of_element_located((By.XPATH, "//button[@name='submitKereses']")))
    submit.click()

    while True:
        # Wait for matches to appear
        WebDriverWait(driver, MEDIUM_WAIT).until(EC.presence_of_element_located((By.XPATH, "//div[contains(@class,'talalatisor-tartalom')]/..")))

        tractor_nodes = [node.find_element(By.XPATH, "./..") for node in driver.find_elements_by_class_name("talalatisor-tartalom")]

        for node in tractor_nodes:
            save_tractor(node, destination)

        # Find "next" button
        next_btn = driver.find_element_by_xpath("//div[@id='talalati']//ul[contains(@class, 'pagination')]//li[contains(@class, 'next')]")
        
        # Click if enabled, otherwise exit the loop
        if "disabled" not in next_btn.get_attribute("class").lower():
            next_btn.click()
            sleep(1)
        else:
            break



def save_tractor(node, destination):
    link = node.find_elements_by_xpath(".//div[contains(@class, 'cim-kontener')]/h3/a")[0]
    href = link.get_attribute("href")

    match = re.search(r"\d+$", href)
    if match:
        local_file = os.path.join(destination, match[0] + ".json")

        if not os.path.exists(local_file):
            print(href)

            document = read_product_page(href)
            tractor = prase_product_page(document)
            tractor["url"] = href

            with open(local_file, "w", encoding='utf8') as f:
                json.dump(tractor, f, ensure_ascii=False)


def read_product_page(url):
    with urllib.request.urlopen(url) as response:
        return response.read()

def prase_product_page(document):
    soup = BeautifulSoup(document, 'html.parser')
    
    datasheet_node = soup.select_one("div#adatlap")
    title_node = datasheet_node.select_one("div.adatlap-cim")
    img_node = datasheet_node.select_one("div#adatlap-kepek-placeholder").select_one("img")
    right_column_node = datasheet_node.select_one("div.adatlap-jobb-hasab")
    details_node = right_column_node.select_one("table.hirdetesadatok")
    equipment_node = right_column_node.select_one("div.felszereltseg")
    description_node = right_column_node.select_one("div.leiras")

    tractor = parse_details(details_node)

    gyarto, tipus = parse_title(title_node)

    tractor["image_url"] = img_node.get("src", None)
    tractor["make"] = gyarto
    tractor["model"] = tipus

    tractor["description"] = parse_description(description_node)

    tractor["equipment"] = parse_equipment(equipment_node)

    return tractor    

def parse_title(node):
    text = node.get_text().strip()

    for make in makes:
        if text.upper().startswith(make):
            return (make, text[len(make):].upper().strip())
    
    parts = text.split(maxsplit=1)

    # extend list to 2 elements
    return tuple(part.upper() for part in parts+[""]*(2-len(parts)))

def parse_description(node):
    text = ""
    if node is not None:
        text = node.select_one("div").get_text().strip()
    
    return text

def parse_details(node):
    result = {}

    for tr in node.select("tr"):
        tds = tr.select("td")
        if len(tds)==2:
            field = tds[0].get_text().strip()
            value = tds[1].get_text().strip()
            if field in field_codes:
                result[field_codes[field]] = value

    return result


def parse_equipment(node):
    result = []
    if node is not None:
        for item in node.select("li"):
            result.append(item.get_text().strip())
        
    return result


makes = [ 
    "AGM", "AGRIKON", "AGROZET", "AL-KO", "AMA", "AMAZONE", "AZIM", "BAUTZ", "BELARUS",
    "BOBCAT", "BRANSON", "BUCHER", "BUSA", "CARRARO", "CASE", "CASE IH", "CATERPILLAR",
    "CLAAS", "CSEPEL", "DAMMANN", "DETK", "DEUTZ-FAHR", "DUTRA", "EGYEDI", "EICHER", "EPPLE",
    "FELLA", "FENDT", "FENG-SHOU", "FERRARI", "FIAT", "FLIEGL", "FORCE", "FORD", "FORT",
    "FORTSCHRITT", "FOTON", "GEO", "GOLDONI", "GREENMECH", "GRILLO", "GUTBROD", "HAKO",
    "HARKOV", "HINOMOTO", "HOFHERR", "HOLDER", "HOLMER", "HONDA", "HUSQVARNA", "HYTEC", "IH",
    "IHC", "IRUM", "ISEKI", "JAKOBY", "JCB", "JOHN DEERE", "KERTITOX", "KOMÁROMIGÉP",
    "KOMATSU", "KRONE", "KSMK", "KUBOTA", "KVERNELAND", "LAMBORGHINI", "LEKO", "LEMKEN",
    "LIEBHERR", "LOMBARDINI", "LS TRACTOR", "LTZ", "MAN", "MANITOU", "MASSEY FERGUSON",
    "MC CORMICK", "MCHALE", "MERCEDES-BENZ", "MERLO", "MITSUBISHI", "MTD", "MTZ", "NAS",
    "NEW HOLLAND", "NEW IDEA", "NOBILI", "ORSI", "PÖTTINGER", "RÁBA", "RABE", "RABEWERK",
    "RANSOMES", "REGENT", "RENAULT", "RTS", "SAME", "SAXONIA", "SIPMA", "SOKORÓ", "SOLIS",
    "STEYR", "TORNADO", "UNIMOG", "VÄDERSTADT", "VALTRA", "VICON", "VLADIMIREC",
    "VOGEL & NOOT", "WARCHALOWSKI", "WEIDEMANN", "WIRAX", "WOLF", "WOPROL", "YANMAR", "YTO",
    "ZETOR",
]


field_codes = {
    "Vételár:": "price",
    "Évjárat:": "year",
    "Állapot:": "condition",
    "Üzemanyag": "fuel_type",
    "Üzemóra:": "hours",
    "Maximális teljesítmény:": "engine_power",
    "Okmányok jellege:": "documents_type",
    "Műszaki vizsga érvényes:": "documents_validity",
}

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Scrapes tractors from hasznaltauto.hu", fromfile_prefix_chars="@")
    parser.add_argument("destination", help="Folder to save the json files")
    args = parser.parse_args()

    if not os.path.isdir(args.destination):
        print("destination is not a directory")
        exit()

    main(args.destination)
