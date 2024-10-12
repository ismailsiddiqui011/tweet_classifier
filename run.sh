set -m
rm /tweet_classifier/fine_tuned_t5/model.safetensors
wget https://media.githubusercontent.com/media/ismailsiddiqui011/tweet_classifier/refs/heads/main/fine_tuned_t5/model.safetensors /tweet_classifier/fine_tuned_t5/model.safetensors

python main.py &

streamlit run streamlit.py

fg %1
