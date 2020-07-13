from collections import Counter
from PIL import Image
import numpy as np

MX = 16


def split_into_images() -> list:
    imgs = []
    img = np.array(Image.open("emoji_chain_stego1.png"))

    h, _, _ = img.shape

    for idx, i in enumerate(range(16, h, 160)):
        cur_img = np.zeros((128, 128, 4), dtype=np.uint8)
        for r in range(128):
            for c in range(128):
                cur_img[r][c] = img[i + r][c + 16]
        imgs.append(cur_img)

    return imgs


def decrypt(img: np.ndarray) -> str:
    set_bits = []
    h, w, _ = img.shape

    for r in range(h):
        for c in range(w):
            if img[r][c][2] & 1:
                set_bits.append([r, c])

    ctr = Counter()
    for pair in set_bits:
        for s in range(-MX, MX + 1):
            r = (pair[0] + s) * pair[1]
            c = pair[0] * (pair[1] + s)

            if 0 < r < 128:
                if r not in ctr:
                    ctr[r] = 0
                ctr[r] += MX + 1 - abs(s)

            if 0 < c < 128:
                if c not in ctr:
                    ctr[c] = 0
                ctr[c] += MX + 1 - abs(s)

    return chr(ctr.most_common(1)[0][0])


def main():
    # to get the link, run zsteg -a top.png
    imgs = split_into_images()
    top = imgs[0]
    Image.fromarray(top).save("top.png")
    imgs = imgs[1:]
    assert len(imgs) == 30

    flag = ""
    for img in imgs:
        flag += decrypt(img)

    print(flag)


if __name__ == '__main__':
    main()
