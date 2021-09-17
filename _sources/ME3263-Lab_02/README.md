# Lab 2 - Static beam deflections with strain gauge

## What is a Strain Gauge?

A strain gauge consists of a looped wire that is embedded in a thin backing. Two
copper coated tabs serve as solder points for the leads. See Figure 1a. The
strain gauge is mounted to the structure, whose deformation is to be measured. As
the structure deforms, the wire stretches (increasing its net length ) and its
electrical resistance changes: $R=\rho L/A$, where $\rho$ is the material
resistivity, $L$ is the total length of the wire, and $A$ is the cross sectional
area of the wire.  Note that as $L$ increases, the cross sectional area changes
as
well due to the Poisson contraction; the resistivity also changes.

![Figure 1: a) A typical strain gauge. b) One common setup: the gauge is
mounted to measure the x-direction strain on the top surface. It's
engaged in a quarter bridge configuration of the Wheatstone bridge
circuit.](https://raw.githubusercontent.com/cooperrc/sensors_and_data/master/ME3263-Lab_02/figure_01.png)

*Figure 1: a) A typical strain gauge. b) One common setup: the gauge is
mounted to measure the x-direction strain on the top surface. It's
engaged in a quarter bridge configuration of the Wheatstone bridge
circuit.*

## Calibration and Use

By applying a known strain to the system, we can validate the calibration of our sensor. Once calibrated, it can be used to determine constitutive properties of our workpiece. In this case, we are interested in measuring Young's modulus. We will take measurements relating applied moment and exhibited strain of a cantilever beam in order to use a least-squares linear regression to determine Young's modulus.

## Deliverables

For this assignment, you and your lab partner will submit a __joint report__ as a .pdf to your HuskyCT section within __one week__ of your lab date. It will only be necessary for one of you to submit the report. Please clearly mark, either in the body as footnotes or in the appendix as a separate section, what each of you contributed to the overall report.

You are limited to __5 pages__ (not including the title page, references, or appendix) and __4 figures__. Additional data, figures, and information can be put in an appendix. The appendix will not be graded, but you may refer to it to explain data, methods, or other relevant information.