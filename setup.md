## Preamble

The [repository](http://github.com/leriomaggio/ppml-tutorial) contains the files to
recreate the Conda Environment with all the required packages.

[**Anaconda**](https://www.anaconda.com/products/distribution) Distribution is recommended, although any version of `Python 3.10` should work fine.

If that's not the case, or if you spot any error/mistake, please feel free to reach out directly to [me](mailto:vmaggio@anaconda.com?subject=PPML%20SciPy23%20Issue), or to open an [Issue](http://github.com/leriomaggio/ppml-tutorial/issues) on the repository.

Any feedback will be very much appreciated!

Thank you! 🙏

## Set up the Environment

If you decided to give [Anaconda Notebooks](https://nb.anaconda.cloud) a go, you can skip
this section entirely, and just jump to the [Test Your Environment](#test-your-environment) Section.

**Before we start**:

All the instructions reported below will consider the **Terminal**
and hence the command-line interface to run all the commands.
Similarly, one could use alternatively [GitHub Desktop](https://desktop.github.com/) and
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

👉 non-Mac Silicon users
```bash
conda env create -f environment.yml
```
👉 Mac Silicon users only:
Not all libraries might be available for Mac Silicon. Adding a prefix allows to to create a conda environment on Intel libs.
```bash
CONDA_SUBDIR=osx-64 conda env create -f environment.yml
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

## Test your Environment

If you're using Anaconda Notebooks, click on the following badge [![open_in_anaconda](https://static.anaconda.cloud/content/a22d04e8445b700f28937ab3231b8cded505d0395c63b7a269696722196d5415)](https://anaconda.cloud/api/nbserve/launch_notebook?nb_url=https%3A%2F%2Fraw.githubusercontent.com%2Fleriomaggio%2Fppml-tutorial%2Fmain%2FGet-Ready.ipynb)
to open the `Get-Ready.ipynb` notebook on [anaconda.cloud](https://anaconda.cloud) and check your environment.

If you followed all the steps reported in the previous section to setup your local machine, you should be ready to 
proceed with **testing your environment**.

To do so, please open the `Get-Ready.ipynb` notebook to check that everything works properly on your end:

```bash
jupyter notebook Get-Ready.ipynb
```
