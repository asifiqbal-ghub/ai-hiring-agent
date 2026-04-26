def decision(data):

    if data.get("ai") == "Yes":
        data["decision"] = "Rejected - AI"

    elif data.get("score", 0) >= 80:
        data["decision"] = "Selected"

    elif data.get("score", 0) >= 70:
        data["decision"] = "Hold"

    else:
        data["decision"] = "Rejected"

    return data