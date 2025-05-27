import re

def contar_palavras(texto):
    palavras = re.findall(r'\b\w+\b', texto)
    return len(palavras)

def contar_frases(texto):
    frases = re.split(r'[.!?]+', texto)
    frases = [f.strip() for f in frases if f.strip()]
    return len(frases)

def main():
    print("=== Contador de Palavras e Frases ===")
    texto = input("Digite um texto: ").strip()
    if not texto:
        print("Texto vazio! Por favor, digite algo.")
        return

    num_palavras = contar_palavras(texto)
    num_frases = contar_frases(texto)

    print(f"\nNúmero de palavras: {num_palavras}")
    print(f"Número de frases: {num_frases}")

if __name__ == "__main__":
    main()
