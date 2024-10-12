set -m

python3 main.py &

streamlit run .\streamlit.py

fg %1
