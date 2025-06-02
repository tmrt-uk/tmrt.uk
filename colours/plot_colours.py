import json
import matplotlib.pyplot as plt
import matplotlib.patches as patches

def plot_color_palettes(nhs_file, tmrt_file):
    """Plot NHS and TMRT color palettes side by side for comparison"""
    
    # Load both color files
    with open(nhs_file, 'r') as f:
        nhs_data = json.load(f)
    
    with open(tmrt_file, 'r') as f:
        tmrt_data = json.load(f)
    
    # Create single figure
    fig, ax = plt.subplots(1, 1, figsize=(20, 12))
    
    y_pos = 0
    centerline = 0
    
    for group_idx, (nhs_group, tmrt_group) in enumerate(zip(nhs_data['groups'], tmrt_data['groups'])):
        nhs_colors = nhs_group['colors']
        tmrt_colors = tmrt_group['colors']
        
        # Plot group titles
        ax.text(-4, y_pos, nhs_group['name'], fontsize=12, fontweight='bold', 
               ha='right', va='center')
        ax.text(4, y_pos, tmrt_group['name'], fontsize=12, fontweight='bold', 
               ha='left', va='center')
        
        # Plot each color pair
        for i, (nhs_color, tmrt_color) in enumerate(zip(nhs_colors, tmrt_colors)):
            color_y = y_pos - 0.5 - (i * 1.2)
            
            # NHS color (left side - adjacent to centerline) - 50% taller
            nhs_rect = patches.Rectangle((-1.5, color_y - 0.6), 1.5, 1.2, 
                                       facecolor=nhs_color['hex'], edgecolor='black', linewidth=1)
            ax.add_patch(nhs_rect)
            
            # NHS color name and hex
            ax.text(-1.7, color_y, nhs_color['name'], fontsize=10, ha='right', va='center')
            ax.text(-1.7, color_y - 0.4, nhs_color['hex'], fontsize=8, ha='right', va='center', color='gray')
            
            # TMRT color (right side - adjacent to centerline) - 50% taller
            tmrt_rect = patches.Rectangle((0, color_y - 0.6), 1.5, 1.2, 
                                        facecolor=tmrt_color['hex'], edgecolor='black', linewidth=1)
            ax.add_patch(tmrt_rect)
            
            # TMRT color name and hex
            ax.text(1.7, color_y, tmrt_color['name'], fontsize=10, ha='left', va='center')
            ax.text(1.7, color_y - 0.4, tmrt_color['hex'], fontsize=8, ha='left', va='center', color='gray')
        
        # Move down for next group
        y_pos -= max(len(nhs_colors), len(tmrt_colors)) * 1.2 + 1.5
    
    # Draw centerline
    ax.axvline(x=centerline, color='lightgray', linestyle='--', alpha=0.5)
    
    # Set plot properties
    ax.set_xlim(-6, 6)
    ax.set_ylim(y_pos, 2)
    ax.set_title('NHS vs TMRT Color Palette Comparison', fontsize=16, fontweight='bold', pad=20)
    ax.axis('off')
    
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_color_palettes('nhs_colour_definition.json', 'tmrt_colour_definition.json')