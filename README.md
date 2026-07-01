# Mathematical-Visualiser
Visualiser that explains why pi ^ 4 + pi ^ 5 is almost equal to e ^ 6. Read introductory comment inside of the source code for further details and derivation of the formula.


$$e^{i\pi} = -1$$
 
Taking the natural logarithm of both sides gives us a bridge between the two constants through the imaginary unit $i$:
$$\ln(-1) = i\pi \implies \pi = \frac{\ln(-1)}{i}$$

If we substitute this definition of $\pi$ directly into our original expression, we can completely eliminate $\pi$ from the equation:
$$\left(\frac{\ln(-1)}{i}\right)^4 + \left(\frac{\ln(-1)}{i}\right)^5 \approx e^6$$

Since $i^4 = 1$ and $i^5 = i$, this simplifies to a purely logarithmic/exponential landscape:
$$\ln^4(-1) - i\ln^5(-1) \approx e^6$$

What this tells us in a playful, complex-calculus sense is that if you plot a logarithmic spiral in the complex plane that rotates
through the geometry of negative space, the sheer momentum of its 4th and 5th dimensional rotations warps the complex plane
into a real-valued exponential growth curve of exactly magnitude 6.
