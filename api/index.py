from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

# Fungsi Generator HWID
def generate_random_hwid_flux(length=96):
    allowed_chars = string.ascii_lowercase + string.digits
    return ''.join(random.choice(allowed_chars) for _ in range(length))

def generate_random_hwid_trigon():
    segments = [
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)),
    ]
    return '-'.join(segments)

def generate_random_hwid_arceus(length=18):
    return ''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(length))

def generate_random_hwid_vegax():
    segments = [
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=6)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
    ]
    return '-'.join(segments)

def generate_random_hwid_evon():
    segments = [
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=8)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=4)),
        ''.join(random.choices(string.ascii_lowercase + string.digits, k=12)),
    ]
    return '-'.join(segments)

def generate_random_hwid_relz():
    segments = [
        ''.join(random.choices(string.hexdigits.lower(), k=8)),
        ''.join(random.choices(string.hexdigits.lower(), k=4)),
        ''.join(random.choices(string.hexdigits.lower(), k=4)),
        ''.join(random.choices(string.hexdigits.lower(), k=4)),
        ''.join(random.choices(string.hexdigits.lower(), k=12)),
    ]
    return '-'.join(segments)

def generate_random_hwid_atlantis():
    return ''.join(random.choices(string.ascii_lowercase + string.digits, k=12))

# Endpoint Dinamis
@app.route('/<service>', methods=['GET'])
def handle_service(service):
    service = service.lower()  # Mengubah input menjadi huruf kecil untuk pencocokan
    if service == 'fluxus':
        random_hwid = generate_random_hwid_flux()
        url = f"https://flux.li/android/external/start.php?HWID={random_hwid}"
    elif service == 'trigon':
        random_hwid = generate_random_hwid_trigon()
        url = f"https://trigonevo.fun/whitelist/?HWID={random_hwid}"
    elif service == 'arceus':
        random_hwid = generate_random_hwid_arceus()
        url = f"https://spdmteam.com/key-system-1?hwid={random_hwid}&zone=Europe/Rome&os=android"
    elif service == 'vegax':
        random_hwid = generate_random_hwid_vegax()
        url = f"https://pandadevelopment.net/getkey?service=vegax&hwid={random_hwid}&provider=linkvertise"
    elif service == 'evon':
        random_hwid = generate_random_hwid_evon()
        url = f"https://pandadevelopment.net/getkey?service=evon&hwid={random_hwid}"
    elif service == 'relz':
        random_hwid = generate_random_hwid_relz()
        url = f"https://getkey.relzscript.xyz/redirect.php?hwid={random_hwid}"
    elif service == 'codex':
        token = ''.join(random.choices(string.ascii_lowercase + string.digits, k=96))
        url = f"https://mobile.codex.lol/?token={token}"
    elif service == 'atlantis':
        random_hwid = generate_random_hwid_atlantis()
        url = f"https://getatlantis.xyz/keysystem?hwid={random_hwid}"
    else:
        return jsonify({"error": "Service not found"}), 404

    return jsonify({"link": url})

if __name__ == '__main__':
    app.run(debug=True)
