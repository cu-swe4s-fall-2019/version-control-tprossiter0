#!/bin/bash
chmod -x run.sh
conda activate swe4s
echo ...running calculate.py...

python3 calculate.py --intadd1 5 --intadd2 5 --numerator 10 --denominator 2
echo ...end of run...
