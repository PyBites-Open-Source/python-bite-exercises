def uppercase_vowels(text: str):
    vowels = "aeiouAEIOU"
    punct = ".?-*=!`';:_,~"
    extensions = [".mp3", ".jpg", ".jpeg", ".pdf", ".txt", ".mp4", ".png", ".exe"]
    cleaned_text = ""
    extension = ""
    for ex in extensions:
        if text.endswith(ex):
            extension = ex
            text = text.replace(ex, "")
            break
    for t in text:
        if t in vowels:
            cleaned_text += t.upper()
        elif t in punct:
            cleaned_text += " "
        else:
            cleaned_text += t.lower()
    return cleaned_text + extension if extension else cleaned_text
