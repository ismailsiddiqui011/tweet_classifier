import streamlit as st
import requests
import json

url = "http://localhost:1411/tweet_clf"

headers = {
  'Content-Type': 'application/json',
  'Authorization': 'Bearer eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJfaWQiOiI2NTMxMTBkOGY0MjQ2NTFkMzFhOWM5ZjUiLCJlbWFpbCI6ImtzNzA4NTcwQGdtYWlsLmNvbSIsInBsYXRmb3JtIjoiV0VCIiwidXNlclR5cGUiOiJVTkxJTUlURUQiLCJwYWNrYWdlSWQiOiJQQUNLQUdFX0lEX1BIT1RfQUlfV0VCIiwiaWF0IjoxNzIxOTc0MjQwfQ.Nx8W3WV43i7YwD9ZtQKWZrRuesCICapAdf9L5sKKLLgDdNZczOdGVy5ujIHQzv_gnyMdmFVlX5TGkegGvYo664Ztqqc4B2T4hETSXTT-XJKkmQ5G0LCbM9ZNGEu03-tkdIeg6QoU5mw9F8qazvEdh1P2xYZl846Yp7KiP8UCyvHwhE_kcnuTQ7XDrpcu4tjyBzUSeov-si2s2zeHQ0G_ADcAuOsSCdtsnsjqCbGWhfVDEAWOMyVrbpcXZ3636r9JNbt6GsVDvf3-_pxzrmwyGhjVM-kG8Bui2S9JarUzD8gIYNjJn30GfPJzIcqHWdRFfYPRIDLYPdzu2M0xbX2K8w'
}

st.title('Tweet Classifier')
st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQejMAWRzRClrWFA8hZbje7x3ErUgJs-YEf3gB328187vSlMbAJbrQGiAMTxEOjQwykXXA&usqp=CAU', width = 300)

try:
    tweet = st.text_input('Enter tweet...')

    payload = json.dumps({"input_tweet": tweet})

    response = requests.request("POST", url, headers=headers, data=payload)

    response = json.loads(response.text)

    st.markdown(f"Emotion: {response['emotion']}")
    st.markdown(f"Product: {response['product']}")
except:
  pass