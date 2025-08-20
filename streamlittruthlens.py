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






# truthlens_full_ensemble.py
"""
TruthLens — Ensemble AI-vs-Human Media Detector (Inference App)

Features:
 - Upload or paste URL for images/videos (any extension).
 - Ensemble: CLIP multi-prompt, optional deepfake classifier, optional frame-level classifier,
   face-crop analysis, EXIF camera checks.
 - Video: samples evenly-spaced frames (MoviePy -> OpenCV fallback).
 - Output: "AI-generated" or "Human-made" and Width x Height resolution only (no percentages).
 - Configurable local model paths via environment variables:
     FRAME_CKPT -> path to frame-level classifier checkpoint (Torch .pth saved via train_frame_classifier)
     VIT_DIR    -> directory for ViT full-image finetuned model (Hugging Face huggingface save_pretrained)
     DEEPFAKE_MODEL_ID -> Hugging Face model id for deepfake classifier (will be loaded online if not local)
 - Face detector files (deploy.prototxt, res10_300x300_ssd_iter_140000.caffemodel) should be present in app folder,
   or the app will attempt to download them.
"""

import os
import io
import tempfile
import time
import math
import requests
from urllib.parse import urlparse
from pathlib import Path

import streamlit as st
import numpy as np
from PIL import Image, ExifTags, UnidentifiedImageError

import torch
import torch.nn.functional as F
import cv2
from moviepy.editor import VideoFileClip

# transformers imports for CLIP and optional deepfake classifier / ViT
from transformers import CLIPProcessor, CLIPModel, AutoImageProcessor, AutoModelForImageClassification

# timm for frame-level classifier if checkpoint provided
import timm
from torchvision import transforms

# -------------------------
# CONFIGURATION
# -------------------------
st.set_page_config(page_title="TruthLens — Ensemble Detector", layout="wide", page_icon="🔎")

# Model sources - configurable via environment variables
FRAME_CKPT = os.environ.get("FRAME_CKPT", "frame_model.pth")   # local checkpoint path (optional)
VIT_DIR = os.environ.get("VIT_DIR", "./vit_finetuned")         # local vit folder (optional)
# If you want the app to attempt to load a deepfake classifier online by id, set:
DEEPFAKE_MODEL_ID = os.environ.get("DEEPFAKE_MODEL_ID", None)  # e.g., "xhlulu/face-detection-model" (optional)

# CLIP repo (we use openai/clip-vit-base-patch32 by default)
CLIP_REPO = os.environ.get("CLIP_REPO", "openai/clip-vit-base-patch32")

# Face detector files (will auto-download if missing)
FACE_PROTO = "deploy.prototxt"
FACE_MODEL = "res10_300x300_ssd_iter_140000.caffemodel"
FACE_PROTO_URL = "https://raw.githubusercontent.com/opencv/opencv/master/samples/dnn/face_detector/deploy.prototxt"
FACE_MODEL_URL = "https://github.com/opencv/opencv_3rdparty/raw/dnn_samples_face_detector_20170830/res10_300x300_ssd_iter_140000.caffemodel"

# Device
DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")

# CLIP prompts (AI vs Human)
AI_PROMPTS = [
    "an AI-generated image, synthetic, digital rendering",
    "a computer-generated picture created by an AI model",
    "AI art, unreal, diffusion model output",
    "synthetic image with perfect edges and painterly look",
]
HUMAN_PROMPTS = [
    "a real photograph captured by a camera",
    "a natural human-made photograph with camera noise",
    "an authentic, real-world image captured by a person",
    "photo with realistic depth of field and natural grain",
]

# -------------------------
# UI: Neon background + header
# -------------------------
st.markdown("""
<style>
html, body, [data-testid="stAppViewContainer"] {
  background: radial-gradient(circle at 10% 10%, #001021, #000000) !important;
}
h1, h2, h3 { color:#00f9ff !important; text-shadow: 0 0 8px #00f9ff; }
.neon-card { border-radius:12px; padding:12px; background: rgba(6,10,20,0.6); box-shadow:0 8px 30px rgba(0,120,255,0.06); color:#dffaff; }
</style>
""", unsafe_allow_html=True)
st.title("🔎 TruthLens — Ensemble AI vs Human Media Detector")
st.markdown('<div class="neon-card">Uploads or paste direct URLs. Output: <b>AI-generated</b> or <b>Human-made</b> plus resolution (no percentages).</div>', unsafe_allow_html=True)

# -------------------------
# Utility functions
# -------------------------
def download_if_missing(url: str, dest: str, timeout: int = 120):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest):
        return dest
    r = requests.get(url, stream=True, timeout=timeout)
    r.raise_for_status()
    with open(dest, "wb") as f:
        for chunk in r.iter_content(chunk_size=16384):
            if chunk:
                f.write(chunk)
    return dest

def exif_has_camera(path_or_bytes) -> bool:
    """Return True if EXIF indicates a real camera (Make/Model etc)."""
    try:
        if isinstance(path_or_bytes, (bytes, bytearray)):
            img = Image.open(io.BytesIO(path_or_bytes))
        else:
            img = Image.open(path_or_bytes)
        exif = img._getexif()
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
# Model loading (cached)
# -------------------------
@st.cache_resource(show_spinner=True)
def load_clip_and_text_features():
    """Load CLIP and pre-encode text prompts (online via HF)."""
    try:
        processor = CLIPProcessor.from_pretrained(CLIP_REPO)
        model = CLIPModel.from_pretrained(CLIP_REPO)
        model.to(DEVICE).eval()
        # text features
        texts = AI_PROMPTS + HUMAN_PROMPTS
        inputs = processor(text=texts, return_tensors="pt", padding=True).to(DEVICE)
        with torch.no_grad():
            text_feats = model.get_text_features(**inputs)
        text_feats = text_feats / text_feats.norm(p=2, dim=-1, keepdim=True)
        return processor, model, text_feats, len(AI_PROMPTS), len(HUMAN_PROMPTS)
    except Exception as e:
        st.error(f"Failed to load CLIP model: {e}")
        raise

@st.cache_resource(show_spinner=True)
def load_deepfake_classifier_candidate(model_id=None):
    """
    Try to load a deepfake classifier from a HF repo ID if provided.
    Returns (processor, model, id2label) or (None, None, None) on failure.
    """
    if not model_id:
        return None, None, None
    try:
        proc = AutoImageProcessor.from_pretrained(model_id)
        mdl = AutoModelForImageClassification.from_pretrained(model_id)
        mdl.to(DEVICE).eval()
        id2label = {}
        if getattr(mdl.config, "id2label", None):
            id2label = mdl.config.id2label
        return proc, mdl, id2label
    except Exception as e:
        st.warning(f"Could not load deepfake classifier '{model_id}': {e}")
        return None, None, None

@st.cache_resource(show_spinner=True)
def load_frame_model_if_present(ckpt_path):
    """Load a timm model from a checkpoint if file exists."""
    if not ckpt_path or not os.path.exists(ckpt_path):
        return None, None
    try:
        ck = torch.load(ckpt_path, map_location="cpu")
        arch = ck.get("arch", "resnest50d")
        model = timm.create_model(arch, pretrained=False, num_classes=2)
        model.load_state_dict(ck["model_state"])
        model.to(DEVICE).eval()
        # simple transform - must match training transform (user should ensure)
        transform = transforms.Compose([
            transforms.Resize((224, 224)),
            transforms.ToTensor(),
            transforms.Normalize([0.485,0.456,0.406],[0.229,0.224,0.225])
        ])
        return model, transform
    except Exception as e:
        st.warning(f"Failed to load frame model from {ckpt_path}: {e}")
        return None, None

# Load CLIP
clip_processor, clip_model, TEXT_FEATS, N_AI, N_HUM = load_clip_and_text_features()

# Try deepfake classifier (if model id env var is set)
df_processor, df_model, df_id2label = load_deepfake_classifier_candidate(DEEPFAKE_MODEL_ID)

# Try frame model (local checkpoint)
frame_model, frame_transform = load_frame_model_if_present(FRAME_CKPT)

# Face detector (ensure model files present)
if not (os.path.exists(FACE_PROTO) and os.path.exists(FACE_MODEL)):
    try:
        download_if_missing(FACE_PROTO_URL, FACE_PROTO)
        download_if_missing(FACE_MODEL_URL, FACE_MODEL)
    except Exception as e:
        st.warning(f"Could not download face detector files: {e}")
FACE_NET = None
try:
    if os.path.exists(FACE_PROTO) and os.path.exists(FACE_MODEL):
        FACE_NET = cv2.dnn.readNetFromCaffe(FACE_PROTO, FACE_MODEL)
except Exception as e:
    st.warning(f"Failed to initialize face detector: {e}")
    FACE_NET = None

# If user provided VIT_DIR, try to load ViT full-image classifier for high accuracy
vit_processor, vit_model = None, None
if os.path.isdir(VIT_DIR) and os.listdir(VIT_DIR):
    try:
        vit_processor = AutoImageProcessor.from_pretrained(VIT_DIR)
        vit_model = AutoModelForImageClassification.from_pretrained(VIT_DIR)
        vit_model.to(DEVICE).eval()
    except Exception as e:
        st.warning(f"Failed to load ViT from {VIT_DIR}: {e}")
        vit_processor, vit_model = None, None

# -------------------------
# Small detector helpers
# -------------------------
def clip_vote_image(pil_img: Image.Image) -> str:
    """CLIP multi-prompt decision for one image (AI-generated or Human-made)."""
    try:
        inputs = clip_processor(images=pil_img, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            img_feats = clip_model.get_image_features(**inputs)
        img_feats = img_feats / img_feats.norm(p=2, dim=-1, keepdim=True)
        logits = img_feats @ TEXT_FEATS.T  # [1, num_texts]
        logits = logits.squeeze(0).cpu()
        ai_score = logits[:N_AI].mean().item()
        hm_score = logits[N_AI:N_AI+N_HUM].mean().item()
        return "AI-generated" if ai_score >= hm_score else "Human-made"
    except Exception:
        return "Human-made"

def deepfake_classifier_predict(pil_img: Image.Image) -> str | None:
    """Return prediction from df_model if loaded, else None."""
    if df_model is None or df_processor is None:
        return None
    try:
        inputs = df_processor(images=pil_img, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            out = df_model(**inputs)
            logits = out.logits
            probs = F.softmax(logits, dim=-1)[0]
            pred = int(torch.argmax(probs).item())
            if df_id2label:
                label = df_id2label.get(pred) or df_id2label.get(str(pred)) or ""
                label_lower = label.lower()
                if "fake" in label_lower or "deep" in label_lower or "ai" in label_lower:
                    return "AI-generated"
                else:
                    return "Human-made"
            return "AI-generated" if pred == 0 else "Human-made"
    except Exception:
        return None

def frame_model_predict(pil_img: Image.Image) -> str | None:
    """Return frame-level classifier prediction if available."""
    if frame_model is None or frame_transform is None:
        return None
    try:
        x = frame_transform(pil_img).unsqueeze(0).to(DEVICE)
        with torch.no_grad():
            logits = frame_model(x)
            pred = int(torch.argmax(logits, dim=1).item())
            # mapping depends on training. default assume 0 => fake/AI, 1 => real
            return "AI-generated" if pred == 0 else "Human-made"
    except Exception:
        return None

def vit_predict(pil_img: Image.Image) -> str | None:
    if vit_model is None or vit_processor is None:
        return None
    try:
        inputs = vit_processor(images=pil_img, return_tensors="pt").to(DEVICE)
        with torch.no_grad():
            out = vit_model(**inputs)
        pred = int(torch.argmax(out.logits, dim=-1).cpu().item())
        return "AI-generated" if pred == 0 else "Human-made"
    except Exception:
        return None

def detect_faces_and_crops(pil_img: Image.Image, min_conf=0.5):
    """Return list of PIL face crops (may be empty)."""
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

# Ensemble logic for a single PIL image
def ensemble_decision_for_image(pil_img: Image.Image):
    votes = {"AI-generated": 0.0, "Human-made": 0.0}

    # EXIF camera check (strong human signal)
    try:
        if exif_has_camera(pil_img):
            votes["Human-made"] += 4.0
    except Exception:
        pass

    # deepfake classifier full image
    df_full = deepfake_classifier_predict(pil_img)
    if df_full == "AI-generated":
        votes["AI-generated"] += 3.0
    elif df_full == "Human-made":
        votes["Human-made"] += 3.0

    # frame model full image
    fm_full = frame_model_predict(pil_img)
    if fm_full == "AI-generated":
        votes["AI-generated"] += 1.5
    elif fm_full == "Human-made":
        votes["Human-made"] += 1.5

    # vit full image
    vit_full = vit_predict(pil_img)
    if vit_full == "AI-generated":
        votes["AI-generated"] += 1.5
    elif vit_full == "Human-made":
        votes["Human-made"] += 1.5

    # CLIP full image
    try:
        clip_full = clip_vote_image(pil_img)
        votes[clip_full] += 1.0
    except Exception:
        pass

    # face crops
    try:
        crops = detect_faces_and_crops(pil_img)
    except Exception:
        crops = []
    for crop in crops:
        df_c = deepfake_classifier_predict(crop)
        if df_c == "AI-generated":
            votes["AI-generated"] += 2.0
        elif df_c == "Human-made":
            votes["Human-made"] += 2.0
        fm_c = frame_model_predict(crop)
        if fm_c == "AI-generated":
            votes["AI-generated"] += 1.0
        elif fm_c == "Human-made":
            votes["Human-made"] += 1.0
        try:
            clip_c = clip_vote_image(crop)
            votes[clip_c] += 0.5
        except Exception:
            pass

    # tie-breaker: if equal, use CLIP full image
    if abs(votes["AI-generated"] - votes["Human-made"]) < 1e-6:
        try:
            return clip_vote_image(pil_img)
        except Exception:
            return "Human-made"
    return "AI-generated" if votes["AI-generated"] > votes["Human-made"] else "Human-made"

# Video helpers
def sample_frames_from_video(path, n_frames=16):
    """Return list of PIL images sampled from video (MoviePy preferred, OpenCV fallback)."""
    frames = []
    try:
        # MoviePy path
        clip = VideoFileClip(path)
        total = max(1, int(clip.fps * clip.duration))
        indices = np.linspace(0, max(0, total - 1), num=min(n_frames, total)).astype(int)
        for idx in indices:
            t = float(idx) / clip.fps
            frame = clip.get_frame(t)
            frames.append(Image.fromarray(frame))
        clip.close()
        return frames
    except Exception:
        # fallback to OpenCV sampling
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            return []
        total = int(cap.get(cv2.CAP_PROP_FRAME_COUNT)) or 0
        if total <= 0:
            cap.release()
            return []
        indices = np.linspace(0, max(0, total - 1), num=min(n_frames, total)).astype(int)
        for idx in indices:
            cap.set(cv2.CAP_PROP_POS_FRAMES, int(idx))
            ok, frame = cap.read()
            if not ok:
                continue
            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            frames.append(Image.fromarray(frame_rgb))
        cap.release()
        return frames

def ensemble_decision_for_video(path, n_sample_frames=16):
    frames = sample_frames_from_video(path, n_frames=n_sample_frames)
    if not frames:
        return None
    votes = {"AI-generated": 0, "Human-made": 0}
    for f in frames:
        d = ensemble_decision_for_image(f)
        votes[d] += 1
    return "AI-generated" if votes["AI-generated"] >= votes["Human-made"] else "Human-made"

# Helpers: get resolution dims for image/video
def get_image_dims_from_path(path):
    try:
        with Image.open(path) as img:
            w,h = img.size
            return w,h
    except Exception:
        return None,None

def get_video_dims(path):
    try:
        cap = cv2.VideoCapture(path)
        if not cap.isOpened():
            return None,None
        w = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
        h = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
        cap.release()
        return w,h
    except Exception:
        return None,None

# Download to temp helper
def download_to_temp(url: str, timeout=240):
    r = requests.get(url, stream=True, timeout=timeout)
    r.raise_for_status()
    suffix = os.path.splitext(urlparse(url).path)[1] or ""
    tmp = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
    for chunk in r.iter_content(chunk_size=1024*1024):
        if chunk:
            tmp.write(chunk)
    tmp.flush(); tmp.close()
    return tmp.name

# -------------------------
# UI Tabs: Upload / URL
# -------------------------
tabs = st.tabs(["📁 Upload", "🌐 URL"])

with tabs[0]:
    st.header("Upload an image or a video (any extension)")
    uploaded = st.file_uploader("Drop file here (images/videos). No type filter — the app will detect.", type=None)
    if uploaded:
        # write to temp file
        suffix = os.path.splitext(uploaded.name)[1] or ""
        tmpf = tempfile.NamedTemporaryFile(delete=False, suffix=suffix)
        tmpf.write(uploaded.read()); tmpf.flush(); tmpf.close()
        path = tmpf.name

        # Try to open as image
        is_image = False
        try:
            with Image.open(path) as _:
                is_image = True
        except Exception:
            is_image = False

        if is_image:
            try:
                pil = Image.open(path).convert("RGB")
                w,h = pil.size
                decision = ensemble_decision_for_image(pil)
                st.image(pil, caption=f"Uploaded Image — {w}×{h}px", use_column_width=True)
                st.success(f"Origin: **{decision}**")
                st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
            except Exception as e:
                st.error(f"Failed to analyze uploaded image: {e}")
        else:
            # treat as video
            try:
                st.video(path)
                decision = ensemble_decision_for_video(path, n_sample_frames=16)
                w,h = get_video_dims(path)
                if decision is None:
                    st.error("Could not read video frames for analysis.")
                else:
                    st.success(f"Origin: **{decision}**")
                    if w and h:
                        st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
            except Exception as e:
                st.error(f"Failed to analyze uploaded video: {e}")

with tabs[1]:
    st.header("Paste an image or video URL (direct link)")
    url = st.text_input("Enter a direct URL to an image or video (e.g. https://.../file.png or https://.../file.mp4)")
    if st.button("Analyze URL"):
        if not url:
            st.error("Please paste a URL to analyze.")
        else:
            tmp_path = None
            try:
                tmp_path = download_to_temp(url)
                # try image
                try:
                    pil = Image.open(tmp_path).convert("RGB")
                    w,h = pil.size
                    decision = ensemble_decision_for_image(pil)
                    st.image(pil, caption=f"URL Image — {w}×{h}px", use_column_width=True)
                    st.success(f"Origin: **{decision}**")
                    st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
                except UnidentifiedImageError:
                    # treat as video
                    st.video(tmp_path)
                    decision = ensemble_decision_for_video(tmp_path, n_sample_frames=16)
                    w,h = get_video_dims(tmp_path)
                    if decision is None:
                        st.error("Could not read video frames for analysis.")
                    else:
                        st.success(f"Origin: **{decision}**")
                        if w and h:
                            st.write(f"Width: **{w}px** — Height: **{h}px** — Resolution: **{w}×{h}**")
            except requests.RequestException as e:
                st.error(f"Network error while downloading media: {e}")
            except Exception as e:
                st.error(f"Failed to analyze URL: {e}")
            finally:
                # optionally remove temp file
                try:
                    if tmp_path and os.path.exists(tmp_path):
                        os.remove(tmp_path)
                except Exception:
                    pass

# Footer disclaimer
st.markdown("---")
st.markdown(
    "<div class='neon-card'>"
    "<b>Note</b>: This app uses an ensemble (CLIP + optional deepfake classifiers + per-frame models + face-crop checks + EXIF). "
    "It maximizes practical detection performance, but no automated system is perfectly accurate. For critical uses, combine "
    "this output with human review, provenance checks, and reverse-image search."
    "</div>", unsafe_allow_html=True)
