# Full duplex Communication
from subprocess import Popen, STDOUT, PIPE
from threading import Thread


class ProcessOutputThread(Thread):
    def __init__(self,p):
        Thread.__init__(self)
        self.p = p
    def run(self):
        while self.p.poll() is None:
            print(self.p.stdout.readline().decode().strip())
            
p = Popen(['bc'], stdout=PIPE, stderr=STDOUT, stdin=PIPE)
out_t = ProcessOutputThread(p)
out_t.start()
while p.poll() is None:
    inp = input("")
    inp = inp + "\n"
    p.stdin.write(inp.encode())
    p.stdin.flush()