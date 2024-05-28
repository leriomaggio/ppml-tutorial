# PPML: Machine Learning on Data you cannot see

Repository for the [tutorial](https://2024.pycon.it/en/submission/ryez) on **Privacy-Preserving Machine Learning** (`PPML`) presented at [PyCon Italia 2024](https://2024.pycon.it)

## Intro

Privacy guarantees are **the** most crucial requirement when it comes to analyse sensitive data. These requirements could be sometimes very stringent, so that it becomes a real barrier for the entire pipeline. Reasons for this are manifold, and involve the fact that data could not be _shared_ nor moved from their silos of resident, let alone analysed in their _raw_ form. As a result, _data anonymisation techniques_ are sometimes used to generate a sanitised version of the original data. However, these techniques alone are not enough to guarantee that privacy will be completely preserved. Moreover, the _memoisation_ effect of Deep learning  models could be maliciously exploited to _attack_ the models, and _reconstruct_  sensitive information about samples used in training, even if these information were not originally provided. 

*Privacy-preserving machine learning* (PPML) methods hold the promise to overcome all those issues, allowing to train machine learning models with full privacy guarantees.

This workshop will be mainly organised in **three** main parts. In the first part, we will introduce the main threats to 
data and machine learning models (e.g. _membership inference attack_ ) for privacy. 
In the second part, we will work our way towards  **differential privacy**: what is it, and how this method works, and 
how differential privacy could be used with Machine learning. 
Lastly, we will conclude the tutorial considering more complex ML scenarios to train Deep learning networks on encrypted data, with specialised _distributed_ settings for **remote analytics**.

### Outline

- **Introduction**: Brief Intro to `PPML` and to the workshop (`10 mins`) [SLIDES](https://speakerdeck.com/leriomaggio/ppml-pyconit24)

- **Part 1**: Data and ML models Threats (`45 mins`)
  - De-identification
  - K-anonimity and limitations
  - ML Model vulnerabilities: Adversarial Examples and _inference attack_

- **Part 2**: Short Introduction to Differential Privacy (`45 mins`)
  
  - Intro to Differential Privacy
  - Properties of Differential Privacy
  - DL training with Differential Privacy

- **Break** (`5 mins`)

- **Part 3**: Primer on Remote Data Science & PySyft (`25 mins`)
  - Intro to Federated Learning
  - DL training on (Homomorphically) Encrypted Data
  - Remote Data Science using PySyft


## Get the material

Clone the current repository by running the following instructions:

```bash
cd $HOME  # This will make sure you'll be in your HOME folder
git clone https://github.com/leriomaggio/ppml-tutorial.git
```

**Note**: This will create a new folder named `ppml-tutorial`. Move into this folder by typing:

```bash
cd ppml-tutorial
```

Well done! Now you should do be in the right location.
Bear with me for another few seconds, following instructions reported below 🙏

## Installation Instructions

All the materials in this tutorial (code, and lecture notes) are made available as
Jupyter notebooks.

**(1)** There is no specific _hardware requirement_ to execute the code, i.e. running everything
on your laptop should be more than fine 😊.

**(2)**: As for the _software requirements_, we will be using a pretty standard Python/PyData stack:
`numpy`, `pandas`, `matplotlib`, and `scikit-learn` for all the data science and Machine learning parts,
along with `pytorch` and `torchvision` to work on the Deep Learning examples.

Moreover, a few **extra** / specialised packages will be also featured:
- [PySyft](https://github.com/OpenMined/PySyft): A platform for Remote Data Science
- [Opacus](https://opacus.ai): A library to train PyTorch models with differential privacy
- [PHE](https://pypi.org/project/phe/): A Python 3 library implementing the Paillier Partially Homomorphic Encryption

Please refer to the [`setup.md`](./setup.md) document for step-by-step instructions to set up the environment
on your computer.

If you spot any error/mistake, please feel free to reach out directly to [me](mailto:valerio@openmined.org?subject=PPML%20SciPy23%20Issue), or to open an [Issue](http://github.com/leriomaggio/ppml-tutorial/issues)
on the repository.

Any feedback will be very much appreciated!

Thank you! 🙏

## Colophon

**Author**: Valerio Maggio ([`@leriomaggio`](https://twitter.com/leriomaggio)),
Researcher, [SSI Fellow](https://www.software.ac.uk/about/fellows/valerio-maggio),
and Data Scientist Advocate at Anaconda.

All the **Code** material is distributed under the terms of the Apache License. See [LICENSE](./LICENSE) file for additional details.

All the instructional materials in this repository are free to use, and made available under the [Creative Commons Attribution
license](https://creativecommons.org/licenses/by/4.0/). The following is a human-readable summary of (and not a substitute for) the [full legal text of the CC BY 4.0
license](https://creativecommons.org/licenses/by/4.0/legalcode).

You are free:

* to **Share**---copy and redistribute the material in any medium or format
* to **Adapt**---remix, transform, and build upon the material

for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the
license terms.

Under the following terms:

* **Attribution** --- You must give appropriate credit, and provide a link to the
  [LICENSE](https://github.com/leriomaggio/ppml-tutorial/LICENSE) [`cc-by-human`](https://creativecommons.org/licenses/by/4.0/),
  and indicate if changes were made.
  You may do so in any reasonable manner, but not in any way that suggests the
  licensor endorses you or your use.
  
* **No additional restrictions** --- You may not apply legal terms or
technological measures that legally restrict others from doing
anything the license permits.

### Acknowledgment and funding

The material developed in this tutorial has been supported by Anaconda, and the [Software Sustainability Institute](https://www.software.ac.uk) (SSI), as part of my 
[SSI fellowship](https://www.software.ac.uk/about/fellows/valerio-maggio) on `PETs` (Privacy Enhancing Technologies).

Please see this [deck](https://speakerdeck.com/leriomaggio/privacy-enhancing-data-science-ssi-fellowship-2022) to know more about my fellowship plans.

Public shout out to all the people at [OpenMined](https://www.openmined.org) for all the encouragement and support with the preparation of this tutorial.
I hope the material in this repository could contribute to raise awareness about all the amazing work on PETs it's being provided to the Open Source and the Python communities.

![OpenMined](./logos/openmined_logo_small.png "OpenMined")

## Contacts

For any questions or doubts, feel free to open an [issue](https://github.com/leriomaggio/ppml-tutorial/issues) in the repository, or drop me an email @ `valerio_at_openmined_dot_org`.
