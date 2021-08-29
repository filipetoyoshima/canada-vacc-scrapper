from classes import scrapper
from classes.web import Web
from classes.scrapper import Scrapper
from pprint import pprint


if __name__ == '__main__':
    web = Web()
    scrapper = Scrapper()
    canada_page = web.get_canada_vacc_page()
    (approved_vaccines, disapproved_vaccines) = scrapper.get_vaccine_info(canada_page)
    pprint(approved_vaccines)
    pprint(disapproved_vaccines)