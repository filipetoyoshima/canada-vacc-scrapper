from bs4 import BeautifulSoup
import re


class Scrapper:
    def get_vaccine_info(self, web_page):
        """
        Input: HTML of 'COVID-19 vaccinated travellers entering Canada'
        web page.
    
        Output: (
            list of approved vaccines,
            list of not yet approved vaccines
        )
        """
        soup = BeautifulSoup(web_page, 'html.parser')
        uls = soup.find_all('ul', {'class': 'fa-ul'})
        vaccine_lists = [
            [re.search('</span>(.*)</li>', str(vac), re.S).group(1) for vac in vac_list] for vac_list in [ul.find_all('li') for ul in uls]
        ]
        vaccine_lists = [[re.sub('\r|\n', '', vac) for vac in vac_list] for vac_list in vaccine_lists]
        vaccine_lists = [[re.sub('\s\s+', ' ', vac) for vac in vac_list] for vac_list in vaccine_lists]
        vaccine_lists = [[re.sub('&amp;', '&', vac) for vac in vac_list] for vac_list in vaccine_lists]
        [approved_vaccs, disapproved_vaccs] = vaccine_lists
        return (approved_vaccs, disapproved_vaccs)