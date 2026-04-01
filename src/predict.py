import joblib
import spacy

MODELS_DIR = "./models/"
DIMENSIONS = ["ie", "ns", "tf", "jp"]

models = {
    dimension: joblib.load(f"{MODELS_DIR}/mbti_{dimension}.joblib")
    for dimension in DIMENSIONS
}

encoders = {"ie": "EI", "ns": "NS", "tf": "FT", "jp": "JP"}

nlp = spacy.load("en_core_web_sm")


def preprocess(text):
    doc = nlp(text.lower())
    tokens = [
        token.lemma_ for token in doc if not token.is_punct and not token.is_space
    ]
    return " ".join(tokens)


def predict_mbti(text):
    label = ""
    cleaned_text = [preprocess(text)]
    for dimension in DIMENSIONS:
        label += models[dimension].predict(cleaned_text)[0]

    return label
