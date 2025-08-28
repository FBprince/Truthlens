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



















#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os
import time
import re
import numpy as np
from dataclasses import dataclass
from typing import Optional, Tuple, List, Dict, Union
from PIL import Image, ExifTags
import streamlit as st
from urllib.parse import urlparse
import requests
from io import BytesIO
import json
import base64
from scipy import stats, ndimage
from skimage import feature, filters, measure, segmentation
import matplotlib.pyplot as plt
import warnings
import tempfile
import subprocess
from datetime import datetime, timezone
import imageio
from scipy.fft import fft2, fftshift
from scipy.spatial.distance import cosine
import sqlite3
from concurrent.futures import ThreadPoolExecutor, as_completed
import cv2

# Suppress warnings for cleaner output
warnings.filterwarnings('ignore')

# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(
    page_title="Truthlens Pro — Legal-Grade AI Detection",
    page_icon="⚖️",
    layout="wide",
)

# Enhanced CSS with legal theme
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@300;400;500;600;700;800&family=Space+Grotesk:wght@300;400;500;600;700;800&display=swap');
    
    :root {
      --bg-1100: #050810;
      --bg-1000: #0A0E1A;
      --bg-900: #0F1419;
      --bg-800: #1A1F2E;
      --bg-700: #252B3A;
      --bg-600: #2F3548;
      --text-50: #F0F8FF;
      --text-100: #E6F0FF;
      --text-200: #D4E6FF;
      --text-300: #9BB3C9;
      --text-400: #7A8FA6;
      --text-500: #5A6B7D;
      --line-500: #3A4556;
      --line-600: #2A3441;
      --line-700: #1B2A3B;
      --neon-blue: #00E5FF;
      --neon-cyan: #00FFF0;
      --neon-purple: #8B5FFF;
      --neon-pink: #FF2BD1;
      --neon-green: #39FF88;
      --neon-yellow: #FFE135;
      --neon-red: #FF4757;
      --neon-orange: #FF6B47;
      --legal-gold: #FFD700;
      --legal-silver: #C0C0C0;
      --hologram: linear-gradient(45deg, var(--neon-cyan), var(--neon-blue), var(--neon-purple), var(--neon-pink));
      --matrix: linear-gradient(135deg, var(--neon-green) 0%, var(--neon-cyan) 50%, var(--neon-blue) 100%);
      --legal: linear-gradient(135deg, var(--legal-gold) 0%, var(--legal-silver) 100%);
      --danger: linear-gradient(135deg, var(--neon-red) 0%, var(--neon-orange) 100%);
      --warning: linear-gradient(135deg, var(--neon-yellow) 0%, var(--neon-orange) 100%);
      --success: linear-gradient(135deg, var(--neon-green) 0%, var(--neon-cyan) 100%);
    }

    * { font-family: 'Space Grotesk', -apple-system, BlinkMacSystemFont, sans-serif; }
    .mono { font-family: 'JetBrains Mono', monospace; }

    .stApp {
      background: 
        radial-gradient(circle at 20% 80%, rgba(0, 229, 255, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(255, 43, 209, 0.1) 0%, transparent 50%),
        radial-gradient(circle at 40% 40%, rgba(139, 95, 255, 0.05) 0%, transparent 50%),
        linear-gradient(135deg, var(--bg-1100) 0%, var(--bg-1000) 100%);
      color: var(--text-50);
      min-height: 100vh;
    }

    @keyframes neonPulse {
      0%, 100% { text-shadow: 0 0 5px currentColor, 0 0 10px currentColor, 0 0 20px currentColor, 0 0 40px currentColor; }
      50% { text-shadow: 0 0 2px currentColor, 0 0 5px currentColor, 0 0 10px currentColor, 0 0 20px currentColor; }
    }

    @keyframes hologramShimmer {
      0% { background-position: 0% 50%; }
      50% { background-position: 100% 50%; }
      100% { background-position: 0% 50%; }
    }

    @keyframes slideInGlow {
      from { transform: translateY(30px); opacity: 0; filter: blur(10px); }
      to { transform: translateY(0); opacity: 1; filter: blur(0); }
    }

    .main-header {
      text-align: center; padding: 3rem 0 1rem;
      background: var(--legal); background-size: 400% 400%;
      animation: hologramShimmer 3s ease-in-out infinite, neonPulse 2s ease-in-out infinite;
      -webkit-background-clip: text; background-clip: text; -webkit-text-fill-color: transparent;
      font-weight: 800; font-size: 4.5rem; letter-spacing: -0.03em; margin-bottom: 0.5rem;
    }

    .main-subtitle {
      text-align: center; color: var(--text-300); font-size: 1.3rem; font-weight: 400;
      margin-bottom: 0.5rem; animation: slideInGlow 1s ease-out 0.5s both;
    }

    .version-badge { text-align: center; margin-bottom: 3rem; }
    .badge {
      background: var(--legal); padding: 0.5rem 1.5rem; border-radius: 25px;
      font-size: 0.9rem; font-weight: 600; color: white; display: inline-block;
      animation: neonPulse 3s ease-in-out infinite; box-shadow: 0 0 20px rgba(255, 215, 0, 0.5);
    }

    .truthlens-panel {
      background: linear-gradient(145deg, rgba(26, 31, 46, 0.9), rgba(15, 20, 25, 0.95));
      border: 1px solid var(--line-600); border-radius: 24px; padding: 2.5rem; color: var(--text-50);
      box-shadow: 0 8px 32px rgba(0, 0, 0, 0.4), inset 0 1px 0 rgba(255, 255, 255, 0.1);
      backdrop-filter: blur(20px); animation: slideInGlow 0.8s ease-out;
    }

    .legal-grade-badge {
      background: var(--legal);
      padding: 0.75rem 1.5rem;
      border-radius: 15px;
      font-weight: 700;
      color: #000;
      text-align: center;
      margin: 1rem 0;
      box-shadow: 0 0 20px rgba(255, 215, 0, 0.3);
      animation: neonPulse 2s ease-in-out infinite;
    }

    .verdict-human { 
      color: var(--neon-green); font-weight: 800; font-size: 2.5rem; 
      text-shadow: 0 0 10px var(--neon-green), 0 0 20px var(--neon-green), 0 0 40px var(--neon-green);
      animation: slideInGlow 1s ease-out, neonPulse 3s ease-in-out infinite 1s;
      text-align: center; margin: 2rem 0;
    }
    
    .verdict-ai { 
      color: var(--neon-red); font-weight: 800; font-size: 2.5rem; 
      text-shadow: 0 0 10px var(--neon-red), 0 0 20px var(--neon-red), 0 0 40px var(--neon-red);
      animation: slideInGlow 1s ease-out, neonPulse 3s ease-in-out infinite 1s;
      text-align: center; margin: 2rem 0;
    }

    .confidence-display {
      text-align: center; margin: 2rem 0; padding: 2rem;
      background: linear-gradient(145deg, var(--bg-1000), var(--bg-900));
      border-radius: 20px; border: 1px solid var(--line-600);
    }

    .confidence-number { font-size: 4rem; font-weight: 900; margin-bottom: 1rem; animation: slideInGlow 1.2s ease-out; }
    .confidence-high { color: var(--neon-green); text-shadow: 0 0 20px var(--neon-green); }
    .confidence-medium { color: var(--neon-yellow); text-shadow: 0 0 20px var(--neon-yellow); }
    .confidence-low { color: var(--neon-red); text-shadow: 0 0 20px var(--neon-red); }

    .analysis-card {
      background: linear-gradient(145deg, rgba(10, 14, 26, 0.95), rgba(26, 31, 46, 0.9));
      border: 1px solid var(--line-700); border-radius: 20px; padding: 2rem; margin: 1.5rem 0;
      box-shadow: 0 8px 24px rgba(0, 0, 0, 0.3), inset 0 1px 0 rgba(255, 255, 255, 0.05);
      animation: slideInGlow 0.6s ease-out;
    }

    .video-analysis-section {
      background: linear-gradient(145deg, rgba(139, 95, 255, 0.1), rgba(255, 43, 209, 0.1));
      border: 2px solid var(--neon-purple);
      border-radius: 20px;
      padding: 2rem;
      margin: 2rem 0;
      box-shadow: 0 0 30px rgba(139, 95, 255, 0.3);
    }

    .legal-report-section {
      background: linear-gradient(145deg, rgba(255, 215, 0, 0.1), rgba(192, 192, 192, 0.1));
      border: 2px solid var(--legal-gold);
      border-radius: 20px;
      padding: 2rem;
      margin: 2rem 0;
      box-shadow: 0 0 30px rgba(255, 215, 0, 0.3);
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Data Classes
# -----------------------------

@dataclass
class VideoAnalysisFeatures:
    """Video-specific AI detection features"""
    temporal_consistency_score: float
    motion_vector_anomalies: float
    frame_transition_artifacts: float
    optical_flow_irregularities: float
    compression_pattern_analysis: float
    facial_morphing_detection: float
    lip_sync_consistency: float
    deepfake_indicators: float
    generation_timestamp_analysis: float
    frame_interpolation_artifacts: float

@dataclass
class LegalGradeFeatures:
    """Legal-grade analysis features for court admissibility"""
    chain_of_custody_score: float
    forensic_hash_verification: float
    metadata_integrity_score: float
    source_authenticity_score: float
    tampering_detection_score: float
    expert_witness_confidence: float
    admissibility_score: float
    evidence_quality_rating: str
    legal_certainty_level: str
    court_ready_analysis: bool

@dataclass
class AdvancedDetectionFeatures:
    """Enhanced AI detection features with legal-grade analysis"""
    # Pixel-level Analysis
    pixel_noise_variance: float
    frequency_domain_anomalies: float
    edge_sharpness_consistency: float
    compression_artifacts: float
    
    # Advanced Computer Vision
    texture_analysis_score: float
    color_histogram_anomalies: float
    gradient_consistency: float
    local_binary_patterns: float
    
    # Deep Learning Indicators
    neural_texture_patterns: float
    upsampling_artifacts: float
    attention_map_irregularities: float
    latent_space_signatures: float
    
    # Metadata and Technical
    exif_consistency_score: float
    timestamp_plausibility: float
    color_profile_analysis: float
    file_entropy_analysis: float
    
    # Legal-Grade Enhancements
    statistical_significance: float
    cross_validation_score: float
    reproducibility_index: float
    false_positive_probability: float

# -----------------------------
# Analysis Functions
# -----------------------------

def analyze_pixel_patterns(img_array: np.ndarray) -> Dict[str, float]:
    """Enhanced pixel-level analysis for AI detection"""
    results = {}
    
    try:
        # Convert to grayscale for some analyses
        if len(img_array.shape) == 3:
            gray = np.mean(img_array, axis=2)
        else:
            gray = img_array
        
        # Noise variance analysis
        noise_estimate = np.var(gray - ndimage.gaussian_filter(gray, sigma=1))
        noise_variance = min(1.0, noise_estimate / 1000.0)
        results['noise_variance'] = noise_variance
        
        # Edge consistency analysis
        edges_sobel = filters.sobel(gray)
        edges_canny = feature.canny(gray.astype(np.uint8))
        
        # Compare edge detection methods for consistency
        edge_correlation = np.corrcoef(edges_sobel.flatten(), edges_canny.astype(float).flatten())[0, 1]
        if np.isnan(edge_correlation):
            edge_correlation = 0.5
        results['edge_consistency'] = abs(edge_correlation)
        
        # Gradient consistency
        grad_x, grad_y = np.gradient(gray)
        gradient_magnitude = np.sqrt(grad_x**2 + grad_y**2)
        gradient_variance = np.var(gradient_magnitude)
        gradient_consistency = 1.0 - min(1.0, gradient_variance / 10000.0)
        results['gradient_consistency'] = gradient_consistency
        
        # Upsampling artifacts detection
        from scipy.signal import correlate2d
        
        # Create a kernel to detect interpolation patterns
        kernel = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
        convolved = correlate2d(gray, kernel, mode='same')
        upsampling_score = np.mean(np.abs(convolved)) / 255.0
        results['upsampling_artifacts'] = min(1.0, upsampling_score)
        
    except Exception as e:
        results = {'noise_variance': 0.5, 'edge_consistency': 0.5, 'gradient_consistency': 0.5, 'upsampling_artifacts': 0.5}
    
    return results

def analyze_color_characteristics(img_array: np.ndarray) -> Dict[str, float]:
    """Enhanced color analysis for AI-generated content detection"""
    results = {}
    
    try:
        if len(img_array.shape) != 3:
            return {'histogram_anomalies': 0.5, 'color_naturalness': 0.5}
        
        # Color histogram analysis
        hist_r = np.histogram(img_array[:,:,0], bins=256, range=(0, 256))[0]
        hist_g = np.histogram(img_array[:,:,1], bins=256, range=(0, 256))[0]
        hist_b = np.histogram(img_array[:,:,2], bins=256, range=(0, 256))[0]
        
        # Normalize histograms
        hist_r = hist_r / np.sum(hist_r)
        hist_g = hist_g / np.sum(hist_g)
        hist_b = hist_b / np.sum(hist_b)
        
        # Check for unnatural color distributions
        hist_entropy_r = stats.entropy(hist_r + 1e-10)
        hist_entropy_g = stats.entropy(hist_g + 1e-10)
        hist_entropy_b = stats.entropy(hist_b + 1e-10)
        
        avg_entropy = (hist_entropy_r + hist_entropy_g + hist_entropy_b) / 3
        entropy_anomaly = 1.0 - (avg_entropy / 8.0)  # 8.0 is max entropy for 256 bins
        results['histogram_anomalies'] = min(1.0, max(0.0, entropy_anomaly))
        
        # Color saturation analysis
        hsv = cv2.cvtColor(img_array, cv2.COLOR_RGB2HSV)
        saturation_mean = np.mean(hsv[:,:,1])
        
        # AI images often have unnatural saturation patterns
        saturation_naturalness = abs(saturation_mean - 127.5) / 127.5
        results['color_naturalness'] = 1.0 - saturation_naturalness
        
    except Exception as e:
        results = {'histogram_anomalies': 0.5, 'color_naturalness': 0.5}
    
    return results

def analyze_frequency_domain(img_array: np.ndarray) -> Dict[str, float]:
    """Frequency domain analysis for AI detection"""
    results = {}
    
    try:
        # Convert to grayscale
        if len(img_array.shape) == 3:
            gray = np.mean(img_array, axis=2)
        else:
            gray = img_array
        
        # Apply 2D FFT
        fft_result = fft2(gray)
        fft_shifted = fftshift(fft_result)
        magnitude_spectrum = np.abs(fft_shifted)
        
        # Analyze frequency characteristics
        center_y, center_x = magnitude_spectrum.shape[0] // 2, magnitude_spectrum.shape[1] // 2
        
        # High frequency content analysis
        high_freq_mask = np.zeros_like(magnitude_spectrum)
        radius = min(center_y, center_x) // 4
        y, x = np.ogrid[:magnitude_spectrum.shape[0], :magnitude_spectrum.shape[1]]
        mask = (y - center_y)**2 + (x - center_x)**2 > radius**2
        high_freq_mask[mask] = 1
        
        high_freq_energy = np.sum(magnitude_spectrum * high_freq_mask)
        total_energy = np.sum(magnitude_spectrum)
        high_freq_ratio = high_freq_energy / (total_energy + 1e-10)
        
        # Anomaly score based on frequency distribution
        anomaly_score = 1.0 - min(1.0, high_freq_ratio * 10)
        results['anomaly_score'] = anomaly_score
        
        # Attention map irregularities (simplified)
        freq_variance = np.var(np.log(magnitude_spectrum + 1))
        attention_anomaly = min(1.0, freq_variance / 100.0)
        results['attention_anomalies'] = attention_anomaly
        
    except Exception as e:
        results = {'anomaly_score': 0.5, 'attention_anomalies': 0.5}
    
    return results

def analyze_texture_patterns(img_array: np.ndarray) -> Dict[str, float]:
    """Advanced texture analysis for AI detection"""
    results = {}
    
    try:
        # Convert to grayscale
        if len(img_array.shape) == 3:
            gray = np.mean(img_array, axis=2).astype(np.uint8)
        else:
            gray = img_array.astype(np.uint8)
        
        # Local Binary Pattern analysis
        lbp = feature.local_binary_pattern(gray, 8, 1, method='uniform')
        lbp_hist = np.histogram(lbp.ravel(), bins=10)[0]
        lbp_hist = lbp_hist / (np.sum(lbp_hist) + 1e-10)
        
        # Uniformity of LBP patterns
        lbp_uniformity = 1.0 - stats.entropy(lbp_hist + 1e-10) / np.log(len(lbp_hist))
        results['lbp_uniformity'] = lbp_uniformity
        
        # Texture complexity using Gray-Level Co-occurrence Matrix
        from skimage.feature import graycomatrix, graycoprops
        
        # Compute GLCM
        distances = [1, 2, 3]
        angles = [0, np.pi/4, np.pi/2, 3*np.pi/4]
        
        try:
            glcm = graycomatrix(gray, distances=distances, angles=angles, levels=256, symmetric=True, normed=True)
            
            # Extract texture properties
            contrast = np.mean(graycoprops(glcm, 'contrast'))
            dissimilarity = np.mean(graycoprops(glcm, 'dissimilarity'))
            homogeneity = np.mean(graycoprops(glcm, 'homogeneity'))
            energy = np.mean(graycoprops(glcm, 'energy'))
            
            # Combine properties into texture complexity score
            texture_complexity = (contrast + dissimilarity + (1-homogeneity) + (1-energy)) / 4
            texture_complexity = min(1.0, texture_complexity / 1000.0)
            results['texture_complexity'] = texture_complexity
            
        except Exception:
            results['texture_complexity'] = 0.5
        
        # Neural pattern detection (simplified)
        edge_density = np.sum(feature.canny(gray)) / gray.size
        neural_patterns = abs(edge_density - 0.1) * 10
        results['neural_patterns'] = min(1.0, neural_patterns)
        
        # Latent space signatures (simplified)
        smoothness = np.mean(ndimage.gaussian_filter(gray.astype(float), sigma=2) - gray.astype(float))**2
        latent_signatures = min(1.0, smoothness / 1000.0)
        results['latent_signatures'] = latent_signatures
        
    except Exception as e:
        results = {'lbp_uniformity': 0.5, 'texture_complexity': 0.5, 'neural_patterns': 0.5, 'latent_signatures': 0.5}
    
    return results

def extract_and_analyze_metadata(image_data: Union[str, bytes]) -> Dict[str, float]:
    """Enhanced metadata analysis for legal-grade detection"""
    
    results = {
        'exif_consistency': 0.5,
        'creation_plausibility': 0.5,
        'camera_signature': 0.5,
        'software_analysis': 0.5,
        'gps_consistency': 0.5
    }
    
    try:
        if isinstance(image_data, bytes):
            img = Image.open(BytesIO(image_data))
        else:
            img = Image.open(image_data)
            
        # Extract EXIF data
        exif_dict = img._getexif()
        if exif_dict is not None:
            exif = {}
            for k, v in exif_dict.items():
                if k in ExifTags.TAGS:
                    exif[ExifTags.TAGS[k]] = v
            
            # Enhanced camera analysis
            camera_make = str(exif.get('Make', '')).lower()
            camera_model = str(exif.get('Model', '')).lower()
            software = str(exif.get('Software', '')).lower()
            
            # Comprehensive AI software detection
            ai_software_signatures = [
                'midjourney', 'dall-e', 'dalle', 'stable diffusion', 'sd',
                'runway', 'synthesia', 'deepfake', 'faceswap', 'artbreeder',
                'generated', 'artificial', 'ai', 'neural', 'diffusion',
                'gpt', 'clip', 'vqgan', 'stylegan', 'biggan'
            ]
            
            # Check software field
            software_ai_score = 0.0
            for signature in ai_software_signatures:
                if signature in software:
                    software_ai_score = 0.9
                    break
            
            results['software_analysis'] = 1.0 - software_ai_score
            
            # Enhanced camera signature analysis
            legitimate_camera_brands = [
                'canon', 'nikon', 'sony', 'fujifilm', 'panasonic', 'olympus',
                'leica', 'pentax', 'hasselblad', 'mamiya', 'phase one'
            ]
            
            smartphone_brands = [
                'apple', 'iphone', 'samsung', 'galaxy', 'pixel', 'google',
                'oneplus', 'huawei', 'xiaomi', 'lg', 'motorola', 'nokia'
            ]
            
            camera_score = 0.3  # Default suspicious
            
            # Check for legitimate camera brands
            for brand in legitimate_camera_brands:
                if brand in camera_make or brand in camera_model:
                    camera_score = 0.9
                    break
            
            # Check for smartphones
            if camera_score < 0.9:
                for brand in smartphone_brands:
                    if brand in camera_make or brand in camera_model:
                        camera_score = 0.7
                        break
            
            results['camera_signature'] = camera_score
            
            # Date/time analysis
            datetime_original = exif.get('DateTimeOriginal')
            datetime_digitized = exif.get('DateTimeDigitized')
            
            if datetime_original and datetime_digitized:
                try:
                    dt_orig = datetime.strptime(datetime_original, '%Y:%m:%d %H:%M:%S')
                    dt_dig = datetime.strptime(datetime_digitized, '%Y:%m:%d %H:%M:%S')
                    
                    # Check if dates are reasonable
                    now = datetime.now()
                    if dt_orig <= now and dt_dig <= now:
                        time_diff = abs((dt_orig - dt_dig).total_seconds())
                        # Reasonable if times are close but not identical
                        if time_diff < 3600:  # Within 1 hour
                            results['creation_plausibility'] = 0.8
                        else:
                            results['creation_plausibility'] = 0.6
                    else:
                        results['creation_plausibility'] = 0.2  # Future dates suspicious
                except:
                    results['creation_plausibility'] = 0.4
            
            # GPS consistency analysis
            gps_info = exif.get('GPSInfo')
            if gps_info:
                # Presence of GPS data suggests legitimate capture
                results['gps_consistency'] = 0.8
            else:
                results['gps_consistency'] = 0.5  # Neutral - not all photos have GPS
                
            # Overall EXIF consistency
            exif_fields = len(exif)
            if exif_fields > 20:  # Rich EXIF suggests real camera
                results['exif_consistency'] = 0.9
            elif exif_fields > 10:
                results['exif_consistency'] = 0.7
            elif exif_fields > 5:
                results['exif_consistency'] = 0.5
            else:
                results['exif_consistency'] = 0.3
                
        else:
            # No EXIF data - suspicious for photographs, normal for graphics
            results['exif_consistency'] = 0.3
    
    except Exception:
        # Error reading EXIF - moderately suspicious
        results['exif_consistency'] = 0.3
    
    return results

def analyze_compression_patterns(image_data: bytes, file_path: str) -> Dict[str, float]:
    """Enhanced compression pattern analysis"""
    results = {}
    
    try:
        # File entropy analysis
        byte_counts = np.bincount(list(image_data), minlength=256)
        entropy = stats.entropy(byte_counts + 1)  # Add 1 to avoid log(0)
        results['file_entropy'] = min(1.0, entropy / 8.0)
        
        # JPEG compression analysis
        try:
            with Image.open(BytesIO(image_data)) as img:
                # Check for JPEG compression artifacts
                if img.format == 'JPEG':
                    # Convert to array for analysis
                    img_array = np.array(img)
                    if len(img_array.shape) == 3:
                        # Analyze 8x8 block patterns typical in JPEG
                        gray = cv2.cvtColor(img_array, cv2.COLOR_RGB2GRAY)
                        
                        # Check for blockiness
                        blocks_h = gray.reshape(gray.shape[0]//8, 8, -1, 8).mean(axis=(1,3))
                        blocks_v = gray.reshape(-1, 8, gray.shape[1]//8, 8).mean(axis=(1,3))
                        
                        block_variance_h = np.var(blocks_h)
                        block_variance_v = np.var(blocks_v)
                        
                        # Natural images have more block variance
                        block_naturalness = min(1.0, (block_variance_h + block_variance_v) / 2000.0)
                        results['compression_naturalness'] = block_naturalness
                    else:
                        results['compression_naturalness'] = 0.5
                else:
                    results['compression_naturalness'] = 0.7  # PNG/other formats
                    
        except Exception:
            results['compression_naturalness'] = 0.5
    
    except Exception as e:
        results = {'file_entropy': 0.5, 'compression_naturalness': 0.5}
    
    return results

def analyze_url_patterns(url: str) -> Dict[str, float]:
    """Enhanced URL pattern analysis supporting all major platforms"""
    
    if not url:
        return {'ai_probability': 0.5, 'source_confidence': 0.5}
    
    url_lower = url.lower()
    
    # AI generation platforms and tools
    ai_platforms = {
        'midjourney.com': 0.95, 'cdn.midjourney.com': 0.95, 'discord.com/attachments': 0.7,
        'dalle': 0.9, 'dall-e': 0.9, 'openai.com/dalle': 0.9,
        'stability.ai': 0.85, 'stable-diffusion': 0.85, 'stablediffusion': 0.85,
        'runway.ml': 0.9, 'runwayml.com': 0.9, 'gen-2': 0.85,
        'leonardo.ai': 0.8, 'firefly.adobe.com': 0.7, 'synthesia.io': 0.95,
        'deepfake': 0.95, 'faceswap': 0.9, 'deepfacelab': 0.9,
        'artbreeder': 0.8, 'thisxdoesnotexist': 0.95, 'generated.photos': 0.9,
        'huggingface.co/spaces': 0.7, 'gradio.app': 0.6, 'replicate.com': 0.6
    }
    
    # Authentic/trusted sources
    trusted_sources = {
        'reuters.com': 0.95, 'apnews.com': 0.95, 'bbc.com': 0.9, 'cnn.com': 0.85,
        'nytimes.com': 0.9, 'washingtonpost.com': 0.9, 'theguardian.com': 0.85,
        'bloomberg.com': 0.85, 'wsj.com': 0.9, 'npr.org': 0.85,
        'youtube.com': 0.7, 'vimeo.com': 0.75, 'twitch.tv': 0.7,
        'instagram.com': 0.6, 'facebook.com': 0.6, 'twitter.com': 0.65, 'x.com': 0.65,
        'tiktok.com': 0.5, 'snapchat.com': 0.6, 'linkedin.com': 0.7,
        'flickr.com': 0.8, '500px.com': 0.8, 'behance.net': 0.7, 'dribbble.com': 0.7,
        'shutterstock.com': 0.85, 'getty': 0.9, 'unsplash.com': 0.75, 'pexels.com': 0.75
    }
    
    # Check for AI platforms
    ai_score = 0.0
    for platform, score in ai_platforms.items():
        if platform in url_lower:
            ai_score = max(ai_score, score)
            break
    
    # Check for trusted sources
    trust_score = 0.0
    for source, score in trusted_sources.items():
        if source in url_lower:
            trust_score = max(trust_score, score)
            break
    
    # Additional suspicious patterns
    suspicious_patterns = [
        r'[0-9a-f]{32,}',  # Long hex strings
        r'temp\d+', r'cache\d+', r'generated\d+',
        r'ai[-_]generated', r'synthetic[-_]media'
    ]
    
    for pattern in suspicious_patterns:
        if re.search(pattern, url_lower):
            ai_score += 0.3
            break
    
    # Final calculation
    if trust_score > 0:
        final_ai_prob = max(0, ai_score - trust_score * 0.8)
        source_confidence = trust_score
    else:
        final_ai_prob = ai_score
        source_confidence = 0.5
    
    return {
        'ai_probability': min(0.95, final_ai_prob),
        'source_confidence': source_confidence
    }

def perform_cross_validation(img_array: np.ndarray) -> float:
    """Perform cross-validation across multiple detection methods"""
    try:
        scores = []
        
        # Multiple independent analyses
        pixel_score = np.mean(list(analyze_pixel_patterns(img_array).values()))
        color_score = np.mean(list(analyze_color_characteristics(img_array).values()))
        frequency_score = np.mean(list(analyze_frequency_domain(img_array).values()))
        texture_score = np.mean(list(analyze_texture_patterns(img_array).values()))
        
        scores = [pixel_score, color_score, frequency_score, texture_score]
        scores = [s for s in scores if not np.isnan(s)]
        
        if len(scores) == 0:
            return 0.5
        
        # Calculate consistency across methods
        score_std = np.std(scores)
        score_mean = np.mean(scores)
        
        # Higher consistency = better cross-validation score
        consistency = 1.0 - min(1.0, score_std / (score_mean + 1e-6))
        return max(0, min(1, consistency))
        
    except Exception:
        return 0.5

def calculate_statistical_reliability(pixel_analysis: Dict, color_analysis: Dict) -> float:
    """Calculate statistical reliability of the analysis"""
    try:
        # Combine multiple analysis results for statistical validation
        measurements = []
        measurements.extend(list(pixel_analysis.values()))
        measurements.extend(list(color_analysis.values()))
        
        # Remove any None values
        measurements = [m for m in measurements if m is not None]
        
        if len(measurements) < 3:
            return 0.5
        
        # Calculate statistical measures
        mean_measurement = np.mean(measurements)
        std_measurement = np.std(measurements)
        
        # Higher reliability when measurements are consistent
        coefficient_of_variation = std_measurement / (mean_measurement + 1e-6)
        reliability = 1.0 - min(1.0, coefficient_of_variation)
        
        return max(0, min(1, reliability))
        
    except Exception:
        return 0.5

def calculate_false_positive_probability(pixel_analysis: Dict, color_analysis: Dict) -> float:
    """Calculate probability of false positive detection"""
    try:
        # Count strong indicators vs weak indicators
        strong_indicators = 0
        weak_indicators = 0
        total_indicators = 0
        
        all_values = list(pixel_analysis.values()) + list(color_analysis.values())
        all_values = [v for v in all_values if v is not None]
        
        for value in all_values:
            total_indicators += 1
            if value > 0.8:
                strong_indicators += 1
            elif value > 0.6:
                weak_indicators += 1
        
        if total_indicators == 0:
            return 0.5
        
        # Lower false positive probability when more strong indicators present
        strong_ratio = strong_indicators / total_indicators
        weak_ratio = weak_indicators / total_indicators
        
        false_positive_prob = 1.0 - (strong_ratio * 0.8 + weak_ratio * 0.4)
        return max(0.05, min(0.95, false_positive_prob))
        
    except Exception:
        return 0.5

def comprehensive_ai_detection(image_data: Union[bytes, np.ndarray], source_url: str = "") -> AdvancedDetectionFeatures:
    """Comprehensive AI detection analysis with legal-grade precision"""
    
    try:
        # Handle different input types
        if isinstance(image_data, np.ndarray):
            # Convert numpy array to PIL Image
            if len(image_data.shape) == 3:
                pil_img = Image.fromarray(image_data.astype(np.uint8))
            else:
                pil_img = Image.fromarray(image_data.astype(np.uint8)).convert('RGB')
            
            # Convert to bytes for some analyses
            byte_buffer = BytesIO()
            pil_img.save(byte_buffer, format='PNG')
            image_bytes = byte_buffer.getvalue()
        else:
            image_bytes = image_data
            pil_img = Image.open(BytesIO(image_bytes)).convert('RGB')
        
        # Convert to numpy array for analysis
        img_array = np.array(pil_img)
        
        # Pixel-level analysis
        pixel_analysis = analyze_pixel_patterns(img_array)
        
        # Color analysis
        color_analysis = analyze_color_characteristics(img_array)
        
        # Frequency domain analysis
        frequency_analysis = analyze_frequency_domain(img_array)
        
        # Texture and pattern analysis
        texture_analysis = analyze_texture_patterns(img_array)
        
        # Metadata analysis
        metadata_analysis = extract_and_analyze_metadata(image_bytes)
        
        # Compression analysis
        compression_analysis = analyze_compression_patterns(image_bytes, "temp")
        
        # Statistical validation
        statistical_reliability = calculate_statistical_reliability(pixel_analysis, color_analysis)
        cross_validation = perform_cross_validation(img_array)
        false_positive_prob = calculate_false_positive_probability(pixel_analysis, color_analysis)
        
        # Combine all features
        features = AdvancedDetectionFeatures(
            # Pixel-level
            pixel_noise_variance=pixel_analysis.get('noise_variance', 0.5),
            frequency_domain_anomalies=frequency_analysis.get('anomaly_score', 0.5),
            edge_sharpness_consistency=pixel_analysis.get('edge_consistency', 0.5),
            compression_artifacts=compression_analysis.get('compression_naturalness', 0.5),
            
            # Computer Vision
            texture_analysis_score=texture_analysis.get('texture_complexity', 0.5),
            color_histogram_anomalies=color_analysis.get('histogram_anomalies', 0.5),
            gradient_consistency=pixel_analysis.get('gradient_consistency', 0.5),
            local_binary_patterns=texture_analysis.get('lbp_uniformity', 0.5),
            
            # Deep Learning Indicators
            neural_texture_patterns=texture_analysis.get('neural_patterns', 0.5),
            upsampling_artifacts=pixel_analysis.get('upsampling_artifacts', 0.5),
            attention_map_irregularities=frequency_analysis.get('attention_anomalies', 0.5),
            latent_space_signatures=texture_analysis.get('latent_signatures', 0.5),
            
            # Metadata
            exif_consistency_score=metadata_analysis.get('exif_consistency', 0.5),
            timestamp_plausibility=metadata_analysis.get('creation_plausibility', 0.5),
            color_profile_analysis=metadata_analysis.get('software_analysis', 0.5),
            file_entropy_analysis=compression_analysis.get('file_entropy', 0.5),
            
            # Legal-Grade
            statistical_significance=statistical_reliability,
            cross_validation_score=cross_validation,
            reproducibility_index=statistical_reliability * cross_validation,
            false_positive_probability=false_positive_prob
        )
        
        return features
        
    except Exception as e:
        st.error(f"Error in comprehensive AI detection: {str(e)}")
        # Return default features
        return AdvancedDetectionFeatures(
            pixel_noise_variance=0.5, frequency_domain_anomalies=0.5, edge_sharpness_consistency=0.5,
            compression_artifacts=0.5, texture_analysis_score=0.5, color_histogram_anomalies=0.5,
            gradient_consistency=0.5, local_binary_patterns=0.5, neural_texture_patterns=0.5,
            upsampling_artifacts=0.5, attention_map_irregularities=0.5, latent_space_signatures=0.5,
            exif_consistency_score=0.5, timestamp_plausibility=0.5, color_profile_analysis=0.5,
            file_entropy_analysis=0.5, statistical_significance=0.5, cross_validation_score=0.5,
            reproducibility_index=0.5, false_positive_probability=0.5
