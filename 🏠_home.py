

import streamlit as st

st.title("Bienvenue dans la :blue[galerie graphique de l'analyste de données !]")

st.subheader("Formateur : Christian MUBA - Data Analyst RH")

st.caption("*Master Gestion & Master Sciences (IAE Dijon & UB Dijon)*")

st.caption("*Ancien coordinateur apprentissage CFA académique / Académie de Dijon*")

st.caption("Vous souhaitez faire analyser vos data RH, prendre des décisions éclairées ou bénéficier d'un tutorat personnalisé ? contactez-moi 📧https://www.linkedin.com/in/chris-muba-io 🌍")

st.subheader("À propos")

st.markdown("*Êtes-vous un analyste de données débutant qui a du mal à créer des graphiques et des visualisations à l'aide de Python ?* Cherchez pas plus loin! La galerie graphique de l'analyste de données est là pour rendre votre journée plus facile.")

st.markdown("Cette application Streamlit est votre destination unique pour explorer différents types de graphiques et de visualisations, ainsi que les extraits de code commentés correspondants.") 

st.markdown("Nous avons inclus des exemples utilisant des packages de visualisation de données populaires tels que :blue[*Altair, Plotly et Matplotlib*].")



st.subheader("🚀Objectifs d'apprentissage🚀")

st.markdown("A la fin de ce cours, les étudiants seront capables de :")

st.markdown("🎯Comprendre comment les données statistiques peuvent éclairer les décisions liées aux RH")
st.markdown("🎯Recueillir, résumer et analyser des données à l'aide de statistiques descriptives")
st.markdown("🎯Interpréter les données à l'aide de techniques statistiques inférentielles")
st.markdown("🎯Évaluer la validité des conclusions statistiques basées sur des données d'échantillon")
st.markdown("🎯Appliquer des techniques statistiques aux problèmes liés aux RH")


st.markdown("")


def redirect_button(url: str, text: str= None, color="#FD504D"):
        st.markdown(
        f"""
        <a href="{url}" target="_blank">
            <div style="
                display: inline-block;
                padding: 0.5em 1em;
                color: #FFFFFF;
                background-color: {color};
                border-radius: 3px;
                text-decoration: none;">
                {text}
            </div
        </a>
        """,
        unsafe_allow_html=True
        )
redirect_button("https://cours-stats-rh.streamlit.app/Chapitre_1_🔖_Introduction_aux_statistiques","Aller au chapitre 1")

