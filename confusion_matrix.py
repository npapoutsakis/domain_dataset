import os
import sys

def read_jarms(filepath):
    """Reads a CSV file and returns a set of JARMs."""
    jarms = set()
    if not os.path.exists(filepath):
        print(f"Warning: File not found: {filepath}")
        return jarms
    
    with open(filepath, 'r') as f:
        for line in f:
            line = line.strip()
            if line:
                parts = line.split(',')
                jarm = parts[0].strip()
                if jarm:
                    jarms.add(jarm)
    return jarms

def main():
    base_dir = "./lists"
    tranco_path = os.path.join(base_dir, "tranco_jarm.csv")
    
    print("Loading Tranco JARMs (Benign Ground Truth)...")
    tranco_set = read_jarms(tranco_path)
    N_actual = len(tranco_set)
    print(f"Total Benign (Tranco): {N_actual}")
    print("-" * 65)
    print(f"{'List Name':<20} | {'TPR %':<8} | {'FPR %':<8} | {'TNR %':<8} | {'FNR %':<8} | {'Precision %':<11} | {'F1 Score':<8}")
    print("-" * 65)

    target_lists = [
        ("Blocklist", "blocklist_jarms.csv"),
        ("PhishTank", "phishtank_jarms.csv"),
        ("ThreatFox", "threadfox_jarms.csv"),
        ("Combined", "../final/dataset.csv")
    ]

    for name, filename in target_lists:
        filepath = os.path.join(base_dir, filename)
        target_set = read_jarms(filepath)
        
        # P_pred = Total in Blocklist (All predicted malicious)
        P_pred = len(target_set)
        
        # FP = In Blocklist AND in Tranco (Predicted Malicious, Actually Benign)
        intersection = tranco_set.intersection(target_set)
        FP = len(intersection)
        
        # TP = In Blocklist AND NOT in Tranco (Predicted Malicious, NOT Benign -> Assumed Malicious)
        TP = P_pred - FP
        
        # TN = In Tranco AND NOT in Blocklist (Actually Benign, Not Predicted Malicious)
        TN = N_actual - FP
        
        # FN = 0 (We don't have a ground truth for "Malicious" outside of the blocklist itself)
        FN = 0
        
        # Rates Calculation
        # TPR = TP / (TP + FN) . Since FN=0, TPR=100%
        if (TP + FN) > 0:
            TPR = (TP / (TP + FN)) * 100
        else:
            TPR = 0.0

        # FPR = FP / (FP + TN) = FP / N_actual
        if (FP + TN) > 0:
            FPR = (FP / (FP + TN)) * 100
        else:
            FPR = 0.0
            
        # TNR = TN / (TN + FP) = TN / N_actual
        if (TN + FP) > 0:
            TNR = (TN / (TN + FP)) * 100
        else:
            TNR = 0.0
            
        # FNR = FN / (FN + TP). Since FN=0, FNR=0%
        if (FN + TP) > 0:
            FNR = (FN / (FN + TP)) * 100
        else:
            FNR = 0.0
        # Precision = TP / (TP + FP) = TP / P_pred
        # This answers: "What percentage of the blocklist is actually malicious?"
        if P_pred > 0:
            Precision = (TP / P_pred) * 100
        else:
            Precision = 0.0

        if (Precision + TPR) > 0:
            F1 = 2 * (Precision * TPR) / (Precision + TPR)
        else:
            F1 = 0.0

        print(f"{name:<20} | {TPR:<8.2f} | {FPR:<8.2f} | {TNR:<8.2f} | {FNR:<8.2f} | {Precision:<11.2f} | {F1:<8.2f}")

if __name__ == "__main__":
    main()
