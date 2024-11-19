Este repositório contém uma implementação básica de uma **rede de Hopfield**, um tipo de rede neural recorrente usada como modelo associativo para armazenamento e recuperação de padrões. A rede de Hopfield é particularmente interessante devido ao seu funcionamento inspirado na física e na computação biológica.

---

### Atualização do Estado dos Neurônios
![Atualização do Estado dos Neurônios](https://latex.codecogs.com/png.image?\dpi{150}s_i(t)=\text{sgn}\left(\sum_{j=1}^n\!w_{ij}s_j-\theta_i\right))

Onde:  
- \( s_i(t) \): Estado do neurônio \(i\) no instante \(t\).  
- \( w_{ij} \): Peso da conexão entre os neurônios \(i\) e \(j\).  
- \( \theta_i \): Limiar do neurônio \(i\).  

---

### Regra de Hebb para Treinamento
![Regra de Hebb](https://latex.codecogs.com/png.image?\dpi{150}w_{ij}=\frac{1}{p}\sum_{\mu=1}^p\!s_i^\mu\cdot\!s_j^\mu)

Onde:  
- \( p \): Número de padrões armazenados.  
- \( s_i^\mu \): Estado do neurônio \(i\) no padrão \(\mu\).  

---

### Energia da Rede
A dinâmica da rede busca minimizar a seguinte função de energia:

![Energia da Rede](https://latex.codecogs.com/png.image?\dpi{150}E=-\frac{1}{2}\sum_{i=1}^n\sum_{j=1}^n\!w_{ij}s_is_j+\sum_{i=1}^n\!\theta_is_i)

Esta função assegura que a rede converge para mínimos locais, correspondendo a padrões armazenados.

---

## Implementações futuras

- **Inicialização da Rede**: Configuração de pesos e estados iniciais.
- **Treinamento com Regra de Hebb**: Aprendizado baseado em padrões binários.
- **Simulação da Dinâmica**: Atualização síncrona e assíncrona.
- **Visualização dos Resultados**: Padrões armazenados e recuperados.
- **Análise da Energia**: Monitoramento da convergência.

---
## 🚀 Pré-requisitos
Certifique-se de ter os seguintes programas instalados:
- Python 3.8+
- Bibliotecas: `numpy`

## 📚 Referências
Hopfield, J. J. (1982). Neural Networks and Physical Systems with Emergent Collective Computational Abilities. Proceedings of the National Academy of Sciences.
Hertz, J., Krogh, A., & Palmer, R. G. (1991). Introduction to the Theory of Neural Computation.
