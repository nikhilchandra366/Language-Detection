from langdetect import detect, DetectorFactory
from langdetect.lang_detect_exception import LangDetectException

# Ensure consistent results
DetectorFactory.seed = 0

def detect_language(text):
    try:
        language = detect(text)
        return language
    except LangDetectException:
        return "Unable to detect the language."

if __name__ == "__main__":
    sample_text = input("Enter text to detect the language: ")
    detected_language = detect_language(sample_text)
    print(f"Detected Language: {detected_language}")
