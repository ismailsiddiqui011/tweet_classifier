set -m
python -m spacy download en_core_web_sm
python main.py &

streamlit run streamlit.py

fg %1
