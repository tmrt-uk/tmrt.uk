import json
import os
import re

def clean_name(name):
    """Clean color name to create valid CSS variable/class names"""
    # Convert to lowercase
    clean = name.lower()
    # Replace spaces with hyphens
    clean = re.sub(r'\s+', '-', clean)
    # Remove parentheses and their contents
    clean = re.sub(r'\([^)]*\)', '', clean)
    # Remove any non-alphanumeric characters except hyphens
    clean = re.sub(r'[^a-z0-9-]', '', clean)
    # Remove multiple consecutive hyphens
    clean = re.sub(r'-+', '-', clean)
    # Remove leading/trailing hyphens
    clean = clean.strip('-')
    return clean

def generate_css(json_file, css_output_dir='assets/css'):
    """Generate CSS from any color definition JSON"""
    
    with open(json_file, 'r') as f:
        data = json.load(f)
    
    # Ensure output directory exists
    os.makedirs(css_output_dir, exist_ok=True)
    
    # Get palette name for file naming
    palette_name = data.get('palette_name', 'Brand Palette')
    file_prefix = clean_name(palette_name.split()[0])  # First word of palette name
    
    css_content = []
    css_content.append("---")
    css_content.append(f"# {palette_name}")
    css_content.append("---")
    css_content.append("")
    css_content.append(f"/* {palette_name} - Generated from JSON */")
    css_content.append("")
    
    # CSS Custom Properties
    css_content.append(":root {")
    
    for group in data['groups']:
        css_content.append(f"  /* {group['name']} */")
        for color in group['colors']:
            var_name = clean_name(color['name'])
            css_content.append(f"  --{var_name}: {color['hex']};")
        css_content.append("")
    
    css_content.append("}")
    css_content.append("")
    
    # Utility classes
    css_content.append("/* Background Colors */")
    for group in data['groups']:
        for color in group['colors']:
            class_name = clean_name(color['name'])
            css_content.append(f".bg-{class_name} {{ background-color: {color['hex']}; }}")
    
    css_content.append("")
    css_content.append("/* Text Colors */")
    for group in data['groups']:
        for color in group['colors']:
            class_name = clean_name(color['name'])
            css_content.append(f".text-{class_name} {{ color: {color['hex']}; }}")
    
    css_content.append("")
    css_content.append("/* Border Colors */")
    for group in data['groups']:
        for color in group['colors']:
            class_name = clean_name(color['name'])
            css_content.append(f".border-{class_name} {{ border-color: {color['hex']}; }}")
    
    # Write CSS file
    css_file = os.path.join(css_output_dir, f'{file_prefix}-colors.css')
    with open(css_file, 'w') as f:
        f.write('\n'.join(css_content))
    
    print(f"CSS generated: {css_file}")
    
    # Show what was generated
    print(f"\nGenerated CSS variables:")
    for group in data['groups']:
        for color in group['colors']:
            var_name = clean_name(color['name'])
            print(f"  --{var_name}: {color['hex']}")

if __name__ == "__main__":
    import sys
    
    if len(sys.argv) > 1:
        json_file = sys.argv[1]
    else:
        # Default to TMRT colors
        json_file = 'tmrt_colour_definition.json'
    
    generate_css(json_file)