import numpy as np


class Transform:
    def __call__(self, x):
        raise NotImplementedError


class RandomFlipHorizontal(Transform):
    def __init__(self, p=0.5):
        self.p = p

    def __call__(self, img):
        """
        Horizonally flip an image, specified as an H x W x C NDArray.
        Args:
            img: H x W x C NDArray of an image
        Returns:
            H x W x C ndarray corresponding to image flipped with probability self.p
        Note: use the provided code to provide randomness, for easier testing
        """
        flip_img = np.random.rand() < self.p
        if flip_img:
            return img[:, ::-1, :]
        else:
            return img


class RandomCrop(Transform):
    def __init__(self, padding=3):
        self.padding = padding

    def __call__(self, img):
        """Zero pad and then randomly crop an image.
        Args:
             img: H x W x C NDArray of an image
        Return
            H x W x C NAArray of cliped image
        Note: generate the image shifted by shift_x, shift_y specified below
        """
        shift_x, shift_y = np.random.randint(
            low=-self.padding, high=self.padding + 1, size=2
        )
        img = np.pad(
            img,
            ((self.padding, self.padding), (self.padding, self.padding), (0, 0)),
            mode="constant",
        )
        img = img[
            self.padding
            + shift_x : self.padding
            + shift_x
            + img.shape[0]
            - 2 * self.padding,
            self.padding
            + shift_y : self.padding
            + shift_y
            + img.shape[1]
            - 2 * self.padding,
            :,
        ]
        return img