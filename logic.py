def get_recommendation(data):
    sip = int(data.get("sip", 0))
    tenure = int(data.get("tenure", 0))
    risk = data.get("risk", "").lower()

    # Dummy logic - Replace with real matrix
    if risk == "high" and tenure >= 7 and sip >= 10000:
        return {
            "fund": "Quant Flexicap Fund",
            "reason_en": "High risk profile, long tenure and good SIP size. Flexicap gives exposure to multi-cap opportunities.",
            "reason_hi": "हाई रिस्क प्रोफाइल, लंबी अवधि और अच्छा SIP. फ्लेक्सीकैप फंड मल्टीकैप अवसर देता है।"
        }
    elif risk == "medium":
        return {
            "fund": "ICICI Prudential Balanced Advantage Fund",
            "reason_en": "Balanced fund suited for medium risk profiles.",
            "reason_hi": "मीडियम रिस्क प्रोफाइल के लिए संतुलित फंड उपयुक्त है।"
        }
    else:
        return {
            "fund": "HDFC Short Term Debt Fund",
            "reason_en": "Lower risk and short-term investment horizon. Safer option.",
            "reason_hi": "कम जोखिम और कम अवधि के लिए सुरक्षित विकल्प।"
        }