import threading
def escrever_texto(texto,quantidade): #escreve o texto a quantidade de vezes que foi passado
    for i in range(quantidade):
        print(texto)

def criar_thread(texto, quantidade): #cria a thread para escrever o texto que  foi passado logo em cima
    thread = threading.Thread(target=escrever_texto, args=(texto,quantidade))
    thread.start()
    return thread

def main():
    thread1 = criar_thread("Thread 01", 10)
    thread2 = criar_thread("Thread 02", 10)

if __name__ == "__main__":
    main()
