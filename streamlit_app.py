import streamlit as st
import random

st.set_page_config(page_title="Wer bin ich?", page_icon="🕵️")

# --- Setup ---
st.title("🕵️ Wer bin ich?")
st.write("Errate, wer du bist, indem du Ja/Nein-Fragen stellst!")

personen = [
    {"name": "Albert Einstein", "hinweise": ["Ich bin ein Wissenschaftler.", "Ich habe wilde Haare.", "Ich bin berühmt für die Relativitätstheorie."]},
    {"name": "Angela Merkel", "hinweise": ["Ich bin Politikerin.", "Ich war Bundeskanzlerin Deutschlands.", "Ich komme aus der CDU."]},
    {"name": "Elon Musk", "hinweise": ["Ich bin Unternehmer.", "Ich leite mehrere Tech-Firmen.", "Ich will zum Mars fliegen."]},
    {"name": "Beyoncé", "hinweise": ["Ich bin Sängerin.", "Ich war Teil einer Girlgroup.", "Ich bin mit Jay-Z verheiratet."]},
]

# Session State initialisieren
if "person" not in st.session_state:
    st.session_state.person = random.choice(personen)
    st.session_state.versuche = 0
    st.session_state.gefragt = False
    st.session_state.aufgegeben = False

person = st.session_state.person

# --- Spiellogik ---
st.subheader("Hinweise:")
for i, hinweis in enumerate(person["hinweise"][:st.session_state.versuche]):
    st.write(f"- {hinweis}")

if st.button("Neuen Hinweis anzeigen"):
    if st.session_state.versuche < len(person["hinweise"]):
        st.session_state.versuche += 1
    else:
        st.info("Keine weiteren Hinweise mehr!")

guess = st.text_input("Dein Tipp:")

if st.button("Antwort prüfen"):
    if guess.lower() == person["name"].lower():
        st.success(f"Richtig! 🎉 Du bist {person['name']}!")
    else:
        st.error("Leider falsch – versuch’s weiter!")

if st.button("Ich gebe auf 😅"):
    st.session_state.aufgegeben = True
    st.warning(f"Die richtige Antwort war: **{person['name']}**")

if st.button("Neues Spiel starten"):
    st.session_state.person = random.choice(personen)
    st.session_state.versuche = 0
    st.session_state.aufgegeben = False
    st.experimental_rerun()
