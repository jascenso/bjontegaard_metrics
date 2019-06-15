# Bjontegaard_metric
Bjontegaard's metric computes the average gain in PSNR or the average saving in bitrate (in %) 
between two rate-distortion curves [1][2].

Similar to other packages [3] this function allows to compute the metric for more than 4 RD points,
but in this case for the python language.

## Usage
Check the test.py for some simple tests.

* bd_psnr = bj_delta(Rate1, PSNR1, Rate2, PSNR2, mode=0))
* bd_rate = bj_delta(Rate1, PSNR1, Rate2, PSNR2, mode=1))

Rate1,PSNR1 - RD points for curve 1. 
Rate2,PSNR2 - RD points for curve 2. 
Mode: 0 for average PSNR difference and 1 for average bitrate savings (%). 
Returns the calculated Bjontegaard metric (BD-Rate or BD-PSNR). 
  
## References:
[1] G. Bjontegaard, "Calculation of average PSNR differences between RD-curves", VCEG-M33, Austin, TX, USA, April 2001. 
[2] S. Pateux, J. Jung, "An excel add-in for computing Bjontegaard metric and its evolution", VCEG-AE07, Marrakech, MA, January 2007. 
[3] G. Valenzise, https://www.mathworks.com/matlabcentral/fileexchange/27798-bjontegaard-metric. 
