set -m
wget https://media.githubusercontent.com/media/ismailsiddiqui011/tweet_classifier/refs/heads/main/fine_tuned_t5/model.safetensors fine_tuned_t5/model.safetensors

python main.py &

streamlit run .\streamlit.py

fg %1
