from classes import scrapper
from classes.web import Web
from classes.scrapper import Scrapper
from pprint import pp, pprint
import re
import sys


def is_approved(vaccine:str, approved_list:list):
    vaccine = vaccine.upper()
    for approved in approved_list:
        if re.search(f'{vaccine}', approved.upper()):
            return True
    return False


if __name__ == '__main__':
    web = Web()
    scrapper = Scrapper()
    canada_page = web.get_canada_vacc_page()
    (approved_vaccines, disapproved_vaccines) = scrapper.get_vaccine_info(canada_page)
    pprint(approved_vaccines)
    pprint(disapproved_vaccines)
    for searched_vacc in sys.argv[1:]:
        if is_approved(searched_vacc, approved_vaccines):
            pprint(f'{searched_vacc} found! :D')
        else:
            pprint(f'{searched_vacc} not found :(')

