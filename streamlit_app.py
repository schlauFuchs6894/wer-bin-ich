import streamlit as st
import random

st.set_page_config(page_title="Wer bin ich?", page_icon="🧠")

st.title("🧠 Wer bin ich? – Das Partyspiel")

# --- Setup ---
personen = [
    "Angela Merkel", "Elon Musk", "Harry Potter", "Beyoncé",
    "Albert Einstein", "Taylor Swift", "Batman", "Shrek",
    "Michael Jackson", "Barack Obama", "Mario", "Spider-Man"
]

# --- Session State ---
if "phase" not in st.session_state:
    st.session_state.phase = "setup"
if "anzahl" not in st.session_state:
    st.session_state.anzahl = 0
if "namen" not in st.session_state:
    st.session_state.namen = []
if "zuweisungen" not in st.session_state:
    st.session_state.zuweisungen = {}
if "aktueller_spieler" not in st.session_state:
    st.session_state.aktueller_spieler = 0


# --- Phase 1: Anzahl Spieler ---
if st.session_state.phase == "setup":
    st.subheader("Schritt 1: Wie viele Spieler seid ihr?")
    anzahl = st.number_input("Anzahl der Spieler", min_value=2, max_value=10, step=1)
    if st.button("Weiter"):
        st.session_state.anzahl = anzahl
        st.session_state.phase = "namen"
        st.rerun()

# --- Phase 2: Spielernamen eingeben ---
elif st.session_state.phase == "namen":
    st.subheader("Schritt 2: Namen der Spieler eingeben")
    namen = []
    for i in range(st.session_state.anzahl):
        name = st.text_input(f"Name von Spieler {i+1}", key=f"name_{i}")
        namen.append(name)

    if st.button("Starten!"):
        if all(namen):
            st.session_state.namen = namen
            # Zufällige Personen zuteilen
            ausgewaehlte_personen = random.sample(personen, len(namen))
            st.session_state.zuweisungen = {
                namen[i]: ausgewaehlte_personen[i] for i in range(len(namen))
            }
            st.session_state.phase = "spiel"
            st.session_state.aktueller_spieler = 0
            st.rerun()
        else:
            st.warning("Bitte gib für alle Spieler einen Namen ein!")

# --- Phase 3: Spiel läuft ---
elif st.session_state.phase == "spiel":
    namen = st.session_state.namen
    aktueller_index = st.session_state.aktueller_spieler
    aktueller_name = namen[aktueller_index]
    st.subheader(f"🔔 {aktueller_name} ist dran!")

    if st.button(f"Ich bin {aktueller_name}"):
        st.session_state.phase = "anzeige"
        st.rerun()

# --- Phase 4: Person anzeigen ---
elif st.session_state.phase == "anzeige":
    namen = st.session_state.namen
    aktueller_index = st.session_state.aktueller_spieler
    aktueller_name = namen[aktueller_index]
    person = st.session_state.zuweisungen[aktueller_name]

    st.success(f"👀 {aktueller_name}, **du bist:** {person}")

    st.write("Zeig das niemandem! 😜")

    if st.button("Weiter zum nächsten Spieler"):
        if st.session_state.aktueller_spieler < len(st.session_state.namen) - 1:
            st.session_state.aktueller_spieler += 1
            st.session_state.phase = "spiel"
        else:
            st.session_state.phase = "fertig"
        st.rerun()

# --- Phase 5: Fertig ---
elif st.session_state.phase == "fertig":
    st.balloons()
    st.success("🎉 Alle Spieler haben ihre Identität bekommen!")
    st.write("Das Spiel kann jetzt beginnen – stellt euch gegenseitig Fragen, um herauszufinden, wer ihr seid!")
    if st.button("Nochmal spielen"):
        for key in list(st.session_state.keys()):
            del st.session_state[key]
        st.rerun()
