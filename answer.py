import pandas as pd

# =====================
# Load data
# =====================
df = pd.read_excel("data_kuesioner.xlsx")
data = df.iloc[:, 1:]  # Q1 - Q17
total_respon = data.size

target_question = input().lower()

# =====================
# Helper functions
# =====================
def persen(jumlah, total):
    return round(jumlah / total * 100, 1)

# Skala skor
score_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

# =====================
# Skor numerik
# =====================
score_df = data.replace(score_map).apply(pd.to_numeric)

# =====================
# Q1
# =====================
if target_question == "q1":
    counts = data.stack().value_counts()
    skala = counts.idxmax()
    jumlah = counts.max()
    print(f"{skala}|{jumlah}|{persen(jumlah, total_respon)}")

# =====================
# Q2
# =====================
elif target_question == "q2":
    counts = data.stack().value_counts()
    skala = counts.idxmin()
    jumlah = counts.min()
    print(f"{skala}|{jumlah}|{persen(jumlah, total_respon)}")

# =====================
# Q3
# =====================
elif target_question == "q3":
    ss_counts = (data == "SS").sum()
    q = ss_counts.idxmax()
    jumlah = ss_counts.max()
    print(f"{q}|{jumlah}|{persen(jumlah, len(df))}")

# =====================
# Q4
# =====================
elif target_question == "q4":
    s_counts = (data == "S").sum()
    q = s_counts.idxmax()
    jumlah = s_counts.max()
    print(f"{q}|{jumlah}|{persen(jumlah, len(df))}")

# =====================
# Q5
# =====================
elif target_question == "q5":
    cs_counts = (data == "CS").sum()
    q = cs_counts.idxmax()
    jumlah = cs_counts.max()
    print(f"{q}|{jumlah}|{persen(jumlah, len(df))}")

# =====================
# Q6
# =====================
elif target_question == "q6":
    cts_counts = (data == "CTS").sum()
    q = cts_counts.idxmax()
    jumlah = cts_counts.max()
    print(f"{q}|{jumlah}|{persen(jumlah, len(df))}")

# =====================
# Q7 (TS)
# =====================
elif target_question == "q7":
    ts_counts = (data == "TS").sum()
    q = ts_counts.idxmax()
    jumlah = ts_counts.max()
    print(f"{q}|{jumlah}|{persen(jumlah, len(df))}")

# =====================
# Q8 (STS)
# =====================
elif target_question == "q8":
    sts_counts = (data == "STS").sum()
    q = sts_counts.idxmax()
    jumlah = sts_counts.max()
    print(f"{q}|{jumlah}|{persen(jumlah, len(df))}")

# =====================
# Q9
# =====================
elif target_question == "q9":
    result = []
    for col in data.columns:
        jumlah = (data[col] == "STS").sum()
        if jumlah > 0:
            result.append(f"{col}:{persen(jumlah, len(df))}")
    print("|".join(result))

# =====================
# Q10
# =====================
elif target_question == "q10":
    avg_all = score_df.mean().mean()
    print(f"{avg_all:.2f}")

# =====================
# Q11
# =====================
elif target_question == "q11":
    avg_q = score_df.mean()
    q = avg_q.idxmax()
    print(f"{q}:{round(avg_q.max(), 2)}")

# =====================
# Q12
# =====================
elif target_question == "q12":
    avg_q = score_df.mean()
    q = avg_q.idxmin()
    print(f"{q}:{round(avg_q.min(), 2)}")

# =====================
# Q13
# =====================
elif target_question == "q13":
    flat = data.stack()
    positif = flat.isin(["SS", "S"]).sum()
    netral = flat.isin(["CS"]).sum()
    negatif = flat.isin(["CTS", "TS", "STS"]).sum()

    print(
        f"positif={positif}:{persen(positif, total_respon)}|"
        f"netral={netral}:{persen(netral, total_respon)}|"
        f"negatif={negatif}:{persen(negatif, total_respon)}"
    )
