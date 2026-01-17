from sklearn.tree import DecisionTreeClassifier, export_text
import pandas as pd
import random

# ----------------------
# Step 1: Create larger dataset
# ----------------------
players = [
    "LeBron", "Curry", "Giannis", "Tatum", "Butler", "Kyrie",
    "Davis", "Harden", "Durant", "Embiid", "Lillard", "Westbrook",
    "Dončić", "Young", "DeRozan"
]

# Random-ish realistic stats for each player
data = {
    "player": players,
    "ppg": [28, 30, 31, 27, 24, 26, 25, 29, 29, 27, 28, 22, 28, 25, 27],
    "apg": [7, 6, 5, 5, 5, 7, 3, 8, 6, 4, 7, 8, 8, 9, 6],
    "rpg": [8, 6, 12, 8, 6, 5, 10, 6, 7, 11, 5, 7, 9, 4, 6],
    "spg": [1.3, 1.2, 1.2, 1.1, 1.5, 1.1, 1.0, 1.4, 0.9, 1.3, 0.8, 1.0, 1.1, 0.9, 1.0],
    "bpg": [0.6, 0.2, 1.3, 0.7, 0.5, 0.3, 2.3, 0.5, 1.2, 1.9, 0.3, 0.4, 0.6, 0.2, 0.4],
    "ts": [0.61, 0.65, 0.64, 0.59, 0.58, 0.60, 0.63, 0.61, 0.62, 0.61, 0.64, 0.57, 0.63, 0.58, 0.60],
    "per": [25, 26, 28, 22, 21, 23, 24, 27, 27, 26, 25, 20, 25, 21, 24],
    "bpm": [8.1, 7.9, 9.8, 6.7, 5.9, 6.2, 7.1, 8.3, 8.5, 7.8, 7.5, 5.6, 7.2, 5.5, 6.9]
}

df = pd.DataFrame(data)

# ----------------------
# Step 2: Create player-vs-player comparisons
# ----------------------
import itertools

comparison_data = []

for p1, p2 in itertools.combinations(df.to_dict("records"), 2):
    features = {
        "diff_ppg": p1["ppg"] - p2["ppg"],
        "diff_apg": p1["apg"] - p2["apg"],
        "diff_rpg": p1["rpg"] - p2["rpg"],
        "diff_spg": p1["spg"] - p2["spg"],
        "diff_bpg": p1["bpg"] - p2["bpg"],
        "diff_ts": p1["ts"] - p2["ts"],
        "diff_per": p1["per"] - p2["per"],
        "diff_bpm": p1["bpm"] - p2["bpm"]
    }

    # Simple scoring formula to define "better" player
    score1 = (p1["ppg"]*0.3 + p1["apg"]*0.2 + p1["rpg"]*0.15 + #defining the label
              p1["ts"]*100*0.15 + p1["bpm"]*0.2)
    score2 = (p2["ppg"]*0.3 + p2["apg"]*0.2 + p2["rpg"]*0.15 +
              p2["ts"]*100*0.15 + p2["bpm"]*0.2)

    better = 1 if score1 > score2 else 0
    features["better"] = better

    comparison_data.append(features)

comparison_df = pd.DataFrame(comparison_data)

# ----------------------
# Step 3: Train the decision tree
# ----------------------
X = comparison_df.drop("better", axis=1)
y = comparison_df["better"]

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier, export_text

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = DecisionTreeClassifier(max_depth=4)
model.fit(X_train, y_train)

#_--------------------------
def compare(playerA, playerB, df, model):
    """
    Compare two players using a trained decision tree.

    Args:
        playerA (str): Name of first player
        playerB (str): Name of second player
        df (pd.DataFrame): Player stats dataframe
        model (DecisionTreeClassifier): Trained tree

    Returns:
        winner (str), confidence (float)
    """
    # Get player stats
    p1 = df[df["player"] == playerA].iloc[0]
    p2 = df[df["player"] == playerB].iloc[0]

    # Compute differences in features
    features = [[
        p1["ppg"] - p2["ppg"],
        p1["apg"] - p2["apg"],
        p1["rpg"] - p2["rpg"],
        p1["spg"] - p2["spg"],
        p1["bpg"] - p2["bpg"],
        p1["ts"] - p2["ts"],
        p1["per"] - p2["per"],
        p1["bpm"] - p2["bpm"]
    ]]

    # Make prediction
    prediction = model.predict(features)[0]
    proba = model.predict_proba(features)[0]

    # Determine winner and confidence
    winner = playerA if prediction == 1 else playerB
    confidence = round(max(proba) * 100, 2)

    # Print stats comparison
    print(f"\nComparing {playerA} vs {playerB}:")
    print(f"Stats differences (A - B):")
    print(f"PPG: {p1['ppg'] - p2['ppg']:.1f}, APG: {p1['apg'] - p2['apg']:.1f}, RPG: {p1['rpg'] - p2['rpg']:.1f}")
    print(f"SPG: {p1['spg'] - p2['spg']:.1f}, BPG: {p1['bpg'] - p2['bpg']:.1f}, TS%: {p1['ts'] - p2['ts']:.2f}")
    print(f"PER: {p1['per'] - p2['per']:.1f}, BPM: {p1['bpm'] - p2['bpm']:.1f}")

    print(f"Winner: {winner} (Confidence: {confidence}%)")
    return winner, confidence


# ----------------------
# Step 4: Print the final tree
# ----------------------
tree_rules = export_text(model, feature_names=list(X.columns))
print("\nFinal Decision Tree:\n")
print(tree_rules)



compare("Tatum", "Curry", df, model)
compare("Giannis", "LeBron", df, model)
compare("Kyrie", "Butler", df, model)