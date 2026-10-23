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
    print("🤖 Bem-vindo ao FitHome Assistant (Seu Treino em Casa) ")
    print("=" * 60)
    
    exercicios = carregar_base_dados()
    if not exercicios:
        return

    print("\n[Assistente]: Olá! Sou seu coach de calistenia. Como posso te ajudar hoje?")
    print("Digite 'listar' para ver os exercícios ou 'sair' para encerrar.")
    print("-" * 60)

    while True:
        pergunta = input("\nVocê: ").strip().lower()
        
        if pergunta == 'sair':
            print("\n[Assistente]: Bom treino! Continue focado e até a próxima! ")
            break
            
        elif 'listar' in pergunta or 'exercicio' in pergunta:
            print("\n[Assistente]: Aqui estão os exercícios disponíveis na minha base:")
            for ex in exercicios:
                print(f"  • {ex['nome']} ({ex['grupo_muscular']} - Nível: {ex['nivel']})")
                print(f"    -> Descrição: {ex['descricao']}")
                
        elif 'perna' in pergunta or 'gluteo' in pergunta:
            print("\n[Assistente]: Para pernas e glúteos, recomendo:")
            for ex in exercicios:
                if "Pernas" in ex['grupo_muscular'] or "Glúteos" in ex['grupo_muscular']:
                    print(f"  • {ex['nome']}: {ex['descricao']}")
                    
        elif 'abdomen' in pergunta or 'core' in pergunta:
            print("\n[Assistente]: Para o core e abdômen, recomendo:")
            for ex in exercicios:
                if "Core" in ex['grupo_muscular']:
                    print(f"  • {ex['nome']}: {ex['descricao']}")
                    
        else:
            print("\n[Assistente]: Desculpe, não entendi bem. Lembre-se que foco apenas em exercícios de peso corporal (calistenia). Tente perguntar sobre 'pernas', 'abdômen' ou digite 'listar'.")

if __name__ == "__main__":
    fit_home_assistant()
