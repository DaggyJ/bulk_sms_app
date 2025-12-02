import requests
from config import CELCOM_API_URL, CELCOM_API_KEY, CELCOM_PARTNER_ID, CELCOM_SHORTCODE


def send_bulk_sms(message, recipients):
    payload = {
        "apikey": CELCOM_API_KEY,
        "partnerID": CELCOM_PARTNER_ID,
        "message": message,
        "mobile": ",".join(recipients),
        "shortcode": CELCOM_SHORTCODE
    }

    try:
        r = requests.post(CELCOM_API_URL, data=payload, timeout=15)

        try:
            return r.json()     # If Celcom returns valid JSON
        except:
            return {"raw": r.text}

    except Exception as e:
        return {"error": str(e)}



# -------------------------
# GET CELCOM BALANCE
# -------------------------
def get_celcom_balance():
    """
    Fetch the current SMS balance from Celcom API.
    Returns:
        int: Current balance (number of SMS units)
    """
    headers = {
        "Authorization": f"Bearer {CELCOM_API_KEY}",
        "Content-Type": "application/json"
    }

    try:
        response = requests.get(CELCOM_API_URL, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        # Assuming the API returns {"balance": 1234}
        return int(data.get("balance", 0))
    except requests.RequestException as e:
        print("Error fetching Celcom balance:", e)
        return 0
    except (ValueError, TypeError) as e:
        print("Error parsing Celcom balance:", e)
        return 0
