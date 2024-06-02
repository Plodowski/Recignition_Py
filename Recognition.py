import cv2
from deepface import DeepFace
import tkinter as tk
from tkinter import messagebox

def face(pessoa):
    imagem = cv2.imread(f"/Users/gabrielmenezes/Desktop/Recignition_Py/DB_FOTOS/" + pessoa + "/FOTO.jpeg")
    if imagem is None:
        root = tk.Tk()
        root.withdraw()
        messagebox.showerror("Erro", f"Não foi possível encontrar a pessoa: {pessoa} na base de dados")
        root.destroy()
    else:
        resultado = DeepFace.analyze(imagem, actions=["age", "emotion", "race"])
        idade = resultado[0]["age"]
        raca = resultado[0]["dominant_race"]
        emocao = resultado[0]["dominant_emotion"]
        window = tk.Tk()
        window.title("Resultado do Face Recognition")
        results_text = f"Nome: {pessoa}\nIdade: {idade}\nRaça: {raca}\nEmoção: {emocao}"
        label = tk.Label(window, text=results_text, padx=20, pady=20)
        label.pack()
        window.mainloop()

pessoa = input("Digite o nome da pessoa:")
face(pessoa)
