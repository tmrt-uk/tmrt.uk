import json
import matplotlib.pyplot as plt
import numpy as np
import colorsys

def hex_to_hsl(hex_color):
    """Convert hex color to HSL"""
    hex_color = hex_color.lstrip('#')
    r, g, b = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    r, g, b = r/255.0, g/255.0, b/255.0
    h, l, s = colorsys.rgb_to_hls(r, g, b)
    return h * 360, s * 100, l * 100

def plot_nhs_color_wheel(json_file):
    """Plot NHS colors on a color wheel with each level as a ring"""
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    fig, ax = plt.subplots(figsize=(12, 12), subplot_kw=dict(projection='polar'))
    
    # Define radius for each level (from inner to outer)
    level_radii = [0.3, 0.5, 0.7, 0.9]
    
    for level_idx, group in enumerate(data['groups']):
        colors = group['colors']
        
        for color in colors:
            hex_color = color['hex']
            
            # Get the actual hue position for this color
            hue, saturation, lightness = hex_to_hsl(hex_color)
            
            # Convert hue to radians (0-360 degrees to 0-2π radians)
            angle = hue * np.pi / 180
            
            # Use the level radius
            radius = level_radii[level_idx]
            
            # Plot as a circle at the correct hue position
            circle_size = 800  # Size of the color circle
            ax.scatter(angle, radius, c=hex_color, s=circle_size, alpha=0.9)
    
    # Remove all labels, ticks, and grid
    ax.set_rticks([])
    ax.set_thetagrids([])
    ax.grid(False)
    ax.set_ylim(0, 1.1)
    
    # Remove the outer circle
    ax.spines['polar'].set_visible(False)
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_nhs_color_wheel('nhs_colour_definition.json')