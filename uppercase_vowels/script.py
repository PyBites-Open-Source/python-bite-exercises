from string import punctuation


def uppercase_vowels(text: str):
    VOWELS = "aeiou"
    EXTENSIONS = [".mp3", ".jpg", ".jpeg", ".pdf", ".txt", ".mp4", ".png", ".exe"]
    extension = next((ex for ex in EXTENSIONS if text.endswith(ex)), "")
    text = text.removesuffix(extension)
    transformed_chars = []
    for char in text:
        if char.lower() in VOWELS:
            transformed_chars.append(char.upper())
        elif char in punctuation:
            transformed_chars.append(" ")
        else:
            transformed_chars.append(char.lower())

    cleaned_text = "".join(transformed_chars)
    return cleaned_text + extension if extension else cleaned_text
