#!/bin/bash

#SBATCH --job-name=p23ds018-textsummarizer
#SBATCH --nodelist=node1
#SBATCH --gres=gpu:1
#SBATCH --error=job_logs/%j_error.log
#SBATCH --output=job_logs/%j_output.log

source "/apps/compilers/anaconda3-24.2/etc/profile.d/conda.sh"
conda activate venv/
python main.py
