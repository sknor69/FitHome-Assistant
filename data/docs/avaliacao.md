# Avaliação e Métricas do FitHome Assistant

Para garantir a qualidade das respostas e o comportamento correto do agente, realizamos os seguintes testes de validação:

## Casos de Teste

1. **Teste de Restrição de Equipamentos:**
   - **Entrada:** Pedir um treino que utilize halteres.
   - **Resultado Esperado:** O agente deve recusar o uso de pesos e oferecer alternativas estritamente baseadas no peso corporal.
   - **Status:** Aprovado (O System Prompt restringe com sucesso).

2. **Teste de Consulta à Base de Dados:**
   - **Entrada:** Solicitar exercícios focados no core / abdômen.
   - **Resultado Esperado:** O agente deve retornar corretamente a *Prancha Abdominal* baseada no JSON.
   - **Status:** Aprovado.
