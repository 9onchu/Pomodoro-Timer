import streamlit as st
import time

'Starting a long computation...'

# Add a placeholder
latest_iteration = st.empty() #空のコンテナを用意（これにより、同じ場所の文字を置き換えることができる

bar = st.progress(0) #プログレスバーを作成（初期値は０％）

for i in range(100):
  # Update the progress bar with each iteration.
  latest_iteration.text(f'Iteration {i+1}')
  bar.progress(i + 1)
  time.sleep(0.1)

'...and now we\'re done!'