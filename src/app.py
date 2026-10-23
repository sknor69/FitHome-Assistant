import json
import os

def carregar_base_dados():
    caminho = os.path.join(os.path.dirname(__file__), '../data/exercicios.json')
    try:
        with open(caminho, 'r', encoding='utf-8') as f:
            return json.load(f)
    except FileNotFoundError:
        print("Erro: Base de dados de exercícios não encontrada.")
        return []

def fit_home_assistant():
    print("=" * 60)
    print("🤖 Bem-vindo ao FitHome Assistant (Seu Treino em Casa) 🏡💪")
    print("=" * 60)
    
    exercicios = carregar_base_dados()
    if not exercicios:
        return

    print("\n[Assistente]: Olá! Estou pronto para te ajudar a treinar em casa sem equipamentos.")
    print("Aqui estão algumas opções disponíveis na minha base de conhecimento:")
    
    for ex in exercicios:
        print(f"- {ex['nome']} ({ex['grupo_muscular']} | Nível: {ex['nivel']})")
    
    print("\n💡 Dica: Para o seu desafio da DIO, este script demonstra a integração bem-sucedida entre a base de dados JSON e a lógica em Python!")
    print("=" * 60)

if __name__ == "__main__":
    fit_home_assistant()
