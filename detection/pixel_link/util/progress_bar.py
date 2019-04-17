"""
# code from http://python.jobbole.com/83692/
"""
import sys, time

class ProgressBar:
    def __init__(self, total = 0, width = None, finish_symbol = '#',  init_symbol = '-', max_width = 100):
        self.count = 0
        self.total = total
        self.finish_symbol = finish_symbol
        self.init_symbol = init_symbol
        
        if width is not None:
            self.width = width
        else:
            self.width = total
            
        self.width = min(self.width, max_width)
            
        
    def move(self, count = 1, msg = ""):
        self.count += count
        sys.stdout.write(' ' * (self.width + 9) + '\r')
        sys.stdout.flush()
        progress = self.width * self.count / self.total
        sys.stdout.write('{}{:3}/{:3}: '.format(msg, self.count, self.total))
        sys.stdout.write(self.finish_symbol * progress + self.init_symbol * (self.width - progress) + '\r')
        if progress == self.width:
            sys.stdout.write('\n')
        sys.stdout.flush()



# bar = ProgressBar(100)
# for i in range(10):
#     bar.move(10)
#     time.sleep(0.1)