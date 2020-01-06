Qn Scale
=========

Purpose
--------
Compute the Qn scale estimate for a variable.

Description
------------
The median absolute deviation (MAD) and interquartile range are the two most commonly used robust alternatives to the standard deviation. The MAD in particular is a very robust scale estimator. However, the MAD has the following limitations:

- It does not have particularly high efficiency for data that is in fact normal (37%). In comparison, the median has 64% efficiency for normal data.
- The MAD statistic also has an implicit assumption of symmetry. That is, it measures the distance from a measure of central location (the median).

Rousseeuw and Croux proposed the Qn estimate of scale as an alternative to the MAD. It shares desirable robustness properties with MAD (50% breakdown point, bounded influence function). In addition, it has significantly better normal efficiency (82%) and it does not depend on symmetry.

