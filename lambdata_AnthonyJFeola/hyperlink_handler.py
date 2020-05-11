import re

def remove_hyperlinks(X):
    removed_hyperlinks = []
    X = X.copy()
    for text in X:
        text = str(text)
        text = re.sub(r'http\S+', '', text)
        text = re.sub(r'https\S+', '', text)
        text = re.sub(r'www\S+', '', text)
        removed_hyperlinks.append(text)
    X = removed_hyperlinks
    return X
