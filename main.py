# Regex andoza:
log_pattern = re.compile(
    r'client:\s*(?P<ip>\d{1,3}(?:\.\d{1,3}){3})',

    re.MULTILINE
)
# Log fayl nomi
log_filename = 'C:\\Users\\User-39\\Downloads\\qttsm.uz\\qttsm.uz\\qttsm.uz2\\logs\\proxy_error_log'
# log ='C:\\Users\\User-39\Downloads\qttsm.uz\qttsm.uz\qttsm.uz2\logs\proxy_error_log'
# log ='C:\\Users\\User-39\Downloads\qttsm.uz\qttsm.uz\qttsm.uz2\logs\proxy_error_log'
log = 'C:/Users/User-39/Downloads/qttsm.uz/qttsm.uz/qttsm.uz2/logs/proxy_error_log'

with open(log, 'r', encoding='utf-8') as file:
    for line in file:
        # Har bir satrni chop etamiz (ixtiyoriy)
        # Har bir satrdagi nomlangan guruh asosida IP manzilini qidiramiz:
        for match in log_pattern.finditer(line):
            data = match.groupdict()
            print(data['ip'])
            # print(f"Vaqt: {data['timestamp']}")
            # print(f"Daraja: {data['level']}")
            # print(f"Mijoz: {data['client']}")
            # print(f"So'rov: {data['method']} {data['url']}")
            # print("-" * 50)
