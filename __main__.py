# Update README.md file with all the images of the repo
import os

image_files = sorted([f for f in os.listdir('.') if f.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))], key=os.path.getmtime)
markdown_content = "# Recent Images\n\n" + '\n\n'.join(f"![{image}](./{image})" for image in image_files)
with open('README.md', 'w') as f:
    f.write(markdown_content)
