import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Titanium v10.9 Elite", layout="wide")
st.title("🛡️ Titanium Global Elite Dashboard")

if os.path.exists("elite_targets.csv"):
    df = pd.read_csv("elite_targets.csv")
    st.metric("Összes Elit Lead", len(df))
    st.write("### Globális Elit Lista (CH, UAE, AU, IN, US, NZ)")
    st.dataframe(df, use_container_width=True)
else:
    st.warning("Adatbázis szinkronizálásra vár...")
