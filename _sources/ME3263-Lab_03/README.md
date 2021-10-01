# Lab 3 - Measuring Natural Frequencies


## What are natural frequencies?

In free vibration (i.e., no external forcing), structural components
oscillate at frequencies (or combinations of frequencies) that are dictated by their geometry and material properties. Since
these vibrations occur in the absence of a driving force, the associated frequencies are referred
to as _natural frequencies_. They describe how the system vibrates if left to
behave on its own. In contrast, driven linear systems vibrate at the
driving frequency. An amplification of the response (called resonance)
occurs when the driving frequency coincides with one of the natural
frequencies. In short, the system is driven at a frequency at which it
likes to vibrate. Large amplitude oscillations are the result. So it is
important to know what the natural frequencies are *a priori* so you can
avoid driving the system into resonance.

## Determining natural frequencies?

In this lab, you will measure the first 3 natural frequencies, $\omega_n$, of a rectangular beam using strain gauge data. 
Your goal is 
to measure the free response time series data using a strain gauge. With this data, you will
determine the first natural frequency in two ways: 

- (i) by peak counting in the time domain (which gives a very rough estimate of $\omega_n$)
- (ii) by a formal frequency domain analysis, using the [fast Fourier transform](https://en.wikipedia.org/wiki/Fast_Fourier_transform) (FFT). 

For a rectangular beam, analytic expressions of the natural frequencies exist,
and you can confirm that you're doing everything properly by getting the
analytical frequencies to agree with the experimental frequencies.

## Deliverables

For this assignment, you and your lab partner will submit a __joint report__ as a .pdf to your HuskyCT section within __one week__ of your lab date. It will only be necessary for one of you to submit the report. Please clearly mark, either in the body as footnotes or in the appendix as a separate section, what each of you contributed to the overall report.

You are limited to __5 pages__ (not including the title page, references, or appendix) and __4 figures__. Additional data, figures, and information can be put in an appendix. The appendix will not be graded, but you may refer to it to explain data, methods, or other relevant information.