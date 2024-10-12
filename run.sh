set -m

python main.py &

streamlit run .\streamlit.py

fg %1
