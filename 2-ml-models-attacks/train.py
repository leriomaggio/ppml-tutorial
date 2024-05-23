import numpy as np
import torch as th
from torch.utils.data import DataLoader
from pathlib import Path
from typing import Tuple
from tqdm.notebook import tqdm
from sklearn.metrics import accuracy_score


def train(
    model: th.nn.Module,
    optimiser: th.optim.Optimizer,
    loaders: Tuple[DataLoader, DataLoader],
    epochs: int = 100,
    model_name: str = None,
    verbose: bool = False,
):
    """Simple Training/Validation Loop using the input model, and the pair of data loaders
    for training and validation, respectively.

    model:
        The target PyTorch model (nn.Module) to train
    optimiser:
        The model optimiser holding reference to model's parameters
    loaders: Tuple[DataLoader]
        Pair of Dataloader for training and validation data, respectively.
    epochs: int (default 100)
        Total number of training epoch
    model_name: str (default "")
        The name of the trained model - used mainly to name the checkpoint file
        that will be saved. If no name will be provided, the default
        `model.__class__.__name__.lower()` will be used.
    verbose: bool (default False)
        Verbosity of the report. If True, the Accuracy of each epoch will be printed.
        If not, only validation accuracy will be shown.
    """
    if model_name is None or not model_name:
        model_name = model.__class__.__name__.lower()

    train_loader, test_loader = loaders
    device = th.device("cuda" if th.cuda.is_available() else "mps" if th.backends.mps.is_available() else "cpu")
    print(f"Using {device} Device")
    # move model to the selected device, in case
    model = model.to(device)
    # both models uses LogSoftmax already! So NLLLoss is what we need
    criterion = th.nn.NLLLoss()

    best_validation_accuracy = 0
    checkpoint_folder = Path("./checkpoints")
    checkpoint_folder.mkdir(exist_ok=True)

    for epoch in tqdm(range(epochs), desc="Epochs"):
        running_loss_pred, training_acc = _step(
            train_loader, model, optimiser, criterion, device, is_training=True
        )
        if verbose:
            print(f"Prediction: {running_loss_pred}; Training ACC: {training_acc}")

        # run validation every 10 epochs
        if (epoch + 1) % 10 == 0:
            _, valid_acc = _step(
                test_loader, model, optimiser, criterion, device, is_training=False
            )
            if verbose:
                print(f"Validation ACC: {valid_acc}")
            if best_validation_accuracy < valid_acc:
                if verbose:
                    print("Saving Best Model Checkpoint")
                chk_path = checkpoint_folder / f"{model_name}.pt"
                print(chk_path)
                th.save(model.state_dict(), chk_path)
                best_validation_accuracy = valid_acc
                print(f"Best Validation ACC: {valid_acc}")


def _step(loader, model, optimiser, criterion, device, is_training: bool):
    samples_count = 0
    running_loss_pred = 0.0
    y_true, y_pred = list(), list()
    for batch in loader:
        images, subject_ids = batch
        images = images.view(-1, 112 * 92).to(device)
        subject_ids = subject_ids.to(device)
        samples_count += len(images)

        # zero the gradient
        model.zero_grad()
        optimiser.zero_grad()

        with th.set_grad_enabled(is_training):
            out = model(images)
            loss = criterion(out, subject_ids)
            _, preds = th.max(out, 1)

            if is_training:
                loss.backward()
                optimiser.step()
                running_loss_pred += loss.item()

        y_pred.append(preds.detach().cpu().numpy())
        y_true.append(subject_ids.detach().cpu().numpy())

    if is_training:
        running_loss_pred /= samples_count
    y_pred = np.hstack(y_pred)
    y_true = np.hstack(y_true)
    step_acc = accuracy_score(y_true, y_pred)
    return running_loss_pred, step_acc
