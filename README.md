## OIM
a Python script for transfer `AZtec` data (.csv) to `OIM` data (.txt) analysis

## Download Python： https://www.python.org/
<img width="669" alt="Screenshot 2024-03-15 at 19 09 41" src="https://github.com/KARASU-SUHN/OIM/assets/43245579/dfb28872-d053-4797-b59a-df870c55d411">

## Open terminal 

## Download pip
```
python3 -m ensurepip --default-pip
```
```
python3 -m pip install --upgrade pip setuptools wheel
```
## Downlod the required packages: `numpy` `pandas`
```
python3 -m pip install numpy
```
```
python3 -m pip install pandas
```
### :o: Test whether your package is installed
```
python3 -m pip list
```

####  If the package is downloaded correctly, you will see the version of numpy and pandas (the following image is for your reference): 
<img width="163" alt="Screenshot 2024-03-15 at 19 24 50" src="https://github.com/KARASU-SUHN/OIM/assets/43245579/0cc6a6a1-f0f4-4c22-b718-ce9a346598f2">


# Installation
### Step a. Download ZIP
<img width="457" alt="Screenshot 2024-03-15 at 18 53 27" src="https://github.com/KARASU-SUHN/OIM/assets/43245579/ab499387-845c-4e0c-b338-db9e4df5a92c">

### Step b. Unzip to current directory 
:warning: only english, number and hyphen is recommend in the directory location. Space can not be used.

### Step c. Open the directory in the terminal
```
cd /d [YourDirectoryPath]/OIM-main
```
### Step d. Refer to `20230227_【修正版】AZtecデータ編集手順書 (to OIM).pdf`, after step 4, save the excel file as `aztec.csv` and put it in the [~/OIM-main/input] directory. 

Now, there should have two files in the input directory (`aztec.csv` and `AZtec to OIM.csv`).

### Step e. Run the Python script
```
python3 script.py
```
## :round_pushpin: Result
When you see `oim file saved to: ~/OIM-main/oim.txt` after running the script, `oim.txt`, the same as the step 9 in `20230227_【修正版】AZtecデータ編集手順書 (to OIM).pdf` have been created in the `output` directory. 
Then you can change the .txt to .ang and open it by OIM analysis. 

## :warning: When reopen the terminal: start from "Installation"-Step c.