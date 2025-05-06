from PIL import Image, ImageDraw, ImageFont
import os

# Chemin vers l’image de base (nom inchangé)
image_path = "ChatGPT_Image.png"
output_dir = "frames"
os.makedirs(output_dir, exist_ok=True)

# Coordonnées des zones du score
left_box = (180, 500, 380, 850)
right_box = (1150, 500, 1350, 850)

# Couleurs et police
bg_color = (26, 29, 23)  # fond du tableau
text_color = (240, 230, 210)  # beige clair
font = ImageFont.truetype("/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf", 300)

# Séquence du score (évolution)
score_sequence = [("3", "3"), ("3", "3"), ("3", "3"), ("4", "3"), ("4", "3")]

# Génération des images
for i, (left, right) in enumerate(score_sequence):
    base = Image.open(image_path).convert("RGBA")
    draw = ImageDraw.Draw(base)

    # Réinitialiser zones
    draw.rectangle(left_box, fill=bg_color)
    draw.rectangle(right_box, fill=bg_color)

    # Afficher les nouveaux scores
    draw.text(((left_box[0] + left_box[2]) // 2, (left_box[1] + left_box[3]) // 2),
              left, font=font, fill=text_color, anchor="mm")
    draw.text(((right_box[0] + right_box[2]) // 2, (right_box[1] + right_box[3]) // 2),
              right, font=font, fill=text_color, anchor="mm")

    base.save(f"{output_dir}/frame_{i}.png")

# Créer le GIF final
frames = [Image.open(f"{output_dir}/frame_{i}.png") for i in range(len(score_sequence))]
frames[0].save("scoreboard.gif", save_all=True, append_images=frames[1:], duration=800, loop=0)
