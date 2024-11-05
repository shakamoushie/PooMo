# external library imports
import streamlit as st
from streamlit import session_state as ss
import streamlit.components.v1 as components
import base64
import os

st.set_page_config(page_title = "PooMo", page_icon="./burger.png", layout = "wide", initial_sidebar_state = "expanded")

# Variables  -----------------------------------------------------------------------------------------------------------------------

# session variables
if "icons" not in ss: ss.icons = {}
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
  icon_array = ["address", "timings", "contacts", "about"]
  for vicon in icon_array:
    iconfl = ReadPictureFile(f"{vicon}.png")
    ss.icons[vicon] = f"""<img src="data:png;base64,{iconfl}" width='20' height='20'>"""

  ss.tmpfls['Menu_png'] = open("./PooMo_Menu.png", 'rb').read()
  ss.tmpfls['Menu_pdf'] = open("./PooMo_Menu.pdf", 'rb').read()

  imgfl = './LandingPage.jpg'
  ss.tmpfls['MainImg'] = f"""<img src="data:jpg;base64,{ReadPictureFile(imgfl)}" width='800' height='500'>"""

def PageHome():
  sc21, sc22 = st.columns((3,1.5))
  sc21.html(ss.tmpfls['MainImg'])
  side_code = f"""
  <h1>PooMo Cafe</h1><br>
  {ss.icons['about']} About: ... <br><br>
  {ss.icons['address']} Address: ... <br><br>
  {ss.icons['timings']} Timings: ... <br><br>
  {ss.icons['contacts']} Contact: ...
  """
  sc22.html(side_code)

def PageMenu():
  ReduceGapFromPageTop()

  sc1, sc2, sc3, sc4 = st.columns((1, 1, 1, 6))
  if sc1.button("Home", icon=":material/home:"): 
    st.markdown(separater_line, True)
    PageHome()

  if sc2.button("Menu", icon=":material/restaurant:", help="Show Menu"): 
    st.markdown(separater_line, True)
    st.image(ss.tmpfls['Menu_png'])
  
  sc3.download_button(label="Download", 
                      icon=":material/download:",
                      data=ss.tmpfls['Menu_pdf'], 
                      file_name="PooMo_Downloaded_Menu.pdf", 
                      mime="application/pdf",
                      help="Download Menu")
  
  st.markdown(separater_line, True)

if 'runpage' not in ss: 
  if ss.starter_func_run_once == False: StarterFunctionRunOnce()
  ss.runpage = PageMenu 

ss.runpage()
