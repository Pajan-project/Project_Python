import cv2

# Load gambar dari file
image = cv2.imread('gambar.jpg')

# Periksa apakah gambar berhasil dimuat
if image is None:
    print('Gambar tidak ditemukan. Pastikan path gambar yang benar.')
else:
    # Tampilkan gambar di jendela
    cv2.imshow('Gambar', image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
