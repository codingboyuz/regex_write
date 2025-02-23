from typing import Any

import requests

def get_ip_info(ip: str) -> str | dict[str, str | Any]:
    try:
        response = requests.get(f"http://ip-api.com/json/{ip}")
        data = response.json()
        if data['status'] == 'fail':
            return "Ma'lumot topilmadi!"
        info = {
            "IP": data.get("query", "Aniqlanmadi"),
            "Mamlakat": data.get("country", "Aniqlanmadi"),
            "Shahar": data.get("city", "Aniqlanmadi"),
            "ISP (provayder)": data.get("isp", "Aniqlanmadi"),
            "Tashkilot": data.get("org", "Aniqlanmadi"),
            "Hudud": data.get("regionName", "Aniqlanmadi"),
            "Koordinatalar": f"{data.get('lat', 'Aniqlanmadi')}, {data.get('lon', 'Aniqlanmadi')}",
            "Tarmoq": data.get("as", "Aniqlanmadi"),
        }
        return info
    except requests.RequestException:
        return "Ma'lumot olishda xatolik yuz berdi!"


