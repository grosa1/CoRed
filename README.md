# CoRed
Python wrapper for the code readability assessment tool proposed by [Scalabrino et al. 2018](https://doi.org/10.1002/smr.1958).
The original code and replication package can be found at https://dibt.unimol.it/report/readability/.

The readability level thresholds are defined based on the evaluation performed by [Piantadosi et al. 2020](https://doi.org/10.1007/s10664-020-09886-9)

**CoRed works only on java source files!**

### USAGE
```
python3 run.py <java project dir>
```
The output will be the csv file `report.csv`, where there is the readability score and readability level for each file.
By default, CoRed reports only java files with a low readability level.

To log all readability levels:
```
python3 run.py <java project dir> --verbose
```
