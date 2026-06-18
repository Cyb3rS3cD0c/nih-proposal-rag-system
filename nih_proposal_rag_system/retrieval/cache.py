import hashlib
import pickle
import os

def _hash_texts(texts):
    m = hashlib.sha256()
    for t in texts:
        m.update(t.encode("utf-8"))
    return m.hexdigest()

def cache_faiss_index(texts, build_index_fn, cache_dir=".faiss_cache"):
    os.makedirs(cache_dir, exist_ok=True)
    key = _hash_texts(texts)
    path = os.path.join(cache_dir, f"{key}.pkl")

    if os.path.exists(path):
        with open(path, "rb") as f:
            return pickle.load(f)

    index = build_index_fn(texts)
    with open(path, "wb") as f:
        pickle.dump(index, f)
    return index