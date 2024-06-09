## Preamble

To run the code included in this tutorial, we will leverage on a pretty "standard" Python/PyData stack:
`numpy`, `pandas`, `matplotlib`, and `scikit-learn` for all the data science and Machine learning parts,
and `pytorch` (w/ `torchvision`) for the Deep Learning examples.

Moreover, a few **extra** / specialised packages will be also featured:
- [PySyft](https://github.com/OpenMined/PySyft): A platform for Remote Data Science
- [Opacus](https://opacus.ai): A library to train PyTorch models with differential privacy
- [PHE](https://pypi.org/project/phe/): A Python 3 library implementing the Paillier Partially Homomorphic Encryption

As for the Python version/distribution: any Python 3.10+ version should be fine.

The [repository](http://github.com/leriomaggio/ppml-tutorial) contains the files to
recreate the Python environment with all the required packages, either you are using [**Miniconda**](https://docs.anaconda.com/free/miniconda/index.html)(i.e. [`environment.yml`](http://github.com/leriomaggio/ppml-tutorial/environment.yml)) or 
Standard Python Distribution (i.e. [`ppml_requirements.txt`](http://github.com/leriomaggio/ppml-tutorial/ppml_requirements.txt)).

## Set up the Environment

**Before we start**:

All the instructions reported below will consider the **Terminal**
and hence the command-line interface to run all the commands.

Similarly, instructions to create the Python virtual environment will consider using 
[`pyenv`](https://github.com/pyenv/pyenv) and [`pyenv-virtualenv`](https://github.com/pyenv/pyenv-virtualenv)
to download the Python distribution, and install the environment.

If you haven't already, let's download (or `git clone`) the current repository on your local computer.

```bash
git clone https://github.com/leriomaggio/ppml-tutorial -b mlforum-24
cd ppml-tutorial
```

**Setup the environment**:

The repository contains a `ppml_requirements.txt` file that can be used to automatically recreate the
environment with all the required packages.

First, let's download the shims of the Python version we want to use. We will be using `Python 3.12`:


```bash
pyenv install 3.12
```

Once this is complete, you should now have the shims of Python 3.12 available in your system. 

The next step is to now point to this version of the interpreter when creating the new virtual environment. 

```bash
pyenv virtualenv 3.12 ppml
```

This will create a new virtual environment called `ppml`. We now need to **activate** the environment:

```bash
pyenv activate ppml
```

**Finally**, you could install all the required packages using `pip`:

```bash

pip install -f ppml_requirements.txt
```

### Well Done! 🎉

## Test your Environment

If you followed all the steps reported in the previous section to setup your local machine, you should be ready to 
proceed with **testing your environment**.

To do so, please open the `Get-Ready.ipynb` notebook to check that everything works properly on your end:

```bash
jupyter lab Get-Ready.ipynb
```