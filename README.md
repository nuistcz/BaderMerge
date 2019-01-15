# Bader Merge

## Rely

- Python 3.6.5
- numpy

## File Requirement

In bader_files folder, there must be

- CHGCAR
- BvAt0001.dat
- ...
- BvAt000n.dat

## Methodology

- Read with function np.loadtxt()
- Skip first 16 lines in .dat
- Shape (51200,5) Totally 40*40*160 = 256000
- Save with np.savetxt

## Useage

```
python task.py -i <Atom Selection 1> -i <Atom Selection 2> -o <outputfile_name>
```

-i Atom Selection
-o name of outputile (Optional, Defalt = "CHGCAR_OUTPUT")

## Example

```
python BaderMerge.py -i 1 -i 4 -i 5
```


## TODO

- The dimensial of Data -- Defalut 256000
- The header of file -- Not sure