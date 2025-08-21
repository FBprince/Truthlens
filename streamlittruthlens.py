# import streamlit as st
# from textblob import TextBlob

# # Page setup
# st.set_page_config(page_title="Real-Time Sentiment Checker", page_icon="😊", layout="centered")

# st.title("📝 Real-Time Sentiment Checker")
# st.write("Type below and see how your text feels instantly!")

# # Text input area
# user_input = st.text_area("Type something here:")

# # Only check sentiment if text is entered
# if user_input.strip():
#     blob = TextBlob(user_input)
#     sentiment = blob.sentiment.polarity

#     # Display result live
#     if sentiment > 0:
#         st.success(f"Positive 😊 (Score: {sentiment:.2f})")
#     elif sentiment < 0:
#         st.error(f"Negative 😢 (Score: {sentiment:.2f})")
#     else:
#         st.info(f"Neutral 😐 (Score: {sentiment:.2f})")
# else:
#     st.warning("Start typing above to see the sentiment!")











# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# from PIL import Image
# import numpy as np
# import cv2
# import io

# st.set_page_config(page_title="TruthLens — Streamlit Edition", page_icon="🛡️", layout="wide")

# # --- Techy Background CSS ---
# page_bg = """
# <style>
# [data-testid="stAppViewContainer"] {
#     background: linear-gradient(135deg, #0f2027, #203a43, #2c5364);
#     background-attachment: fixed;
#     color: white;
# }
# [data-testid="stHeader"] {
#     background: rgba(0,0,0,0);
# }
# [data-testid="stSidebar"] {
#     background-color: rgba(20, 20, 20, 0.8);
# }
# .stMarkdown, .stText, .stAlert {
#     background-color: rgba(255,255,255,0.05);
#     padding: 10px;
#     border-radius: 8px;
# }
# h1, h2, h3 {
#     color: #00f5ff !important;
#     text-shadow: 0px 0px 10px #00f5ff;
# }
# </style>
# """
# st.markdown(page_bg, unsafe_allow_html=True)

# st.title("🛡️ TruthLens — Misinformation Scanner (Streamlit)")
# st.write("Analyze webpages and media for manipulative language, AI-generated patterns, or other suspicious traits.")

# # --- Helper Functions ---
# def analyze_url(url):
#     try:
#         resp = requests.get(url, timeout=10)
#         soup = BeautifulSoup(resp.text, "lxml")
#         text = " ".join(p.get_text() for p in soup.find_all("p"))

#         words = text.lower().split()
#         trigger_words = ["shocking", "amazing", "you won't believe", "breaking", "exclusive"]
#         score = sum(1 for w in words if w in trigger_words) / max(len(words), 1) * 100

#         ai_status = "🔴 URL is AI" if score > 15 else "🟢 URL is not AI"

#         return {
#             "status": "success",
#             "word_count": len(words),
#             "trigger_count": sum(1 for w in words if w in trigger_words),
#             "risk_score": round(score, 2),
#             "ai_detection": ai_status,
#             "preview": text[:500] + "..." if text else "No text found."
#         }
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_image(file_bytes):
#     try:
#         img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
#         np_img = np.array(img)

#         # Edge detection
#         edges = cv2.Canny(np_img, 100, 200)
#         edge_density = np.mean(edges > 0) * 100

#         ai_status = "🔴 Image is AI" if edge_density > 15 else "🟢 Image is not AI"

#         return {
#             "status": "success",
#             "width": img.width,
#             "height": img.height,
#             "edge_density": round(edge_density, 2),
#             "ai_detection": ai_status
#         }
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_video(file_bytes):
#     try:
#         with open("temp_video.mp4", "wb") as f:
#             f.write(file_bytes)
#         cap = cv2.VideoCapture("temp_video.mp4")
#         frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#         cap.release()
#         return {"status": "success", "frame_count": frame_count}
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# # --- Tabs ---
# tab1, tab2 = st.tabs(["🌐 Analyze URL", "📁 Analyze Media"])

# with tab1:
#     url = st.text_input("Enter webpage URL")
#     if st.button("Scan URL"):
#         if url:
#             with st.spinner("Analyzing..."):
#                 st.write(analyze_url(url))
#         else:
#             st.warning("Please enter a URL.")

# with tab2:
#     uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4"])
#     if uploaded_file:
#         file_bytes = uploaded_file.read()
#         if uploaded_file.type.startswith("image"):
#             result = analyze_image(file_bytes)
#             st.image(file_bytes, caption="Uploaded Image", use_column_width=True)
#             st.write(result)
#         elif uploaded_file.type == "video/mp4":
#             st.video(file_bytes)
#             st.write(analyze_video(file_bytes))










# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# from PIL import Image
# import numpy as np
# import cv2
# import io
# import os

# st.set_page_config(page_title="TruthLens — Streamlit Edition", page_icon="🛡️", layout="wide")

# # --- Nebula Background CSS ---
# page_bg = """
# <style>
# [data-testid="stAppViewContainer"] {
#     background: url('https://images.unsplash.com/photo-1504384308090-c894fdcc538d?auto=format&fit=crop&w=1470&q=80');
#     background-size: cover;
#     background-attachment: fixed;
#     color: white;
# }
# [data-testid="stHeader"] {
#     background: rgba(0,0,0,0);
# }
# [data-testid="stSidebar"] {
#     background-color: rgba(0, 0, 0, 0.7);
# }
# .stMarkdown, .stText, .stAlert {
#     background-color: rgba(0,0,0,0.5);
#     padding: 12px;
#     border-radius: 10px;
# }
# h1, h2, h3 {
#     color: #00f5ff !important;
#     text-shadow: 0px 0px 12px #00f5ff;
# }
# </style>
# """
# st.markdown(page_bg, unsafe_allow_html=True)

# st.title("🛡️ TruthLens — Misinformation Scanner")
# st.write("Scan webpages, images, or videos to detect AI-generated content or manipulative patterns with confidence.")

# # --- Helper Functions ---
# def analyze_url(url):
#     try:
#         resp = requests.get(url, timeout=10)
#         try:
#             soup = BeautifulSoup(resp.text, "lxml")
#         except:
#             soup = BeautifulSoup(resp.text, "html.parser")
#         text = " ".join(p.get_text() for p in soup.find_all("p"))

#         words = text.lower().split()
#         trigger_words = ["shocking", "amazing", "you won't believe", "breaking", "exclusive"]
#         score = sum(1 for w in words if w in trigger_words) / max(len(words), 1) * 100

#         if score > 15:
#             ai_status = "🔴 This content **may be AI-generated** or highly sensational."
#         else:
#             ai_status = "🟢 This content **appears human-written and credible**."

#         return {
#             "status": "success",
#             "word_count": len(words),
#             "trigger_count": sum(1 for w in words if w in trigger_words),
#             "risk_score": round(score, 2),
#             "ai_detection": ai_status,
#             "preview": text[:500] + "..." if text else "No text found."
#         }
#     except requests.exceptions.RequestException as e:
#         return {"status": "error", "error": f"Request failed: {e}"}
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_image(file_bytes):
#     try:
#         img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
#         np_img = np.array(img)
#         edges = cv2.Canny(np_img, 100, 200)
#         edge_density = np.mean(edges > 0) * 100

#         if edge_density > 15:
#             ai_status = "🔴 This image **likely contains AI-generated elements**."
#         else:
#             ai_status = "🟢 This image **appears human-made and natural**."

#         return {
#             "status": "success",
#             "width": img.width,
#             "height": img.height,
#             "edge_density": round(edge_density, 2),
#             "ai_detection": ai_status
#         }
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_video(file_bytes):
#     temp_file = "temp_video.mp4"
#     try:
#         with open(temp_file, "wb") as f:
#             f.write(file_bytes)
#         cap = cv2.VideoCapture(temp_file)
#         frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#         width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         cap.release()
#         os.remove(temp_file)
#         return {
#             "status": "success",
#             "frame_count": frame_count,
#             "width": width,
#             "height": height,
#             "ai_detection": "🔵 Video appears **natural**."
#         }
#     except Exception as e:
#         if os.path.exists(temp_file):
#             os.remove(temp_file)
#         return {"status": "error", "error": str(e)}

# # --- Tabs ---
# tab1, tab2 = st.tabs(["🌐 Analyze URL", "📁 Analyze Media"])

# with tab1:
#     url = st.text_input("Enter webpage URL")
#     if st.button("Scan URL"):
#         if url:
#             with st.spinner("Analyzing webpage..."):
#                 result = analyze_url(url)
#                 if result["status"] == "success":
#                     st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                     st.markdown(f"**Word Count:** {result['word_count']}, **Trigger Words:** {result['trigger_count']}")
#                     st.markdown(f"**Preview:** {result['preview']}")
#                 else:
#                     st.error(result["error"])
#         else:
#             st.warning("Please enter a URL.")

# with tab2:
#     uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4"])
#     if uploaded_file:
#         file_bytes = uploaded_file.read()
#         if uploaded_file.type.startswith("image"):
#             result = analyze_image(file_bytes)
#             st.image(file_bytes, caption="Uploaded Image", use_column_width=True)
#             if result["status"] == "success":
#                 st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                 st.markdown(f"**Width:** {result['width']} px, **Height:** {result['height']} px")
#                 st.markdown(f"**Edge Density:** {result['edge_density']}")
#             else:
#                 st.error(result["error"])
#         elif uploaded_file.type == "video/mp4":
#             st.video(file_bytes)
#             result = analyze_video(file_bytes)
#             if result["status"] == "success":
#                 st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                 st.markdown(f"**Frames:** {result['frame_count']}, **Resolution:** {result['width']}x{result['height']}")
#             else:
#                 st.error(result["error"])








# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# from PIL import Image
# import numpy as np
# import cv2
# import io
# import os

# st.set_page_config(page_title="TruthLens — Streamlit Edition", page_icon="🛡️", layout="wide")

# # --- High-Tech Space Nebula Background & UI ---
# page_bg = """
# <style>
# body {
#     background: url('https://images.unsplash.com/photo-1580674284434-cf1054c19b2b?auto=format&fit=crop&w=1470&q=80') no-repeat center center fixed;
#     background-size: cover;
#     color: white;
#     font-family: 'Courier New', monospace;
# }
# [data-testid="stSidebar"] {
#     background-color: rgba(0, 0, 0, 0.7);
#     border-right: 2px solid #00f5ff;
# }
# h1, h2, h3 {
#     color: #00f5ff !important;
#     text-shadow: 0 0 5px #00f5ff, 0 0 10px #00f5ff, 0 0 20px #00f5ff;
# }
# .stMarkdown, .stText, .stAlert {
#     background: rgba(0,0,0,0.7);
#     border-left: 4px solid #00f5ff;
#     padding: 15px;
#     margin-bottom: 15px;
#     border-radius: 12px;
#     box-shadow: 0 0 15px #00f5ff;
# }
# .stButton>button {
#     background-color: #00f5ff;
#     color: black;
#     font-weight: bold;
#     border-radius: 10px;
#     padding: 10px 20px;
# }
# .stButton>button:hover {
#     background-color: #00d4ff;
# }
# </style>
# """
# st.markdown(page_bg, unsafe_allow_html=True)

# st.title("🛡️ TruthLens — Misinformation Scanner")
# st.write("Scan webpages, images, or videos to detect AI-generated content or manipulative patterns with confidence.")

# # --- Helper Functions ---
# def analyze_url(url):
#     try:
#         resp = requests.get(url, timeout=10)
#         try:
#             soup = BeautifulSoup(resp.text, "lxml")
#         except:
#             soup = BeautifulSoup(resp.text, "html.parser")
#         text = " ".join(p.get_text() for p in soup.find_all("p"))

#         words = text.lower().split()
#         trigger_words = ["shocking", "amazing", "you won't believe", "breaking", "exclusive"]
#         score = sum(1 for w in words if w in trigger_words) / max(len(words), 1) * 100

#         if score > 15:
#             ai_status = "🔴 This content **may be AI-generated** or highly sensational."
#         else:
#             ai_status = "🟢 This content **appears human-written and credible**."

#         return {
#             "status": "success",
#             "word_count": len(words),
#             "trigger_count": sum(1 for w in words if w in trigger_words),
#             "risk_score": round(score, 2),
#             "ai_detection": ai_status,
#             "preview": text[:500] + "..." if text else "No text found."
#         }
#     except requests.exceptions.RequestException as e:
#         return {"status": "error", "error": f"Request failed: {e}"}
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_image(file_bytes):
#     try:
#         img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
#         np_img = np.array(img)
#         edges = cv2.Canny(np_img, 100, 200)
#         edge_density = np.mean(edges > 0) * 100

#         if edge_density > 15:
#             ai_status = "🔴 This image **likely contains AI-generated elements**."
#         else:
#             ai_status = "🟢 This image **appears human-made and natural**."

#         return {
#             "status": "success",
#             "width": img.width,
#             "height": img.height,
#             "edge_density": round(edge_density, 2),
#             "ai_detection": ai_status
#         }
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_video(file_bytes):
#     temp_file = "temp_video.mp4"
#     try:
#         with open(temp_file, "wb") as f:
#             f.write(file_bytes)
#         cap = cv2.VideoCapture(temp_file)
#         frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#         width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         cap.release()
#         os.remove(temp_file)
#         return {
#             "status": "success",
#             "frame_count": frame_count,
#             "width": width,
#             "height": height,
#             "ai_detection": "🔵 Video appears **natural**."
#         }
#     except Exception as e:
#         if os.path.exists(temp_file):
#             os.remove(temp_file)
#         return {"status": "error", "error": str(e)}

# # --- Tabs ---
# tab1, tab2 = st.tabs(["🌐 Analyze URL", "📁 Analyze Media"])

# with tab1:
#     url = st.text_input("Enter webpage URL")
#     if st.button("Scan URL"):
#         if url:
#             with st.spinner("Analyzing webpage..."):
#                 result = analyze_url(url)
#                 if result["status"] == "success":
#                     col1, col2 = st.columns([2,3])
#                     with col1:
#                         st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                         st.markdown(f"**Word Count:** {result['word_count']}")
#                         st.markdown(f"**Trigger Words Found:** {result['trigger_count']}")
#                     with col2:
#                         st.markdown(f"**Preview:** {result['preview']}")
#                 else:
#                     st.error(result["error"])
#         else:
#             st.warning("Please enter a URL.")

# with tab2:
#     uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4"])
#     if uploaded_file:
#         file_bytes = uploaded_file.read()
#         if uploaded_file.type.startswith("image"):
#             result = analyze_image(file_bytes)
#             st.image(file_bytes, caption="Uploaded Image", use_column_width=True)
#             if result["status"] == "success":
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                     st.markdown(f"**Width:** {result['width']} px")
#                     st.markdown(f"**Height:** {result['height']} px")
#                 with col2:
#                     st.markdown(f"**Edge Density:** {result['edge_density']}")
#             else:
#                 st.error(result["error"])
#         elif uploaded_file.type == "video/mp4":
#             st.video(file_bytes)
#             result = analyze_video(file_bytes)
#             if result["status"] == "success":
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                     st.markdown(f"**Frames:** {result['frame_count']}")
#                 with col2:
#                     st.markdown(f"**Resolution:** {result['width']}x{result['height']}")
#             else:
#                 st.error(result["error"])




































# import streamlit as st
# import requests
# from bs4 import BeautifulSoup
# from PIL import Image
# import numpy as np
# import cv2
# import io
# import os

# st.set_page_config(page_title="TruthLens — Streamlit Edition", page_icon="🛡️", layout="wide")

# # --- Full-page Star Nebula Background with Neon Theme ---
# st.markdown(
#     """
#     <style>
#     /* Full-page fixed background */
#     .stApp::before {
#         content: "";
#         position: fixed;
#         top: 0;
#         left: 0;
#         width: 100%;
#         height: 100%;
#         background-image: url('https://images.unsplash.com/photo-1580674284434-cf1054c19b2b?auto=format&fit=crop&w=1470&q=80');
#         background-size: cover;
#         background-position: center;
#         opacity: 1;
#         z-index: -1;
#     }
#     /* Sidebar styling */
#     [data-testid="stSidebar"] {
#         background-color: rgba(0,0,0,0.7);
#         border-right: 2px solid #00f5ff;
#     }
#     /* Card-style results */
#     .stMarkdown, .stText, .stAlert {
#         background: rgba(0,0,0,0.7);
#         border-left: 4px solid #00f5ff;
#         padding: 15px;
#         margin-bottom: 15px;
#         border-radius: 12px;
#         box-shadow: 0 0 15px #00f5ff;
#     }
#     /* Neon headers */
#     h1, h2, h3 {
#         color: #00f5ff !important;
#         text-shadow: 0 0 5px #00f5ff, 0 0 10px #00f5ff, 0 0 20px #00f5ff;
#     }
#     /* Neon buttons */
#     .stButton>button {
#         background-color: #00f5ff;
#         color: black;
#         font-weight: bold;
#         border-radius: 10px;
#         padding: 10px 20px;
#     }
#     .stButton>button:hover {
#         background-color: #00d4ff;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )

# st.title("🛡️ TruthLens — Misinformation Scanner")
# st.write("Scan webpages, images, or videos to detect AI-generated content or manipulative patterns with confidence.")

# # --- Helper Functions ---
# def analyze_url(url):
#     try:
#         resp = requests.get(url, timeout=10)
#         try:
#             soup = BeautifulSoup(resp.text, "lxml")
#         except:
#             soup = BeautifulSoup(resp.text, "html.parser")
#         text = " ".join(p.get_text() for p in soup.find_all("p"))

#         words = text.lower().split()
#         trigger_words = ["shocking", "amazing", "you won't believe", "breaking", "exclusive"]
#         score = sum(1 for w in words if w in trigger_words) / max(len(words), 1) * 100

#         if score > 15:
#             ai_status = "🔴 This content **may be AI-generated** or highly sensational."
#         else:
#             ai_status = "🟢 This content **appears human-written and credible**."

#         return {
#             "status": "success",
#             "word_count": len(words),
#             "trigger_count": sum(1 for w in words if w in trigger_words),
#             "risk_score": round(score, 2),
#             "ai_detection": ai_status,
#             "preview": text[:500] + "..." if text else "No text found."
#         }
#     except requests.exceptions.RequestException as e:
#         return {"status": "error", "error": f"Request failed: {e}"}
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_image(file_bytes):
#     try:
#         img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
#         np_img = np.array(img)
#         edges = cv2.Canny(np_img, 100, 200)
#         edge_density = np.mean(edges > 0) * 100

#         if edge_density > 15:
#             ai_status = "🔴 This image **likely contains AI-generated elements**."
#         else:
#             ai_status = "🟢 This image **appears human-made and natural**."

#         return {
#             "status": "success",
#             "width": img.width,
#             "height": img.height,
#             "edge_density": round(edge_density, 2),
#             "ai_detection": ai_status
#         }
#     except Exception as e:
#         return {"status": "error", "error": str(e)}

# def analyze_video(file_bytes):
#     temp_file = "temp_video.mp4"
#     try:
#         with open(temp_file, "wb") as f:
#             f.write(file_bytes)
#         cap = cv2.VideoCapture(temp_file)
#         frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#         width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         cap.release()
#         os.remove(temp_file)
#         return {
#             "status": "success",
#             "frame_count": frame_count,
#             "width": width,
#             "height": height,
#             "ai_detection": "🔵 Video appears **natural**."
#         }
#     except Exception as e:
#         if os.path.exists(temp_file):
#             os.remove(temp_file)
#         return {"status": "error", "error": str(e)}

# # --- Tabs ---
# tab1, tab2 = st.tabs(["🌐 Analyze URL", "📁 Analyze Media"])

# with tab1:
#     url = st.text_input("Enter webpage URL")
#     if st.button("Scan URL"):
#         if url:
#             with st.spinner("Analyzing webpage..."):
#                 result = analyze_url(url)
#                 if result["status"] == "success":
#                     col1, col2 = st.columns([2,3])
#                     with col1:
#                         st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                         st.markdown(f"**Word Count:** {result['word_count']}")
#                         st.markdown(f"**Trigger Words Found:** {result['trigger_count']}")
#                     with col2:
#                         st.markdown(f"**Preview:** {result['preview']}")
#                 else:
#                     st.error(result["error"])
#         else:
#             st.warning("Please enter a URL.")

# with tab2:
#     uploaded_file = st.file_uploader("Upload an image or video", type=["jpg", "jpeg", "png", "mp4"])
#     if uploaded_file:
#         file_bytes = uploaded_file.read()
#         if uploaded_file.type.startswith("image"):
#             result = analyze_image(file_bytes)
#             st.image(file_bytes, caption="Uploaded Image", use_column_width=True)
#             if result["status"] == "success":
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                     st.markdown(f"**Width:** {result['width']} px")
#                     st.markdown(f"**Height:** {result['height']} px")
#                 with col2:
#                     st.markdown(f"**Edge Density:** {result['edge_density']}")
#             else:
#                 st.error(result["error"])
#         elif uploaded_file.type == "video/mp4":
#             st.video(file_bytes)
#             result = analyze_video(file_bytes)
#             if result["status"] == "success":
#                 col1, col2 = st.columns(2)
#                 with col1:
#                     st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                     st.markdown(f"**Frames:** {result['frame_count']}")
#                 with col2:
#                     st.markdown(f"**Resolution:** {result['width']}x{result['height']}")
#             else:
#                 st.error(result["error"])







































                















# import streamlit as st
# import requests, socket, io, os, tempfile
# from bs4 import BeautifulSoup
# from PIL import Image
# import numpy as np
# import cv2
# import threading

# # --- Check Internet ---
# def has_internet(host="8.8.8.8", port=53, timeout=3):
#     try:
#         socket.setdefaulttimeout(timeout)
#         socket.socket(socket.AF_INET, socket.SOCK_STREAM).connect((host, port))
#         return True
#     except:
#         return False

# ONLINE = has_internet()

# # --- Async Hugging Face Detector ---
# detector = None
# if ONLINE:
#     def load_hf_model():
#         global detector
#         from transformers import pipeline
#         detector = pipeline("image-classification", model="f-schmidt/ai-or-human")
#     threading.Thread(target=load_hf_model, daemon=True).start()

# # --- Streamlit Config & UI ---
# st.set_page_config(page_title="TruthLens", page_icon="🛡️", layout="wide")
# st.markdown("""
# <style>
# .stApp::before {content: "";position: fixed;top:0;left:0;width:100%;height:100%;
# background-image: url('https://images.unsplash.com/photo-1580674284434-cf1054c19b2b?auto=format&fit=crop&w=1470&q=80');
# background-size: cover;background-position:center;opacity:1;z-index:-1;}
# [data-testid="stSidebar"] {background-color: rgba(0,0,0,0.7); border-right:2px solid #00f5ff;}
# .stMarkdown, .stText, .stAlert {background:rgba(0,0,0,0.7); border-left:4px solid #00f5ff; padding:15px;
# margin-bottom:15px; border-radius:12px; box-shadow:0 0 15px #00f5ff;}
# h1,h2,h3{color:#00f5ff!important; text-shadow:0 0 5px #00f5ff,0 0 10px #00f5ff,0 0 20px #00f5ff;}
# .stButton>button{background-color:#00f5ff;color:black;font-weight:bold;border-radius:10px;padding:10px 20px;}
# .stButton>button:hover{background-color:#00d4ff;}
# </style>
# """, unsafe_allow_html=True)

# st.title("🛡️ TruthLens — Misinformation Scanner")
# st.write("Scan webpages, images, or videos to detect AI-generated content or manipulative patterns with confidence.")

# # --- URL/Text Analysis ---
# def analyze_url(url):
#     try:
#         resp = requests.get(url, timeout=10)
#         soup = BeautifulSoup(resp.text, "lxml")
#         text = " ".join(p.get_text() for p in soup.find_all("p"))
#         words = text.lower().split()
#         triggers = ["shocking","amazing","you won't believe","breaking","exclusive"]
#         score = sum(1 for w in words if w in triggers)/max(len(words),1)*100
#         ai_status = "🔴 May be AI/sensational" if score>15 else "🟢 Appears human-written"
#         return {"status":"success","word_count":len(words),"trigger_count":sum(1 for w in words if w in triggers),
#                 "risk_score":round(score,2),"ai_detection":ai_status,"preview":text[:500]+"..." if text else "No text found."}
#     except Exception as e:
#         return {"status":"error","error":str(e)}

# # --- Offline Image Detector ---
# def analyze_image_offline(file_bytes):
#     img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
#     np_img = np.array(img)
#     width, height = img.width, img.height

#     edges = cv2.Canny(np_img, 100, 200)
#     edge_density = np.mean(edges > 0)
#     color_std = np.std(np_img / 255.0)
#     gray = cv2.cvtColor(np_img, cv2.COLOR_RGB2GRAY)
#     lap_var = cv2.Laplacian(gray, cv2.CV_64F).var()

#     confidence = 0.4 * edge_density + 0.3 * (1 - color_std) + 0.3 * (1 - min(lap_var / 1000,1))

#     if confidence < 0.10:
#         ai_status = "🟢 Likely Human-made"
#     elif confidence < 0.25:
#         ai_status = "🟡 Possibly AI-generated"
#     else:
#         ai_status = "🔴 Likely AI-generated"

#     return {"status":"success","ai_detection":ai_status,"confidence_score":round(confidence*100,2),
#             "width": width,"height": height}

# # --- Hybrid Image Detector ---
# def analyze_image(file_bytes):
#     if ONLINE and detector:
#         try:
#             img = Image.open(io.BytesIO(file_bytes)).convert("RGB")
#             result = detector(img)[0]
#             score = result['score']*100
#             if score < 30:
#                 ai_status = "🟢 Likely Human-made"
#             elif score < 70:
#                 ai_status = "🟡 Possibly AI-generated"
#             else:
#                 ai_status = "🔴 Likely AI-generated"
#             return {"status":"success","ai_detection":ai_status,"confidence_score":round(score,2),
#                     "width": img.width,"height": img.height}
#         except:
#             return analyze_image_offline(file_bytes)
#     else:
#         return analyze_image_offline(file_bytes)

# # --- Video Detector ---
# def analyze_video(file_bytes):
#     with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tmp:
#         tmp.write(file_bytes)
#         temp_file = tmp.name

#     cap = cv2.VideoCapture(temp_file)
#     frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#     height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

#     sample_frames = 5
#     interval = max(1, frame_count//sample_frames)
#     confidence_scores = []

#     for i in range(0, frame_count, interval):
#         cap.set(cv2.CAP_PROP_POS_FRAMES, i)
#         ret, frame = cap.read()
#         if not ret: continue
#         frame_img = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
#         buf = io.BytesIO()
#         frame_img.save(buf, format="PNG")
#         result = analyze_image(buf.getvalue())
#         confidence_scores.append(result["confidence_score"])

#     cap.release()
#     os.remove(temp_file)
#     avg_conf = np.mean(confidence_scores) if confidence_scores else 0

#     if avg_conf < 30:
#         ai_status = "🟢 Likely Human-made"
#     elif avg_conf < 50:
#         ai_status = "🟡 Possibly AI-generated"
#     else:
#         ai_status = "🔴 Likely AI-generated"

#     return {"status":"success","frame_count":frame_count,"width":width,"height":height,
#             "ai_detection":f"{ai_status} ({round(avg_conf,2)}%)"}

# # --- Tabs ---
# tab1, tab2 = st.tabs(["🌐 Analyze URL","📁 Analyze Media"])

# with tab1:
#     url = st.text_input("Enter webpage URL")
#     if st.button("Scan URL"):
#         if url:
#             with st.spinner("Analyzing webpage..."):
#                 result = analyze_url(url)
#                 if result["status"]=="success":
#                     col1,col2 = st.columns([2,3])
#                     with col1:
#                         st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                         st.markdown(f"**Word Count:** {result['word_count']}")
#                         st.markdown(f"**Trigger Words:** {result['trigger_count']}")
#                     with col2:
#                         st.markdown(f"**Preview:** {result['preview']}")
#                 else:
#                     st.error(result["error"])
#         else:
#             st.warning("Please enter a URL.")

# with tab2:
#     uploaded_file = st.file_uploader("Upload an image or video", type=["jpg","jpeg","png","mp4"])
#     if uploaded_file:
#         file_bytes = uploaded_file.read()
#         if uploaded_file.type.startswith("image"):
#             result = analyze_image(file_bytes)
#             st.image(file_bytes, caption="Uploaded Image", use_column_width=True)
#             if result["status"]=="success":
#                 st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                 st.markdown(f"**Confidence Score:** {result['confidence_score']}%")
#                 st.markdown(f"**Width:** {result['width']} px")
#                 st.markdown(f"**Height:** {result['height']} px")
#             else:
#                 st.error(result["error"])
#         elif uploaded_file.type=="video/mp4":
#             st.video(file_bytes)
#             result = analyze_video(file_bytes)
#             if result["status"]=="success":
#                 col1,col2 = st.columns(2)
#                 with col1:
#                     st.markdown(f"**Detection Result:** {result['ai_detection']}")
#                     st.markdown(f"**Frames:** {result['frame_count']}")
#                 with col2:
#                     st.markdown(f"**Resolution:** {result['width']}x{result['height']}")
#             else:
#                 st.error(result["error"])




# truthlens_ai_detector.py
"""
Truthlens-Ai Detector — Full single-file Streamlit app with Hugging Face deepfake integration.

Features:
 - URL tab first (paste direct media URL, page URL, or data URI)
 - Upload tab (images/videos)
 - Ensemble of signals: EXIF, CLIP multi-prompt, optional ViT/frame models, face-crop deepfake checks,
   heuristics (ELA, JPEG quant variance, noise), and a dedicated Hugging Face deepfake classifier.
 - Video support: OpenCV sampling of frames and per-frame ensemble voting with configurable AI ratio threshold.
 - Tunable slider weights in sidebar.
 - Default deepfake model: "prithivMLmods/deepfake-detector-model-v1" (override with DEEPFAKE_MODEL_ID env var).
 - Note: Improves detection accuracy for realistic fakes but cannot guarantee 100% accuracy.

Requirements (example):
 - Python packages: streamlit, requests, beautifulsoup4, pillow, torch, torchvision, transformers,
   timm, opencv-python-headless, numpy
 - Optionally set environment variables FRAME_CKPT, VIT_DIR, DEEPFAKE_MODEL_ID to load extra models.

Default deepfake model source: prithivMLmods/deepfake-detector-model-v1 (Hugging Face). See model card for details.
"""
import os
import io
import tempfile
import atexit
from urllib.parse import urlparse
import mimetypes
import base64
import time

import streamlit as st
import requests
from bs4 import BeautifulSoup
from PIL import Image, ExifTags, UnidentifiedImageError, ImageChops, ImageOps, ImageSequence
import numpy as np
import torch
import torch.nn.functional as F
from transformers import CLIPProcessor, CLIPModel, AutoImageProcessor, AutoModelForImageClassification
import cv2
import timm
from torchvision import transforms

# -------------------------
# Top-level config / UI
# -------------------------
st.set_page_config(page_title="Truthlens-Ai Detector", layout="wide", page_icon="🔎")
st.markdown("""<style>
html, body, [data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 10% 10%, #001021, #000000) !important;
}
h1, h2, h3 { color:#00f9ff !important; text-shadow: 0 0 8px #00f9ff; }
.neon-card { border-radius:12px; padding:12px; background: rgba(6,10,20,0.6); box-shadow:0 8px 30px rgba(0,120,255,0.06); color:#dffaff; }
small { color:#9fdfff; }
</style>""", unsafe_allow_html=True)

st.title("🔎 Truthlens-Ai Detector — Deepfake-integrated")
st.markdown('<div class="neon-card">Paste any link (direct media URL, page URL, or data URI) or upload a file. Output: <b>AI-generated</b> or <b>Human-made</b> plus resolution. Use the sidebar to tune weights.</div>', unsafe_allow_html=True)

# -------------------------
# Device / model config (safe fallback)
# -------------------------
try:
    DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
except Exception:
    DEVICE = torch.device("cpu")

FRAME_CKPT = os.environ.get("FRAME_CKPT", "")
VIT_DIR = os.environ.get("VIT_DIR", "")
# Default deepfake model (change via env var): prithivMLmods/deepfake-detector-model-v1
DEEPFAKE_MODEL_ID = os.environ.get("DEEPFAKE_MODEL_ID", "prithivMLmods/deepfake-detector-model-v1")
CLIP_REPO = os.environ.get("CLIP_REPO", "openai/clip-vit-base-patch32")

# CLIP prompts (extendable)
AI_PROMPTS = [
    "an AI-generated image, synthetic, digital rendering",
    "a computer-generated picture created by an AI model",
]
HUMAN_PROMPTS = [
    "a real photograph taken by a camera",
    "an authentic, real-world image captured by a person",
]

# -------------------------
# Sidebar: tunables
# -------------------------
st.sidebar.header("Ensemble settings")
exif_weight = st.sidebar.slider("EXIF (camera) weight", 0.0, 6.0, 4.0, 0.5)
deepfake_weight = st.sidebar.slider("Deepfake classifier weight", 0.0, 5.0, 3.0, 0.5)
frame_weight = st.sidebar.slider("Frame model weight", 0.0, 3.0, 1.5, 0.25)
vit_weight = st.sidebar.slider("ViT weight", 0.0, 3.0, 1.5, 0.25)
clip_weight = st.sidebar.slider("CLIP weight", 0.0, 2.0, 1.0, 0.25)
face_crop_weights = st.sidebar.slider("Face-crop multiplier (per face)", 0.0, 3.0, 1.0, 0.1)
video_ratio = st.sidebar.slider("Video decision min AI frame ratio", 0.0, 1.0, 0.7, 0.05)
st.sidebar.markdown("**Guidance:** Increase weights to trust that signal more. No single signal should determine the outcome alone.")
st.sidebar.markdown("**Note:** This improves robustness but cannot reach 100% accuracy.")

# -------------------------
# Temp file registry & cleanup
# -------------------------
TMP_FILES = []
def register_tmp(p):
    if p:
        TMP_FILES.append(p)
def cleanup_tmp():
    for p in list(TMP_FILES):
        try:
            if os.path.exists(p):
                os.remove(p)
        except Exception:
            pass
atexit.register(cleanup_tmp)

# -------------------------
# Networking helpers
# -------------------------
def safe_get(url, stream=True, timeout=30, allow_redirects=True):
    headers = {"User-Agent": "Truthlens/1.0 (+https://example.org)"}
    return requests.get(url, stream=stream, timeout=timeout, headers=headers, allow_redirects=allow_redirects)

def head_request(url, timeout=15):
    try:
        headers = {"User-Agent": "Truthlens/1.0 (+https://example.org)"}
        r = requests.head(url, timeout=timeout, headers=headers, allow_redirects=True)
        return r
    except Exception:
        return None

def is_data_uri(u: str):
    return u.strip().startswith("data:")

def save_data_uri(data_uri: str):
    try:
        header, b64 = data_uri.split(",", 1)
        meta = header.split(";")
        mime = meta[0][5:] if meta and meta[0].startswith("data:") else "application/octet-stream"
        ext = mimetypes.guess_extension(mime) or ""
        data = base64.b64decode(b64)
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=ext)
        tmp.write(data); tmp.flush(); tmp.close()
        register_tmp(tmp.name)
        return tmp.name
    except Exception:
        return None

def download_to_temp(url: str, timeout=120):
    if is_data_uri(url):
        return save_data_uri(url)
    head = head_request(url)
    content_type = None
    if head is not None and head.status_code < 400:
        content_type = head.headers.get("Content-Type")
    try:
        r = safe_get(url, stream=True, timeout=timeout)
        r.raise_for_status()
    except Exception as e:
        raise requests.RequestException(f"Failed to download: {e}")
    suffix = os.path.splitext(urlparse(url).path)[1] or ""
    ct = content_type or r.headers.get("Content-Type") or ""
    if "text/html" in ct:
        tmp = tempfile.NamedTemporaryFile(delete=False, suffix=".html", mode="wb")
        tmp.write(r.content); tmp.flush(); tmp.close()
        register_tmp(tmp.name)
        return tmp.name
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    for chunk in r.iter_content(chunk_size=1024*1024):
        if chunk:
            tmp.write(chunk)
    tmp.flush(); tmp.close()
    register_tmp(tmp.name)
    return tmp.name

# -------------------------
# EXIF camera check (robust)
# -------------------------
def exif_has_camera(img_or_path) -> bool:
    try:
        if isinstance(img_or_path, (bytes, bytearray)):
            img = Image.open(io.BytesIO(img_or_path))
        elif isinstance(img_or_path, str) and os.path.exists(img_or_path):
            img = Image.open(img_or_path)
        elif isinstance(img_or_path, Image.Image):
            img = img_or_path
        else:
            return False
        exif = getattr(img, "_getexif", lambda: None)()
        if not exif:
            return False
        for tag_id, value in exif.items():
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            if tag in ("Make", "Model", "LensModel", "CreatorTool"):
                if value:
                    return True
    except Exception:
        return False
    return False

# -------------------------
# Load models (cached resources)
# -------------------------
@st.cache_resource(show_spinner=True)
def load_clip():
    proc = CLIPProcessor.from_pretrained(CLIP_REPO)
    model = CLIPModel.from_pretrained(CLIP_REPO).to(DEVICE).eval()
    texts = AI_PROMPTS + HUMAN_PROMPTS
    inputs = proc(text=texts, return_tensors="pt", padding=True).to(DEVICE)
    with torch.no_grad():
        text_feats = model.get_text_features(**inputs)
    text_feats = text_feats / text_feats.norm(p=2, dim=-1, keepdim=True)
    return proc, model, text_feats, len(AI_PROMPTS), len(HUMAN_PROMPTS)

@st.cache_resource(show_spinner=True)
def load_deepfake_model_if_set(model_id):
    if not model_id:
        return None, None, None
    try:
        proc = AutoImageProcessor.from_pretrained(model_id)
        mdl = AutoModelForImageClassification.from_pretrained(model_id).to(DEVICE).eval()
        id2label = getattr(mdl.config, "id2label", {}) or {}
        return proc, mdl, id2label
    except Exception:
        return None, None, None

@st.cache_resource(show_spinner=True)
def load_frame_model_if_present(ckpt_path):
    if not ckpt_path or not os.path.exists(ckpt_path):
        return None, None
    try:
        ck = torch.load(ckpt_path, map_location="cpu")
        arch = ck.get("arch", "resnest50d")
        model = timm.create_model(arch, pretrained=False, num_classes=2)
        model.load_state_dict(ck["model_state"])
        model.to(DEVICE).eval()
        transform = transforms.Compose([
            transforms.Resize((224,224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
        ])
        return model, transform
    except Exception:
        return None, None

@st.cache_resource(show_spinner=True)
def load_vit_if_present(vit_dir):
    if not vit_dir or not os.path.isdir(vit_dir):
        return None, None
    try:
        proc = AutoImageProcessor.from_pretrained(vit_dir)
        mdl = AutoModelForImageClassification.from_pretrained(vit_dir).to(DEVICE).eval()
        return proc, mdl
    except Exception:
        return None, None

# load models
with st.spinner("Loading CLIP (and optional models)..."):
    clip_proc, clip_model, TEXT_FEATS, N_AI, N_HUM = load_clip()
df_proc, df_model, df_id2label = load_deepfake_model_if_set(DEEPFAKE_MODEL_ID)
frame_model, frame_transform = load_frame_model_if_present(FRAME_CKPT)
vit_proc, vit_model = load_vit_if_present(VIT_DIR)

# -------------------------
# Face detector (OpenCV DNN) - ensure weights exist if possible
# -------------------------
FACE_PROTO = "deploy.prototxt"
FACE_MODEL = "res10_300x300_ssd_iter_140000.caffemodel"
if not (os.path.exists(FACE_PROTO) and os.path.exists(FACE_MODEL)):
    try:
        p = requests.get("https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt", timeout=30)
        p.raise_for_status()
        with open(FACE_PROTO, "wb") as f: f.write(p.content)
        m = requests.get("https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel", timeout=60)
        m.raise_for_status()
        with open(FACE_MODEL, "wb") as f: f.write(m.content)
    except Exception:
        pass

FACE_NET = None
if os.path.exists(FACE_PROTO) and os.path.exists(FACE_MODEL):
    try:
        FACE_NET = cv2.dnn.readNetFromCaffe(FACE_PROTO, FACE_MODEL)
    except Exception:
        FACE_NET = None

# -------------------------
# Heuristics: ELA, quantization, noise
# -------------------------
def error_level_analysis(pil_img: Image.Image, scale=90):
    try:
        tmp_io = io.BytesIO()
        pil_img.save(tmp_io, "JPEG", quality=scale)
        tmp_io.seek(0)
        recompressed = Image.open(tmp_io).convert("RGB")
        diff = ImageChops.difference(pil_img.convert("RGB"), recompressed)
        gray = diff.convert("L")
        arr = np.asarray(gray).astype(np.float32)
        return float(arr.mean())
    except Exception:
        return 0.0

def jpeg_quantization_score(pil_img: Image.Image):
    try:
        if not hasattr(pil_img, "quantization") or pil_img.format != "JPEG":
            return 0.0
        q = getattr(pil_img, "quantization", None)
        if not q:
            return 0.0
        vals = []
        for k, tbl in q.items():
            if isinstance(tbl, dict):
                tbl_vals = list(tbl.values())
            elif isinstance(tbl, (list, tuple)):
                tbl_vals = list(tbl)
            else:
                continue
            vals.extend(tbl_vals)
        if not vals:
            return 0.0
        return float(np.var(vals))
    except Exception:
        return 0.0

def noise_uniformity_score(pil_img: Image.Image):
    try:
        gray = ImageOps.grayscale(pil_img).resize((256,256))
        arr = np.asarray(gray).astype(np.float32)
        lap = cv2.Laplacian(arr, cv2.CV_64F)
        return float(np.mean(np.abs(lap)))
    except Exception:
        return 0.0

# -------------------------
# Model prediction helpers
# -------------------------
def clip_vote_image(pil_img: Image.Image) -> str:
    try:
        inputs = clip_proc(images=pil_img, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            img_feats = clip_model.get_image_features(**inputs)
        img_feats = img_feats / img_feats.norm(p=2, dim=-1, keepdim=True)
        logits = img_feats @ TEXT_FEATS.T
        logits = logits.squeeze(0).cpu()
        ai_score = logits[:N_AI].mean().item()
        hm_score = logits[N_AI:N_AI+N_HUM].mean().item()
        return "AI-generated" if ai_score >= hm_score else "Human-made"
    except Exception:
        return "Human-made"

def deepfake_predict(pil_img: Image.Image):
    # Use the huggingface deepfake image classifier if available
    if df_model is None or df_proc is None:
        return None
    try:
        inputs = df_proc(images=pil_img, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            out = df_model(**inputs)
            # Some models have .logits, some return a dict
            logits = getattr(out, "logits", None) or out
            if logits is None:
                return None
            pred = int(torch.argmax(logits, dim=-1).cpu().item())
            if df_id2label:
                label = df_id2label.get(pred) or df_id2label.get(str(pred)) or ""
                if "fake" in label.lower() or "deep" in label.lower() or "ai" in label.lower():
                    return "AI-generated"
                else:
                    return "Human-made"
            # fallback assumption: class 0 -> fake, 1 -> real (many HF deepfake models use this mapping)
            return "AI-generated" if pred == 0 else "Human-made"
    except Exception:
        return None

def frame_predict(pil_img: Image.Image):
    if frame_model is None or frame_transform is None:
        return None
    try:
        x = frame_transform(pil_img).unsqueeze(0).to(DEVICE)
        with torch.no_grad():
            logits = frame_model(x)
            pred = int(torch.argmax(logits, dim=1).cpu().item())
        return "AI-generated" if pred == 0 else "Human-made"
    except Exception:
        return None

def vit_predict(pil_img: Image.Image):
    if vit_model is None or vit_proc is None:
        return None
    try:
        inputs = vit_proc(images=pil_img, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            out = vit_model(**inputs)
        pred = int(torch.argmax(out.logits, dim=-1).cpu().item())
        return "AI-generated" if pred == 0 else "Human-made"
    except Exception:
        return None

def detect_faces_and_crops(pil_img: Image.Image, min_conf=0.5):
    if FACE_NET is None:
        return []
    img = np.array(pil_img.convert("RGB"))
    h, w = img.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(img, (300, 300)), 1.0, (300, 300), (104.0, 177.0, 123.0))
    FACE_NET.setInput(blob)
    detections = FACE_NET.forward()
    crops = []
    for i in range(0, detections.shape[2]):
        conf = float(detections[0, 0, i, 2])
        if conf > min_conf:
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (x1, y1, x2, y2) = box.astype("int")
            pad = int(0.05 * max(x2 - x1, y2 - y1))
            x1 = max(0, x1 - pad); y1 = max(0, y1 - pad)
            x2 = min(w, x2 + pad); y2 = min(h, y2 + pad)
            crop = Image.fromarray(img[y1:y2, x1:x2])
            crops.append(crop)
    return crops

# -------------------------
# Ensemble for single image
# -------------------------
def ensemble_decision_for_image(pil_img: Image.Image) -> (str, dict):
    votes = {"AI-generated": 0.0, "Human-made": 0.0}
    evidence = []

    # EXIF camera -> human signal
    try:
        if exif_has_camera(pil_img):
            votes["Human-made"] += exif_weight
            evidence.append(("EXIF", "Human-made", exif_weight))
    except Exception:
        pass

    # deepfake classifier (full image)
    df_full = deepfake_predict(pil_img)
    if df_full == "AI-generated":
        votes["AI-generated"] += deepfake_weight
        evidence.append(("DeepfakeCls", "AI-generated", deepfake_weight))
    elif df_full == "Human-made":
        votes["Human-made"] += deepfake_weight
        evidence.append(("DeepfakeCls", "Human-made", deepfake_weight))

    # frame model
    fm_full = frame_predict(pil_img)
    if fm_full == "AI-generated":
        votes["AI-generated"] += frame_weight
        evidence.append(("FrameModel", "AI-generated", frame_weight))
    elif fm_full == "Human-made":
        votes["Human-made"] += frame_weight
        evidence.append(("FrameModel", "Human-made", frame_weight))

    # ViT model
    vit_full = vit_predict(pil_img)
    if vit_full == "AI-generated":
        votes["AI-generated"] += vit_weight
        evidence.append(("ViT", "AI-generated", vit_weight))
    elif vit_full == "Human-made":
        votes["Human-made"] += vit_weight
        evidence.append(("ViT", "Human-made", vit_weight))

    # CLIP
    try:
        clip_full = clip_vote_image(pil_img)
        votes[clip_full] += clip_weight
        evidence.append(("CLIP", clip_full, clip_weight))
    except Exception:
        pass

    # Heuristics: ELA, quantization var, noise
    ela_score = error_level_analysis(pil_img)
    quant_var = jpeg_quantization_score(pil_img)
    noise_score = noise_uniformity_score(pil_img)
    if ela_score > 8.0:
        votes["AI-generated"] += 0.8
        evidence.append(("ELA", "AI-like", 0.8))
    if quant_var < 20.0 and quant_var > 0.0:
        votes["AI-generated"] += 0.6
        evidence.append(("QuantVarLow", "AI-like", 0.6))
    if noise_score < 1.0:
        votes["AI-generated"] += 0.4
        evidence.append(("NoiseLow", "AI-like", 0.4))

    # face crops analysis
    try:
        crops = detect_faces_and_crops(pil_img)
    except Exception:
        crops = []
    for crop in crops:
        df_c = deepfake_predict(crop)
        if df_c == "AI-generated":
            votes["AI-generated"] += (deepfake_weight * 0.6) * face_crop_weights
            evidence.append(("DeepfakeCrop", "AI-generated", (deepfake_weight * 0.6) * face_crop_weights))
        elif df_c == "Human-made":
            votes["Human-made"] += (deepfake_weight * 0.6) * face_crop_weights
            evidence.append(("DeepfakeCrop", "Human-made", (deepfake_weight * 0.6) * face_crop_weights))
        fm_c = frame_predict(crop)
        if fm_c == "AI-generated":
            votes["AI-generated"] += (frame_weight * 0.6) * face_crop_weights
            evidence.append(("FrameCrop", "AI-generated", (frame_weight * 0.6) * face_crop_weights))
        elif fm_c == "Human-made":
            votes["Human-made"] += (frame_weight * 0.6) * face_crop_weights
            evidence.append(("FrameCrop", "Human-made", (frame_weight * 0.6) * face_crop_weights))
        try:
            clip_c = clip_vote_image(crop)
            votes[clip_c] += 0.2 * face_crop_weights
            evidence.append(("CLIPCrop", clip_c, 0.2 * face_crop_weights))
        except Exception:
            pass

    # tie-breaker
    if abs(votes["AI-generated"] - votes["Human-made"]) < 1e-6:
        try:
            tie = clip_vote_image(pil_img)
            evidence.append(("TieBreak-CLIP", tie, 0.0))
            return tie, {"votes": votes, "evidence": evidence, "heuristics": {"ela": ela_score, "quant_var": quant_var, "noise": noise_score}}
        except Exception:
            return "Human-made", {"votes": votes, "evidence": evidence, "heuristics": {"ela": ela_score, "quant_var": quant_var, "noise": noise_score}}
    final = "AI-generated" if votes["AI-generated"] > votes["Human-made"] else "Human-made"
    return final, {"votes": votes, "evidence": evidence, "heuristics": {"ela": ela_score, "quant_var": quant_var, "noise": noise_score}}

# -------------------------
# Video helpers
# -------------------------
def sample_frames_from_video_opencv(path, n_frames=16):
    cap = cv2.VideoCapture(path)
    if not cap.isOpened():
        return []
    total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 0
    if total <= 0:
        cap.release()
        return []
    indices = np.linspace(0, max(0, total - 1), num=min(n_frames, total)).astype(int)
    frames = []
    for idx in indices:
        cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))
        ok, frame = cap.read()
        if not ok:
            continue
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frames.append(Image.fromarray(frame_rgb))
    cap.release()
    return frames

def ensemble_decision_for_video(path, n_sample_frames=12):
    frames = sample_frames_from_video_opencv(path, n_frames=n_sample_frames)
    if not frames:
        return None, {}
    counts = {"AI-generated": 0, "Human-made": 0}
    frame_details = []
    for f in frames:
        d, meta = ensemble_decision_for_image(f)
        counts[d] += 1
        frame_details.append((d, meta))
    ai_ratio = counts["AI-generated"] / max(1, (counts["AI-generated"] + counts["Human-made"]))
    decision = "AI-generated" if ai_ratio >= video_ratio else "Human-made"
    return decision, {"counts": counts, "ai_ratio": ai_ratio, "frame_details": frame_details}

# -------------------------
# Helpers for dims & HTML scraping
# -------------------------
def get_image_dims(path):
    try:
        with Image.open(path) as img:
            return img.size
    except Exception:
        return None, None

def get_video_dims(path):
    try:
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            return None, None
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)); h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()
        return w, h
    except Exception:
        return None, None

def extract_media_from_html(html_path_or_bytes, base_url=None):
    try:
        if isinstance(html_path_or_bytes, (str, bytes)):
            if isinstance(html_path_or_bytes, str) and os.path.exists(html_path_or_bytes):
                with open(html_path_or_bytes, "rb") as f:
                    html = f.read()
            else:
                html = html_path_or_bytes if isinstance(html_path_or_bytes, bytes) else html_path_or_bytes.encode("utf-8")
        else:
            return None
        soup = BeautifulSoup(html, "html.parser")
        og = soup.find("meta", property="og:image")
        if og and og.get("content"):
            return requests.compat.urljoin(base_url or "", og.get("content"))
        tw = soup.find("meta", attrs={"name": "twitter:image"})
        if tw and tw.get("content"):
            return requests.compat.urljoin(base_url or "", tw.get("content"))
        vid = soup.find("video")
        if vid:
            src = vid.get("src")
            if src:
                return requests.compat.urljoin(base_url or "", src)
            source = vid.find("source")
            if source and source.get("src"):
                return requests.compat.urljoin(base_url or "", source.get("src"))
        imgs = soup.find_all("img")
        if imgs:
            candidates = []
            for im in imgs:
                for attr in ("data-src", "srcset", "src"):
                    v = im.get(attr)
                    if not v:
                        continue
                    if attr == "srcset":
                        v = v.split(",")[0].strip().split(" ")[0]
                    candidates.append(requests.compat.urljoin(base_url or "", v))
            if candidates:
                return candidates[0]
        return None
    except Exception:
        return None

# -------------------------
# UI Tabs (URL first)
# -------------------------
tab_url, tab_upload = st.tabs(["🌐 URL", "📁 Upload"])

# ---- URL tab ----
with tab_url:
    st.header("Paste any link (direct media URL, page URL, or data URI)")
    url = st.text_input("Enter URL (or data URI):", placeholder="https://.../image.jpg or https://example.com/article or data:image/png;base64,...")
    col1, col2 = st.columns([1,3])
    with col1:
        analyze_url = st.button("Analyze URL")
    with col2:
        st.markdown("Tip: paste a social post/page URL — the app will try to find embedded media (og:image / video tags).")

    if analyze_url:
        if not url:
            st.error("Please paste a URL to analyze.")
        else:
            tmp_path = None
            try:
                with st.spinner("Resolving URL and downloading / scraping..."):
                    tmp_path = download_to_temp(url)
                    if tmp_path and tmp_path.endswith(".html"):
                        media_url = extract_media_from_html(tmp_path, base_url=url)
                        if media_url:
                            try:
                                if os.path.exists(tmp_path):
                                    os.remove(tmp_path); TMP_FILES.remove(tmp_path)
                            except Exception:
                                pass
                            tmp_path = download_to_temp(media_url)
                        else:
                            st.warning("Page did not contain clear embedded media (og:image / video / img). Attempting to analyze page snapshot as image if possible.")
                    try:
                        pil = Image.open(tmp_path)
                        if pil.format == "GIF":
                            frames = [f.copy().convert("RGB") for f in ImageSequence.Iterator(pil)]
                            base_frame = frames[0]
                            w, h = base_frame.size
                            decision, meta = ensemble_decision_for_image(base_frame)
                            st.image(base_frame, caption=f"GIF image (frame 0) — {w}×{h}px", use_column_width=True)
                            st.success(f"Origin: **{decision}**")
                            st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
                            st.json({"meta_summary": meta})
                        else:
                            pil = pil.convert("RGB")
                            w, h = pil.size
                            with st.spinner("Analyzing image (ensemble heuristics + models)..."):
                                decision, meta = ensemble_decision_for_image(pil)
                            st.image(pil, caption=f"URL Image — {w}×{h}px", use_column_width=True)
                            st.success(f"Origin: **{decision}**")
                            st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
                            st.markdown("**Evidence (top signals):**")
                            for e in meta.get("evidence", [])[:8]:
                                st.write(f"- {e[0]} → {e[1]} (weight {e[2]:.2f})")
                            heur = meta.get("heuristics", {})
                            st.write(f"ELA score: {heur.get('ela'):.2f}, QuantVar: {heur.get('quant_var'):.2f}, Noise: {heur.get('noise'):.2f}")
                    except UnidentifiedImageError:
                        st.video(tmp_path)
                        with st.spinner("Sampling and analyzing video frames..."):
                            decision, meta = ensemble_decision_for_video(tmp_path, n_sample_frames=12)
                        w, h = get_video_dims(tmp_path)
                        if decision is None:
                            st.error("Could not read video frames for analysis.")
                        else:
                            st.success(f"Origin: **{decision}**")
                            if w and h:
                                st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
                            st.json({"video_meta": meta})
            except requests.RequestException as e:
                st.error(f"Network error while downloading media: {e}")
            except Exception as e:
                st.error(f"Failed to analyze URL: {e}")
            finally:
                try:
                    if tmp_path and os.path.exists(tmp_path):
                        os.remove(tmp_path); TMP_FILES.remove(tmp_path)
                except Exception:
                    pass

# ---- Upload tab ----
with tab_upload:
    st.header("Upload an image or a video (any extension)")
    uploaded = st.file_uploader("Drop file here (images/videos). The app auto-detects the type.", type=None)
    if uploaded is not None:
        suffix = os.path.splitext(uploaded.name)[1] or ""
        tmpf = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        tmpf.write(uploaded.read()); tmpf.flush(); tmpf.close()
        register_tmp(tmpf.name)
        path = tmpf.name
        try:
            pil = Image.open(path).convert("RGB")
            w, h = pil.size
            with st.spinner("Analyzing upload..."):
                decision, meta = ensemble_decision_for_image(pil)
            st.image(pil, caption=f"Uploaded Image — {w}×{h}px", use_column_width=True)
            st.success(f"Origin: **{decision}**")
            st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
            st.json({"meta": meta})
        except UnidentifiedImageError:
            st.video(path)
            with st.spinner("Sampling video and analyzing..."):
                decision, meta = ensemble_decision_for_video(path, n_sample_frames=12)
            w, h = get_video_dims(path)
            if decision is None:
                st.error("Could not read video frames for analysis.")
            else:
                st.success(f"Origin: **{decision}**")
                if w and h:
                    st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
                st.json({"video_meta": meta})

# footer
st.markdown("---")
st.markdown('<div class="neon-card">Note: This ensemble maximizes practical detection accuracy using a dedicated deepfake classifier + heuristics + CLIP. It still cannot guarantee 100% accuracy — use provenance checks and human review for critical decisions.</div>', unsafe_allow_html=True)

