def detect_keywords(text):
    keywords = ["urgent", "verify", "login", "update", "click"]
    found = [word for word in keywords if word in text.lower()]
    return found

if __name__ == "__main__":
    email = input("Paste the email content:\n")
    result = detect_keywords(email)
    if result:
        print("Possible phishing attempt. Keywords found:", result)
    else:
        print(" No phishing keywords detected.")
