# 🎧 NWS Divisor V2

Ferramenta em Python para separação de áudio em múltiplos stems utilizando modelos de machine learning, com foco em simplicidade, praticidade e desempenho.

---

## 🚀 Visão Geral

O **NWS Divisor V2** permite dividir arquivos de áudio em diferentes componentes (stems), como:

* 🎤 Vocais
* 🎸 Instrumental
* 🥁 Bateria
* 🎹 Outros elementos

Tudo isso de forma automatizada utilizando o **Spleeter**.

---

## ⚡ Formas de Uso

Você pode usar o projeto de duas maneiras:

### 🧑‍💻 1. Via Python (recomendado para desenvolvedores)

### 🖥️ 2. Via Executável (.exe)

👉 Para quem não quer instalar nada

---

## 📦 Pré-requisitos (modo Python)

* Python 3.8 ou superior
* pip

---

## ⚙️ Instalação

Clone o repositório do GitHub:

```bash
git clone https://github.com/alexanderoliveira94/DivisorNwsv2.git
cd DivisorNwsv2
```

Crie um ambiente virtual (opcional, mas recomendado):

```bash
python -m venv venv

# Windows
venv\Scripts\activate

# Linux/Mac
source venv/bin/activate
```

Instale as dependências:

```bash
pip install -r requirements.txt
```

---

## ▶️ Como Executar

```bash
python main.py
```

---

## 🧠 Modelos de Machine Learning

Os modelos são gerenciados automaticamente pelo Spleeter.

📥 **Na primeira execução**, os modelos serão baixados automaticamente.

✔️ Você não precisa baixar nada manualmente
✔️ Não é necessário manter arquivos grandes no projeto

---

## 🎵 Como Usar

1. Abra o sistema
2. Escolha uma música ou uma pasta
3. Selecione o número de stems:

   * 2 stems
   * 4 stems
   * 5 stems
4. Escolha a pasta de saída (opcional)
5. Aguarde o processamento

📁 Os arquivos serão salvos automaticamente na pasta de saída.

---

## 📁 Estrutura do Projeto

```
DivisorNwsv2/
│
├── src/                        # Código fonte
├── input/                      # (Opcional) arquivos de entrada
├── output/                     # Resultados gerados
├── requirements.txt            # Dependências
├── main.py                     # Aplicação principal
└── README.md
```

---

## 🖥️ Executável (.exe)

Se você não deseja instalar Python ou dependências:

👉 Baixe o executável na aba **Releases** do repositório.

✔️ Basta baixar e executar
✔️ Não requer instalação

---

## ⚠️ Observações

* O primeiro processamento pode demorar mais (download dos modelos)
* O tempo de execução depende do tamanho do áudio e do hardware
* Arquivos grandes podem levar mais tempo para processamento

---

## 🛠️ Tecnologias Utilizadas

* Python
* Spleeter
* CustomTkinter (interface gráfica)

---

## 🤝 Contribuição

Contribuições são bem-vindas!

Sinta-se à vontade para:

* abrir uma issue
* sugerir melhorias
* enviar pull requests

---

## 📄 Licença

Este projeto pode ser utilizado livremente para fins de estudo e desenvolvimento.
