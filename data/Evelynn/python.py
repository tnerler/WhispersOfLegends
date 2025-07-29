import json

with open(r"C:\Users\pc\OneDrive\Masaüstü\whispers_of_legends\data\Evelynn\roleplay_engine\conversations.json", "r", encoding="utf-8") as f:
    data = json.load(f)

print(len(data))