import requests

def get_meta():
    url = "https://api.metatft.com/tft/comps?queue=1100"

    try:
        res = requests.get(url, timeout=10)
        data = res.json()

        comps = []

        for c in data.get("data", [])[:10]:
            comps.append({
                "name": c.get("name", "Unknown"),
                "tier": c.get("tier", "A"),
                "image": c.get("image", ""),
                "units": [u.get("name", "") for u in c.get("units", [])],
                "items": ["Auto"],
                "augments": ["Auto"]
            })

        return comps

    except Exception as e:
        print("META ERROR:", e)
        return []