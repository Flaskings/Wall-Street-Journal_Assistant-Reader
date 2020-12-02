from data import maps, tab


def point(k1, k2, k3):
    """target: One specific item tuple"""
    k = list(tab[3].keys())[0]  # first bracket determines tab
    v = list(tab[3].values())[0]
    print("KEY: ", k)
    print("VAL: ", v)
    snap = list(e for e in maps)[v]
    listing = snap[k][1]  # second bracket determines sub
    return listing[k2][0]  # second bracket determines item
