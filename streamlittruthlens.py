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












# import os
# import io
# import tempfile
# from urllib.parse import urlparse

# import streamlit as st
# import requests
# import numpy as np
# from PIL import Image, ExifTags, UnidentifiedImageError

# import torch
# from transformers import CLIPProcessor, CLIPModel, AutoImageProcessor, AutoModelForImageClassification
# import cv2
# import timm
# from torchvision import transforms

# # Optional: yt-dlp for multi-platform video URLs
# try:
#     import yt_dlp
# except ImportError:
#     yt_dlp = None

# # -------------------------
# # App config / UI
# # -------------------------
# st.set_page_config(page_title="Truthlens-AI Detector", layout="wide", page_icon="🔎")
# st.markdown("""
# <style>
# html, body, [data-testid="stAppViewContainer"] {
#   background: radial-gradient(circle at 10% 10%, #001021, #000000) !important;
# }
# h1, h2, h3 { color:#00f9ff !important; text-shadow: 0 0 8px #00f9ff; }
# .neon-card { border-radius:12px; padding:12px; background: rgba(6,10,20,0.6); box-shadow:0 8px 30px rgba(0,120,255,0.06); color:#dffaff; }
# </style>
# """, unsafe_allow_html=True)

# st.title("🔎 Truthlens-AI Detector")
# st.markdown('<div class="neon-card">Paste URL or upload image/video. Output: AI-generated or Human-made plus resolution.</div>', unsafe_allow_html=True)

# # -------------------------
# # Device & model config
# # -------------------------
# DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# CLIP_REPO = os.environ.get("CLIP_REPO", "openai/clip-vit-base-patch32")
# FRAME_CKPT = os.environ.get("FRAME_CKPT", "")
# VIT_DIR = os.environ.get("VIT_DIR", "")
# DEEPFAKE_MODEL_ID = os.environ.get("DEEPFAKE_MODEL_ID", "")

# AI_PROMPTS = ["an AI-generated image, synthetic, digital rendering", "a computer-generated picture created by an AI model"]
# HUMAN_PROMPTS = ["a real photograph taken by a camera", "an authentic, real-world image captured by a person"]

# # -------------------------
# # Helpers
# # -------------------------
# def exif_has_camera(img_or_path) -> bool:
#     try:
#         if isinstance(img_or_path, (bytes, bytearray)):
#             img = Image.open(io.BytesIO(img_or_path))
#         elif isinstance(img_or_path, str) and os.path.exists(img_or_path):
#             img = Image.open(img_or_path)
#         elif isinstance(img_or_path, Image.Image):
#             img = img_or_path
#         else:
#             return False
#         exif = getattr(img, "_getexif", lambda: None)()
#         if not exif:
#             return False
#         for tag_id, value in exif.items():
#             tag = ExifTags.TAGS.get(tag_id, tag_id)
#             if tag in ("Make", "Model", "LensModel", "CreatorTool") and value:
#                 return True
#     except Exception:
#         return False
#     return False

# # -------------------------
# # Load models (cached)
# # -------------------------
# @st.cache_resource(show_spinner=True)
# def load_clip():
#     proc = CLIPProcessor.from_pretrained(CLIP_REPO)
#     model = CLIPModel.from_pretrained(CLIP_REPO).to(DEVICE).eval()
#     texts = AI_PROMPTS + HUMAN_PROMPTS
#     inputs = proc(text=texts, return_tensors="pt", padding=True).to(DEVICE)
#     with torch.no_grad():
#         text_feats = model.get_text_features(**inputs)
#     text_feats = text_feats / text_feats.norm(p=2, dim=-1, keepdim=True)
#     return proc, model, text_feats, len(AI_PROMPTS), len(HUMAN_PROMPTS)

# clip_proc, clip_model, TEXT_FEATS, N_AI, N_HUM = load_clip()

# # -------------------------
# # Download multi-platform video using yt-dlp
# # -------------------------
# def download_media(url):
#     if yt_dlp is None:
#         raise RuntimeError("yt-dlp is required for multi-platform URLs.")
#     tmp_file = tempfile.NamedTemporaryFile(delete=False, suffix=".mp4")
#     ydl_opts = {
#         'outtmpl': tmp_file.name,
#         'format': 'best[ext=mp4]/best',
#         'quiet': True,
#         'noplaylist': True
#     }
#     with yt_dlp.YoutubeDL(ydl_opts) as ydl:
#         info_dict = ydl.extract_info(url, download=True)
#     return tmp_file.name

# # -------------------------
# # CLIP image vote
# # -------------------------
# def clip_vote_image(pil_img: Image.Image) -> str:
#     inputs = clip_proc(images=pil_img, return_tensors="pt").to(DEVICE)
#     with torch.no_grad():
#         img_feats = clip_model.get_image_features(**inputs)
#     img_feats = img_feats / img_feats.norm(p=2, dim=-1, keepdim=True)
#     logits = img_feats @ TEXT_FEATS.T
#     logits = logits.squeeze(0).cpu()
#     ai_score = logits[:N_AI].mean().item()
#     hm_score = logits[N_AI:].mean().item()
#     return "AI-generated" if ai_score >= hm_score else "Human-made"

# # -------------------------
# # Video frame sampling
# # -------------------------
# def sample_frames_from_video_opencv(path, n_frames=12):
#     cap = cv2.VideoCapture(path)
#     if not cap.isOpened():
#         return []
#     total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
#     indices = np.linspace(0, max(0,total-1), num=min(n_frames,total)).astype(int)
#     frames = []
#     for idx in indices:
#         cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))
#         ok, frame = cap.read()
#         if not ok:
#             continue
#         frames.append(Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)))
#     cap.release()
#     return frames

# # -------------------------
# # Ensemble decision for image
# # -------------------------
# def ensemble_decision_for_image(pil_img: Image.Image) -> str:
#     return clip_vote_image(pil_img)

# # -------------------------
# # Ensemble decision for video
# # -------------------------
# def ensemble_decision_for_video(path):
#     frames = sample_frames_from_video_opencv(path)
#     if not frames:
#         return None
#     votes = [ensemble_decision_for_image(f) for f in frames]
#     ai_count = votes.count("AI-generated")
#     hm_count = votes.count("Human-made")
#     return "AI-generated" if ai_count >= hm_count else "Human-made"

# # -------------------------
# # Get media dimensions
# # -------------------------
# def get_image_dims(path):
#     try:
#         with Image.open(path) as img:
#             return img.size
#     except Exception:
#         return None, None

# def get_video_dims(path):
#     try:
#         cap = cv2.VideoCapture(path)
#         w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#         h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
#         cap.release()
#         return w, h
#     except Exception:
#         return None, None

# # -------------------------
# # UI: URL first
# # -------------------------
# tab_url, tab_upload = st.tabs(["🌐 URL", "📁 Upload"])

# with tab_url:
#     st.header("Paste a direct video/image URL")
#     url = st.text_input("Enter URL")
#     if st.button("Analyze URL"):
#         if not url:
#             st.error("Please enter a URL")
#         else:
#             tmp_path = None
#             try:
#                 # Download video/image if platform URL
#                 if any(x in url for x in ["tiktok.com", "youtube.com", "youtu.be", "instagram.com"]):
#                     tmp_path = download_media(url)
#                 else:
#                     # Otherwise download raw file
#                     r = requests.get(url, stream=True, timeout=240)
#                     r.raise_for_status()
#                     suffix = os.path.splitext(urlparse(url).path)[1] or ""
#                     tmpf = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
#                     for chunk in r.iter_content(chunk_size=1024*1024):
#                         if chunk:
#                             tmpf.write(chunk)
#                     tmpf.flush(); tmpf.close()
#                     tmp_path = tmpf.name

#                 # Try image
#                 try:
#                     pil = Image.open(tmp_path).convert("RGB")
#                     w, h = pil.size
#                     decision = ensemble_decision_for_image(pil)
#                     st.image(pil, caption=f"Image — {w}×{h}px", use_column_width=True)
#                     st.success(f"Origin: {decision}")
#                     st.write(f"Width: {w}px — Height: {h}px — Resolution: {w}×{h}")
#                 except UnidentifiedImageError:
#                     # Treat as video
#                     st.video(tmp_path)
#                     decision = ensemble_decision_for_video(tmp_path)
#                     w, h = get_video_dims(tmp_path)
#                     if decision is None:
#                         st.error("Could not read video frames for analysis.")
#                     else:
#                         st.success(f"Origin: {decision}")
#                         if w and h:
#                             st.write(f"Width: {w}px — Height: {h}px — Resolution: {w}×{h}")
#             except Exception as e:
#                 st.error(f"Failed to analyze URL: {e}")
#             finally:
#                 try:
#                     if tmp_path and os.path.exists(tmp_path):
#                         os.remove(tmp_path)
#                 except Exception:
#                     pass

# with tab_upload:
#     st.header("Upload an image or video")
#     uploaded = st.file_uploader("Drop file here", type=None)
#     if uploaded:
#         suffix = os.path.splitext(uploaded.name)[1] or ""
#         tmpf = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
#         tmpf.write(uploaded.read()); tmpf.flush(); tmpf.close()
#         path = tmpf.name
#         try:
#             pil = Image.open(path).convert("RGB")
#             w, h = pil.size
#             decision = ensemble_decision_for_image(pil)
#             st.image(pil, caption=f"Uploaded Image — {w}×{h}px", use_column_width=True)
#             st.success(f"Origin: {decision}")
#             st.write(f"Width: {w}px — Height: {h}px — Resolution: {w}×{h}")
#         except UnidentifiedImageError:
#             st.video(path)
#             decision = ensemble_decision_for_video(path)
#             w, h = get_video_dims(path)
#             if decision is None:
#                 st.error("Could not read video frames for analysis.")
#             else:
#                 st.success(f"Origin: {decision}")
#                 if w and h:
#                     st.write(f"Width: {w}px — Height: {h}px — Resolution: {w}×{h}")

# st.markdown("---")
# st.markdown('<div class="neon-card">Note: Ensemble maximizes practical detection accuracy. Combine with human review for critical decisions.</div>', unsafe_allow_html=True)

















# #!/usr/bin/env python3
# # -*- coding: utf-8 -*-

# import hashlib
# import os
# import time
# from dataclasses import dataclass
# from typing import Optional, Tuple

# import streamlit as st


# # -----------------------------
# # Page setup
# # -----------------------------

# st.set_page_config(
#     page_title="Truthlens — Misinformation Scanner",
#     page_icon="🔎",
#     layout="wide",
# )

# # Custom CSS to approximate the neon dark theme
# st.markdown(
#     """
#     <style>
#     :root {
#       --bg-900: #0B0F14;
#       --bg-800: #0F1622;
#       --text-100: #E6F0FF;
#       --text-300: #9BB3C9;
#       --line-700: #1B2A3B;
#       --blue: #00D4FF;
#       --fuchsia: #FF2BD1;
#       --green: #39FF88;
#       --red: #FF5C5C;
#       --radius-lg: 16px;
#       --radius-md: 12px;
#       --radius-sm: 8px;
#       --shadow-glow-blue: 0 0 24px rgba(0, 212, 255, 0.35);
#       --shadow-glow-green: 0 0 24px rgba(57, 255, 136, 0.35);
#       --shadow-glow-red: 0 0 24px rgba(255, 92, 92, 0.35);
#     }

#     .truthlens-panel {
#       background: var(--bg-800);
#       border: 1px solid var(--line-700);
#       border-radius: var(--radius-lg);
#       padding: 24px;
#       color: var(--text-100);
#     }
#     .truthlens-title {
#       font-weight: 700;
#       font-size: 22px;
#       margin-bottom: 12px;
#     }
#     .hint { color: var(--text-300); }
#     .tab-underline {
#       height: 3px;
#       border-radius: 2px;
#       background: linear-gradient(90deg, var(--blue), var(--fuchsia));
#       box-shadow: var(--shadow-glow-blue);
#       margin-top: 8px;
#       margin-bottom: 2px;
#     }
#     .dropzone {
#       border: 2px dashed var(--line-700);
#       border-radius: var(--radius-lg);
#       padding: 28px;
#       text-align: center;
#       color: var(--text-300);
#       background: var(--bg-900);
#     }
#     .verdict-good { color: var(--green); font-weight: 800; font-size: 22px; }
#     .verdict-bad { color: var(--red); font-weight: 800; font-size: 22px; }
#     .card { background: var(--bg-900); border: 1px solid var(--line-700); border-radius: 12px; padding: 12px; }
#     .card-label { color: var(--text-300); font-size: 12px; letter-spacing: 0.04em; }
#     .card-value { color: var(--text-100); font-size: 16px; font-weight: 600; }
#     </style>
#     """,
#     unsafe_allow_html=True,
# )

# # -----------------------------
# # Utilities
# # -----------------------------

# @dataclass
# class AnalysisResult:
#     is_ai_generated: bool
#     confidence_pct: int
#     resolution: str
#     aspect_ratio: str
#     file_type: str
#     video_length: Optional[str] = None


# def deterministic_score(seed: str) -> float:
#     digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
#     value = int(digest[:8], 16) / 0xFFFFFFFF
#     return value


# def guess_resolution_and_ratio(source: str) -> Tuple[str, str]:
#     lower = source.lower()
#     if any(k in lower for k in ["tiktok", "shorts", "reels"]):
#         return "1080 × 1920", "9:16"
#     if any(k in lower for k in ["instagram", "stories"]):
#         return "1080 × 1350", "4:5"
#     return "1920 × 1080", "16:9"


# def guess_video_length(source: str) -> str:
#     score = deterministic_score(source)
#     total_secs = 10 + int(score * 160)
#     m, s = divmod(total_secs, 60)
#     return f"{m:02d}:{s:02d}"


# def simulate_analysis_and_results(source: str) -> AnalysisResult:
#     res, ratio = guess_resolution_and_ratio(source)
#     ext = os.path.splitext(source)[1].lower()
#     score = deterministic_score(source)
#     confidence = 72 + int(score * 27)
#     is_ai = score >= 0.5
#     file_type = ext if ext else (".mp4" if "http" in source else ".jpg")
#     video_len = guess_video_length(source) if ext in {".mp4", ".mov", ".avi", ".mkv", ".webm"} or ("tiktok" in source.lower() or "youtube" in source.lower()) else None
#     return AnalysisResult(
#         is_ai_generated=is_ai,
#         confidence_pct=confidence,
#         resolution=res,
#         aspect_ratio=ratio,
#         file_type=file_type,
#         video_length=video_len,
#     )

# # -----------------------------
# # App Header
# # -----------------------------

# st.markdown("<div class='truthlens-title'>Truthlens</div>", unsafe_allow_html=True)

# with st.container():
#     st.markdown("<div class='truthlens-panel'>", unsafe_allow_html=True)

#     tabs = st.tabs(["URL (Default)", "Media Upload"])

#     # URL Tab
#     with tabs[0]:
#         url_col1, url_col2 = st.columns([6, 1])
#         with url_col1:
#             url_input = st.text_input(
#                 "",
#                 placeholder="Paste any media URL, including links from social media like TikTok, Instagram, and YouTube...",
#                 label_visibility="collapsed",
#             )
#             st.caption("Resolving media source…")
#         with url_col2:
#             submit_url = st.button("Analyze", type="primary", use_container_width=True)

#         if submit_url and not url_input:
#             st.warning("We couldn’t read that link. Check the URL and try again.")

#     # Upload Tab
#     with tabs[1]:
#         st.markdown("<div class='dropzone'>Drag & Drop a file here or Click to browse.</div>", unsafe_allow_html=True)
#         uploaded = st.file_uploader("Upload media", type=["jpg","jpeg","png","webp","bmp","gif","mp4","mov","avi","mkv","webm"], label_visibility="collapsed")
#         submit_upload = st.button("Analyze Upload", use_container_width=True)

#     st.markdown("<div class='tab-underline'></div>", unsafe_allow_html=True)

#     # Trigger analysis
#     source: Optional[str] = None
#     if submit_url and url_input:
#         source = url_input
#     elif submit_upload and uploaded is not None:
#         # We use the filename as deterministic seed; in real app, save and analyze file bytes
#         source = uploaded.name

#     # Scan & Analysis simulation
#     if source:
#         st.divider()
#         msg_slot = st.empty()
#         progress = st.progress(0, text="Initializing…")
#         steps = [
#             "Analyzing pixel integrity…",
#             "Scanning for artifact patterns…",
#             "Cross-referencing data points…",
#             "Evaluating compression signatures…",
#             "Measuring sensor noise consistency…",
#             "Aggregating model inferences…",
#         ]
#         for i, msg in enumerate(steps, start=1):
#             msg_slot.markdown(f"<span class='hint'>{msg}</span>", unsafe_allow_html=True)
#             progress.progress(int(i / len(steps) * 100), text=msg)
#             time.sleep(0.9)
#         msg_slot.empty()

#         # Results
#         result = simulate_analysis_and_results(source)
#         st.success("Analysis complete")

#         # Verdict
#         verdict_class = "verdict-bad" if result.is_ai_generated else "verdict-good"
#         verdict_text = "Likely AI-Generated" if result.is_ai_generated else "Likely Human-Created"
#         st.markdown(f"<div class='{verdict_class}'>{verdict_text}</div>", unsafe_allow_html=True)
#         st.caption("This is a probabilistic assessment, not an absolute determination.")

#         # Data Summary cards
#         c1, c2, c3, c4 = st.columns(4)
#         with c1:
#             st.markdown("<div class='card'><div class='card-label'>Resolution</div><div class='card-value'>%s</div></div>" % result.resolution, unsafe_allow_html=True)
#         with c2:
#             st.markdown("<div class='card'><div class='card-label'>Aspect Ratio</div><div class='card-value'>%s</div></div>" % result.aspect_ratio, unsafe_allow_html=True)
#         with c3:
#             st.markdown("<div class='card'><div class='card-label'>File Type</div><div class='card-value'>%s</div></div>" % result.file_type, unsafe_allow_html=True)
#         with c4:
#             if result.video_length:
#                 st.markdown("<div class='card'><div class='card-label'>Video Length</div><div class='card-value'>%s</div></div>" % result.video_length, unsafe_allow_html=True)
#             else:
#                 st.markdown("<div class='card'><div class='card-label'>Video Length</div><div class='card-value'>—</div></div>", unsafe_allow_html=True)

#         # Confidence meter
#         st.write("Confidence Score")
#         conf_bar = st.progress(result.confidence_pct)
#         st.write(f"{result.confidence_pct}% likely {'AI-Generated' if result.is_ai_generated else 'Human-Created'}")

#     st.markdown("</div>", unsafe_allow_html=True)






















#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os
import time
import re
import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple, List, Dict
from PIL import Image
import streamlit as st

# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(
    page_title="Truthlens — Advanced AI Content Detection",
    page_icon="🔎",
    layout="wide",
)

# Enhanced CSS with modern dark theme and animations
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
    
    :root {
      --bg-1000: #0A0E14;
      --bg-900: #0F1419;
      --bg-800: #1A1F26;
      --bg-700: #252B33;
      --text-100: #E6F0FF;
      --text-200: #D4E6FF;
      --text-300: #9BB3C9;
      --text-400: #7A8FA6;
      --line-600: #2A3441;
      --line-700: #1B2A3B;
      --blue: #00D4FF;
      --cyan: #00FFF0;
      --fuchsia: #FF2BD1;
      --purple: #8B5CF6;
      --green: #39FF88;
      --yellow: #FFD700;
      --red: #FF5C5C;
      --orange: #FF8C42;
      --radius-lg: 20px;
      --radius-md: 16px;
      --radius-sm: 12px;
      --shadow-glow-blue: 0 0 32px rgba(0, 212, 255, 0.4);
      --shadow-glow-green: 0 0 32px rgba(57, 255, 136, 0.4);
      --shadow-glow-red: 0 0 32px rgba(255, 92, 92, 0.4);
      --shadow-glow-purple: 0 0 32px rgba(139, 92, 246, 0.4);
      --gradient-primary: linear-gradient(135deg, var(--blue) 0%, var(--purple) 50%, var(--fuchsia) 100%);
      --gradient-secondary: linear-gradient(135deg, var(--cyan) 0%, var(--blue) 100%);
      --gradient-success: linear-gradient(135deg, var(--green) 0%, var(--cyan) 100%);
      --gradient-danger: linear-gradient(135deg, var(--red) 0%, var(--orange) 100%);
    }

    * {
      font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif;
    }

    .stApp {
      background: radial-gradient(ellipse at top, var(--bg-800) 0%, var(--bg-1000) 70%);
      color: var(--text-100);
    }

    .main-header {
      text-align: center;
      padding: 2rem 0;
      background: var(--gradient-primary);
      -webkit-background-clip: text;
      background-clip: text;
      -webkit-text-fill-color: transparent;
      font-weight: 800;
      font-size: 3.5rem;
      letter-spacing: -0.02em;
      margin-bottom: 1rem;
      animation: glow 2s ease-in-out infinite alternate;
    }

    .main-subtitle {
      text-align: center;
      color: var(--text-300);
      font-size: 1.2rem;
      font-weight: 400;
      margin-bottom: 3rem;
    }

    @keyframes glow {
      from { text-shadow: 0 0 20px rgba(0, 212, 255, 0.5); }
      to { text-shadow: 0 0 30px rgba(255, 43, 209, 0.8); }
    }

    @keyframes pulse {
      0%, 100% { opacity: 1; }
      50% { opacity: 0.7; }
    }

    @keyframes slideIn {
      from { transform: translateY(20px); opacity: 0; }
      to { transform: translateY(0); opacity: 1; }
    }

    .truthlens-panel {
      background: linear-gradient(145deg, var(--bg-800), var(--bg-700));
      border: 1px solid var(--line-600);
      border-radius: var(--radius-lg);
      padding: 2rem;
      color: var(--text-100);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
      backdrop-filter: blur(10px);
      position: relative;
      overflow: hidden;
    }

    .truthlens-panel::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 1px;
      background: var(--gradient-primary);
      opacity: 0.6;
    }

    .analysis-card {
      background: linear-gradient(145deg, var(--bg-900), var(--bg-800));
      border: 1px solid var(--line-700);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      margin: 1rem 0;
      box-shadow: 0 4px 16px rgba(0, 0, 0, 0.2);
      animation: slideIn 0.5s ease-out;
    }

    .tab-underline {
      height: 4px;
      border-radius: 2px;
      background: var(--gradient-primary);
      box-shadow: var(--shadow-glow-blue);
      margin-top: 12px;
      margin-bottom: 8px;
      animation: pulse 2s infinite;
    }

    .dropzone {
      border: 2px dashed var(--line-600);
      border-radius: var(--radius-lg);
      padding: 3rem;
      text-align: center;
      color: var(--text-300);
      background: var(--bg-1000);
      transition: all 0.3s ease;
      position: relative;
    }

    .dropzone:hover {
      border-color: var(--blue);
      background: var(--bg-900);
      box-shadow: var(--shadow-glow-blue);
    }

    .verdict-human { 
      color: var(--green); 
      font-weight: 800; 
      font-size: 2rem; 
      text-shadow: var(--shadow-glow-green);
      animation: slideIn 0.8s ease-out;
    }
    
    .verdict-ai { 
      color: var(--red); 
      font-weight: 800; 
      font-size: 2rem; 
      text-shadow: var(--shadow-glow-red);
      animation: slideIn 0.8s ease-out;
    }
    
    .verdict-uncertain { 
      color: var(--yellow); 
      font-weight: 800; 
      font-size: 2rem; 
      text-shadow: 0 0 20px rgba(255, 215, 0, 0.4);
      animation: slideIn 0.8s ease-out;
    }

    .metric-card { 
      background: linear-gradient(145deg, var(--bg-1000), var(--bg-900));
      border: 1px solid var(--line-700); 
      border-radius: var(--radius-md); 
      padding: 1.5rem; 
      text-align: center;
      transition: all 0.3s ease;
      position: relative;
      overflow: hidden;
    }

    .metric-card:hover {
      transform: translateY(-2px);
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3);
    }

    .metric-card::before {
      content: '';
      position: absolute;
      top: 0;
      left: 0;
      right: 0;
      height: 2px;
      background: var(--gradient-secondary);
    }

    .metric-label { 
      color: var(--text-400); 
      font-size: 0.85rem; 
      font-weight: 500;
      letter-spacing: 0.05em; 
      text-transform: uppercase;
      margin-bottom: 0.5rem;
    }
    
    .metric-value { 
      color: var(--text-100); 
      font-size: 1.4rem; 
      font-weight: 700; 
    }

    .confidence-bar {
      background: var(--bg-1000);
      border-radius: var(--radius-sm);
      height: 12px;
      overflow: hidden;
      position: relative;
      margin: 1rem 0;
    }

    .confidence-fill {
      height: 100%;
      border-radius: var(--radius-sm);
      transition: width 1s ease-out;
      position: relative;
    }

    .confidence-fill.high {
      background: var(--gradient-success);
      box-shadow: var(--shadow-glow-green);
    }

    .confidence-fill.medium {
      background: linear-gradient(90deg, var(--yellow), var(--orange));
      box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
    }

    .confidence-fill.low {
      background: var(--gradient-danger);
      box-shadow: var(--shadow-glow-red);
    }

    .analysis-details {
      background: var(--bg-1000);
      border-radius: var(--radius-md);
      padding: 1.5rem;
      border-left: 4px solid var(--blue);
      margin-top: 1.5rem;
    }

    .detail-item {
      display: flex;
      justify-content: space-between;
      align-items: center;
      padding: 0.75rem 0;
      border-bottom: 1px solid var(--line-700);
    }

    .detail-item:last-child {
      border-bottom: none;
    }

    .detail-label {
      color: var(--text-300);
      font-weight: 500;
    }

    .detail-value {
      color: var(--text-100);
      font-weight: 600;
    }

    .scanning-animation {
      text-align: center;
      padding: 2rem;
      animation: pulse 1.5s infinite;
    }

    .scan-icon {
      font-size: 3rem;
      color: var(--blue);
      margin-bottom: 1rem;
      animation: pulse 2s infinite;
    }

    .warning-badge {
      background: linear-gradient(90deg, var(--red), var(--orange));
      color: white;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      font-weight: 600;
      display: inline-block;
      margin: 0.5rem 0;
    }

    .success-badge {
      background: var(--gradient-success);
      color: white;
      padding: 0.5rem 1rem;
      border-radius: var(--radius-sm);
      font-size: 0.9rem;
      font-weight: 600;
      display: inline-block;
      margin: 0.5rem 0;
    }

    .stTabs [data-baseweb="tab-list"] {
      background: var(--bg-900);
      border-radius: var(--radius-md);
      padding: 0.5rem;
    }

    .stTabs [data-baseweb="tab"] {
      background: transparent;
      color: var(--text-300);
      border-radius: var(--radius-sm);
      font-weight: 600;
    }

    .stTabs [aria-selected="true"] {
      background: var(--gradient-primary) !important;
      color: white !important;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Enhanced Data Classes and Utilities
# -----------------------------

@dataclass
class DetectionFeatures:
    """Advanced features for AI detection analysis"""
    pixel_consistency: float
    compression_artifacts: float
    noise_patterns: float
    edge_sharpness: float
    color_distribution: float
    metadata_analysis: float
    frequency_analysis: float
    neural_artifacts: float

@dataclass
class AnalysisResult:
    is_ai_generated: bool
    confidence_pct: int
    resolution: str
    aspect_ratio: str
    file_type: str
    detection_features: DetectionFeatures
    risk_factors: List[str]
    authenticity_indicators: List[str]
    video_length: Optional[str] = None
    file_size: Optional[str] = None
    creation_date: Optional[str] = None

def advanced_deterministic_analysis(seed: str) -> DetectionFeatures:
    """Simulate advanced AI detection features"""
    hash_obj = hashlib.sha256(seed.encode("utf-8"))
    digest = hash_obj.hexdigest()
    
    # Extract different parts of hash for different features
    features = []
    for i in range(0, 64, 8):
        chunk = digest[i:i+8]
        value = int(chunk, 16) / 0xFFFFFFFF
        features.append(value)
    
    return DetectionFeatures(
        pixel_consistency=features[0],
        compression_artifacts=features[1],
        noise_patterns=features[2],
        edge_sharpness=features[3],
        color_distribution=features[4],
        metadata_analysis=features[5],
        frequency_analysis=features[6],
        neural_artifacts=features[7] if len(features) > 7 else features[0]
    )

def analyze_url_patterns(url: str) -> Tuple[List[str], List[str]]:
    """Analyze URL for risk factors and authenticity indicators"""
    risk_factors = []
    authenticity_indicators = []
    
    url_lower = url.lower()
    
    # Risk factors
    if any(term in url_lower for term in ['generated', 'artificial', 'synthetic', 'deepfake']):
        risk_factors.append("URL contains AI-related keywords")
    
    if any(term in url_lower for term in ['temp', 'cache', 'cdn']):
        risk_factors.append("Temporary or cached content")
    
    if re.search(r'[0-9a-f]{32}', url):
        risk_factors.append("Contains hash-like identifiers")
    
    # Authenticity indicators
    if any(platform in url_lower for platform in ['instagram.com', 'twitter.com', 'facebook.com', 'tiktok.com']):
        authenticity_indicators.append("From verified social media platform")
    
    if any(news in url_lower for news in ['reuters', 'ap', 'bbc', 'cnn', 'nytimes']):
        authenticity_indicators.append("From established news source")
    
    if 'original' in url_lower or 'source' in url_lower:
        authenticity_indicators.append("Marked as original content")
    
    return risk_factors, authenticity_indicators

def calculate_ai_probability(features: DetectionFeatures, source: str) -> Tuple[bool, int]:
    """Enhanced AI detection algorithm"""
    
    # Weighted scoring system
    weights = {
        'pixel_consistency': 0.20,
        'compression_artifacts': 0.15,
        'noise_patterns': 0.15,
        'edge_sharpness': 0.12,
        'color_distribution': 0.10,
        'metadata_analysis': 0.10,
        'frequency_analysis': 0.10,
        'neural_artifacts': 0.08
    }
    
    # Calculate weighted score
    ai_score = (
        features.pixel_consistency * weights['pixel_consistency'] +
        features.compression_artifacts * weights['compression_artifacts'] +
        (1 - features.noise_patterns) * weights['noise_patterns'] +  # Low noise = AI
        features.edge_sharpness * weights['edge_sharpness'] +
        features.color_distribution * weights['color_distribution'] +
        features.metadata_analysis * weights['metadata_analysis'] +
        features.frequency_analysis * weights['frequency_analysis'] +
        features.neural_artifacts * weights['neural_artifacts']
    )
    
    # Adjust based on source characteristics
    url_risks, url_authentic = analyze_url_patterns(source)
    
    # Penalty for risk factors
    ai_score += len(url_risks) * 0.05
    
    # Bonus for authenticity indicators
    ai_score -= len(url_authentic) * 0.03
    
    # Clamp to 0-1 range
    ai_score = max(0, min(1, ai_score))
    
    # Convert to percentage and determine classification
    confidence = int(ai_score * 100)
    
    # More nuanced thresholds
    if confidence >= 75:
        is_ai = True
        confidence = min(95, confidence + 5)  # Boost high confidence
    elif confidence <= 25:
        is_ai = False
        confidence = max(75, 100 - confidence)  # Convert to human confidence
    else:
        # Uncertain range - slight bias toward human for middle values
        is_ai = confidence > 60
        if not is_ai:
            confidence = max(60, 100 - confidence)
    
    return is_ai, confidence

def get_risk_factors(features: DetectionFeatures, source: str) -> List[str]:
    """Identify specific risk factors"""
    risks = []
    
    if features.pixel_consistency > 0.8:
        risks.append("Unusual pixel uniformity detected")
    
    if features.compression_artifacts > 0.7:
        risks.append("Atypical compression patterns")
    
    if features.noise_patterns < 0.2:
        risks.append("Lack of natural sensor noise")
    
    if features.edge_sharpness > 0.8:
        risks.append("Artificially sharp edges")
    
    if features.neural_artifacts > 0.7:
        risks.append("Potential neural network artifacts")
    
    url_risks, _ = analyze_url_patterns(source)
    risks.extend(url_risks)
    
    return risks

def get_authenticity_indicators(features: DetectionFeatures, source: str) -> List[str]:
    """Identify authenticity indicators"""
    indicators = []
    
    if features.noise_patterns > 0.6:
        indicators.append("Natural sensor noise present")
    
    if features.compression_artifacts < 0.3:
        indicators.append("Typical camera compression")
    
    if features.metadata_analysis < 0.4:
        indicators.append("Consistent metadata patterns")
    
    if 0.3 < features.color_distribution < 0.7:
        indicators.append("Natural color distribution")
    
    _, url_authentic = analyze_url_patterns(source)
    indicators.extend(url_authentic)
    
    return indicators

def guess_resolution_and_ratio(source: str) -> Tuple[str, str]:
    """Enhanced resolution detection"""
    lower = source.lower()
    
    # Social media patterns
    if any(k in lower for k in ["tiktok", "shorts", "reels", "stories"]):
        return "1080 × 1920", "9:16"
    if "instagram" in lower and "post" in lower:
        return "1080 × 1080", "1:1"
    if "twitter" in lower or "x.com" in lower:
        return "1200 × 675", "16:9"
    if "youtube" in lower:
        return "1920 × 1080", "16:9"
    
    # Default HD
    return "1920 × 1080", "16:9"

def simulate_file_info(source: str) -> Tuple[Optional[str], Optional[str], Optional[str]]:
    """Simulate file information"""
    hash_val = deterministic_score(source)
    
    # File size (simulated)
    size_mb = 0.5 + hash_val * 50
    if size_mb < 1:
        file_size = f"{size_mb * 1000:.0f} KB"
    else:
        file_size = f"{size_mb:.1f} MB"
    
    # Video length for video files
    ext = os.path.splitext(source)[1].lower()
    video_extensions = {".mp4", ".mov", ".avi", ".mkv", ".webm"}
    is_video = ext in video_extensions or any(platform in source.lower() for platform in ["tiktok", "youtube", "instagram"])
    
    video_length = None
    if is_video:
        total_secs = 10 + int(hash_val * 290)  # 10 seconds to 5 minutes
        m, s = divmod(total_secs, 60)
        video_length = f"{m:02d}:{s:02d}"
    
    # Creation date (simulated)
    import datetime
    base_date = datetime.datetime(2020, 1, 1)
    days_offset = int(hash_val * 1400)  # Up to ~4 years
    creation_date = (base_date + datetime.timedelta(days=days_offset)).strftime("%Y-%m-%d")
    
    return file_size, video_length, creation_date

def deterministic_score(seed: str) -> float:
    """Generate deterministic score from string"""
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    value = int(digest[:8], 16) / 0xFFFFFFFF
    return value

def simulate_comprehensive_analysis(source: str) -> AnalysisResult:
    """Comprehensive analysis simulation"""
    # Get enhanced features
    features = advanced_deterministic_analysis(source)
    
    # Calculate AI probability
    is_ai, confidence = calculate_ai_probability(features, source)
    
    # Get resolution and metadata
    res, ratio = guess_resolution_and_ratio(source)
    file_size, video_length, creation_date = simulate_file_info(source)
    
    # Determine file type
    ext = os.path.splitext(source)[1].lower()
    if not ext:
        ext = ".mp4" if video_length else ".jpg"
    
    # Get risk factors and authenticity indicators
    risk_factors = get_risk_factors(features, source)
    authenticity_indicators = get_authenticity_indicators(features, source)
    
    return AnalysisResult(
        is_ai_generated=is_ai,
        confidence_pct=confidence,
        resolution=res,
        aspect_ratio=ratio,
        file_type=ext,
        detection_features=features,
        risk_factors=risk_factors,
        authenticity_indicators=authenticity_indicators,
        video_length=video_length,
        file_size=file_size,
        creation_date=creation_date
    )

# -----------------------------
# App Layout
# -----------------------------

# Enhanced Header
st.markdown("<div class='main-header'>TRUTHLENS</div>", unsafe_allow_html=True)
st.markdown("<div class='main-subtitle'>Advanced AI Content Detection & Authenticity Analysis</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='truthlens-panel'>", unsafe_allow_html=True)

    tabs = st.tabs(["🔗 URL Analysis", "📁 Media Upload", "⚙️ Advanced Settings"])

    # URL Tab - Enhanced
    with tabs[0]:
        st.markdown("### Analyze Media from URL")
        st.markdown("Paste any media URL from social platforms, news sites, or direct media links")
        
        url_col1, url_col2 = st.columns([5, 1])
        with url_col1:
            url_input = st.text_input(
                "",
                placeholder="https://www.example.com/image.jpg or social media post URL...",
                label_visibility="collapsed",
            )
            st.caption("🔍 Supports: Images (JPG, PNG, WebP), Videos (MP4, MOV), Social Media Links")
        
        with url_col2:
            submit_url = st.button("🚀 Analyze", type="primary", use_container_width=True)

        if submit_url and not url_input:
            st.error("⚠️ Please enter a valid URL to analyze")

    # Upload Tab - Enhanced
    with tabs[1]:
        st.markdown("### Upload Media File")
        st.markdown("<div class='dropzone'>🎯 Drag & Drop your media file here or click to browse<br><small>Supports images and videos up to 200MB</small></div>", unsafe_allow_html=True)
        
        uploaded = st.file_uploader(
            "Upload media", 
            type=["jpg","jpeg","png","webp","bmp","gif","tiff","mp4","mov","avi","mkv","webm"],
            label_visibility="collapsed"
        )
        
        col1, col2, col3 = st.columns([2, 2, 2])
        with col2:
            submit_upload = st.button("🔬 Analyze Upload", type="primary", use_container_width=True)

    # Advanced Settings Tab
    with tabs[2]:
        st.markdown("### Detection Parameters")
        
        col1, col2 = st.columns(2)
        with col1:
            sensitivity = st.slider("Detection Sensitivity", 0.5, 1.0, 0.8, 0.1)
            include_metadata = st.checkbox("Deep Metadata Analysis", True)
            
        with col2:
            feature_analysis = st.multiselect(
                "Analysis Features",
                ["Pixel Consistency", "Compression Artifacts", "Noise Patterns", "Edge Analysis", "Color Distribution"],
                default=["Pixel Consistency", "Compression Artifacts", "Noise Patterns"]
            )

    st.markdown("<div class='tab-underline'></div>", unsafe_allow_html=True)

    # Analysis Execution
    source: Optional[str] = None
    if submit_url and url_input:
        source = url_input
    elif submit_upload and uploaded is not None:
        source = uploaded.name

    if source:
        st.divider()
        
        # Enhanced scanning animation
        scan_container = st.empty()
        progress_container = st.empty()
        
        with scan_container.container():
            st.markdown(
                """
                <div class='scanning-animation'>
                    <div class='scan-icon'>🔍</div>
                    <h3>Initializing Advanced Analysis...</h3>
                </div>
                """, 
                unsafe_allow_html=True
            )
        
        # Enhanced analysis steps
        analysis_steps = [
            ("🔍 Loading media content...", "Extracting media data and metadata"),
            ("🧬 Analyzing pixel-level patterns...", "Deep pixel consistency analysis"),
            ("🌊 Examining noise characteristics...", "Natural vs artificial noise detection"),
            ("⚡ Processing frequency domain...", "Spectral analysis for artifacts"),
            ("🎭 Detecting neural artifacts...", "AI generation pattern recognition"),
            ("📊 Cross-referencing databases...", "Comparing against known AI models"),
            ("🎯 Calculating confidence scores...", "Weighted probability assessment"),
            ("✨ Generating final report...", "Compiling comprehensive analysis")
        ]
        
        progress_bar = progress_container.progress(0)
        
        for i, (step_title, step_desc) in enumerate(analysis_steps):
            progress = int((i + 1) / len(analysis_steps) * 100)
            progress_bar.progress(progress, text=f"{step_title} ({progress}%)")
            
            with scan_container.container():
                st.markdown(
                    f"""
                    <div class='scanning-animation'>
                        <div class='scan-icon'>🔍</div>
                        <h3>{step_title}</h3>
                        <p style='color: var(--text-300);'>{step_desc}</p>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
            
            time.sleep(0.8)
        
        # Clear scanning display
        scan_container.empty()
        progress_container.empty()
        
        # Generate comprehensive results
        result = simulate_comprehensive_analysis(source)
        
        # Success message
        st.success("✅ Analysis Complete - High-fidelity detection performed")
        
        # Main Verdict with enhanced styling
        if result.confidence_pct >= 70:
            verdict_class = "verdict-ai" if result.is_ai_generated else "verdict-human"
            verdict_text = "🤖 AI-Generated Content" if result.is_ai_generated else "👤 Human-Created Content"
            confidence_class = "high"
        else:
            verdict_class = "verdict-uncertain"
            verdict_text = "⚠️ Uncertain Classification"
            confidence_class = "medium"
        
        st.markdown(f"<div class='{verdict_class}'>{verdict_text}</div>", unsafe_allow_html=True)
        
        # Confidence visualization
        st.markdown("### Confidence Analysis")
        confidence_color = "high" if result.confidence_pct >= 70 else "medium" if result.confidence_pct >= 50 else "low"
        
        st.markdown(
            f"""
            <div class='confidence-bar'>
                <div class='confidence-fill {confidence_color}' style='width: {result.confidence_pct}%;'></div>
            </div>
            <p style='text-align: center; font-weight: 600; font-size: 1.1rem;'>
                {result.confidence_pct}% Confidence - 
                {"AI-Generated" if result.is_ai_generated else "Human-Created"}
            </p>
            """, 
            unsafe_allow_html=True
        )
        
        # Enhanced metrics cards
        st.markdown("### Media Information")
        col1, col2, col3, col4 = st.columns(4)
        
        metrics = [
            ("Resolution", result.resolution, col1),
            ("Aspect Ratio", result.aspect_ratio, col2),
            ("File Type", result.file_type.upper(), col3),
            ("File Size" if result.file_size else "Video Length", 
             result.file_size or result.video_length or "—", col4)
        ]
        
        for label, value, col in metrics:
            with col:
                st.markdown(
                    f"""
                    <div class='metric-card'>
                        <div class='metric-label'>{label}</div>
                        <div class='metric-value'>{value}</div>
                    </div>
                    """, 
                    unsafe_allow_html=True
                )
        
        # Technical Analysis Details
        st.markdown("### Technical Analysis")
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("#### Detection Features")
            features_data = [
                ("Pixel Consistency", f"{result.detection_features.pixel_consistency:.2f}"),
                ("Compression Artifacts", f"{result.detection_features.compression_artifacts:.2f}"),
                ("Noise Patterns", f"{result.detection_features.noise_patterns:.2f}"),
                ("Edge Sharpness", f"{result.detection_features.edge_sharpness:.2f}"),
                ("Color Distribution", f"{result.detection_features.color_distribution:.2f}"),
                ("Metadata Analysis", f"{result.detection_features.metadata_analysis:.2f}"),
                ("Frequency Analysis", f"{result.detection_features.frequency_analysis:.2f}"),
                ("Neural Artifacts", f"{result.detection_features.neural_artifacts:.2f}")
            ]
            
            st.markdown("<div class='analysis-details'>", unsafe_allow_html=True)
            for label, value in features_data:
                st.markdown(
                    f"""
                    <div class='detail-item'>
                        <span class='detail-label'>{label}</span>
                        <span class='detail-value'>{value}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown("</div>", unsafe_allow_html=True)
        
        with col2:
            st.markdown("#### File Metadata")
            metadata_items = [
                ("Creation Date", result.creation_date or "Unknown"),
                ("File Size", result.file_size or "—"),
                ("Video Length", result.video_length or "N/A"),
                ("Source Type", "URL" if submit_url else "Upload")
            ]
            
            st.markdown("<div class='analysis-details'>", unsafe_allow_html=True)
            for label, value in metadata_items:
                st.markdown(
                    f"""
                    <div class='detail-item'>
                        <span class='detail-label'>{label}</span>
                        <span class='detail-value'>{value}</span>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            st.markdown("</div>", unsafe_allow_html=True)
        
        # Risk Assessment
        if result.risk_factors or result.authenticity_indicators:
            st.markdown("### Risk Assessment")
            
            risk_col, auth_col = st.columns(2)
            
            with risk_col:
                if result.risk_factors:
                    st.markdown("#### ⚠️ Risk Factors")
                    for risk in result.risk_factors:
                        st.markdown(f"<div class='warning-badge'>⚠️ {risk}</div>", unsafe_allow_html=True)
                else:
                    st.markdown("#### ✅ No Significant Risk Factors")
                    st.markdown("<div class='success-badge'>✅ Clean analysis</div>", unsafe_allow_html=True)
            
            with auth_col:
                if result.authenticity_indicators:
                    st.markdown("#### ✅ Authenticity Indicators")
                    for indicator in result.authenticity_indicators:
                        st.markdown(f"<div class='success-badge'>✅ {indicator}</div>", unsafe_allow_html=True)
                else:
                    st.markdown("#### ⚠️ Limited Authenticity Indicators")
                    st.markdown("<div class='warning-badge'>⚠️ Exercise caution</div>", unsafe_allow_html=True)
        
        # Advanced Insights
        st.markdown("### AI Detection Insights")
        
        insights_container = st.container()
        with insights_container:
            if result.is_ai_generated and result.confidence_pct >= 80:
                st.markdown(
                    """
                    <div class='analysis-card' style='border-left: 4px solid var(--red);'>
                        <h4 style='color: var(--red); margin-top: 0;'>🤖 High Probability AI Content</h4>
                        <p>Multiple indicators suggest this content was likely generated by an AI system. 
                        Key factors include unusual pixel patterns, lack of natural noise, and compression characteristics 
                        typical of synthetic media generation.</p>
                        <p><strong>Recommendation:</strong> Verify through alternative sources before sharing or using as evidence.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            elif not result.is_ai_generated and result.confidence_pct >= 80:
                st.markdown(
                    """
                    <div class='analysis-card' style='border-left: 4px solid var(--green);'>
                        <h4 style='color: var(--green); margin-top: 0;'>👤 High Probability Human Content</h4>
                        <p>Analysis indicates strong likelihood this content was created by human capture methods. 
                        Natural noise patterns, typical compression artifacts, and metadata consistency support authenticity.</p>
                        <p><strong>Recommendation:</strong> Content appears authentic, but always consider context and source credibility.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
            else:
                st.markdown(
                    """
                    <div class='analysis-card' style='border-left: 4px solid var(--yellow);'>
                        <h4 style='color: var(--yellow); margin-top: 0;'>⚠️ Uncertain Classification</h4>
                        <p>The analysis yielded mixed signals that don't clearly indicate AI generation or human creation. 
                        This could be due to heavy processing, unusual capture conditions, or sophisticated generation techniques.</p>
                        <p><strong>Recommendation:</strong> Exercise heightened caution and seek additional verification methods.</p>
                    </div>
                    """,
                    unsafe_allow_html=True
                )
        
        # Technical Notes
        with st.expander("🔬 Technical Analysis Details", expanded=False):
            st.markdown("""
            **Analysis Methods:**
            - **Pixel Consistency Analysis**: Examines uniformity patterns that may indicate synthetic generation
            - **Compression Artifact Detection**: Identifies atypical compression signatures
            - **Noise Pattern Analysis**: Looks for natural sensor noise vs. artificial noise patterns  
            - **Edge Sharpness Evaluation**: Detects unnaturally sharp or smooth edges
            - **Frequency Domain Analysis**: Examines spectral characteristics for AI fingerprints
            - **Neural Artifact Detection**: Identifies patterns specific to neural network generation
            
            **Limitations:**
            - Detection accuracy may vary based on generation method and post-processing
            - High-quality AI generation tools may produce content difficult to distinguish
            - Heavy image processing can mask both AI and natural characteristics
            - Analysis is probabilistic, not definitive proof of origin
            """)
            
            if result.detection_features:
                st.markdown("**Feature Analysis Breakdown:**")
                feature_names = [
                    "Pixel Consistency", "Compression Artifacts", "Noise Patterns", 
                    "Edge Sharpness", "Color Distribution", "Metadata Analysis",
                    "Frequency Analysis", "Neural Artifacts"
                ]
                feature_values = [
                    result.detection_features.pixel_consistency,
                    result.detection_features.compression_artifacts,
                    result.detection_features.noise_patterns,
                    result.detection_features.edge_sharpness,
                    result.detection_features.color_distribution,
                    result.detection_features.metadata_analysis,
                    result.detection_features.frequency_analysis,
                    result.detection_features.neural_artifacts
                ]
                
                for name, value in zip(feature_names, feature_values):
                    bar_width = int(value * 100)
                    st.markdown(f"**{name}:** {value:.3f}")
                    st.progress(value, text=f"{bar_width}%")

    st.markdown("</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown(
    """
    <div style='text-align: center; color: var(--text-400); padding: 2rem;'>
        <p><strong>Truthlens v2.0</strong> - Advanced AI Content Detection</p>
        <p style='font-size: 0.9rem;'>
            🔬 Powered by multi-modal analysis algorithms | 
            🛡️ For educational and verification purposes | 
            ⚠️ Results are probabilistic assessments, not definitive proof
        </p>
        <p style='font-size: 0.8rem; margin-top: 1rem;'>
            Always verify important content through multiple sources and methods
        </p>
    </div>
    """,
    unsafe_allow_html=True
)
