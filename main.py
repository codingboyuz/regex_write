import re
import argparse
from datetime import datetime

from get_ip_info import get_ip_info


def date_time_parser(date_time):
    # DateTime formatiga o'girish
    parsed_time = datetime.strptime(date_time, "%d/%b/%Y:%H:%M:%S %z")

    formatted_date = parsed_time.strftime("%Y-%m-%d")
    return formatted_date

def access_log():
    parser = argparse.ArgumentParser(description="Filter log by IP address and date")
    parser.add_argument("-p",type=str, metavar="--path", help="Log file path input")
    parser.add_argument("-ip",type=str, metavar="--ipaddress", help="IP address to filter")
    parser.add_argument("-dt",type=str, metavar="--datetime", help="DataTime to filter example '2021-08-10'")
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
    # request counter
    counter = 0

    with open(args.p,'r', encoding='utf-8') as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                data = match.groupdict()
                ip_match = args.ip is None or args.ip == data['ip']
                log_datetime = date_time_parser(data['datetime'])
                time_match = args.dt is None or args.dt == log_datetime
                if ip_match and time_match:
                    counter += 1
                    print(f"DateTime: {data['datetime']}")
                    print(f"IP: {data['ip']}")
                    print(f"Request: {data['request']}")
                    print(f"Http: {data['http']}")
                    print(f"Status: {data['status']}")
                    print('-'*90)

            else:
                print("No match")
    print(f'Request counter: {counter}')
    ip_info= get_ip_info(args.ip)
    for key,value in ip_info.items():
        print(f"{key}: {value}")




if __name__ == '__main__':
    access_log()