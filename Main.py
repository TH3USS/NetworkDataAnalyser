import requests
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# Configurar o Access Token e a URL base da API
ACCESS_TOKEN = "SEU_ACCESS_TOKEN_AQUI"
BASE_URL = "https://graph.instagram.com"

# Função para obter dados de posts
def get_instagram_posts(user_id="me", fields="id,caption,media_type,like_count,comments_count", limit=10):
    url = f"{BASE_URL}/{user_id}/media?fields={fields}&access_token={ACCESS_TOKEN}&limit={limit}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("data", [])
    else:
        print("Erro na requisição:", response.status_code, response.text)
        return []

# Função para extrair hashtags de captions
def extract_hashtags(captions):
    hashtags = []
    for caption in captions:
        if caption:
            hashtags.extend([word for word in caption.split() if word.startswith("#")])
    return hashtags

# Função para plotar gráfico das hashtags mais frequentes
def plot_hashtag_frequency(hashtags):
    counter = Counter(hashtags)
    most_common = counter.most_common(10)

    hashtags, counts = zip(*most_common)

    plt.figure(figsize=(10, 6))
    plt.barh(hashtags, counts, color='skyblue')
    plt.xlabel("Frequência")
    plt.title("Top 10 Hashtags mais usadas")
    plt.gca().invert_yaxis()
    plt.show()

# Coletar posts e processar hashtags
if __name__ == "__main__":
    posts = get_instagram_posts()
    captions = [post.get("caption", "") for post in posts]

    hashtags = extract_hashtags(captions)
    if hashtags:
        print("Hashtags encontradas:", hashtags)
        plot_hashtag_frequency(hashtags)
    else:
        print("Nenhuma hashtag encontrada.")
