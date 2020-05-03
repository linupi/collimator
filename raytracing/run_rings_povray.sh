## to submit use
## oarsub -l /nodes=2,walltime=00:02:00
## oarsub -l nodes=1/core=8,walltime=00:02:00 ./raytracing/run_rings_povray.sh

source  ~/anaconda3/bin/activate sollersim
time python raytracing/rings_povray.py examples/id31_draft/ring_raytracing.yml
