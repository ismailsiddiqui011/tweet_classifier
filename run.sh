set -m

python main.py &

python -m streamlit run .\streamlit.py

fg %1
