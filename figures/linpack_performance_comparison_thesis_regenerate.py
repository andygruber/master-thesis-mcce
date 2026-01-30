#!/usr/bin/env python3
"""
Regenerate Linpack performance comparison figure in monochrome style
Based on data from Felter et al. 2015
"""

import matplotlib.pyplot as plt
import numpy as np

# Data from Felter et al. 2015 - actual raw data
configurations = ['Native', 'Docker', 'KVM']
performance = [290.82864, 290.86775, 130.28326]  # GFLOPS (exact means)
std_dev = [1.13338588, 0.98102301, 7.56577276]  # Standard deviations (exact)

# Create figure with thesis-appropriate styling
fig, ax = plt.subplots(figsize=(8, 6))

# Define greyscale colors and patterns
colors = ['0.3', '0.5', '0.7']  # Dark grey, medium grey, light grey
hatches = ['', '///', '\\\\\\']  # No pattern, diagonal lines, reverse diagonal

# Create bars
x_pos = np.arange(len(configurations))
bars = ax.bar(x_pos, performance,
               color=colors,
               edgecolor='black',
               linewidth=1.5,
               width=0.6,
               yerr=std_dev,
               capsize=8,
               error_kw={'linewidth': 2, 'ecolor': 'black'})

# Add hatching patterns for better distinction in monochrome
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

# Customize axes
ax.set_ylabel('Linpack GFLOPS', fontsize=14, fontweight='bold')
ax.set_xlabel('Environment type', fontsize=14, fontweight='bold')
ax.set_xticks(x_pos)
ax.set_xticklabels(configurations, fontsize=12)
ax.set_ylim(0, 350)

# Add grid for better readability
ax.yaxis.grid(True, linestyle='-', alpha=0.3, color='grey', linewidth=0.5)
ax.set_axisbelow(True)

# Customize tick parameters
ax.tick_params(axis='both', which='major', labelsize=11)

# Add value labels on top of bars (rounded for display)
for i, (perf, std) in enumerate(zip(performance, std_dev)):
    ax.text(i, perf + std + 10, f'{perf:.1f}',
            ha='center', va='bottom', fontsize=11, fontweight='bold')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save figure in multiple formats
output_base = 'c:/work/master-thesis-mcce/figures/linpack_performance_comparison'
plt.savefig(f'{output_base}_thesis.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_base}_thesis.pdf', bbox_inches='tight')

print(f"Figure saved to:")
print(f"  - {output_base}_thesis.png")
print(f"  - {output_base}_thesis.pdf")

plt.show()
