from classes import scrapper
from classes.web import Web
from classes.scrapper import Scrapper
from classes.gui import Gui
from pprint import pp, pprint
import re
import sys


def is_in(search:str, vacc_list:list):
    search = search.upper()
    for vacc in vacc_list:
        if re.search(f'{search}', vacc.upper()):
            return True
    return False


def is_searched(searches:list, vacc:str):
    for search in searches:
        search = search.upper()
        if re.search(f'{search}', vacc.upper()):
            return True
    return False


if __name__ == '__main__':
    web = Web()
    scrapper = Scrapper()
    canada_page = web.get_canada_vacc_page()
    (approved_vaccines, disapproved_vaccines) = scrapper.get_vaccine_info(canada_page)
    pprint(approved_vaccines)
    pprint(disapproved_vaccines)
    search_vaccs = sys.argv[1:]        

    approved_vaccines_hilights = [(vacc, True) if is_searched(search_vaccs, vacc) else (vacc, False) for vacc in approved_vaccines]
    disapproved_vaccines_hilights = [(vacc, True) if is_searched(search_vaccs, vacc) else (vacc, False) for vacc in disapproved_vaccines]

    if len([vacc for vacc in search_vaccs if not is_in(vacc, approved_vaccines + disapproved_vaccines)]) > 0:
        disapproved_vaccines_hilights[-1] = (disapproved_vaccines_hilights[-1][0], True)
    gui = Gui(approved_vaccines_hilights, disapproved_vaccines_hilights)
    gui.mainloop()
    

