# PPML: Machine Learning on Data you cannot see

Repository for the [tutorial](https://schedule.mozillafestival.org/session/3TAPD8-1) on **Privacy-Preserving Machine Learning** (`PPML`) presented at [SciPy 2023](https://www.scipy2023.scipy.org/)

## Intro

Privacy guarantee is **the** most crucial requirement when it comes to analyse sensitive data.
However, data anonymisation techniques alone do not always provide complete privacy protection;
moreover Machine Learning models could also be exploited to _leak_ sensitive data when _attacked_,
and no counter-measure is applied.
*Privacy-preserving machine learning* (PPML) methods hold the promise to overcome all these issues,
allowing to train machine learning models with full privacy guarantees. In this tutorial we will explore
several methods for privacy-preserving data analysis, and how these techniques can be used to safely train
ML models _without_ actually seeing the data.

### Outline

TBD

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

### Installation Instructions

All the materials in this tutorial (code and lecture notes) are available as Jupyter notebooks.

There is no specific (hardware) requirement to execute all the code on your computer,
so executing everything on your laptop should be more than ok 😊.

Please refer to the [`setup.md`](./setup.md) document for a step-by-step guide on how to set up the environment,
and to check that all is working.

**Alternatively** you could use [**Anaconda Notebooks**](https://nb.anaconda.cloud) to run all the notebooks interactively, and without install anything on your laptop. 

All notebooks in this tutorial are self-contained: any specific package that is not already part of [**Anaconda Distribution**](https://www.anaconda.com/download) can be installed directly from the notebook.

All you'd need is just sign up to get your [account](https://www.anaconda.com/code-in-the-cloud)

**Note**: All the notebooks that will be listed in the TOC will include a badge [!Open in Anaconda Notebook Badge](https://static.anaconda.cloud/content/a22d04e8445b700f28937ab3231b8cded505d0395c63b7a269696722196d5415)
to automatically import and open a notebook on [Anaconda.cloud](https://anaconda.cloud).

## Colophon

**Author**: Valerio Maggio ([`@leriomaggio`](https://twitter.com/leriomaggio)),
Researcher, [SSI Fellow](https://www.software.ac.uk/about/fellows/valerio-maggio),
and Data Scientist Advocate at Anaconda.

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

The material developed in this tutorial has been supported by Anaconda, and the [Software Sustainability Institute](https://www.software.ac.uk) (SSI), as part of my [SSI fellowship](https://www.software.ac.uk/about/fellows/valerio-maggio) on `PETs` (Privacy Enhancing Technologies).

Please see this [deck](https://speakerdeck.com/leriomaggio/privacy-enhancing-data-science-ssi-fellowship-2022) to know more about my fellowship plans.

Public shout out to all the people at [OpenMined](https://www.openmined.org) for all the encouragement and support with the preparation of this tutorial.
I hope the material in this repository could contribute to raise awareness about all the amazing work on PETs it's being provided to the Open Source and the Python communities.

![Anaconda Logo](./logos/anaconda_logo_small.png "Anaconda")
![OpenMined](./logos/openmined_logo_small.png "OpenMined")

## Contacts

For any questions or doubts, feel free to open an [issue](https://github.com/leriomaggio/ppml-tutorial/issues) in the repository, or drop me an email @ `vmaggio_at_anaconda_dot_com`