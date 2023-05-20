import numpy as np

def calculate(list):
    if len(list) < 9:
        raise ValueError("List must contain nine numbers.")
    ar = np.array(list).reshape((3,3))
    calculations = {
        "mean": [ar.mean(axis=0).tolist(), ar.mean(axis=1).tolist(), ar.mean()],
        "variance": [ar.var(axis=0).tolist(), ar.var(axis=1).tolist(), ar.var()],
        "standard deviation": [ar.std(axis=0).tolist(), ar.std(axis=1).tolist(), ar.std()],
        "max": [ar.max(axis=0).tolist(), ar.max(axis=1).tolist(), ar.max()],
        "min": [ar.min(axis=0).tolist(), ar.min(axis=1).tolist(), ar.min()],
        "sum": [ar.sum(axis=0).tolist(), ar.sum(axis=1).tolist(), ar.sum()]
    }

    return calculations

print(calculate([0,1,2,3,4,5,6,7,8]))