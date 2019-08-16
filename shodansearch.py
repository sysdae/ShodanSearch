import shodan
import sys


shodan_api_key = "" #Enter your shodan API key here

api = shodan.Shodan(shodan_api_key)

if len(sys.argv)< 2:
    print(" ")
    print(" -------------------------------")
    print("| -> SHODANSEARCH <- by SystemD |")
    print(" -------------------------------")
    print(" ")
    print("Results are limited to 100")
    print("First enter your shodan API key")
    print("usage : python3 shodansearch.py <query search>")
    print("ie : python3 shodansearch.py apache")
    print(" ")
    sys.exit(0)

try:
    print(" ")
    print(" -------------------------------")
    print("| -> SHODANSEARCH <- by SystemD |")
    print(" -------------------------------")
    print(" ")
    query=sys.argv[1]
    results = api.search(query)

    for result in results['matches']:
        print(result['ip_str'])
    
    print(" ")

except shodan.APIError as e:
    print(e)
