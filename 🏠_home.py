

import streamlit as st

st.title("Bienvenue dans la :blue[galerie graphique de l'analyste de données !]")

st.sidebar.success("Selectionner un graphique.📈")


st.caption("Vous souhaitez faire analyser vos data, prendre des décisions éclairées ou bénéficier d'un tutorat personnalisé ? parlons‑en : 📧https://www.linkedin.com/in/chris-muba-io 🌍")


st.subheader("À propos")

st.markdown("Êtes-vous un analyste de données débutant qui a du mal à créer des graphiques et des visualisations à l'aide de Python🐍 ? Cherchez pas plus loin ! :blue[La galerie graphique de l'analyste de données] est là pour rendre votre journée plus facile.")

st.markdown("Notre application Streamlit est votre destination unique pour explorer différents types de graphiques et de visualisations, ainsi que les extraits de code commentés correspondants.") 

st.markdown("Nous avons inclus des exemples utilisant des packages de visualisation de données populaires tels que :blue[*Altair, Plotly et Matplotlib*].")


st.subheader("Caractéristiques")

st.markdown("🎯**Exemples interactifs** : vous voulez voir à quoi ressemble un *diagramme circulaire avec Altair* ? Ou à quoi ressemblerait un *graphique à barres avec Plotly* ? vous pouvez trouver tout cela et bien plus encore ici ! Nous fournissons des exemples interactifs pour différents types de graphiques, ce qui vous permet de comprendre facilement les concepts.")

st.markdown("🎯**Vitrine de code** : notre application est conçue pour être conviviale, sélectionnez simplement le graphique que vous souhaitez voir et nous l'afficherons accompagné d'extraits de code Python commentés. Vous pouvez même copier-coller le code pour reproduire le graphique directement dans vos propres projets !")

st.markdown("🎯**Comparaison des packages** : comparez la façon dont le même graphique peut être créé à l’aide de différents packages. Découvrez les avantages et les inconvénients de chaque approche.")

st.markdown("🎯**Utile pour tous** : que vous soyez un analyste de données débutant cherchant à améliorer vos compétences en visualisation de données ou un professionnel chevronné en quête d'inspiration, notre avons quelque chose pour vous. Alors pourquoi attendre ? Commencez à explorer dès maintenant et faites passer votre visualisation de données au niveau supérieur !")

st.markdown("🎯**Apprenez à votre rythme** : que vous soyez un apprenant visuel ou que vous préfériez plonger directement dans le code, notre galerie s'adapte à votre style d'apprentissage.")




st.subheader("🚀Objectifs d'apprentissage🚀")

st.markdown("A la fin de ce cours, les étudiants seront capables de :")


st.write("Made with ❤️ by me")







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

