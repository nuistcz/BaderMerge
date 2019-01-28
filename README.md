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
- BvAtxxxx.dat

## Usage of atom_selection.txt

- First line must be 'list(List/LIST)' or 'range(Range/RANGE)'
- If it's list mode, the next few rows should include each atom number
- If it's range mode, the next row should be 'X/x', 'Y/y' or 'Z/z', then give the range minimum and maximum.

### Example of atom_selection.txt

Select No.1 No.4 and No.5 atom:
```
List
1
4
5
```

Select atoms in z-aixs with range 0-0.5: (Includes 0 and Excludes 0.5)
```
Range
z
0
0.5
```

## Methodology

- Process atom_selection.txt
- Find the atoms selected and print out
- Read with function np.loadtxt(), skip the header rows
- Process the header and footer content
- Calculate the sum of them
- Save with np.savetxt

## Useage

```
python BaderMerge.py -o <outputfile_name>
```
-o name of outputile (Optional, Defalt = "CHGCAR_OUTPUT")

## Example

```
python BaderMerge.py
```