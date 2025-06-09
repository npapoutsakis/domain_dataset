import pandas as pd

def main():
    phishtank = pd.read_csv("./lists/phishtank_jarms.csv", header=None)
    blocklist = pd.read_csv("./lists/blocklist_jarms.csv", header=None)
    threadfox = pd.read_csv("./lists/threadfox_jarms.csv", header=None)

    merged_df = pd.concat([blocklist, phishtank, threadfox], ignore_index=True)
    merged_df = merged_df.drop_duplicates(keep='first')
    merged_df.to_csv("./final/dataset.csv", index=False, header=False)
    
    return


if __name__ == "__main__":
    main()