set -m
rm fine_tuned_t5/model.safetensors
wget https://oshi.at/JgoC/model.safetensors fine_tuned_t5/model.safetensors

python main.py &

streamlit run streamlit.py

fg %1
