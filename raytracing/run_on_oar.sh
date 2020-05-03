## to submit use
## oarsub -l /nodes=2,walltime=00:02:00
## oarsub -l nodes=1/core=8,walltime=00:02:00 ./run_on_oar.sh

source  ~/anaconda3/bin/activate sollersim
time python rings_only_run_povray.py
