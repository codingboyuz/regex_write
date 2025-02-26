import re
import argparse
from datetime import datetime

from get_ip_info import get_ip_info
from collections import Counter
def date_time_parser(date_time):
    # DateTime formatiga o'girish
    parsed_time = datetime.strptime(date_time, "%d/%b/%Y:%H:%M:%S %z")

    formatted_date = parsed_time.strftime("%Y-%m-%d")
    return formatted_date

def access_log():
    # request counter
    counter = 0
    ip_counter = Counter()


    parser = argparse.ArgumentParser(description="Filter log by IP address and date")
    parser.add_argument("-c",type=str, metavar="--counter", help="all ip addresses request counter ")
    parser.add_argument("-r",type=str, metavar="--request", help="Requests type post or get ")
    parser.add_argument("-p",type=str, metavar="--path", help="Log file path input")
    parser.add_argument("-ip",type=str, metavar="--ipaddress", help="IP address to filter")
    
    parser.add_argument("-dt",type=str, metavar="--datetime", help="DataTime to filter example '2021-08-10'")
    parser.add_argument("-s",type=str, metavar="--ststusCode", help="Status code to filter example '2021-08-10'")
    args = parser.parse_args()


    # Dict ko'rinishida filterlash
    log_pattern = re.compile(
        r'(?P<ip>\d{1,3}(?:\.\d{1,3}){3})\s+-\s+-\s+' 
        r'\[(?P<datetime>[^\]]+)\]\s+'  
        r'"(?P<request>[^"]+)"\s+'  
        r'(?P<status>\d{3})\s+'  
        r'\d+\s+"(?P<http>[^"]+)"',
        re.MULTILINE
    )

    try:
        with open(args.p,'r', encoding='utf-8') as file:
            for line in file:
                match = log_pattern.search(line)
                if match:

                    data = match.groupdict()

                    if args.c == "y":
                        ip_counter[data['ip']] += 1

                    ip_match = args.ip is None or args.ip == data['ip']
                    log_datetime = date_time_parser(data['datetime'])
                    time_match = args.dt is None or args.dt == log_datetime
                    request_match = args.r is None or args.r.upper() in data['request']
                    status_match = args.s is None or args.s in data['status']
                    if ip_match and time_match and request_match and status_match:
                        counter += 1
                        print(f"DateTime: {data['datetime']}")
                        print(f"IP: {data['ip']}")
                        print(f"Request: {data['request']}")
                        print(f"Http: {data['http']}")
                        print(f"Status: {data['status']}")
                        print('-'*90)

                else:
                    print("No match")
        print('\n\n')
        if args.c == 'y':
            with open('ip', 'w', encoding='utf-8') as f:
                for ip, cnt in ip_counter.most_common():
                    f.write(f"{ip}: {cnt} so'ro'v\n")

                print("-"*50)

        print(f'Request counter: {counter}')

        try:
            if counter != 0:
                ip_info= get_ip_info(args.ip)
                for key,value in ip_info.items():
                    print(f"{key}: {value}")
            print('No request')
        except Exception:
            print(f"No IP address")

    except FileNotFoundError:
        print("No such file or directory")




if __name__ == '__main__':
    access_log()