## Preamble

The [repository](http://github.com/leriomaggio/ppml-pyconde) contains the files to recreate the Python virtual environment with all the required packages.

[**Anaconda**](https://www.anaconda.com/products/distribution) Python Distribution is recommended, although any version of `Python 3.8+` should work fine.

If that's not the case, or if you spot any error/mistake, please feel free to reach out directly to [me](mailto:valerio.maggio@bristol.ac.uk?subject=PPML%20PyConDE%20Issue), or to open an [Issue](http://github.com/leriomaggio/ppml-pyconde/issues) on the repository.

Any feedback will be very much appreciated!

Thank you! 🙏

## Set up the Environment

To create the conda environment, please **open a Terminal** and run the following command:

```bash
conda env create -f environment.yml
```

The previous command, will create a new environmment named `ppml`.

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

To do so, you could run the `Get-Ready.ipynb` notebook to check that everything works properly:

```bash
jupyter notebook Get-Ready.ipynb
```