# external library imports
import streamlit as st
from streamlit import session_state as ss
from streamlit_pdf_reader import pdf_reader   # pip install streamlit-pdf-reader
import base64
import os

st.set_page_config(page_title = "PooMo", page_icon="./burger.png", layout = "wide", initial_sidebar_state = "expanded")

# Variables  -----------------------------------------------------------------------------------------------------------------------

# session variables
if "tmpfls" not in ss: ss.tmpfls = {}
if "starter_func_run_once" not in ss: ss.starter_func_run_once = False

# general variables
vDrive = os.path.splitdrive(os.getcwd())[0]
application_path = "C:/Users/Shawn/dev/PooMo/" if vDrive == "C:" else "./"
application_link = "http://localhost:8501/" if vDrive == "C:" else "http://poomocafe.streamlit.app"

separater_line = f"<hr style='margin-top: 0; margin-bottom: 0; size: 1px; border: 1px solid; color: #000000; '>"

# Functions  -------------------------------------------------------------------------------------------------------------------------

# SCTN: Common Utility Functions

def ReduceGapFromPageTop(): st.markdown(" <style> div[class^='stMainBlockContainer'] { padding-top: 3rem; } </style> ", True)

def ReadPictureFile(wch_fl, fldr_location="./"):
  try:
    pxfl = f"{fldr_location}{wch_fl}"
    return base64.b64encode(open(pxfl, 'rb').read()).decode()

  except: return ""

def StarterFunctionRunOnce():
  ss.tmpfls['Menu_pdf'] = open("./PooMo_Menu.pdf", 'rb').read()

  imgfl = './LandingPage.jpg'
  ss.tmpfls['MainImg'] = f"""<img src="data:jpg;base64,{ReadPictureFile(imgfl)}" width='600' height='480'>"""

  imgfl = './cafe title.png'
  ss.tmpfls['CafeName'] = f"""<img src="data:jpg;base64,{ReadPictureFile(imgfl)}" width='550' height='100'>"""

@st.dialog("View Menu")
def ShowMenu(): pdf_reader('./PooMo_Menu.pdf')

def PageHome():
  ReduceGapFromPageTop()

  st.html(ss.tmpfls['CafeName'])
  st.markdown(separater_line, True)

  sc21, sc22 = st.columns(2)
  sc22.html(ss.tmpfls['MainImg'])

  with sc21:
    st.text("⚠️ About: ...")
    st.text("📌 Address: ...")
    st.text("🕒 Timings: ...")
    st.text("☎️ Contact: ...")
    st.text("🍽️ Menu:")

    sc1, sc2, sc3 = st.columns((1, 1, 2.5))
    if sc1.button("View", icon=":material/visibility:", help="View Menu"): ShowMenu()
    sc2.download_button(label="Download", 
                      icon=":material/download:",
                      data=ss.tmpfls['Menu_pdf'], 
                      file_name="PooMo_Downloaded_Menu.pdf", 
                      mime="application/pdf",
                      help="Download Menu")

  st.markdown(separater_line, True)


if 'runpage' not in ss: 
  if ss.starter_func_run_once == False: StarterFunctionRunOnce()
  ss.runpage = PageHome 

ss.runpage()