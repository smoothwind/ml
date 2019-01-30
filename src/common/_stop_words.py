__all__ = []


def stop_words(path):
    with open(path, encoding="utf-8") as f:
        return [l.strip() for l in f]
