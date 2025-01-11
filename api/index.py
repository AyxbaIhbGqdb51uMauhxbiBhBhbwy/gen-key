from flask import Flask, jsonify
import random
import string

app = Flask(__name__)

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

@app.route('/fluxus', methods=['GET'])
def fluxus():
    random_hwid = generate_random_hwid_flux()
    url = f"https://flux.li/android/external/start.php?HWID={random_hwid}"
    return jsonify({"result": url})

@app.route('/trigon', methods=['GET'])
def trigon():
    random_hwid = generate_random_hwid_trigon()
    url = f"https://trigonevo.fun/whitelist/?HWID={random_hwid}"
    return jsonify({"result": url})

@app.route('/arceus', methods=['GET'])
def arceus():
    random_hwid = generate_random_hwid_arceus()
    url = f"https://spdmteam.com/key-system-1?hwid={random_hwid}&zone=Europe/Rome&os=android"
    return jsonify({"result": url})

@app.route('/vegax', methods=['GET'])
def vegax():
    random_hwid = generate_random_hwid_vegax()
    url = f"https://pandadevelopment.net/getkey?service=vegax&hwid={random_hwid}&provider=linkvertise"
    return jsonify({"result": url})

@app.route('/evon', methods=['GET'])
def evon():
    random_hwid = generate_random_hwid_evon()
    url = f"https://pandadevelopment.net/getkey?service=evon&hwid={random_hwid}"
    return jsonify({"result": url})

@app.route('/relz', methods=['GET'])
def relz():
    random_hwid = generate_random_hwid_relz()
    url = f"https://getkey.relzscript.xyz/redirect.php?hwid={random_hwid}"
    return jsonify({"result": url})

@app.route('/codex', methods=['GET'])
def codex():
    token = ''.join(random.choices(string.ascii_lowercase + string.digits, k=96))
    url = f"https://mobile.codex.lol/?token={token}"
    return jsonify({"result": url})

if __name__ == '__main__':
    app.run(debug=True)
