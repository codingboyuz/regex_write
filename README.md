# **Loglarni tahlil qilish dasturi**  

Ushbu dastur Apache yoki Nginx server loglarini tahlil qilish uchun mo‘ljallangan. Log faylni o‘qib, IP-manzillar, so‘rov turlari, status kodlari va boshqa ma’lumotlarni filtrlash imkonini beradi.  

## **O‘rnatish**  
Dasturdan foydalanish uchun quyidagi kutubxonalar talab qilinadi:  

```bash
pip install requests
```

## **Foydalanish**  
Dasturdan foydalanish uchun `main.py` faylini ishga tushirish kerak:  

```bash
python main.py -p log_file_path
```

### **Qo‘llab-quvvatlanadigan argumentlar:**  
- `-p` — Log fayl yo‘li (majburiy)  
- `-ip` — Faqat berilgan IP-manzil bo‘yicha filtr  
- `-dt` — Sana bo‘yicha filtr (`YYYY-MM-DD` formatida)  
- `-r` — So‘rov turi (`GET`, `POST`, va h.k.)  
- `-s` — Status kodi (`200`, `404`, va h.k.)  
- `-rp` — So‘rov yo‘li bo‘yicha filtr (`wp-admin`, `wp-login`, va h.k.)  
- `-a` — User-agent bo‘yicha filtr  
- `-c y` — Barcha IP-manzillarning so‘rovlar sonini hisoblash  

### **Misollar va natijalar**  

#### **1. Log faylni tahlil qilish:**  
```bash
python main.py -p access.log
```
**Natija:**  
```
DateTime: 27/Feb/2024:12:30:15 +0000
IP: 192.168.1.1
Request: GET /index.html HTTP/1.1
User agent: Mozilla/5.0
Http: https://example.com
Status: 200
------------------------------------------------------------------------------------------
Request counter: 1
```

#### **2. Muayyan IP bo‘yicha filtrlash:**  
```bash
python main.py -p access.log -ip 192.168.1.1
```
**Natija:**  
```
DateTime: 27/Feb/2024:12:30:15 +0000
IP: 192.168.1.1
Request: GET /index.html HTTP/1.1
User agent: Mozilla/5.0
Http: https://example.com
Status: 200
------------------------------------------------------------------------------------------
Request counter: 1

IP haqida ma'lumot:
IP: 192.168.1.1
Mamlakat: USA
Shahar: New York
ISP (provayder): AT&T
Tashkilot: AT&T Services Inc.
Hudud: New York
Koordinatalar: 40.7128, -74.0060
Tarmoq: AS7018 AT&T Services Inc.
```

#### **3. GET so‘rovlarini chiqarish:**  
```bash
python main.py -p access.log -r GET
```
**Natija:**  
```
DateTime: 27/Feb/2024:12:30:15 +0000
IP: 192.168.1.1
Request: GET /index.html HTTP/1.1
User agent: Mozilla/5.0
Http: https://example.com
Status: 200
------------------------------------------------------------------------------------------
Request counter: 1
```

#### **4. Barcha IP-larning so‘rovlar sonini hisoblash:**  
```bash
python main.py -p access.log -c y
```
**Natija (`ip` fayliga yoziladi):**  
```
192.168.1.1: 10 so'ro'v
192.168.1.2: 7 so'ro'v
192.168.1.3: 5 so'ro'v
```

## **Muammo va xatolar**  
- Agar log fayli topilmasa: `No such file or directory`  
- Agar mos keluvchi log topilmasa: `No match`  
- Agar IP haqida ma’lumot olinmasa: `Ma'lumot topilmadi!`  

Dastur log tahlil qilish va xavfsizlik monitoringi uchun foydali hisoblanadi.
---

## 1. Asosiy tushunchalar

### 1.1. Maxsus belgilar
- **.** — har qanday bitta belgini ifodalaydi (yangi qatordan tashqari).
- **^** — satr boshini anglatadi.
- **$** — satr oxirini anglatadi.
- **\*** — oldingi belgi yoki guruh 0 yoki ko‘p marta takrorlanishini bildiradi.
- **+** — oldingi belgi yoki guruh 1 yoki ko‘p marta takrorlanishini bildiradi.
- **?** — oldingi belgi yoki guruh 0 yoki 1 marta takrorlanishini bildiradi.
- **\d** — raqam (0-9) bilan mos keladi.
- **\w** — so‘z belgilari (harflar, raqamlar va pastki chiziq: _).
- **\s** — bo‘shliq (space, tab, yangi qator).
- **[]** — qavs ichida berilgan har qanday belgiga mos keladi. Masalan, `[abc]` — faqat `a`, `b` yoki `c`.
- **[^]** — qavs ichidagi belgilardan tashqari bo‘lgan har qanday belgi. Masalan, `[^abc]` — `a`, `b`, `c` bo‘lmagan har qanday belgi.
- **()** — qavslar yordamida guruh yaratish va keyinchalik o‘sha guruhni alohida ajratish mumkin.
- **|** — "yoki" operatori. Masalan, `cat|dog` — `cat` yoki `dog`.

### 1.2. Qaytaruvchi miqdorlar (Quantifiers)
- **{n}** — oldingi belgi yoki guruh aniq n marta takrorlanishi kerak. Masalan, `\d{3}` — aniq uchta raqam.
- **{n,}** — kamida n marta.
- **{n,m}** — n marta minimal va m marta maksimal.

---

## 2. Misollar bilan tushuntirish

### 2.1. Oddiy misollar

**Misol 1:**  
Matndan barcha raqamlarni qidirish:  
- Regex: `\d+`  
  - **\d** — raqam belgisini bildiradi.  
  - **+** — bitta yoki ko‘p raqam.  
  - Natija: "123", "4567", "89" kabi raqamlar.

**Misol 2:**  
Matndan faqat inglizcha so‘zlarni ajratib olish:  
- Regex: `\b[a-zA-Z]+\b`  
  - **\b** — so‘z chegarasi.  
  - **[a-zA-Z]+** — bitta yoki ko‘p ingliz harfi.
  - Natija: "Hello", "world" kabi so‘zlar.

**Misol 3:**  
Email manzillarini aniqlash:  
- Regex: `[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+`  
  - Bu andoza email adreslarining oddiy shaklini qamrab oladi.

### 2.2. Guruhlar va oraliqlar

**Misol 4:**  
Telefon raqamini qidirish (masalan, (123) 456-7890 formatida):  
- Regex: `\(\d{3}\)\s?\d{3}-\d{4}`  
  - `\(` va `\)` — qavslarni belgilash uchun (maxsus belgilar, shuning uchun escape qilinadi).  
  - `\d{3}` — uchta raqam.
  - `\s?` — bo‘shliq (ixtiyoriy).
  - `-` — chiziq belgisini bildiradi.
  - `\d{4}` — to‘rtta raqam.

**Misol 5:**  
URL dan protokolni, domen nomini va resurs yo‘lini ajratish:  
- Regex: `^(?P<protocol>https?)://(?P<domain>[^/]+)(?P<path>/.*)?$`  
  - `(?P<protocol>https?)` — nomlangan guruh, "http" yoki "https"  
  - `://` — protokolni ajratish belgisi.
  - `(?P<domain>[^/]+)` — domen nomi, `/` belgidan tashqari barcha belgilar.
  - `(?P<path>/.*)?` — resurs yo‘li, ixtiyoriy.

---

## 3. Python-dagi regex misoli

Quyidagi kod yordamida matndan email adreslarini qidirishni ko‘rib chiqamiz:

```python
import re

# Misol matn
text = "Bizning elektron pochta: example.user@mail.com va boshqa: test123@example.co.uk"

# Email aniqlash regex andozasi
email_pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')

# Matndan email manzillarini qidirish
emails = email_pattern.findall(text)

print("Topilgan email manzillari:")
for email in emails:
    print(email)
```

---

## 4. Amaliyot va maslahatlar

- **Amaliyot qiling:**  
  Turli misollar yozing va ularda regex ishlatib ko‘ring. Regex101 kabi saytlar yordamida andozalarni sinab ko‘rish qulay (https://regex101.com/).

- **Qayta ko‘rib chiqing:**  
  Regexlar murakkab bo‘lishi mumkin. Har bir belgi va guruhning ma’nosini yaxshilab tushunishga harakat qiling.

- **Qayta ishlash:**  
  Real loyihalarda regexni qo‘llashdan oldin, uni sinab ko‘ring va natijalarni tekshiring.

---

Regex yozishni o‘rganish va amaliyotda qo‘llash orqali siz murakkab matn manipulyatsiyalari va qidiruvlarini oson amalga oshirishingiz mumkin. Agar qo‘shimcha savollar bo‘lsa yoki maxsus misol kerak bo‘lsa, so‘rashingiz mumkin!
