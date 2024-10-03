#!/bin/bash
### Here are the SBATCH parameters that you should always consider:

### Here are the SBATCH parameters that you should always consider:
#SBATCH --gpus=A100:1
# SBATCH --gpus=1
#SBATCH --time=0-01:30:00   ## days-hours:minutes:seconds
#SBATCH --mem=30G
#SBATCH --ntasks-per-node=10
# SBATCH --output=fine_tuning.out

module load gpu
module load cuda
module load python/3.12
source /home/hranjb/data/ST-TR/env/bin/activate

python code/main.py --config /home/hranjb/data/ST-TR/code/config/st_gcn/islr/train_sttr.yaml --work-dir /home/hranjb/data/ST-TR/experiments/exp_sttr_lr0.00001 --phase 'train'
