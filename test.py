from bj_delta import *


print("Test 1")
Rate1 = np.array([686.76, 309.58, 157.11, 85.95])
PSNR1 = np.array([40.28, 37.18, 34.24, 31.42])
Rate2 = np.array([893.34, 407.8, 204.93, 112.75])
PSNR2 = np.array([40.39, 37.21, 34.17, 31.24])

print("BD-PSNR: ", bj_delta(Rate1, PSNR1, Rate2, PSNR2, mode=0))
print("BD-RATE: ", bj_delta(Rate1, PSNR1, Rate2, PSNR2, mode=1))

print("Test 2")
Rate1 = np.array([0.001, 0.005, 0.020, 0.100, 0.7500])
PSNR1 = np.array([18.02, 20.57, 23.09, 27.71, 35.74])
Rate2 = np.array([0.00103, 0.00507, 0.02098, 0.09638, 0.73051])
PSNR2 = np.array([24.81, 29.08, 33.09, 37.27, 43.12])

print("BD-PSNR: ", bj_delta(Rate1, PSNR1, Rate2, PSNR2, mode=0))
print("BD-RATE: ", bj_delta(Rate1, PSNR1, Rate2, PSNR2, mode=1))
