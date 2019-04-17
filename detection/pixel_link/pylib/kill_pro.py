import sys
import util
name = sys.argv[1]
print util.proc.ps_aux_grep(name)
print 'kill them all?[n] y/n.'
yes = raw_input()
if yes == 'yes' or yes == 'y' or yes == 'Y':
    util.proc.kill(name)
