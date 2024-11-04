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

# general variables
vDrive = os.path.splitdrive(os.getcwd())[0]
application_path = "C:/Users/Shawn/dev/PooMo/" if vDrive == "C:" else "./"
application_link = "http://localhost:8501/" if vDrive == "C:" else "http://poomocafe.streamlit.app"

separater_line = f"<hr style='margin-top: 0; margin-bottom: 0; size: 1px; border: 1px solid; color: #000000; '>"

# Functions  -------------------------------------------------------------------------------------------------------------------------

# SCTN: Common Utility Functions

def ReduceGapFromPageTop(): st.markdown(" <style> div[class^='block-container'] { padding-top: 0rem; } </style> ", True)

def ReadPictureFile(wch_fl, fldr_location="./"):
  try:
    pxfl = f"{fldr_location}{wch_fl}"
    return base64.b64encode(open(pxfl, 'rb').read()).decode()

  except: return ""

def AutoDownload(file_object, mime_type, file_name): # re take from file copy 26Aug24
  st.toast(f"📥 Downloading as file: {file_name}...")
  dlink = f"""<html><head>
                <script src="http://code.jquery.com/jquery-3.2.1.min.js"> </script>
                <script> $('<a href="data:{mime_type};base64,{file_object}" download="{file_name}">')[0].click() </script>
              </head></html> """
  
  components.html(dlink, height=0, width=0)

def PageMenu():
  ReduceGapFromPageTop()

  sc1, sc2, sc3 = st.columns((1, 1, 6))
  menu_btn = sc1.button("Menu", icon=":material/restaurant:")
  dnld_btn = sc2.button("Download", icon=":material/download:")
  st.markdown(separater_line, True)

  if menu_btn: image_content = st.image(open("./PooMo_Menu.png", 'rb').read())
  else:
    if len(ss.icons) == 0:
      icon_array = ["address", "timings", "contacts", "about"]
      for vicon in icon_array:
        iconfl = ReadPictureFile(f"{vicon}.png")
        ss.icons[vicon] = f"""<img src="data:png;base64,{iconfl}" width='20' height='20'>"""
    
    imgfl = './LandingPage.jpg'
    img_code = f"""<img src="data:jpg;base64,{ReadPictureFile(imgfl)}" width='900' height='550'>"""
    sc21, sc22 = st.columns((4,1.5))
    sc21.html(img_code)
    side_code = f"""
    <h1>PooMa Cafe</h1><br>
    {ss.icons['about']} About: ... <br><br>
    {ss.icons['address']} Address: ... <br><br>
    {ss.icons['timings']} Timings: ... <br><br>
    {ss.icons['contacts']} Contact: ...
    """
    sc22.html(side_code)

  if dnld_btn:
    pdf_content = open("./PooMo.pdf", 'rb').read()
    file_object = base64.b64encode(pdf_content).decode()
    # AutoDownload(file_object, "application/octet-stream", "PooMo_Menu.pdf")
    AutoDownload(file_object, "application/pdf", "PooMo_Menu.pdf")

if 'runpage' not in ss: ss.runpage = PageMenu 
ss.runpage()
