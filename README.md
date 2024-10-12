# Assignment
## sigma.ipynb: Contains preprocessing, EDA and model training
## Model:
- I have use T5 for fine-tuning.
- Alternate approach: Use embeddings of BERT with any classification ML model.

## Deployment:
### Approach 1: FASTAPI + Docker
  
### Apprach 2: Used FASTAPI + Streamlit (to get basic UI) I have deployed this on RunPod 

UI Url : http://213.173.105.86:47705/

Note: You can also use FASTAPI by using below code and docs:

Docs: http://213.173.105.86:47704/redoc

```python 
import requests
import json

url = "http://213.173.105.86:47704/tweet_clf"

payload = json.dumps({
  "input_tweet": "this sony tv is very bad"
})
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)

```

```console
curl --location 'http://213.173.105.86:47704/tweet_clf' \
--header 'Content-Type: application/json' \
--data '{"input_tweet" : "this sony tv is very bad"}'```
