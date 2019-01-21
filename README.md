# Bader Merge

## Rely

- Python 3.6.5
- numpy

## File Requirement

In bader_files folder, there must be

- atom_selection.txt
- CHGCAR
- BvAt0001.dat
- ...
- BvAt000n.dat

## Methodology

- Read with function np.loadtxt()
- Skip first 16 lines in .dat
- Shape (51200,5) Totally 40*40*160 = 256000
- Process the header and footer content
- Save with np.savetxt

## Useage

```
python task.py -o <outputfile_name>
```

-o name of outputile (Optional, Defalt = "CHGCAR_OUTPUT")

## Example

```
python BaderMerge.py
```
