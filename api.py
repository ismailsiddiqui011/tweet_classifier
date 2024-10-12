import warnings
warnings.filterwarnings('ignore')
import time, traceback, json
from pydantic import BaseModel
from fastapi import FastAPI, Response
from utils import predict, remove_stopwords
app = FastAPI()

class Input(BaseModel):
    input_tweet: str

@app.post("/tweet_clf")
def generator(input: Input):
    try:
        tot = time.time()
        tweet = input.input_tweet
        tweet = remove_stopwords(tweet)
        emotion, product = predict(tweet)
        result = {'emotion' : emotion, 'product' : product}
            
        print('Total Time: ', time.time()-tot)
        print('---'*15)
        
        return Response(content=json.dumps(result, default=str), headers={"Content-Type": "application/json"}, status_code=200)
    except:
        response_ = f'Internal Server Error: \n {traceback.format_exc()}'
        print(response_)
        response_ = {'message' : response_}
        return Response(content=json.dumps(response_, default=str), headers={"Content-Type": "application/json"}, status_code=500)