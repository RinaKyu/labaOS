class FCFS():
    def __init__(self, processes=[]):
        self.processes = processes
        self.visual_representation = []
        self.update_visual_representation()

    def add_process(self, process):
        self.processes.append(process)
        self.update_visual_representation()
        
    def clean(self):
        self.processes = []
        self.update_visual_representation()
    
    def update_visual_representation(self):
        self.visual_representation = [[] for i in self.processes]

        for i in range(len(self.processes)):
            self.visual_representation[i] = len(self.visual_representation[i-1])*['    Г'] + self.processes[i]*['    И']

    def __str__(self) -> str:
        return '\n'.join([' '.join(i) for i in self.visual_representation])

# if __name__ == '__main__':
    # a = FCFS()
    # a.add_process(13)
    # a.add_process(4)
    # a.add_process(1)
    # print(a)
a = FCFS()
a.add_process(13)
a.add_process(4)
a.add_process(1)
print(a)