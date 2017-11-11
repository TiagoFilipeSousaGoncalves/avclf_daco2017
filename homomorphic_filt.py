#Simple Direct Implementation of the Homomorphic Filter 
#First Try: 2017/11/11
#import scipy.fftpack # For FFT2 
import cv2

#OpenCV provides the functions cv2.dft() and cv2.idft() for this. 
#It returns the same result as previous, but with two channels. 
#First channel will have the real part of the result 
#and second channel will have the imaginary part of the result. 
#The input image should be converted to np.float32 first.
# We will see how to do it.

img = np.float32(img)

rows,cols,dim=img.shape

rh, rl, cutoff = 2.5,0.5,32

imgYCrCb = cv2.cvtColor(img, cv2.COLOR_BGR2YCR_CB)
y,cr,cb = cv2.split(imgYCrCb)

y_log = np.log(y+0.01)

y_fft = np.fft.fft2(y_log)

y_fft_shift = np.fft.fftshift(y_fft)


DX = cols/cutoff
G = np.ones((rows,cols))
for i in range(rows):
    for j in range(cols):
        G[i][j]=((rh-rl)*(1-np.exp(-((i-rows/2)**2+(j-cols/2)**2)/(2*DX**2))))+rl

result_filter = G * y_fft_shift

result_interm = np.real(np.fft.ifft2(np.fft.ifftshift(result_filter)))

result = np.exp(result_interm)

print(result.shape)


cv2.imshow('Homomorphic Filtered Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()
