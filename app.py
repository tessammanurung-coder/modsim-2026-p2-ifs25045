import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
import numpy as np

st.set_page_config(page_title="Analisis Kuesioner", layout="wide")

# =====================
# Load Data
# =====================
df = pd.read_excel("data_kuesioner.xlsx")
data = df.iloc[:, 1:]

# Skala skor
score_map = {
    "SS": 6,
    "S": 5,
    "CS": 4,
    "CTS": 3,
    "TS": 2,
    "STS": 1
}

score_df = data.replace(score_map).apply(pd.to_numeric)

# =====================
# 1. Bar Chart - Distribusi Jawaban Keseluruhan
# =====================
st.header("1️⃣ Distribusi Jawaban Keseluruhan")

overall = data.stack().value_counts().reset_index()
overall.columns = ["Jawaban", "Jumlah"]

fig1 = px.bar(
    overall,
    x="Jawaban",
    y="Jumlah",
    title="Distribusi Jawaban Kuesioner"
)
st.plotly_chart(fig1, use_container_width=True)

# =====================
# 2. Pie Chart - Proporsi Jawaban
# =====================
st.header("2️⃣ Proporsi Jawaban Keseluruhan")

fig2 = px.pie(
    overall,
    names="Jawaban",
    values="Jumlah",
    title="Proporsi Jawaban Kuesioner"
)
st.plotly_chart(fig2, use_container_width=True)

# =====================
# 3. Stacked Bar - Distribusi per Pertanyaan
# =====================
st.header("3️⃣ Distribusi Jawaban per Pertanyaan")

per_question = data.apply(pd.Series.value_counts).fillna(0).reset_index()
per_question = per_question.melt(id_vars="index", var_name="Pertanyaan", value_name="Jumlah")
per_question.rename(columns={"index": "Jawaban"}, inplace=True)

fig3 = px.bar(
    per_question,
    x="Pertanyaan",
    y="Jumlah",
    color="Jawaban",
    title="Distribusi Jawaban per Pertanyaan",
    barmode="stack"
)
st.plotly_chart(fig3, use_container_width=True)

# =====================
# 4. Bar Chart - Rata-rata Skor
# =====================
st.header("4️⃣ Rata-rata Skor per Pertanyaan")

avg_score = score_df.mean().reset_index()
avg_score.columns = ["Pertanyaan", "Rata-rata Skor"]

fig4 = px.bar(
    avg_score,
    x="Pertanyaan",
    y="Rata-rata Skor",
    title="Rata-rata Skor per Pertanyaan"
)
st.plotly_chart(fig4, use_container_width=True)

# =====================
# 5. Bar Chart - Positif / Netral / Negatif
# =====================
st.header("5️⃣ Distribusi Kategori Jawaban")

flat = data.stack()

kategori = flat.apply(
    lambda x: "Positif" if x in ["SS", "S"]
    else "Netral" if x == "CS"
    else "Negatif"
)

kategori_df = kategori.value_counts().reset_index()
kategori_df.columns = ["Kategori", "Jumlah"]

fig5 = px.bar(
    kategori_df,
    x="Kategori",
    y="Jumlah",
    title="Distribusi Jawaban Positif, Netral, dan Negatif"
)
st.plotly_chart(fig5, use_container_width=True)

# =====================
# 6. Heatmap (Tambahan)
# =====================
st.header("6️⃣ Heatmap Intensitas Jawaban")

heatmap_df = score_df.T

fig6 = px.imshow(
    heatmap_df,
    aspect="auto",
    title="Heatmap Skor Jawaban per Pertanyaan"
)
st.plotly_chart(fig6, use_container_width=True)

# =====================
# 7. Box Plot (Tambahan)
# =====================
st.header("7️⃣ Sebaran Skor per Pertanyaan")

box_df = score_df.melt(var_name="Pertanyaan", value_name="Skor")

fig7 = px.box(
    box_df,
    x="Pertanyaan",
    y="Skor",
    title="Sebaran Skor Tiap Pertanyaan"
)
st.plotly_chart(fig7, use_container_width=True)
