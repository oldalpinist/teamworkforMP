from typing import Dict, List
import time
import requests
import csv


with open("output.csv", "w", encoding='utf8') as f:
    csv_writer = csv.writer(f)
    count = 0
    inn = input()
    for inn in range(100000000, 999999999):
        result = requests.get(f"https://egrul.itsoft.ru/{inn}.json")
        time.sleep(0.001)
        if inn in result:
            if result.status_code != 404:
                data = result.json()
            if 'СвЮЛ' not in data or '@attributes' not in data['СвЮЛ']:
                print("Unexpected format", data)
                continue
            company: Dict[str, str] = data['СвЮЛ']['@attributes']
            if count == 0:
                 csv_writer.writerow(company.keys())
            count = count + 1
            csv_writer.writerow(company.values())