import json
import colorsys

def hex_to_rgb(hex_color):
    """Convert hex color to RGB (0-1 range)"""
    hex_color = hex_color.lstrip('#')
    return tuple(int(hex_color[i:i+2], 16) / 255.0 for i in (0, 2, 4))

def rgb_to_hex(r, g, b):
    """Convert RGB (0-1 range) to hex"""
    return f"#{int(r*255):02X}{int(g*255):02X}{int(b*255):02X}"

def shift_hue(hex_color, hue_shift_degrees):
    """Shift the hue of a color by specified degrees"""
    # Convert hex to RGB
    r, g, b = hex_to_rgb(hex_color)
    
    # Convert RGB to HSV
    h, s, v = colorsys.rgb_to_hsv(r, g, b)
    
    # Shift hue by specified degrees (convert to 0-1 range)
    h_shifted = (h + hue_shift_degrees / 360.0) % 1.0
    
    # Convert back to RGB
    r_new, g_new, b_new = colorsys.hsv_to_rgb(h_shifted, s, v)
    
    # Convert back to hex
    return rgb_to_hex(r_new, g_new, b_new)

def create_tmrt_colors(input_file, output_file, hue_shift=10):
    """Create TMRT color definition by shifting NHS colors"""
    
    # Load NHS color data
    with open(input_file, 'r') as f:
        nhs_data = json.load(f)
    
    # Create TMRT data structure
    tmrt_data = {
        "palette_name": "TMRT Brand Palette",
        "columns": nhs_data["columns"],
        "groups": []
    }
    
    # Process each group
    for group in nhs_data["groups"]:
        new_group = {
            "name": group["name"].replace("NHS", "TMRT"),
            "colors": []
        }
        
        # Process each color in the group
        for color in group["colors"]:
            # Skip white and very neutral grays (they don't shift well)
            if color["hex"] in ["#FFFFFF", "#231F20"]:
                new_hex = color["hex"]
            else:
                new_hex = shift_hue(color["hex"], hue_shift)
            
            new_color = {
                "name": color["name"].replace("NHS", "TMRT"),
                "hex": new_hex
            }
            new_group["colors"].append(new_color)
        
        tmrt_data["groups"].append(new_group)
    
    # Save TMRT color data
    with open(output_file, 'w') as f:
        json.dump(tmrt_data, f, indent=2)
    
    print(f"TMRT color palette created: {output_file}")
    print(f"All colors shifted by {hue_shift} degrees on the color wheel")

if __name__ == "__main__":
    create_tmrt_colors('nhs_colour_definition.json', 'tmrt_colour_definition.json', 10)