import pandas as pd

def printChamp(players, st_igralcev):
#   Kodric would straight up die without pandas. --> BIG FACTS
    df1 = pd.read_csv("champs.txt", names=["picks"])
    sample = df1.sample(st_igralcev)
    sample["igralec"] = players
    sample = sample[["igralec", "picks"]]
    left_aligned_df = sample.style.set_properties(**{'text-align': 'left'}).hide(axis="index").hide(axis="columns")
    left_aligned_df = left_aligned_df.to_string()
    return left_aligned_df