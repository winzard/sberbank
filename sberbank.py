from bs4 import BeautifulSoup
import sys
report_file_name = str(sys.argv[1])
with open(report_file_name, 'r') as fp:
    with open(report_file_name+'.csv', "w") as output:
        soup = BeautifulSoup(fp, 'html.parser')
        soup_str = soup.prettify() # нужно, чтобы парсер не жрал первые буквы в строках. Не понял, почему он так работает
        soup = BeautifulSoup(soup_str, 'html.parser')
        transactions = soup.find_all(attrs={"class": "trs_head"})
        for transaction in transactions:
            name = transaction.find(attrs={"class": "trs_name"}).string.strip()
            data = transaction.find(attrs={"class": "idate"})['data-date']
            summ_tag = transaction.find(attrs={"class": "trs_sum"})
            income = summ_tag.find(attrs={"class": "trs_st-refill"})
            summ = summ_tag.get_text().strip()
            if not income:
                summ = '-' + summ
            category = transaction.find(attrs={"class": "icat"}).get_text().strip()
            print(name, ";", data, ";", summ, ";", category, file=output)
