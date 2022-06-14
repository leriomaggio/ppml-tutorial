"""
This module provides access to the ORLFaces (ORL Database of Faces)
as encapsulated as a `torchvision.datasets.VisionDataset` class.

Notes
-----
The ORLFaces dataset [1]_ contains image files of `40` different subjects (orgainsed one per folder).
Images are `112x92` pixels, with `256` grey levels per pixel, and stored in PGM format.
Folders have names of the form `sID`, where `ID` indicates the subject number (between `1` and `40`).
In each of these directories, there are **ten different** images of that subject, which have names of the
form `Y.pgm`, where `Y` is the image number for that subject (between `1` and `10`) - accounting for
a total of `400` images (10 per 40 subjects).

Images are randomly partitioned in training and test sets.

References
-----------
.. [1]  https://www.cl.cam.ac.uk/research/dtg/attarchive/facedatabase.html
"""

import os
import torch
import numpy as np
import re
from collections import defaultdict
from PIL import Image
from torchvision.datasets import VisionDataset
from torchvision.datasets.utils import download_url, extract_archive
from enum import Enum
from pathlib import Path
from typing import Callable, Optional, Any, List, Tuple


class Partition(Enum):
    """
    Enumeration of Data Partitions for Machine learning experiments
    """

    train = "training"
    test = "test"


class ORLFaces(VisionDataset):
    """`ORL Faces` (The ORL Database of Faces)

    The Dataset contains a folder with faces of 40 different subjects
    taken at different times, varying the lightning, facial expressions
    (e.g. open/closed eyes, smiling/serious face), and facial details.

    This dataset is being used in research as facial detection dataset.

    Attributes
    ----------
    root : str
        Root directory where the local copy of dataset is stored.
    split : {"train", "test"} (default: "train")
        Target data data_partition. Two data partitions are available, namely
        "training", and "test". Training data_partition is considered
        by default. Any _validation_ partition could be extracted from the
        training dataset.
    download :  bool, optional (False)
        If true, the dataset will be downloaded from the internet and saved in the root
        directory. If dataset is already downloaded, it is not downloaded again.
    transform : Callable, optional
        A function/transform that takes in an image and returns a transformed version
    seed: int optinal (123456)
        Random seed used to split images in training and testing partitions.
        The partitions are generated randomly (but consistently given the same random seed).
        Different values of this parameter will affect this generation.
        Note: Data partitions are generated only the first time the dataset is initialised,
        and before the local torch (tensor) files are saved.
        Multiple instances of this dataset with different seed won't have any effect, unless
        local partition files are effectively deleted.
    """

    RAW_DATA_FOLDER = "orl_faces"

    resources = [
        (
            "https://www.dropbox.com/s/gxus70grtlt8bpq/orl_faces.tar.gz?dl=1",
            "83134c1ac2309b40441b35d5fa37a3f1",
        )
    ]

    data_files = {
        Partition.train: "training.pt",
        Partition.test: "test.pt",
    }

    classes = list(range(1, 41))

    def __init__(
        self,
        root: str,
        split: str = "train",
        download: bool = False,
        transform: Optional[Callable[[Any], Any]] = None,
        seed: int = 123456,
    ):
        super(ORLFaces, self).__init__(root, transform=transform)
        self._seed = seed
        self.random_gen = np.random.RandomState(self._seed)
        split = split.strip().lower()
        if split not in Partition.__members__.keys():
            raise ValueError(
                "Data Partition not recognised. "
                "Accepted values are 'train', 'validation', 'test'."
            )

        if download:
            self.download()

        if not self._check_exists():
            raise RuntimeError(
                "Dataset not found." + " You can use download=True to download it"
            )

        self.split = Partition[split]
        data_file = self.data_files[self.split]
        data_filepath = self.processed_folder / data_file
        self.data, self.targets = torch.load(data_filepath)

    def __len__(self):
        return len(self.data)

    def __getitem__(self, index):
        """

        Parameters
        ----------
        index : int
            Index of the sample

        Returns
        -------
        tuple
            (Image, Target) where target is index of the target class.
        """
        img, target = self.data[index], int(self.targets[index])

        # doing this so that it is consistent with all other datasets
        # to return a PIL Image
        img = Image.fromarray(img.numpy(), mode="L")

        if self.transform is not None:
            img = self.transform(img)

        return img, target

    @property
    def processed_folder(self):
        return Path(self.root) / self.__class__.__name__ / "processed"

    @property
    def raw_folder(self):
        return Path(self.root) / self.__class__.__name__ / "raw"

    @property
    def partition(self):
        return self.split

    @property
    def class_to_idx(self):
        return {_class: i for i, _class in enumerate(self.classes)}

    @property
    def idx_to_class(self):
        return {v: k for k, v in self.class_to_idx.items()}

    def classes_map(self):
        return {i: c for i, c in enumerate(self.classes)}

    def _check_exists(self):
        for data_fname in self.data_files.values():
            data_file = self.processed_folder / data_fname
            if not data_file.exists():
                return False
        return True

    def extra_repr(self):
        return "Split: {}".format(self.split.value)

    def _download_and_extract_archive(
        self,
        url: str,
        download_root: str,
        filename: Optional[str] = None,
        md5: Optional[str] = None,
    ):
        download_root = os.path.expanduser(download_root)
        extract_root = download_root
        if not filename:
            filename = os.path.basename(url)

        from torchvision.datasets import utils

        utils._get_redirect_url = lambda ulr, max_hops: url
        download_url(url, download_root, filename, md5)
        archive = os.path.join(download_root, filename)
        print("Extracting {} to {}".format(archive, extract_root))
        extract_archive(archive, extract_root, remove_finished=False)

    def download(self):
        """Download the ORLFaces data if it doesn't already exist in the processed folder"""

        if self._check_exists():
            return

        os.makedirs(self.raw_folder, exist_ok=True)
        os.makedirs(self.processed_folder, exist_ok=True)

        # download files
        for url, md5 in self.resources:
            filename = url.rpartition("/")[-1].split("?")[0]
            self._download_and_extract_archive(
                url, download_root=str(self.raw_folder), filename=filename, md5=md5
            )

        print("Processing...", end="")
        self._process_partitions()
        print("Done!")

    def _process_partitions(self):
        raw_data_filepath = self.raw_folder / self.RAW_DATA_FOLDER
        partitions = defaultdict(list)

        for subj_folder in os.listdir(raw_data_filepath):
            if not subj_folder.startswith("s"):
                continue  # skip folder
            # class is zero-indexed!
            subj_class = int(subj_folder.replace("s", "").strip()) - 1
            # select training set images, randomly - using the input seed
            training_indices = self.random_gen.choice(
                np.arange(10), size=7, replace=False
            )

            # sort image files, so we could use randomly selected indices, quickly
            subject_folder_path = raw_data_filepath / subj_folder
            image_files = filter(
                lambda f: not f.startswith("."), os.listdir(subject_folder_path)
            )
            subject_images = sorted(image_files, key=lambda f: int(f.split(".")[0]))
            subject_images = map(
                lambda f: subject_folder_path / f, subject_images
            )  # store full path
            subject_images = np.asarray(
                list(subject_images)
            )  # convert to array for easy indexing

            # Add new pair (images, class) to corresponding partitions
            partitions[Partition.train].append(
                (subject_images[training_indices], subj_class)
            )
            partitions[Partition.test].append(
                (np.delete(subject_images, training_indices), subj_class)
            )

        # store partitions locally - to be reloaded later
        for partition, dataset in partitions.items():
            images, labels = self._dataset_as_torch_tensors(dataset)
            data_file = self.processed_folder / self.data_files[partition]
            with open(data_file, "wb") as f:
                torch.save((images, labels), f)

    @staticmethod
    def read_pgm(filename, byteorder=">"):
        """Return image data from a raw PGM file as numpy array.
        Format specification: http://netpbm.sourceforge.net/doc/pgm.html
        """
        with open(filename, "rb") as f:
            buffer = f.read()
        try:
            header, width, height, maxval = re.search(
                b"(^P5\s(?:\s*#.*[\r\n])*"
                b"(\d+)\s(?:\s*#.*[\r\n])*"
                b"(\d+)\s(?:\s*#.*[\r\n])*"
                b"(\d+)\s(?:\s*#.*[\r\n]\s)*)",
                buffer,
            ).groups()
        except AttributeError:
            raise ValueError("Not a raw PGM file: '%s'" % filename)
        return np.frombuffer(
            buffer,
            dtype="u1" if int(maxval) < 256 else byteorder + "u2",
            count=int(width) * int(height),
            offset=len(header),
        ).reshape((int(height), int(width)))

    def _dataset_as_torch_tensors(
        self, dataset: List[Tuple[List[str], int]]
    ) -> Tuple[torch.TensorType, torch.TensorType]:
        """
        Collect all the images per subject and convert them in torch.Tensor.
        Labels will also be returned as tensor, repeated for each corresponding subject.

        Parameters
        ----------
        dataset : List[Tuple[List[str], int]]
            Set of images and corresponding label for each subject, in the considered partition
            (i.e. train, or test)
        Returns
        -------
        torch.TensorType
            [sample x pixels] tensor representing the whole data data_partition as
            torch Tensor.
        torch.TensorType
            [sample] tensor array of corresponding label (i.e. subject ID for each subject)
        """
        images, labels = [], []
        for subject, class_id in dataset:
            subject_images = np.asarray(list(map(self.read_pgm, subject)))
            subject_labels = np.zeros(shape=len(subject))
            subject_labels.fill(class_id)
            images.append(subject_images)
            labels.append(subject_labels)
        images = np.vstack(images)
        labels = np.hstack(labels)
        return torch.from_numpy(images), torch.from_numpy(labels)
