# PPML: Machine Learning on Data you cannot see

Repository for the [tutorial](https://schedule.mozillafestival.org/session/3TAPD8-1) on **Privacy-Preserving Machine Learning** (`PPML`) presented at [Mozilla Festival 2023](https://www.mozillafestival.org/)

- [Abstract](#abstract)
    - [Outline](#outline)
- [Get the Material](#get-the-material)
    - [Set up the Environment](#set-up-your-environment)
- [Colophon](#colophon)
    - [Acknowledgments and Fundings](#acknowledgment-and-funding)
- [Contacts](#contacts)

## Abstract

Privacy guarantees are one of the most crucial requirements when it comes to analyse sensitive information. However, data anonymisation techniques alone do not always provide complete privacy protection; moreover Machine Learning (ML) models could also be exploited to _leak_ sensitive data when _attacked_ and no counter-measure is put in place.  

*Privacy-preserving machine learning* (PPML) methods hold the promise to overcome all those issues, allowing to train machine learning models with full privacy guarantees.

This workshop will be mainly organised in **two parts**. In the first part, we will explore one example of ML model exploitation (i.e. _inference attack_ ) to reconstruct original data from a trained model, and we will then see how **differential privacy** can help us protecting the privacy of our model, with _minimum disruption_ to the original pipeline. In the second part of the workshop, we will examine a more complicated ML scenario to train Deep learning networks on encrypted data, with specialised _distributed federated_ _learning_ strategies.

### Outline

- **Introduction**: Brief Intro to `PPML` and to the workshop ([slides](https://speakerdeck.com/leriomaggio/ppml-jgi))

- **Part 1**: Strengthening Deep Neural Networks
    - Model vulnerabilities: 
        - Adversarial Examples and `FGSM` (_Fast Gradient Sign Method_) [notebook](1-fast-gradient-sign-method/FSGM Attack.ipynb)
        - Model _Inference attack_ notebooks: [training](2-mia-differential-privacy/1-MIA-Training.ipynb) | [reconstruction](2-mia-differential-privacy/2-MIA-Reconstruction.ipynb)
    - Deep Learning with Differential Privacy
        - Model _Inference attack_ with `OPACUS`  notebooks: [training](2-mia-differential-privacy/4-MIA-Training-OPACUS.ipynb) | [reconstruction](2-mia-differential-privacy/5-MIA-Reconstruction-OPACUS.ipynb)

- **Part 2**: Primer on Privacy-Preserving Machine Learning
    - Introduction to Federated Learning [notebook](./3-federated-learning/1-Intro-Federated-Learning.ipynb)
    - DL training on (Homomorphically) Encrypted Data [notebook](./3-federated-learning/2-Homomorphic-Encryption.ipynb)
    - OpenMined and PrivateAI series [notebook](./3-federated-learning/3-OpenMined-private-AI-series.ipynb)
        - Introduction to Remote Data Science [notebooks](./3-federated-learning/duet_iris_classifier/)
        - SplitNN [notebooks](./3-federated-learning/duet_splitnn/)

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

### Set up your Environment

There are indeed two (possibly _three_) methods that you could use to execute the code in the notebooks.

The **recommended** method is to setup a new `ppml` Python environment on your local machine.

Please refer to the [`setup.md`](./setup.md) document for a step-by-step guide on how to set up the environment, and to check that all is working.

**Alternartively** you could rely on services such as [MyBinder](https://mybinder.org) or [Google Colab](https://colab.research.google.com) to run the notebooks interactively, and without needing to install anything.

[![Binder](https://mybinder.org/badge_logo.svg)](https://mybinder.org/v2/gh/leriomaggio/ppml-tutorial/HEAD) | [![Open In Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/leriomaggio/ppml-tutorial/blob/main/index.ipynb)

However, these alternative solutions come with some **caveats and workarounds** that should be considered:

1. MyBinder does not support connection to remote hosts on (not-allowed) network ports. This means that all the examples in Sec. 3 running `syft` and `duet` will **never** work.
    - I would recommend running those notebooks in `Colab` in case.
2. To use Google Colab it is necessary to have a **Google Account**. Plus, the environment cannot be setup automatically so sometimes additional deps and packages should be installed first
    - On this note, please consider that notebooks requiring additional dependencies contain instructions to do so, in their preamble section.

## Colophon

**Author**: Valerio Maggio ([`@leriomaggio`](https://twitter.com/leriomaggio)), Senior Research Associate, University of Bristol. 

All the **Code** material is distributed under the terms of the Apache License. See [LICENSE](./LICENSE) file for additional details.

All the instructional materials in this repository are free to use, and made available under the [Creative Commons Attribution
license][https://creativecommons.org/licenses/by/4.0/]. The following is a human-readable summary of (and not a substitute for) the [full legal text of the CC BY 4.0
license](https://creativecommons.org/licenses/by/4.0/legalcode).

You are free:

* to **Share**---copy and redistribute the material in any medium or format
* to **Adapt**---remix, transform, and build upon the material

for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the
license terms.

Under the following terms:

* **Attribution**---You must give appropriate credit (mentioning that
  your work is derived from work that is Copyright © Software
  Carpentry and, where practical, linking to
  http://software-carpentry.org/), provide a [link to the
  license][cc-by-human], and indicate if changes were made. You may do
  so in any reasonable manner, but not in any way that suggests the
  licensor endorses you or your use.

**No additional restrictions**---You may not apply legal terms or
technological measures that legally restrict others from doing
anything the license permits.

### Acknowledgment and funding

The material developed in this tutorial has been supported by Anaconda, the University of Bristol, and by the [Software Sustainability Institute](https://www.software.ac.uk) (SSI), as part of my [SSI fellowship](https://www.software.ac.uk/about/fellows/valerio-maggio) on `PETs` (Privacy Enchancing Technologies).

Please see this [deck](https://speakerdeck.com/leriomaggio/privacy-enhancing-data-science-ssi-fellowship-2022) to know more about my fellowship plans.

Public shout out all the people at [OpenMined](https://www.openmined.org) for all the encouragement and support with the preparation of this tutorial.
I hope the material in this repository could contribute to raise awareness about all the amazing work on PETs it's being provided to the Open Source and the Python communities.

![Anaconda Logo](./logos/anaconda_logo_small.png "Anaconda")
![OpenMined](./logos/openmined_logo_small.png "OpenMined")

## Contacts

For any questions or doubts, feel free to open an [issue](https://github.com/leriomaggio/ppml-tutorial/issues) in the repository, or drop me an email @ `valerio.maggio_at_anaconda_dot_com`