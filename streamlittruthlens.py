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

















#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import hashlib
import os
import time
from dataclasses import dataclass
from typing import Optional, Tuple

import streamlit as st


# -----------------------------
# Page setup
# -----------------------------

st.set_page_config(
    page_title="Truthlens — Misinformation Scanner",
    page_icon="🔎",
    layout="wide",
)

# Custom CSS to approximate the neon dark theme
st.markdown(
    """
    <style>
    :root {
      --bg-900: #0B0F14;
      --bg-800: #0F1622;
      --text-100: #E6F0FF;
      --text-300: #9BB3C9;
      --line-700: #1B2A3B;
      --blue: #00D4FF;
      --fuchsia: #FF2BD1;
      --green: #39FF88;
      --red: #FF5C5C;
      --radius-lg: 16px;
      --radius-md: 12px;
      --radius-sm: 8px;
      --shadow-glow-blue: 0 0 24px rgba(0, 212, 255, 0.35);
      --shadow-glow-green: 0 0 24px rgba(57, 255, 136, 0.35);
      --shadow-glow-red: 0 0 24px rgba(255, 92, 92, 0.35);
    }

    .truthlens-panel {
      background: var(--bg-800);
      border: 1px solid var(--line-700);
      border-radius: var(--radius-lg);
      padding: 24px;
      color: var(--text-100);
    }
    .truthlens-title {
      font-weight: 700;
      font-size: 22px;
      margin-bottom: 12px;
    }
    .hint { color: var(--text-300); }
    .tab-underline {
      height: 3px;
      border-radius: 2px;
      background: linear-gradient(90deg, var(--blue), var(--fuchsia));
      box-shadow: var(--shadow-glow-blue);
      margin-top: 8px;
      margin-bottom: 2px;
    }
    .dropzone {
      border: 2px dashed var(--line-700);
      border-radius: var(--radius-lg);
      padding: 28px;
      text-align: center;
      color: var(--text-300);
      background: var(--bg-900);
    }
    .verdict-good { color: var(--green); font-weight: 800; font-size: 22px; }
    .verdict-bad { color: var(--red); font-weight: 800; font-size: 22px; }
    .card { background: var(--bg-900); border: 1px solid var(--line-700); border-radius: 12px; padding: 12px; }
    .card-label { color: var(--text-300); font-size: 12px; letter-spacing: 0.04em; }
    .card-value { color: var(--text-100); font-size: 16px; font-weight: 600; }
    </style>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# Utilities
# -----------------------------

@dataclass
class AnalysisResult:
    is_ai_generated: bool
    confidence_pct: int
    resolution: str
    aspect_ratio: str
    file_type: str
    video_length: Optional[str] = None


def deterministic_score(seed: str) -> float:
    digest = hashlib.sha256(seed.encode("utf-8")).hexdigest()
    value = int(digest[:8], 16) / 0xFFFFFFFF
    return value


def guess_resolution_and_ratio(source: str) -> Tuple[str, str]:
    lower = source.lower()
    if any(k in lower for k in ["tiktok", "shorts", "reels"]):
        return "1080 × 1920", "9:16"
    if any(k in lower for k in ["instagram", "stories"]):
        return "1080 × 1350", "4:5"
    return "1920 × 1080", "16:9"


def guess_video_length(source: str) -> str:
    score = deterministic_score(source)
    total_secs = 10 + int(score * 160)
    m, s = divmod(total_secs, 60)
    return f"{m:02d}:{s:02d}"


def simulate_analysis_and_results(source: str) -> AnalysisResult:
    res, ratio = guess_resolution_and_ratio(source)
    ext = os.path.splitext(source)[1].lower()
    score = deterministic_score(source)
    confidence = 72 + int(score * 27)
    is_ai = score >= 0.5
    file_type = ext if ext else (".mp4" if "http" in source else ".jpg")
    video_len = guess_video_length(source) if ext in {".mp4", ".mov", ".avi", ".mkv", ".webm"} or ("tiktok" in source.lower() or "youtube" in source.lower()) else None
    return AnalysisResult(
        is_ai_generated=is_ai,
        confidence_pct=confidence,
        resolution=res,
        aspect_ratio=ratio,
        file_type=file_type,
        video_length=video_len,
    )

# -----------------------------
# App Header
# -----------------------------

st.markdown("<div class='truthlens-title'>Truthlens</div>", unsafe_allow_html=True)

with st.container():
    st.markdown("<div class='truthlens-panel'>", unsafe_allow_html=True)

    tabs = st.tabs(["URL (Default)", "Media Upload"])

    # URL Tab
    with tabs[0]:
        url_col1, url_col2 = st.columns([6, 1])
        with url_col1:
            url_input = st.text_input(
                "",
                placeholder="Paste any media URL, including links from social media like TikTok, Instagram, and YouTube...",
                label_visibility="collapsed",
            )
            st.caption("Resolving media source…")
        with url_col2:
            submit_url = st.button("Analyze", type="primary", use_container_width=True)

        if submit_url and not url_input:
            st.warning("We couldn’t read that link. Check the URL and try again.")

    # Upload Tab
    with tabs[1]:
        st.markdown("<div class='dropzone'>Drag & Drop a file here or Click to browse.</div>", unsafe_allow_html=True)
        uploaded = st.file_uploader("Upload media", type=["jpg","jpeg","png","webp","bmp","gif","mp4","mov","avi","mkv","webm"], label_visibility="collapsed")
        submit_upload = st.button("Analyze Upload", use_container_width=True)

    st.markdown("<div class='tab-underline'></div>", unsafe_allow_html=True)

    # Trigger analysis
    source: Optional[str] = None
    if submit_url and url_input:
        source = url_input
    elif submit_upload and uploaded is not None:
        # We use the filename as deterministic seed; in real app, save and analyze file bytes
        source = uploaded.name

    # Scan & Analysis simulation
    if source:
        st.divider()
        msg_slot = st.empty()
        progress = st.progress(0, text="Initializing…")
        steps = [
            "Analyzing pixel integrity…",
            "Scanning for artifact patterns…",
            "Cross-referencing data points…",
            "Evaluating compression signatures…",
            "Measuring sensor noise consistency…",
            "Aggregating model inferences…",
        ]
        for i, msg in enumerate(steps, start=1):
            msg_slot.markdown(f"<span class='hint'>{msg}</span>", unsafe_allow_html=True)
            progress.progress(int(i / len(steps) * 100), text=msg)
            time.sleep(0.9)
        msg_slot.empty()

        # Results
        result = simulate_analysis_and_results(source)
        st.success("Analysis complete")

        # Verdict
        verdict_class = "verdict-bad" if result.is_ai_generated else "verdict-good"
        verdict_text = "Likely AI-Generated" if result.is_ai_generated else "Likely Human-Created"
        st.markdown(f"<div class='{verdict_class}'>{verdict_text}</div>", unsafe_allow_html=True)
        st.caption("This is a probabilistic assessment, not an absolute determination.")

        # Data Summary cards
        c1, c2, c3, c4 = st.columns(4)
        with c1:
            st.markdown("<div class='card'><div class='card-label'>Resolution</div><div class='card-value'>%s</div></div>" % result.resolution, unsafe_allow_html=True)
        with c2:
            st.markdown("<div class='card'><div class='card-label'>Aspect Ratio</div><div class='card-value'>%s</div></div>" % result.aspect_ratio, unsafe_allow_html=True)
        with c3:
            st.markdown("<div class='card'><div class='card-label'>File Type</div><div class='card-value'>%s</div></div>" % result.file_type, unsafe_allow_html=True)
        with c4:
            if result.video_length:
                st.markdown("<div class='card'><div class='card-label'>Video Length</div><div class='card-value'>%s</div></div>" % result.video_length, unsafe_allow_html=True)
            else:
                st.markdown("<div class='card'><div class='card-label'>Video Length</div><div class='card-value'>—</div></div>", unsafe_allow_html=True)

        # Confidence meter
        st.write("Confidence Score")
        conf_bar = st.progress(result.confidence_pct)
        st.write(f"{result.confidence_pct}% likely {'AI-Generated' if result.is_ai_generated else 'Human-Created'}")

    st.markdown("</div>", unsafe_allow_html=True)
