import sys
import subprocess

import numpy as np

sys.path.append("./dataset")
sys.path.append('./dnn')
sys.path.append("./shared")
import activationfunction as af
import neural_network as nn
import logic_circuit as lc

def test_main():
    main_result = subprocess.run(('python', 'cnn/main.py'))
    assert main_result.returncode == 0