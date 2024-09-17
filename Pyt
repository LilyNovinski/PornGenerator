import urllib.parse

def generate_google_search_link():
    def input_with_skip(prompt):
        return input(f"{prompt} (Cliquez sur Entrée si vous vous en fichez) : ").lower()

    skin_tone_input = input_with_skip("Quel pourcentage de couleur de peau préférez-vous? (0% étant albino, 100% étant noir complet)")
    if skin_tone_input.isdigit():
        skin_tone = int(skin_tone_input)
        if 0 <= skin_tone < 20:
            skin_tag = 'albino'
        elif 20 <= skin_tone < 40:
            skin_tag = 'light-skinned'
        elif 40 <= skin_tone < 60:
            skin_tag = 'olive-skinned'
        elif 60 <= skin_tone < 80:
            skin_tag = 'brown-skinned'
        else:
            skin_tag = 'dark-skinned'
    else:
        skin_tag = ""

    yeux_bridés = input_with_skip("Préférez-vous des yeux bridés? (oui/non)")
    yeux_tag = 'slanted eyes' if yeux_bridés == "oui" else ""

    hair_input = input_with_skip("Quel pourcentage de couleur de cheveux préférez-vous? (0% étant blanc, 100% étant noir, tapez 'couleur' pour des couleurs hors du commun)")
    if hair_input.isdigit():
        hair_color_percentage = int(hair_input)
        if 0 <= hair_color_percentage <= 10:
            hair_tag = 'white hair'
        elif 11 <= hair_color_percentage <= 30:
            hair_tag = 'blonde hair'
        elif 31 <= hair_color_percentage <= 50:
            hair_tag = 'light brown hair'
        elif 51 <= hair_color_percentage <= 70:
            hair_tag = 'dark brown hair'
        elif 71 <= hair_color_percentage <= 90:
            hair_tag = 'brunette hair'
        elif 91 <= hair_color_percentage <= 100:
            hair_tag = 'black hair'
        else:
            hair_tag = ""
    elif hair_input == "couleur":
        couleur = input_with_skip("Sélectionnez une couleur (rouge, orange, jaune, vert, bleu, violet, rose, rainbow)")
        color_map = {
            "rouge": "red", "orange": "orange", "jaune": "yellow", "vert": "green",
            "bleu": "blue", "violet": "purple", "rose": "pink", "rainbow": "rainbow"
        }
        if couleur in color_map:
            shade = input_with_skip("Voulez-vous que la couleur soit claire, foncée ou vive?")
            shade_map = {"claire": "light", "foncée": "dark", "vive": "bright"}
            hair_tag = f'{shade_map.get(shade, "")} {color_map[couleur]} hair' if shade else f'{color_map[couleur]} hair'
        else:
            hair_tag = ""
    else:
        hair_tag = ""

    origine = input_with_skip("Préférez-vous une région ou un continent spécifique (Est, Ibérique, Maghrébine, Orientale, Latinas, Israélienne, Autochtone, Indienne, Afrique, Asie, Europe, Amérique, Océanie)? ")
    region_map = {
        "est": "eastern european", "ibérique": "iberian", "maghrébine": "maghreb", "orientale": "middle eastern", "latinas": "latina",
        "israélienne": "israeli", "autochtones": "native american", "indienne": "indian", "afrique": "african", "asie": "asian",
        "europe": "european", "amérique": "american", "océanie": "oceanian"
    }
    origine_tag = region_map.get(origine, "")

    corpulence = input_with_skip("Préférez-vous une femme mince, moyenne ou ronde? ")
    corpulence_tag = corpulence if corpulence in ["mince", "moyenne", "ronde"] else ""

    age = input_with_skip("Quel âge préférez-vous? (18 à 80 ans) ")
    if age.isdigit() and 18 <= int(age) <= 80:
        age = int(age)
        if 18 <= age < 25:
            age_tag = "teen"
        elif 25 <= age < 35:
            age_tag = "young adult"
        elif 35 <= age < 50:
            age_tag = "mature"
        elif 50 <= age < 70:
            age_tag = "milf"
        else:
            age_tag = "granny"
    else:
        age_tag = ""

    poitrine = input_with_skip("Quelle taille de poitrine préférez-vous (petite, moyenne, grosse)? ")
    poitrine_tag = f'{poitrine} breasts' if poitrine in ["petite", "moyenne", "grosse"] else ""

    sexe = input_with_skip("Quel type de sexe préférez-vous (normal, poilu, très poilu, taillé, épilé)? ")
    sexe_map = {
        "normal": "normal pussy", "poilu": "hairy pussy", "très poilu": "bushy pussy", "taillé": "trimmed pussy", "épilé": "shaved pussy"
    }
    sexe_tag = sexe_map.get(sexe, "")

    tatouage = input_with_skip("Tatouée ou non? (oui/non) ")
    tatouage_tag = "tattooed" if tatouage == "oui" else ""

    piercing = input_with_skip("Piercing ou non? (oui/non) ")
    piercing_tag = "pierced" if piercing == "oui" else ""

    role = input_with_skip("Préférez-vous une dominatrice ou une soumise? ")
    role_map = {"dominatrice": "dominatrix", "soumise": "submissive"}
    role_tag = role_map.get(role, "")

    group_size = input_with_skip("Combien de personnes? (donnez un chiffre): ")
    if group_size.isdigit():
        group_size = int(group_size)
        if group_size == 1:
            group_tag = "solo"
        elif group_size == 2:
            group_tag = "couple"
        elif group_size == 3:
            group_tag = "threesome"
        elif group_size == 4:
            group_tag = "foursome"
        elif group_size > 4:
            choice = input_with_skip("Préférez-vous un gangbang ou une orgie? ")
            group_tag = "gangbang" if choice == "gangbang" else "orgy" if choice == "orgie" else ""
        else:
            group_tag = ""
    else:
        group_tag = ""

    sexe_type = input_with_skip("Préférez-vous du sexe soft ou hard? ")
    sexe_type_tag = sexe_type if sexe_type in ["soft", "hard"] else ""

    media_type = input_with_skip("Préférez-vous une image, une vidéo ou un GIF? ")

    # Générer l'URL en fonction du type de média sélectionné
    query = f'{skin_tag} {origine_tag} {yeux_tag} {hair_tag} {corpulence_tag} {age_tag} {poitrine_tag} {sexe_tag} {tatouage_tag} {piercing_tag} {role_tag} {group_tag} {sexe_type_tag} "porn"'
    query = " ".join(query.split())
    encoded_query = urllib.parse.quote(query)

    if media_type == "vidéo":
        google_url = f"https://www.google.com/search?q={encoded_query}&sca_esv=98d43e591c93d847&sca_upv=1&hl=fr&sxsrf=ADLYWIIQSXkR_VUUQqAAggrzqXqYa87jHw%3A1726548943583&tbm=vid&source=hp&ei=zwvpZoGjIdaJkdUPlO_1kQ8&iflsig=AL9hbdgAAAAAZukZ37fhY6q4QJXxYhgdFOyO70BFCCpW&ved=0ahUKEwjBxt6DmMmIAxXWRKQEHZR3PfIQ4dUDCBM&uact=5&oq={encoded_query}&gs_lp=Egx3aXotdmlkZW8taHAiFGxlIGxpZW4gZGUgcmVjaGVyY2hl"
    else:
        google_url = f"https://www.google.com/search?q={encoded_query}&tbm=isch"

    print(f"Le lien de recherche Google est : {google_url}")

generate_google_search_link()
