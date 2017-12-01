import subprocess

'''proc = subprocess.Popen(['hostname'], stdout=subprocess.PIPE)
(out, err) = proc.communicate()
containers = str(out)'''

comando = str(input('>>>: ')).lower().strip().split()

if 'status' in comando:
    subprocess.call(comando[1])
