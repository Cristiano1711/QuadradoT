# 🟦 Quadrado T – Fractal Recursivo com Turtle Graphics

**Geração visual de um fractal do tipo Quadrado T utilizando recursividade em Python**

---

## 1. Resumo (Abstract)

Este projeto implementa a construção do fractal **Quadrado T** por meio de **recursividade**, utilizando a biblioteca gráfica **Turtle** da linguagem **Python**. A aplicação permite ao usuário definir dinamicamente o nível de profundidade do fractal e a cor dos quadrados, demonstrando conceitos fundamentais de computação gráfica, geometria e funções recursivas de forma visual e interativa.

## 2. Introdução

Fractais são estruturas geométricas caracterizadas por auto-similaridade, onde padrões se repetem em diferentes escalas. O **Quadrado T** é um exemplo clássico utilizado no ensino de algoritmos recursivos, pois combina simplicidade conceitual com forte apelo visual.

Este projeto tem como objetivo:
- Demonstrar o uso de **recursividade controlada por profundidade**
- Explorar **coordenadas cartesianas** no plano
- Aplicar conceitos básicos de **renderização gráfica**

## 3. Arquitetura do Programa

### 3.1 Configuração da Janela Gráfica

A aplicação inicializa uma janela gráfica com dimensões fixas, garantindo espaço suficiente para a renderização do fractal em níveis mais profundos.

- Resolução: 900 × 900
- Sistema de coordenadas centralizado
- Renderização instantânea (velocidade máxima)

### 3.2 Controle da Tartaruga (Turtle)

A tartaruga gráfica é configurada para:
- Alta performance (`speed(0)`)
- Desenho limpo (cursor oculto)
- Controle explícito de caneta (`penup` / `pendown`)

### 3.3 Funções Principais

#### Função `quadrado`
Responsável por desenhar um quadrado preenchido de determinado tamanho e cor a partir da posição atual da tartaruga.

#### Função `quadradoT`
Função **recursiva** que:
- Desenha um quadrado central
- Divide seu tamanho pela metade
- Gera quatro novos quadrados nos cantos (superior esquerdo, superior direito, inferior esquerdo e inferior direito)
- Interrompe a execução ao atingir o nível máximo definido pelo usuário

Essa abordagem garante crescimento exponencial controlado do fractal.

## 4. Metodologia de Implementação

A lógica recursiva segue o padrão:

1. Caso base: interromper quando `nivel > nivel_max`
2. Caso recursivo:
   - Desenhar o quadrado atual
   - Calcular novo tamanho
   - Chamar a função para os quatro cantos

Essa estratégia preserva a simetria do fractal e evita sobreposição incorreta dos elementos.

## 5. Especificações Técnicas

| Requisito | Tecnologia |
|---------|------------|
| **Linguagem** | Python 3 |
| **Biblioteca Gráfica** | Turtle Graphics |
| **Paradigma** | Programação Recursiva |
| **Entrada de Dados** | Terminal (stdin) |
| **Saída** | Janela Gráfica Interativa |

## 6. Como Executar o Projeto

### 6.1 Pré-requisitos

- Python 3 instalado
- Biblioteca Turtle (já inclusa na instalação padrão do Python)

### 6.2 Execução

No terminal, execute:

```bash
python QuadradoT.py
```

### 6.3 Interação

Durante a execução, o programa solicitará:
1. O **nível do fractal** (quanto maior, mais detalhado)
2. A **cor do quadrado** (em inglês, ex: `blue`, `red`, `green`)

## 7. Aplicações Educacionais

Este projeto é especialmente indicado para:
- Ensino de recursividade
- Introdução à computação gráfica
- Visualização de algoritmos
- Projetos acadêmicos e portfólio iniciante/intermediário

## 8. Conclusão

O projeto **Quadrado T** demonstra como conceitos matemáticos e computacionais podem ser integrados para criar visualizações elegantes e didáticas. A simplicidade do código aliada ao impacto visual do fractal torna este projeto uma excelente peça para repositórios educacionais e portfólios de programação.

---

**Autor:** [Seu Nome]  
**Instituição:** Universidade Federal do Amazonas (UFAM)  
**Disciplina:** Computação Gráfica / Programação 
