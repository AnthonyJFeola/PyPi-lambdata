from string import punctuation


def remove_punctuation(X):
    removed_punc = []
    X = X.copy()
    for text in X:
        text = str(text)
        text = "".join([char for char in text if char not in punctuation])
        removed_punc.append(text)
    X = removed_punc
    return X