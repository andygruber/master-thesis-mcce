#!/usr/bin/env python3
"""
Regenerate DevContainer setup difficulty figure in monochrome style
Based on data from Valstar et al. 2020 - Using DevContainers to Standardize Student Development Environments
"""

import matplotlib.pyplot as plt
import numpy as np

# Data from Valstar et al. 2020 (ITiCSE '20, page 5, Figure 3)
# Survey question: "How difficult/easy was it to set up the DevContainer?"
# Text states: 18% difficult/very difficult, 35% easy/very easy
# From visual inspection and text alignment
categories = ['1. Very\ndifficult', '2. Difficult', '3. Neutral',
              '4. Easy', '5. Very\neasy', 'Did not try\nto setup']
percentages = [3, 15, 33, 23, 12, 14]  # Sums to 100%, 18% difficult, 35% easy

# Verification
difficult_total = percentages[0] + percentages[1]  # Should be 18%
easy_total = percentages[3] + percentages[4]      # Should be 35%
print(f"Verification: Difficult+Very difficult = {difficult_total}% (should be 18%)")
print(f"Verification: Easy+Very easy = {easy_total}% (should be 35%)")

# Create figure with thesis-appropriate styling
fig, ax = plt.subplots(figsize=(10, 6))

# Define greyscale colors and hatching patterns for distinction
colors = ['0.2', '0.35', '0.5', '0.65', '0.8', '0.5']  # Gradient from dark to light
hatches = ['', '///', '', '\\\\\\', '', 'xxx']  # Varied patterns for distinction

# Create bars
x_pos = np.arange(len(categories))
bars = ax.bar(x_pos, percentages,
               color=colors,
               edgecolor='black',
               linewidth=1.5,
               width=0.7)

# Add hatching patterns for better distinction in monochrome
for bar, hatch in zip(bars, hatches):
    bar.set_hatch(hatch)

# Customize axes
ax.set_ylabel('% of students', fontsize=18, fontweight='bold')
ax.set_xlabel('Response', fontsize=18, fontweight='bold')
ax.set_title('How difficult/easy was it to set up the DevContainer?',
             fontsize=20, fontweight='bold', pad=20)
ax.set_xticks(x_pos)
ax.set_xticklabels(categories, fontsize=14)
ax.set_ylim(0, 40)

# Add horizontal grid for better readability
ax.yaxis.grid(True, linestyle='-', alpha=0.3, color='grey', linewidth=0.5)
ax.set_axisbelow(True)

# Customize tick parameters
ax.tick_params(axis='both', which='major', labelsize=14)

# Add value labels on top of bars
for i, pct in enumerate(percentages):
    ax.text(i, pct + 0.5, f'{pct}',
            ha='center', va='bottom', fontsize=14, fontweight='bold')

# Add reference lines and annotations for key insights
# Difficult/Very difficult (18%)
ax.axhline(y=18, xmin=0, xmax=0.21, color='black', linestyle='--',
           linewidth=1, alpha=0.5)
ax.text(-0.5, 19, '18% difficult', fontsize=13, style='italic')

# Easy/Very easy (35%)
ax.axhline(y=35, xmin=0.48, xmax=0.69, color='black', linestyle='--',
           linewidth=1, alpha=0.5)
ax.text(3.5, 36, '35% easy', fontsize=13, style='italic')

# Adjust layout to prevent label cutoff
plt.tight_layout()

# Save figure in multiple formats
output_base = 'c:/work/master-thesis-mcce/figures/devcontainer_setup_difficulty'
plt.savefig(f'{output_base}_thesis.png', dpi=300, bbox_inches='tight')
plt.savefig(f'{output_base}_thesis.pdf', bbox_inches='tight')

print(f"\nFigure saved to:")
print(f"  - {output_base}_thesis.png")
print(f"  - {output_base}_thesis.pdf")
print(f"\nSource: Valstar et al. (2020) - Using DevContainers to Standardize Student")
print(f"        Development Environments: An Experience Report. ITiCSE '20.")

plt.show()
