set -m

python3.11 main.py &

python3.11 -m streamlit run .\streamlit.py

fg %1
