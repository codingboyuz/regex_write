import re
def proxy_error_log():
    log_pattern = re.compile(
        r'(?P<date>\d{4}/\d{2}/\d{2})\s*(?P<time>\d{2}:\d{2}:\d{2}).*?'
        r'\[(?P<status>\w+)\]\s+(?P<error>[^\]]+?),.*?'  
        r'client:\s*(?P<ip>\d{1,3}(?:\.\d{1,3}){3}).*?' 
        r'server:\s*(?P<server>[^\s,]+).*?'  
        r'request:\s*"(?P<request>[^"]+)".*?'
        r'upstream:\s*"(?P<upstream>[^"]+)"',
        re.MULTILINE
    )

    log_file = '/home/alpha/Downloads/regex_write/logs/proxy_error_log'

    with open(log_file, 'r', encoding='utf-8') as file:
        for line in file:
            match = log_pattern.search(line)
            if match:
                data = match.groupdict()
                print(f"DateTime: {data['date']} {data['time']}")
                print(f"Status: [{data['status']}] {data['error']}")
                print(f"Client IP: {data['ip']}")
                print(f"Upstream: {data['upstream']}")  # ✅ To‘g‘ri chiqadi
                print(f"Request: {data['request']}")
                print("-" * 90)
                print("\n")
