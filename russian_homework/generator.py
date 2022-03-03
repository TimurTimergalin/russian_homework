import webbrowser
import requests
from bs4 import BeautifulSoup


class Generator:
    def handle_dictionary(self, dct):
        return {
            f"prob{x}": int(dct.get(x, 0))
            for x in range(1, 27)
        }

    def get_id_from_url(self, url):
        return url.split("id=")[1].split("&")[0]

    def get_test_inps(self, html):
        bs = BeautifulSoup(html, features="lxml")

        test_inps = bs.find_all(class_="test_inp")

        return {x["name"]: x["value"] for x in test_inps}

    def get_answers(self, html):
        bs = BeautifulSoup(html, features="lxml")

        ans = []

        for tr in bs.find_all(class_="res_row"):
            ans.append(tr.find_all("td")[-1].get_text())

        return ans

    def fill_answers(self, inps, answers):
        for i, key in enumerate(inps.keys()):
            if i < 5:
                continue
            inps[key] = answers[i - 5]

    def get_html(self, data):
        url = "https://rus.reshuege.ru"

        generator_url = "https://rus.reshuege.ru/test?a=generate"
        check_url = "https://rus.reshuege.ru/test"

        with requests.session() as s:
            s.get(url)

            res = s.post(generator_url, params=data)

            test_url = res.url

            test = s.get(test_url)

            inps = self.get_test_inps(test.text)

            res = s.post(check_url, params=inps)

            answer_page = s.get(res.url)

            answers = self.get_answers(answer_page.text)

            self.fill_answers(inps, answers)

            res = s.post(check_url, params=inps)

            return res.url

    def run(self, dct):
        webbrowser.open(self.get_html(self.handle_dictionary(dct)))


if __name__ == '__main__':
    g = Generator()

    data = {1: 3, 25: 4}

    # with open("testt.html", "w") as f:
    #     f.write(g.get_html(g.handle_dictionary(data)))

    g.run(data)




