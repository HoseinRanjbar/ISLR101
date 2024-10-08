#!/bin/bash
### Here are the SBATCH parameters that you should always consider:

### Here are the SBATCH parameters that you should always consider:
#SBATCH --gpus=A100:1
# SBATCH --gpus=1
#SBATCH --time=0-02:00:00   ## days-hours:minutes:seconds
#SBATCH --mem=30G
#SBATCH --ntasks-per-node=10
# SBATCH --output=fine_tuning.out

module load gpu
module load cuda
module load python/3.12
source ./env/bin/activate

python ./main.py --config ./config/train_ttr.yaml --work-dir ./experiments --phase 'train'
