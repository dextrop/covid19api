from requests import get
from bs4 import BeautifulSoup

class ScrapFromWiki():
    def __init__(self):
        self.url_india_count = "https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_India"

    def get_state_wise_data(self, state, other_details):
        state_name = state[1].text.replace("\n", "")
        active, death, recoveries, total = other_details[0].text, other_details[1].text, other_details[2].text, \
                                           other_details[3].text
        return {
            "name": state_name.replace("\n", ""),
            "active": int(active.replace("\n", "")),
            "death": int(death.replace("\n", "")),
            "recoveries": int(recoveries.replace("\n", "")),
            "total": int(total.replace("\n", ""))
        }

    def getDataIndia(self):
        html = get(self.url_india_count)
        soup = BeautifulSoup(html.text)
        tables = soup.find_all("table")
        data = []
        response = {
            "total": 0,
            "active": 0,
            "death": 0,
            "recovered": 0,
            "state_wise": []
        }
        for table in tables:
            if "2020 coronavirus pandemic in India by state and union territory" in table.text:
                table_row = table.find_all("tr")[2:]
                for element in table_row:
                    headings = element.find_all("th")
                    if (len(headings) == 2):
                        other_details = element.find_all("td")
                        try:
                            data.append(
                                self.get_state_wise_data(headings, other_details)
                            )
                        except:
                            pass

                    if (len(headings) == 5):
                        response["active"] = headings[1].text
                        response["death"] = headings[2].text
                        response["recovered"] = headings[3].text
                        response["total"] = headings[4].text

        response["state_wise"] = data
        return data
if __name__ == '__main__':
    print ScrapFromWiki().getDataIndia()