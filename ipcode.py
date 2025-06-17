import requests



def get_info_by_ip(ip='127.0.0.1'):
    try:
        response = requests.get(url=f'http://ip-api.com/json/{ip}').json()

        data = {
            '[IP]': response.get('query'),
            '[Int prov]': response.get('isp'),
            '[Org]': response.get('org'),
            '[Country]': response.get('country'),
            '[Region Name]': response.get('regionName'),
            '[City]': response.get('city'),
            '[ZIP]': response.get('zip'),
            '[Lat]': response.get('lat'),
            '[Lon]': response.get('lon'),
        }

        result = "🔍 Info about IP:\n\n"
        for k, v in data.items():
            if v:
                result += f"<b>{k}:</b> {v}\n"


        if data['Широта'] and data['Долгота']:
            result += f"\n🌍 https://www.google.com/maps?q={data['Широта']},{data['Долгота']}"

        return result

    except requests.exceptions.ConnectionError:
        return "⚠️ Connection error. Please check your internet connection."

