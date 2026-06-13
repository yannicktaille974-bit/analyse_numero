import streamlit as st
import phonenumbers
from phonenumbers import geocoder, carrier, timezone

st.title("Analyse Numéro de Téléphone 📱")

numero = st.text_input("Entre un numéro (ex: +33612345678)")

if st.button("Analyser"):
    try:
        parsed = phonenumbers.parse(numero)

        valide = phonenumbers.is_valid_number(parsed)
        possible = phonenumbers.is_possible_number(parsed)
        pays = geocoder.description_for_number(parsed, "fr")
        operateur = carrier.name_for_number(parsed, "fr")
        fuseaux = timezone.time_zones_for_number(parsed)

        st.success("Analyse réussie")
        st.write("**Valide :**", valide)
        st.write("**Possible :**", possible)
        st.write("**Pays :**", pays)
        st.write("**Opérateur :**", operateur)
        st.write("**Fuseaux horaires :**", fuseaux)

    except:
        st.error("Numéro invalide")
