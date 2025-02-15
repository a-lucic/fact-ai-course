#!/bin/bash

echo 'Starting tests...'

export PYTHONPATH="$PWD"

cd $PYTHONPATH/Transparency

python3 train_and_run_experiments_bc.py --dataset 20News_sports --data_dir . --output_dir outputs/ --attention all --encoder lstm
python3 train_and_run_experiments_bc.py --dataset 20News_sports --data_dir . --output_dir outputs/ --attention none --encoder lstm

echo 'Done!'