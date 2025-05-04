import numpy as np
import cv2
import matplotlib.pyplot as plt

# 画像の読み込み（カラー画像）
img = cv2.imread('Lenna.png')  # パスは適宜変更してください

# 平均化カーネル（5x5）を作成
kernel = np.ones((5, 5), np.float32) / 25

# カーネルを使って画像にフィルタを適用
dst = cv2.filter2D(img, -1, kernel)

# OpenCVはBGRなので、RGBに変換して表示
dst_rgb = cv2.cvtColor(dst, cv2.COLOR_BGR2RGB)

# 結果の表示
plt.imshow(dst_rgb)
plt.title('Filtered with 5x5 Average Kernel')
plt.axis('off')
plt.show()
