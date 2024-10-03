<h1 align="center">ISLR101: Iranian Word-Level Sign Language Recognition Dataset</h1>

<p align="center">
  <b>
    <span style="color:blue"> Hossein Ranjbar<sup>1</sup>, Alireza Taheri<sup>2</sup></span>
  </b>
</p>

<p align="center">
  <sup>1</sup> <span style="color:darkgreen">Department of Computational Linguistics, University of Zurich, Zurich, Switzerland</span> <br>
  <sup>2</sup> <span style="color:darkgreen">Department of Mechanical Engineering, Sharif University of Technology, Tehran, Iran</span>
</p>


---

## Introduction

we introduce ISLR101 dataset, the first publicly available
Iranian Sign Language dataset for isolated sign language recognition. This comprehensive
dataset includes 4,614 videos covering 101 distinct signs, recorded from 10 different signers,
along with pose information extracted using OpenPose. We establish visual appearance-based
and skeleton-based frameworks as baseline models, thoroughly training and evaluating them
on ISLR101 to demonstrate their effectiveness.

<div align="center">
  <img src="https://github.com/user-attachments/assets/a919d4c1-b0c2-4fac-9b94-3cbbf26343f8" alt="1" height="300">
</div>

This repository provides a PyTorch-based implementation of **Skeleton-based sign language recognition**. 

## Instalation

### 1. Clone this repository

```bash
git clone https://github.com/HoseinRanjbar/ISLR101.git
cd ISLR101
```

### 2. Download ISLR101 pose data

```bash
mkdir data
cd data
wget https://drive.google.com/uc?export=download&id=1mqWgZJ7mJZEDyuK5lixC4g4ZUKa1ZKme
wget https://drive.google.com/uc?export=download&id=1Q1Y1noTdG0pJSLecLqZnvt_fnNbs306I
cd ..
```

### 3. Install dependent packages
   
```bash
pip install -r requirements.txt
```

## Usage

### 1. Test
   
To test the model on the ISLR101 dataset, use the following command:

- ttr configuration:

```bash
./scripts/test_ttr.sh
```

- str configuration:

```bash
./scripts/test_str.sh
```

- sttr1s configuration:

```bash
./scripts/test_sttr1s.sh
```

### 2. Training

To train the model on the ISLR101 dataset, use the following command:

- ttr configuration:

```bash
./scripts/train_ttr.sh
```

- str configuration:

```bash
./scripts/train_str.sh
```

- sttr1s configuration:

```bash
./scripts/train_sttr1s.sh
```
