import json
import uuid
import random

# Listas de palavras para gerar combinações aleatórias realistas
adjetivos = ["Ergonômica", "Industrial", "Premium", "Nórdica", "Modular", "Vintage", "Minimalista", "Rústica", "Contemporânea", "Inteligente"]
substantivos = ["Cadeira", "Mesa", "Sofá", "Luminária", "Estante", "Poltrona", "Tapete", "Quadro", "Espelho", "Escrivaninha"]
categorias = ["Móveis", "Decoração", "Iluminação", "Escritório", "Jardim"]

produtos = []

# Gerar 10.000 produtos
for i in range(10000):
    titulo = f"{random.choice(substantivos)} {random.choice(adjetivos)} {random.randint(100, 999)}"
    
    produto = {
        "id": str(uuid.uuid4()),
        "title": titulo,
        "description": f"Este é um produto incrível da categoria {random.choice(categorias)}. Possui design {random.choice(adjetivos).lower()} e acabamento de alta qualidade. Perfeito para qualquer ambiente.",
        "price": round(random.uniform(50.0, 5000.0), 2), # Preço aleatório entre 50 e 5000
        "category": random.choice(categorias),
        "rating": round(random.uniform(3.0, 5.0), 1),    # Avaliação entre 3.0 e 5.0
        "inStock": random.choice([True, True, True, False]), # 75% de probabilidade de estar em stock
        "imageUrl": f"https://picsum.photos/seed/prod{i}/500/500" # Imagem única baseada no índice
    }
    produtos.append(produto)

# Guardar no ficheiro
with open("produtos_estresse.json", "w", encoding="utf-8") as f:
    json.dump(produtos, f, ensure_ascii=False, indent=2)

print(f"Ficheiro 'produtos_estresse.json' gerado com sucesso com {len(produtos)} itens!")