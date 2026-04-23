import os
import threading
import subprocess
import json
import customtkinter as ctk
from tkinter import filedialog, messagebox

CONFIG_FILE = "config.json"

# --- Config ---
APP_NAME = "NWS DIVISOR"
ctk.set_appearance_mode("Dark")  # Modos: "Dark", "Light", "System"
ctk.set_default_color_theme("blue")  # Temas: "blue", "green", "dark-blue"

def carregar_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    return {"ultima_entrada": "", "ultima_saida": ""}

def salvar_config():
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f)

config = carregar_config()

# --- Funções ---
def log(msg):
    texto_log.configure(state="normal")
    texto_log.insert(ctk.END, msg + "\n")
    texto_log.see(ctk.END)
    texto_log.configure(state="disabled")

def separar_arquivo(arquivo, stems, pasta_saida):
    comando = f'py -3.10 -m spleeter separate -p spleeter:{stems}stems -o "{pasta_saida}" "{arquivo}"'
    subprocess.run(comando, shell=True)

def escolher_arquivo():
    arquivo = filedialog.askopenfilename(
        initialdir=config["ultima_entrada"],
        filetypes=[("Audio", "*.mp3 *.wav")]
    )
    if arquivo:
        config["ultima_entrada"] = os.path.dirname(arquivo)
        salvar_config()
        threading.Thread(target=processar_arquivo, args=(arquivo,)).start()

def escolher_pasta():
    pasta = filedialog.askdirectory(initialdir=config["ultima_entrada"])
    if pasta:
        config["ultima_entrada"] = pasta
        salvar_config()
        threading.Thread(target=processar_pasta, args=(pasta,)).start()

def escolher_saida():
    pasta = filedialog.askdirectory(initialdir=config["ultima_saida"])
    if pasta:
        config["ultima_saida"] = pasta
        salvar_config()
        label_saida.configure(text=f"Saída: {pasta}")

def processar_arquivo(arquivo):
    iniciar_processo()
    stems = combo_stems.get()[0]
    pasta_saida = config["ultima_saida"] or os.path.dirname(arquivo)

    progresso.set(0)
    log(f"Separando: {os.path.basename(arquivo)}")
    separar_arquivo(arquivo, stems, pasta_saida)
    progresso.set(1)

    finalizar_processo(pasta_saida)

def processar_pasta(pasta):
    iniciar_processo()
    stems = combo_stems.get()[0]
    pasta_saida = config["ultima_saida"] or pasta

    arquivos = [f for f in os.listdir(pasta) if f.endswith(".mp3") or f.endswith(".wav")]
    progresso.set(0)
    progresso.configure(maximum=len(arquivos))

    for i, arquivo in enumerate(arquivos):
        caminho = os.path.join(pasta, arquivo)
        log(f"Separando ({i+1}/{len(arquivos)}): {arquivo}")
        separar_arquivo(caminho, stems, pasta_saida)
        progresso.set(i+1)

    finalizar_processo(pasta_saida)

def iniciar_processo():
    btn_arquivo.configure(state="disabled")
    btn_pasta.configure(state="disabled")
    btn_saida.configure(state="disabled")
    status_var.set("Processando...")

def finalizar_processo(pasta_saida):
    status_var.set("Concluído")
    log(f"\nArquivos salvos em: {pasta_saida}\n")
    btn_arquivo.configure(state="normal")
    btn_pasta.configure(state="normal")
    btn_saida.configure(state="normal")
    if messagebox.askyesno("Abrir pasta", "Deseja abrir a pasta de saída?"):
        os.startfile(pasta_saida)

# --- Interface ---
janela = ctk.CTk()
janela.title(APP_NAME)
janela.geometry("700x500")
try:
    janela.iconbitmap("icon.ico")
except:
    pass

frame_topo = ctk.CTkFrame(janela, corner_radius=10)
frame_topo.pack(pady=10, padx=10, fill="x")

ctk.CTkLabel(frame_topo, text=APP_NAME, font=ctk.CTkFont(size=20, weight="bold")).pack(pady=5)

combo_stems = ctk.CTkOptionMenu(frame_topo, values=["2 stems", "4 stems", "5 stems"])
combo_stems.set("5 stems")
combo_stems.pack(pady=5)

frame_botoes = ctk.CTkFrame(janela, corner_radius=10)
frame_botoes.pack(pady=10, padx=10, fill="x")

btn_arquivo = ctk.CTkButton(frame_botoes, text="Escolher Música", command=escolher_arquivo)
btn_arquivo.pack(pady=5, padx=20, fill="x")

btn_pasta = ctk.CTkButton(frame_botoes, text="Escolher Pasta (Lote)", command=escolher_pasta)
btn_pasta.pack(pady=5, padx=20, fill="x")

btn_saida = ctk.CTkButton(frame_botoes, text="Escolher Pasta de Saída", command=escolher_saida)
btn_saida.pack(pady=5, padx=20, fill="x")

label_saida = ctk.CTkLabel(janela, text=f"Saída: {config['ultima_saida']}")
label_saida.pack(pady=5)

progresso = ctk.CTkProgressBar(janela, width=650)
progresso.pack(pady=10)

status_var = ctk.StringVar(value="Aguardando...")
label_status = ctk.CTkLabel(janela, textvariable=status_var)
label_status.pack(pady=5)

texto_log = ctk.CTkTextbox(janela, height=15)
texto_log.pack(padx=10, pady=10, fill="both", expand=True)
texto_log.configure(state="disabled")

janela.mainloop()