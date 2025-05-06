# 🟢 Tableau de score rétro - Animation GIF

Ce projet génère un GIF animé à partir d'une image de tableau de score rétro, inspiré d'un visuel authentique.  
Il met en scène l'évolution du score entre deux clubs fictifs :

- **Stade Lamballais**
- **US Clohars-Carnoët**

## 🎯 Objectif

Afficher dynamiquement le passage du score de **3-3** à **4-3** à l’aide d’un visuel réaliste et fidèle au tableau d’affichage d’époque.

## 🛠️ Utilisation

1. Clone le dépôt :
```bash
git clone https://github.com/votre-utilisateur/retro-scoreboard.git
cd retro-scoreboard
```

2. Place l’image `ChatGPT_Image.png` fournie dans ce dossier.

3. Assure-toi d’avoir Python et Pillow :
```bash
pip install pillow
```

4. Lance le script :
```bash
python generate_scoreboard_from_template.py
```

✅ Un GIF `scoreboard.gif` sera généré, ainsi qu’un dossier `frames/` contenant les images intermédiaires.

---

## 🖼️ Résultat attendu

![Scoreboard](scoreboard.gif)
