from classes import scrapper
from classes.web import Web
from classes.scrapper import Scrapper
from classes.gui import Gui
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
    search_results = [
        (searched_vacc, True) if is_approved(searched_vacc, approved_vaccines) else (searched_vacc, False) for searched_vacc in sys.argv[1:]
    ]
    gui = Gui(approved_vaccines, disapproved_vaccines, search_results)
    gui.mainloop()
    

