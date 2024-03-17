---
tags:
  - OMSCS
  - AI
  - ML
---
# Mixture Models and EM Notes

Notes on paper: [[Mixture_Models_and_EM.pdf]]

This chapter contains the source image from Module 7 on K-means.

There's a really interesting graphic in the paper which shows how to use K-means to compress an image (lossy). Essentially each color is plotted in some color space, and they use some number of K to pick how many colors the output image should have.

> This also illustrates of the use of vector quantization for data compression \[...\] smaller values of $K$ give higher compression at the expense of poorer image quality.

> The image segmentation problem discussed above also provides an illustration of the use of clustering for data compression. Suppose the original image has N pixels comprising $\left\{R, G, B\right\}$ values each of which is stored with 8 bits of precision. Then to transmit the whole image directly would cost $24N$ bits. Now suppose we first run K-means on the image data, and then instead of transmitting the original pixel intensity vectors we transmit the identity of the nearest vector $μ_k$. Because there are $K$ such vectors, this requires $log_2 K$ bits per pixel. We must also transmit the K code book vectors $μ_k$, which requires $24K$ bits, and so the total number of bits required to transmit the image is $24K + N log_2 K$ (rounding up to the nearest integer). The original image shown in Figure 9.3 has $240 × 180 = 43,200$ pixels and so requires $24 × 43, 200 = 1,036,800$ bits to transmit directly. By comparison, the compressed images require $43,248$ bits $(K = 2)$, $86,472$ bits $(K = 3)$, and $173,040$ bits $(K = 10)$.

This paper also has the diagram showing how a mixture of gaussians finds 2 groups of points from a cloud of points.