import re

def get_text_to_list_v3(content):
    # Utilisation de re.findall pour récupérer les mots et les signes spécifiques (., et ,)
    return re.findall(r'\w+|[.,]', content)

# Exemple d'utilisation
content = "Bonjour, voici un exemple. Testons ce code!"
print(get_text_to_list_v3(content))