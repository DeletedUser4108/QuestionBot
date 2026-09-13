import streamlit as sl

setup_page = sl.Page(
    "pages/setup.py",
    title="Setup",
    icon=":material/settings:"
)

practice_page = sl.Page(
    "pages/practice.py",
    title="Practice",
    icon=":material/quiz:"
)

pg = sl.navigation([setup_page, practice_page])

pg.run()