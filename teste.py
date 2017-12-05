from docker import from_env

client = from_env()
loop = 1


while loop != 0:
    comando = input('>>> ').lower().strip().split()
    container = client.containers.get(comando[1])

    def start():
        if 'start' in comando:
            if '-t' in comando[1]:
                container1 = client.containers.get(comando[3])
                container1.start()
                container1.stop(timeout=int(comando[2]))
            else:
                container.start()

    def stop():
        if 'stop' in comando:
            container.stop()

    def status():
        if 'status' in comando:
            container.status()

    def executar():
        if 'exec' in comando:
            container.exec_run(cmd=str, stdout=True, stderr=True)
     
    def fechar():
        if comando == 'exit':
            exit()

    if comando is not None:
        start(), status(), stop(), fechar(), executar()
