import os
import sys

def read_jarms(filepath):
    """Reads a CSV file and returns a set of JARMs.
       Assumes JARMs are in the first column or are the only content of the line.
       Strip whitespace.
    """
    jarms = set()
    if not os.path.exists(filepath):
        print(f"Warning: File not found: {filepath}")
        return jarms
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                # Handle potential CSV format if there are multiple columns, take the first one
                parts = line.split(',')
                jarm = parts[0].strip()
                if jarm:
                    jarms.add(jarm)
    return jarms

def main():
    base_dir = "./lists"
    tranco_path = os.path.join(base_dir, "tranco_jarm.csv")
    
    print("Loading Tranco JARMs...")
    tranco_set = read_jarms(tranco_path)
    print(f"Total Tranco JARMs: {len(tranco_set)}")
    print("-" * 60)
    print(f"{'List Name':<20} | {'Tranco Coverage %':<17}")
    print("-" * 40)

    target_lists = [
        ("Blocklist", "blocklist_jarms.csv"),
        ("PhishTank", "phishtank_jarms.csv"),
        ("ThreatFox", "threadfox_jarms.csv")
    ]

    for name, filename in target_lists:
        filepath = os.path.join(base_dir, filename)
        target_set = read_jarms(filepath)
        
        intersection = tranco_set.intersection(target_set)
        overlap_count = len(intersection)
        
        tranco_count = len(tranco_set)
        if tranco_count > 0:
            coverage = (overlap_count / tranco_count) * 100
        else:
            coverage = 0.0
            
        print(f"{name:<20} | {coverage:<10.2f}%")

if __name__ == "__main__":
    main()
