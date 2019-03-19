def indices(text, sub, idxs=[], offset=0):
    idx = text.find(sub, offset)
    while idx >= 0:
        idxs.append(idx)
        idx = text.find(sub, idx + 1)
    return idxs
