class FCFS():

    def __init__(self):
        self.processes = []
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

    def time_calculate(self):
        try:
            self.avg_wait = round(sum(i.count('    Г') for i in self.visual_representation)/len(self.processes),2)
            self.avg_all = round(sum(len(i) for i in self.visual_representation)/len(self.processes),2)
        except (ZeroDivisionError, AttributeError):
            self.avg_wait = 0
            self.avg_all = 0
    
    def __str__(self) -> str:
        self.time_calculate()
        return ('\n'.join([' '.join(i) for i in self.visual_representation])
                +f'\n avg_wait = {self.avg_wait}\n avg_all = {self.avg_all}'
                )

class RR(FCFS):
    
    def update_visual_representation(self):
        q = 1
        self.visual_representation = [[] for i in self.processes]
        process = self.processes.copy()
        while any(i!=0 for i in process):
            for i in range(len(process)):
                if process[i]>0:
                    if process[i]<=q:
                        self.visual_representation[i] += process[i]*['    И']
                        for j in list(range(0,i))+list(range(i+1,len(process))):
                            if process[j] != 0:
                                self.visual_representation[j] += process[i]*['    Г']
                        process[i] = 0
                    else:
                        self.visual_representation[i] += q*['    И']
                        for j in list(range(0,i))+list(range(i+1,len(process))):
                            if process[j] != 0:
                                self.visual_representation[j] += q*['    Г']
                        process[i]-=q
    
    def time_calculate(self):
        try:
            self.T = round(sum(len(i) for i in self.visual_representation)/len(self.processes),2)
            self.M = round(sum(i.count('    Г') for i in self.visual_representation)/len(self.processes),2)
            self.R = round(sum(i.count('    И') for i in self.visual_representation)/sum(len(i) for i in self.visual_representation),2)
            self.P = round((self.T*len(self.processes))/sum(i.count('    И') for i in self.visual_representation),2)
        except (ZeroDivisionError, AttributeError):
            self.T = 0
            self.M = 0
            self.R = 0
            self.P = 0
    def __str__(self) -> str:
        self.time_calculate()
        return ('\n'.join([' '.join(i) for i in self.visual_representation])
                # +f'\n avg_wait = {self.avg_wait}\n avg_all = {self.avg_all}'
                +f'\n T = {self.T}\n M = {self.M}\n R = {self.R}\n P = {self.P}'
                )

class SJF(RR):
    def update_visual_representation(self):
        process = self.processes.copy()
        self.visual_representation = [[] for i in self.processes]
        for i in range(len(process)):
            i = process.index(min(process))
            self.visual_representation[i] += process[i]*['    И']
            for j in list(range(0,i))+list(range(i+1,len(process))):
                            if process[j] != 999:
                                self.visual_representation[j] += process[i]*['    Г']
            process[i] = 999

class PSJF_PSJF(SJF):
    pass

class RR_SJF(RR):

    def update_visual_representation(self):
        q = 1
        self.visual_representation = [[] for i in self.processes]
        process = sorted(self.processes.copy())
        while any(i!=0 for i in process):
            for i in range(len(process)):
                if process[i]>0:
                    if process[i]<=q:
                        self.visual_representation[i] += process[i]*['    И']
                        for j in list(range(0,i))+list(range(i+1,len(process))):
                            if process[j] != 0:
                                self.visual_representation[j] += process[i]*['    Г']
                        process[i] = 0
                    else:
                        self.visual_representation[i] += q*['    И']
                        for j in list(range(0,i))+list(range(i+1,len(process))):
                            if process[j] != 0:
                                self.visual_representation[j] += q*['    Г']
                        process[i]-=q
        vr = [[] for i in self.processes]
        used = []
        for i in range(len(self.processes)):
            for j in range(len(self.visual_representation)):
                if (self.visual_representation[i].count('    И') == self.processes[j]) and j not in used:
                    vr[i] = self.visual_representation[j]
                    used.append(j)
                    break
                    
                    
        self.visual_representation = vr
