import streamlit as st
from streamlit_option_menu import option_menu

st.set_page_config(page_title="FarmRobo", page_icon="images/logo.png", layout="wide")
hide_st_style = """<style>#MainMenu {visibility: hidden;}footer {visibility: hidden;}</style>"""
st.markdown(hide_st_style, unsafe_allow_html=True)
st.markdown("""<style>.centered {text-align: center;}</style><div class="centered"><h1 style='color: green; font-size: 30px; font-family: "Arial", Helvetica, sans-serif;'>FarmRobo Technologies Pvt Ltd</h1></div>""", unsafe_allow_html=True)

def code_streamlit():
  selected_page = option_menu(
      None,
      ["Home", "Data", "Analysis", "Images", "Control Center", "Contact", "LogOut"],
      icons=['house', 'table', 'bar-chart-line', 'image', 'gear', 'envelope', '©'],
      orientation="horizontal",
      styles={
          "container": {"padding": "0 0 0 0", "background-color": "transparent", "border": "2px solid red", "border-radius": "12px"},
          "icon": {"color": "white", "font-size": "15px"},
          "nav-link": {"font-size": "15px", "text-align": "center", "margin": "0px", "--hover-color": "pink"},
          "nav-link-selected": {"background-color": "red"}})

  if selected_page == "Home":pass
  elif selected_page == "Data":pass
  elif selected_page == "Analysis":pass
  elif selected_page == "Images":st.header("Will Get Back to You Soon, Stay Tuned .. Build is under construction")
  elif selected_page == "Control Center":pass
  elif selected_page == 'Contact':pass
  elif selected_page == 'LogOut':pass

code_streamlit()