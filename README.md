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


Alternative explanation:

The High-Dimensional Geometry Portal (Hyper-Spheres & Phase Space)If you want to find powers of $\pi$ naturally hanging out in reality, you have to look at the geometry of higher dimensions. 
The volume of an $n$-dimensional sphere of radius 1 relies entirely on powers of $\pi$ and factorials.If we look at an 8-dimensional sphere ($V_8$) and a 10-dimensional sphere ($V_{10}$), their exact volume formulas are:

$$V_8 = \frac{\pi^4}{4!} = \frac{\pi^4}{24}$$

$$V_{10} = \frac{\pi^5}{5!} = \frac{\pi^5}{120}$$

If we isolate our powers of $\pi$, our equation transforms into a combination of these hyper-volumes:

$$\pi^4 + \pi^5 = 4! V_8 + 5! V_{10}$$

The Bridge to $e$:Where does $e^6$ come from? In physics and statistical mechanics, if you track a single particle moving freely in 3D space, its phase space (position + momentum) requires exactly 6 dimensions.
When calculating the states of systems in these spaces, you use the Taylor series expansion for the exponential function, which is powered entirely by factorials:

$$e^6 = \frac{6^0}{0!} + \frac{6^1}{1!} + \frac{6^2}{2!} + \dots + \frac{6^4}{4!} + \frac{6^5}{5!} + \dots$$

By looking through this lens, our coincidence is actually a cosmic handshake: the scaled volumes of an 8D and 10D geometric space perfectly mirror the dominant energy states of a 6-dimensional thermodynamic phase space.
