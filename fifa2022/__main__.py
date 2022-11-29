import requests
import json
import time 

def main():
    url = "https://api.fifa.com/api/v3/calendar/17/255711/285063/standing"

    querystring = {"language":"en"}

    payload = ""
    headers = {
        "authority": "api.fifa.com",
        "accept": "application/json, text/plain, */*",
        "accept-language": "en-GB,en;q=0.8",
        "if-modified-since": "Tue, 29 Nov 2022 07:31:45 GMT",
        "origin": "https://www.fifa.com",
        "sec-ch-ua": 'Brave";v="107", "Chromium";v="107", "Not=A?Brand";v="24"',
        "sec-ch-ua-mobile": "?0",
        "sec-ch-ua-platform": "Linux",
        "sec-fetch-dest": "empty",
        "sec-fetch-mode": "cors",
        "sec-fetch-site": "same-site",
        "sec-gpc": "1",
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"
    }

    response = requests.request("GET", url, data=payload, headers=headers, params=querystring)

    # print(response.text)

    data=response.json()
    standing=[]

    for team in data['Results']:
        
        stat=( team['Position'], team['Group'][0]['Description'],team['Team']['ShortClubName'])
        standing.append(stat)

    standing.sort()

    index=[]
    country=[]

    for j in standing:
        index.append(j[1].split()[-1]+str(j[0]))
        country.append(j[2])

    D=dict(zip(index,country))

    t = time.localtime()
    current_time = time.strftime("%H:%M:%S", t)
    print("\nLast updated",current_time,'\n')

    print("PRE-QUARTER")
    print("__________________________________________________________")
    print(f"\nGroup A winner ({D['A1']}) x Group B runner ({D['B2']})")
    print(f"Group C winner ({D['C1']}) x Group D runner ({D['D2']})\n")
    print("----------------------------------------------------------")
    print(f"\nGroup D winner ({D['D1']}) x Group C runner ({D['C2']})")
    print(f"Group B winner ({D['B1']}) x Group A runner ({D['A2']})\n")
    print("----------------------------------------------------------")
    print(f"\nGroup E winner ({D['E1']}) x Group F runner ({D['F2']})")
    print(f"Group G winner ({D['G1']}) x Group H runner ({D['H2']})\n")
    print("----------------------------------------------------------")
    print(f"\nGroup F winner ({D['F1']}) x Group E runner ({D['E2']})")
    print(f"Group H winner ({D['H1']}) x Group G runner ({D['G2']})\n")
    print("----------------------------------------------------------")
    print("\nQUARTER")
    print("__________________________________________________________")
    print(f"\nGroup A winner ({D['A1']}) x Group B runner ({D['B2']})")
    print("                              vs                          ")
    print(f"Group C winner ({D['C1']}) x Group D runner ({D['D2']})\n")
    print("----------------------------------------------------------")
    print(f"\nGroup D winner ({D['D1']}) x Group C runner ({D['C2']})")
    print("                              vs                          ")
    print(f"Group B winner ({D['B1']}) x Group A runner ({D['A2']})\n")
    print("----------------------------------------------------------")
    print(f"\nGroup E winner ({D['E1']}) x Group F runner ({D['F2']})")
    print("                              vs                          ")
    print(f"Group G winner ({D['G1']}) x Group H runner ({D['H2']})\n")
    print("----------------------------------------------------------")
    print(f"\nGroup F winner ({D['F1']}) x Group E runner ({D['E2']})")
    print("                              vs                          ")
    print(f"Group H winner ({D['H1']}) x Group G runner ({D['G2']})")
    print("----------------------------------------------------------")

if __name__ == "__main__":
    main()