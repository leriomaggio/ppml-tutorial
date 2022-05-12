# PPML: Machine Learning on Data you cannot see

Repository for the [tutorial](https://2022.pycon.de/program/QHJ7SX/) on **Privacy-Preserving Machine Learning** (`PPML`) presented at [PyConDE 2022](https://2022.pycon.de/)

## Abstract

Privacy guarantees are one of the most crucial requirements when it comes to analyse sensitive information. However, data anonymisation techniques alone do not always provide complete privacy protection; moreover Machine Learning (ML) models could also be exploited to _leak_ sensitive data when _attacked_ and no counter-measure is put in place.  

*Privacy-preserving machine learning* (PPML) methods hold the promise to overcome all those issues, allowing to train machine learning models with full privacy guarantees.

This workshop will be mainly organised in **two parts**. In the first part, we will explore one example of ML model exploitation (i.e. _inference attack_ ) to reconstruct original data from a trained model, and we will then see how **differential privacy** can help us protecting the privacy of our model, with _minimum disruption_ to the original pipeline. In the second part of the workshop, we will examine a more complicated ML scenario to train Deep learning networks on encrypted data, with specialised _distributed federated_ _learning_ strategies. 

### Outline

- **Introduction**: Brief Intro to `PPML` and to the workshop ([slides](https://speakerdeck.com/leriomaggio/ppml-pyconde))

- **Part 1**: Strengthening Deep Neural Networks
    - ML Model vulnerabilities: Adversarial Examples and _inference attack_
    - DL training with Differential Privacy

- **Part 2**: Primer on Privacy-Preserving Machine Learning
    - DL training on (Homomorphically) Encrypted Data
    - Federated Learning and Intro to Remote Data Science

_Note_: the material has been updated after the conference, to match the flow of the presentation as delivered during the conference, as well as to incorporate feedbacks received afterwards.

### Get the material

Clone the current repository, in order to get the course materials. To do so, once connected to your remote machine (via `SSH`), execute the following instructions:

```bash
cd $HOME  # This will make sure you'll be in your HOME folder
git clone https://github.com/leriomaggio/ppml-pyconde.git
```

**Note**: This will create a new folder named `ppml-pyconde`. Move into this folder by typing:

```bash
cd ppml-pyconde
```

Well done! Now you should do be in the right location. Bear with me another few seconds, following instructions reported below 🙏

### Updating your Environment

To execute the notebooks in this repository, it is necessary to set up the environment. 

Please refer to the [`Get-Ready.ipynb`](./Get-Ready.ipynb) notebook for a step-by-step guide on how to setup the environment, and check that all is working, and ready to go.

**Note**: You could run this notebook directly in [VSCode](https://vscode.dev), or in your existing Jupyter notebook/lab environment:

```bash
jupyter notebook Get-Ready.ipynb
```

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
The material developed in this tutorial has been supported by the University of Bristol, and by the [Software Sustainability Institute](https://www.software.ac.uk) (SSI), as part of my [SSI fellowship](https://www.software.ac.uk/about/fellows/valerio-maggio) on `PETs` (Privacy Enchancing Technologies).
Please see this [deck](https://speakerdeck.com/leriomaggio/privacy-enhancing-data-science-ssi-fellowship-2022) to know more about my fellowship plans.

![SSI Logo](./logos/ssi_logo_small.png "Software Sustainability Institute")
![UoB Logo](./logos/uob_logo_small.png "University of Bristol")


### Contacts 

For any questions or doubts, feel free to open an [issue](https://github.com/leriomaggio/ppml-pyconde/issues) in the repository, or drop me an email @ `valerio.maggio_at_gmail_dot_com`