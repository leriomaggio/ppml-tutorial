## Preamble

The [repository](http://github.com/leriomaggio/ppml-tutorial) contains the files to
recreate the Conda Environment with all the required packages.

[**Anaconda**](https://www.anaconda.com/products/distribution) Distribution is recommended, although any version of `Python 3.10` should work fine.

If that's not the case, or if you spot any error/mistake, please feel free to reach out directly to [me](mailto:vmaggio@anaconda.com?subject=PPML%20SciPy23%20Issue), or to open an [Issue](http://github.com/leriomaggio/ppml-tutorial/issues) on the repository.

Any feedback will be very much appreciated!

Thank you! 🙏

## Set up the Environment


**Note**: All the instructions reported in this section will assume the use of the **Terminal**
and of a command-line interface to run all the commands. Similarly, one could use
[GitHub Desktop](https://desktop.github.com/) and
[Anaconda Navigator](https://docs.anaconda.com/free/navigator/index.html) to interact with
GitHub repositories, and conda environment.

First thing, let's download or `git clone` the current repository on your local computer.

```bash
git clone https://github.com/leriomaggio/ppml-tutorial
cd ppml-tutorial
```

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

If those steps above completed successfully, you should be ready to proceed with **testing the environment**.

To do so, you could run the `Get-Ready.ipynb` notebook to check that everything works properly on your end:

```bash
jupyter notebook Get-Ready.ipynb
```