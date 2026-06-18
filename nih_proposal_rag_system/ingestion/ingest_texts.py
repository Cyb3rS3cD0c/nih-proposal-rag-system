import os

def load_texts_from_folder(folder_path: str):
    texts = []
    for filename in os.listdir(folder_path):
        if filename.endswith(".txt"):
            with open(os.path.join(folder_path, filename), "r", encoding="utf-8") as f:
                texts.append(f.read())
    return "\n\n".join(texts)