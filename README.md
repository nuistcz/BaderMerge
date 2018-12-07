# CHGCAR /bader_filesarray merge

## Rely

- Python 3.6.5
- numpy
- pandas(TODO)

## Methodology

- Read with function np.loadtxt()
- Skip first 16 lines in .dat
- Shape (51200,5) Totally 40*40*160 = 256000
- Save with np.savetxt

## Useage

```
python task.py -i <inputfile_1> -i <inputfile_2> -i <inputfile_n> -o <outputfile_name>
```

-i name of inputfile (In folder ./bader_files)
-o name of outputile (Optional, Defalt = "Out")

## TODO

- The dimensial of Data -- Defalut 256000
- The header of file -- Not sure