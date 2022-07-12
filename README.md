<!-- ABOUT THE PROJECT -->
## What is Homolig?

Homolig is a python package to physiochemically compare immune receptor and
epitope sequences.

<!-- GETTING STARTED -->
## Getting Started

### Installation

To get a local copy of Homolig up and running follow these simple example steps.
(Once publicly available, this will be installable directly from pip without the
need for cloning.) 

1. Clone the repository
```bash
git clone https://github.com/edavis71/homolig
```
2. Pip install
```bash
cd homolig 
python3 -m pip install .
```

You should now be able to import homolig within python.

## Documentation
Homolig uses the IMGT/V-QUEST reference directory release 202214-2 (05 April
2022).
More documentation can be found at

## File format
The input file is a comma separated file containing the TCR or BCR CDR3 amino acid sequence and varible
gene name in IMGT format.   

For cases where paired alpha and beta chain information is available:  
| CDR3.beta.aa | TRBV | CDR3.alpha.aa | TRAV |
| --- | --- |  --- | --- |
| CASSAGTSPTDTQYF | TRBV6-4*01 | CAVMDSSYKLIF | TRAV1-2*01 |

### Basic Usage

```python
import homolig as hg

def main():
    adata = hg.homolig(input_file = 'tcr.csv',
        seq_type = 'tcr',
        chains = 'paired',
        metric='aadist',
        species='human')

if __name__ == '__main__':
    main()
```

## To Do

- See full checklist tsv file. 

## Citation

If you use this software, please cite our manuscript:

<!-- CONTACT -->
## Contact

Please send feedback to Emily Marcisak - [@efaithd](https://twitter.com/efaithd) -
<edavis71@jhu.edu>

## Support
We are happy to assist with problems when using homolig. Please report any bugs,
feature requests, or help requests using the issue tracker.

<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.
