import sys, os
INTERP = os.path.join(os.environ['HOME'], 'msk93.dreamhosters.com', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)
sys.path.append(os.getcwd())

sys.path.append('myapp')
from myapp.app import app as application
