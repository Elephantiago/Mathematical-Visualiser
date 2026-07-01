import numpy as np
import matplotlib.pyplot as plt

# -------------------------------------------------------------------------
# MATHEMATICAL SETUP: THE MATRIX OF THE CONCOCTED COINCIDENCE
# -------------------------------------------------------------------------
#
# $$e^{i\pi} = -1$$
#
# Taking the natural logarithm of both sides gives us a bridge between the two constants through the imaginary unit $i$:
# $$\ln(-1) = i\pi \implies \pi = \frac{\ln(-1)}{i}$$
#
# If we substitute this definition of $\pi$ directly into our original expression, we can completely eliminate $\pi$ from the equation:
# $$\left(\frac{\ln(-1)}{i}\right)^4 + \left(\frac{\ln(-1)}{i}\right)^5 \approx e^6$$
#
# Since $i^4 = 1$ and $i^5 = i$, this simplifies to a purely logarithmic/exponential landscape:
# $$\ln^4(-1) - i\ln^5(-1) \approx e^6$$
#
# What this tells us in a playful, complex-calculus sense is that if you plot a logarithmic spiral in the complex plane that rotates
# through the geometry of negative space, the sheer momentum of its 4th and 5th dimensional rotations warps the complex plane
# into a real-valued exponential growth curve of exactly magnitude 6.
#
#
#
# In complex analysis, the principal value of ln(-1) is exactly i * pi.
# We will track how its powers spiral through the complex plane.

ln_neg1 = complex(0, np.pi)

# Calculate the discrete steps (dimensions 0 through 5)
# n=0: 1 (Real)
# n=1: i*pi (Imaginary)
# n=2: -pi^2 (Negative Real -> "Negative Space")
# n=3: -i*pi^3 (Negative Imaginary)
# n=4: pi^4 (Real) -> The 4th Dimensional anchor
# n=5: i*pi^5 (Imaginary) -> The 5th Dimensional anchor
steps = [ln_neg1**n for n in range(6)]

# The final "warped" combination from our theory: pi^4 + pi^5
# Because: ln^4(-1) = pi^4  and  -i * ln^5(-1) = -i * (i * pi^5) = pi^5
warped_sum = (ln_neg1**4) - (1j * ln_neg1**5)
e_to_the_6 = np.exp(6)

# -------------------------------------------------------------------------
# VISUALIZATION ENGINE: CYBERPUNK DARK MODE
# -------------------------------------------------------------------------
plt.style.use('dark_background')
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7))
fig.suptitle("THE PI-E QUANTUM WORMHOLE VISUALIZER\nMapping the Expression: ln^4(-1) - i*ln^5(-1) ≈ e^6", 
             fontsize=16, color='#00ffcc', fontweight='bold')

# --- PANEL 1: THE COMPLEX PLANE SPIRAL ---
ax1.set_title("Discrete Logarithmic Spiral of ln^n(-1)", color='#ff007f', fontsize=12)

# Generate a continuous log spiral to visually connect the discrete dimensions
theta_continuous = np.linspace(0, 5 * np.pi / 2, 500)
# r = pi^(2*theta/pi) to match the discrete exponential steps at axes intersections
r_continuous = np.pi**(2 * theta_continuous / np.pi)
x_spiral = r_continuous * np.cos(theta_continuous)
y_spiral = r_continuous * np.sin(theta_continuous)
ax1.plot(x_spiral, y_spiral, color='#333333', linestyle='--', alpha=0.7, label='Logarithmic Phase Path')

# Plot the progression through "Negative Space" and Imaginary axes
colors = ['#ffffff', '#00ffcc', '#ff9900', '#ff007f', '#00ff00', '#00ffff']
for n, step in enumerate(steps):
    ax1.plot([0, step.real], [0, step.imag], color=colors[n], alpha=0.3)
    ax1.scatter(step.real, step.imag, color=colors[n], s=100, zorder=5,
                label=f"Dim {n}: ln^{n}(-1)" if n < 6 else "")
    # Label each dimension node
    ax1.text(step.real * 1.1, step.imag * 1.1 + 5, f"n={n}", color=colors[n], 
             fontsize=10, fontweight='bold', ha='center')

# Aesthetic tuning for Panel 1
ax1.axhline(0, color='#444444', linewidth=1)
ax1.axvline(0, color='#444444', linewidth=1)
ax1.set_xlabel("REAL SPACE", color='#ffffff')
ax1.set_ylabel("IMAGINARY SPACE", color='#ffffff')
ax1.grid(True, color='#222222')
ax1.set_xlim(-350, 150)
ax1.set_ylim(-50, 350)

# --- PANEL 2: THE 4D/5D DIMENSIONAL WARP TO E^6 ---
ax2.set_title("The Phase-Shift Warp onto the Real Axis", color='#00ffcc', fontsize=12)

# 1. Plot the continuous exponential growth curve e^x for reference
x_vals = np.linspace(0, 6.5, 200)
y_vals = np.exp(x_vals)
ax2.plot(x_vals, y_vals, color='#ff007f', linewidth=2, label='Real Exponential Growth Curve: e^x')

# 2. Plot the 4th dimension component on the real line: (x = 4, y = pi^4)
pi_4 = steps[4].real
ax2.scatter(4, pi_4, color='#00ff00', s=120, zorder=5)
ax2.text(3.6, pi_4 + 15, f"4D Anchor\n(π⁴ ≈ {pi_4:.2f})", color='#00ff00', ha='center', fontsize=9)

# 3. Simulate the 5th dimension warping onto the real axis
# Nominally, ln^5(-1) is purely imaginary (on the y-axis of the complex plane).
# Multiplying by -i rotates it -90 degrees, rendering it entirely real (π^5).
pi_5 = ( -1j * steps[5] ).real
ax2.scatter(5, pi_5, color='cyan', s=120, zorder=5)
ax2.text(4.6, pi_5 - 25, f"Warped 5D Anchor\n(-i * i*π⁵ = π⁵ ≈ {pi_5:.2f})", color='cyan', ha='center', fontsize=9)

# 4. Show the combined momentum vector reaching up to x=6
ax2.plot([4, 5, 6], [pi_4, pi_5, warped_sum.real], color='#00ffcc', linestyle='-', linewidth=2, 
         label='Vector Addition Path (π⁴ + π⁵)')

# 5. Highlight the final landing zone against e^6
ax2.scatter(6, warped_sum.real, color='#ffff00', s=200, marker='*', zorder=6, 
            label=f'Combined Value: {warped_sum.real:.5f}')
ax2.scatter(6, e_to_the_6, color='#ff007f', s=100, facecolors='none', edgecolors='#ff007f', linewidths=2, zorder=6,
            label=f'Target e⁶ Value: {e_to_the_6:.5f}')

# Draw a zoom-in callout box text to prove how close they are
error = abs(warped_sum.real - e_to_the_6)
ax2.text(1.5, 300, f"REAL-VALUED COLLISION DETAILS:\n"
                  f"----------------------------------\n"
                  f"π⁴ + π⁵ = {warped_sum.real:.7f}\n"
                  f"e⁶      = {e_to_the_6:.7f}\n"
                  f"Absolute Warp Error = {error:.7f}\n"
                  f"Precision Matrix: 99.999996%", 
         color='#ffffff', bbox=dict(facecolor='#111111', edgecolor='#00ffcc', boxstyle='round,pad=1'))

# Aesthetic tuning for Panel 2
ax2.set_xlabel("EXPONENTIAL MAGNITUDE (x)", color='#ffffff')
ax2.set_ylabel("VALUE OUTPUT", color='#ffffff')
ax2.grid(True, color='#222222')
ax2.set_xlim(0, 6.5)
ax2.set_ylim(0, 450)
ax2.legend(loc='lower right', fontsize=9)

# Show the manifestation of reality warping
plt.tight_layout()
plt.show()
