from typing import DefaultDict
import requests


DEFAULT_LINK = 'https://travel.gc.ca/travel-covid/travel-restrictions/covid-vaccinated-travellers-entering-canada'


class Web:
    def __init__(self, link=DEFAULT_LINK):
        self.link = link

    
    def get_canada_vacc_page(self):
        r = requests.get(self.link)
        if r.ok:
            return r.text
        else:
            r.raise_for_status()