## Preamble

To run the code included in this tutorial, we will leverage on a pretty "standard" Python/PyData stack:
`numpy`, `pandas`, `matplotlib`, and `scikit-learn` for all the data science and Machine learning parts,
and `pytorch` (w/ `torchvision`) for the Deep Learning examples.

Moreover, a few **extra** / specialised packages will be also featured:
- [Opacus](https://opacus.ai): A library to train PyTorch models with differential privacy
- [PHE](https://pypi.org/project/phe/): A Python 3 library implementing the Paillier Partially Homomorphic Encryption
- [Flower](https://flower.dev): A Federated Learning library for PyTorch

As for the Python version/distribution: any Python 3.10+ version should be fine.

I would recommend using [**Anaconda Distribution**](https://anaconda.com/download)
to have immediate access to all the main required packages, regardless of the platform/OS you are on,
and to easily install the extra ones.

The [repository](http://github.com/leriomaggio/ppml-tutorial) contains the files to
recreate the Conda Environment (i.e. [`environment.yml`](http://github.com/leriomaggio/ppml-tutorial/environment.yml))
with all the required packages.

Read ["Set up the Environment"](#set-up-the-environment) section for detailed instructions on how to proceed.

**Alternatively** you could use [**Anaconda Notebooks**](https://nb.anaconda.cloud) to run all the code,
and without needing to install anything at all on your computer.

Please see ["Using Anaconda Notebooks"](#anaconda-notebooks) section for further information on how to get started.

## Set up the Environment

If you decided to give [Anaconda Notebooks](https://nb.anaconda.cloud) a go, you can skip
this section entirely, and jump to the [Anaconda Notebooks](#anaconda-notebooks) Section.

**Before we start**:

All the instructions reported below will consider the **Terminal**
and hence the command-line interface to run all the commands.
Similarly, one could use in alternative [GitHub Desktop](https://desktop.github.com/) and
[Anaconda Navigator](https://docs.anaconda.com/free/navigator/index.html) to interact with
GitHub repositories, and conda environment, respectively.

If you haven't already, let's download (or `git clone`) the current repository on your local computer.

```bash
git clone https://github.com/leriomaggio/ppml-tutorial
cd ppml-tutorial
```

**Setup the environment**:

The repository contains an `environment.yml` file that can be used to automatically recreate the
conda environment with all the required packages:


```bash
conda env create -f environment.yml
```

Once this is complete, you should now have a new conda environment named `ppml`.

To double check that you can run the following command:

```bash 
conda env list
```

This command lists all the available conda environment you have on your computer.
The new `ppml` environment should be in that list.

If that completes successfully, all you need to do now is to **activate** the new environment:

```bash
conda activate ppml
```

### Using `pip`

**Alternatively**, you could install all the required packages using `pip`:

```bash

pip install -f ppml_requirements.txt
```

### Well Done! 🎉

## Anaconda Notebooks

All notebooks in this tutorial are self-contained: any specific package that is not already part of [**Anaconda Distribution**](https://www.anaconda.com/download) can be installed directly from the notebook.

All you'd need is just sign up to get your [account](https://www.anaconda.com/code-in-the-cloud)

**SPECIAL CODE**: Use the Code `SCIPY23` to get special access to 30-days free trial to the
[**Starter Tier**](https://www.anaconda.com/pricing/individuals) (_valid until August 18th, 2023_).

All the notebooks listed in the TOC include a special badge ![Open in Anaconda Notebook Badge](https://static.anaconda.cloud/content/a22d04e8445b700f28937ab3231b8cded505d0395c63b7a269696722196d5415)
to automatically import, and open the notebook on [Anaconda.cloud](https://anaconda.cloud).

⚠️ **Please** only make sure to select the `scipy-tutorials-2023` iPython kernel.

Anaconda Notebook badges can be generated for your notebooks using the [Anaconda Badge Generator](https://leriomaggio.pyscriptapps.com/anaconda-notebook-badge-generator/)
app on [PyScript.com](https://pyscript.com).

## Test your Environment

If you're using Anaconda Notebooks, click on the following badge [![open_in_anaconda](https://static.anaconda.cloud/content/a22d04e8445b700f28937ab3231b8cded505d0395c63b7a269696722196d5415)](https://anaconda.cloud/api/nbserve/launch_notebook?nb_url=https%3A%2F%2Fraw.githubusercontent.com%2Fleriomaggio%2Fppml-tutorial%2Fmain%2FGet-Ready.ipynb)
to open the `Get-Ready.ipynb` notebook on [anaconda.cloud](https://anaconda.cloud) and check your environment.

If you followed all the steps reported in the previous section to setup your local machine, you should be ready to 
proceed with **testing your environment**.

To do so, please open the `Get-Ready.ipynb` notebook to check that everything works properly on your end:

```bash
jupyter notebook Get-Ready.ipynb
```