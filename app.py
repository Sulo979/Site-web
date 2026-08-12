from flask import Flask, request

app = Flask(__name__)

# Balise Meta pour l'adaptation mobile (crucial pour smartphones !)
META_VIEWPORT = "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"

# Styles réactifs (adaptés pour PC et Téléphones)
STYLE_TITRE = "style='color: #2c3e50; font-size: 2.5em; font-weight: bold; margin-bottom: 10px;'"
STYLE_BOUTON = "style='display: inline-block; padding: 15px 25px; background-color: #27ae60; color: white; text-decoration: none; border-radius: 50px; font-weight: bold; margin: 5px; box-shadow: 0 4px 6px rgba(0,0,0,0.1);'"
STYLE_CARTE = "style='display: inline-block; background-color: white; padding: 0; border-radius: 15px; margin: 15px 10px; box-shadow: 0px 10px 20px rgba(0,0,0,0.1); width: 90%; max-width: 340px; vertical-align: top; text-align: left; overflow: hidden;'"
STYLE_AVIS = "style='display: inline-block; background-color: white; padding: 20px; border-radius: 15px; margin: 15px 10px; box-shadow: 0px 5px 10px rgba(0,0,0,0.05); width: 90%; max-width: 300px; vertical-align: top; font-style: italic; border-left: 5px solid #27ae60; text-align: left; box-sizing: border-box;'"
STYLE_FOOTER = "style='background-color: #2c3e50; color: white; text-align: center; padding: 40px 20px; margin-top: 50px;'"
STYLE_INPUT = "style='width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; font-size: 1em;'"

@app.route("/")
def accueil():
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        {META_VIEWPORT}
        <title>Sulo Créateur</title>
    </head>
    <body style='background-color: #f8f9fa; font-family: Arial, sans-serif; margin: 0; padding: 0;'>
        <div style='padding: 60px 20px; background: linear-gradient(135deg, #ffffff, #f1f8e9); text-align: center;'>
            <h1 {STYLE_TITRE}>Sulo Créateur</h1>
            <p style='color: #7f8c8d; font-size: 1.2em; max-width: 600px; margin: 0 auto 25px auto;'>Développement de sites web modernes, rapides et optimisés pour tous les écrans.</p>
            <div>
                <a href="/portfolio" {STYLE_BOUTON}>Voir mes projets</a>
                <a href="/contact" {STYLE_BOUTON} style='background-color: #2980b9;'>Me contacter</a>
            </div>
        </div>

        <div style='padding: 50px 15px; text-align: center;'>
            <h2 style='color: #2c3e50; margin-bottom: 30px;'>Mes Expertises</h2>
            <div {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1517694712202-14dd9538aa97?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 200px; object-fit: cover;'>
                <div style='padding: 20px;'>
                    <h3 style='color: #27ae60; margin-top: 0;'>Développement Python</h3>
                    <p style='color: #666; font-size: 0.95em;'>Applications web sur-mesure et performantes avec Flask.</p>
                </div>
            </div>
            <div {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1542744095-291d1f67b221?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 200px; object-fit: cover;'>
                <div style='padding: 20px;'>
                    <h3 style='color: #27ae60; margin-top: 0;'>UX/UI Design</h3>
                    <p style='color: #666; font-size: 0.95em;'>Interfaces fluides, adaptées aux smartphones et PC.</p>
                </div>
            </div>
            <div {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1522202176988-66273c2fd55f?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 200px; object-fit: cover;'>
                <div style='padding: 20px;'>
                    <h3 style='color: #27ae60; margin-top: 0;'>Solutions Sur-Mesure</h3>
                    <p style='color: #666; font-size: 0.95em;'>Accompagnement de A à Z dans la création de votre projet.</p>
                </div>
            </div>
        </div>

        <div style='padding: 50px 20px; background-color: #ffffff; text-align: center;'>
            <h2 style='color: #2c3e50; margin-bottom: 20px;'>À propos de moi</h2>
            <p style='color: #555; font-size: 1.05em; max-width: 650px; margin: 0 auto; line-height: 1.6;'>
                Passionné par le développement web, je crée des sites performants, élégants et complètement adaptés aux mobiles pour vous aider à développer votre présence en ligne.
            </p>
        </div>

        <div style='padding: 50px 15px; text-align: center;'>
            <h2 style='color: #2c3e50; margin-bottom: 30px;'>Foire Aux Questions (FAQ)</h2>
            <div style='max-width: 600px; margin: 0 auto; text-align: left;'>
                <div style='background: white; padding: 15px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0px 2px 5px rgba(0,0,0,0.05);'>
                    <strong style='color: #2c3e50;'>Combien de temps prend la création d'un site ?</strong>
                    <p style='color: #555; margin: 5px 0 0 0;'>Généralement entre quelques jours et une semaine selon le projet.</p>
                </div>
                <div style='background: white; padding: 15px; margin-bottom: 15px; border-radius: 8px; box-shadow: 0px 2px 5px rgba(0,0,0,0.05);'>
                    <strong style='color: #2c3e50;'>Est-ce que le site fonctionne bien sur mobile ?</strong>
                    <p style='color: #555; margin: 5px 0 0 0;'>Oui, 100% responsive et optimisé pour une lisibilité parfaite sur téléphone.</p>
                </div>
            </div>
        </div>

        <div style='padding: 50px 15px; background-color: #ffffff; text-align: center;'>
            <h2 style='color: #2c3e50; margin-bottom: 30px;'>Avis Clients</h2>
            <div {STYLE_AVIS}>
                <p style='margin-top: 0;'>"Super travail, site livré très rapidement et idéal sur mon téléphone !"</p>
                <b style='color: #27ae60;'>- Thomas L.</b>
            </div>
            <div {STYLE_AVIS}>
                <p style='margin-top: 0;'>"Très professionnel, les images et le formulaire de contact sont top."</p>
                <b style='color: #27ae60;'>- Sarah M.</b>
            </div>
        </div>

        <div {STYLE_FOOTER}>
            <p style='margin: 0 0 15px 0;'>&copy; 2026 Sulo Créateur - Tous droits réservés.</p>
            <p style='margin: 0;'>
                <a href='/' style='color: #2ecc71; text-decoration: none; margin: 0 10px;'>Accueil</a> | 
                <a href='/portfolio' style='color: #2ecc71; text-decoration: none; margin: 0 10px;'>Portfolio</a> | 
                <a href='/contact' style='color: #2ecc71; text-decoration: none; margin: 0 10px;'>Contact</a>
            </p>
        </div>
    </body>
    </html>
    """

@app.route("/portfolio")
def portfolio():
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        {META_VIEWPORT}
        <title>Portfolio - Sulo Créateur</title>
    </head>
    <body style='background-color: #f8f9fa; font-family: Arial, sans-serif; text-align: center; padding: 40px 15px; margin: 0;'>
        <h1 {STYLE_TITRE}>Mes Réalisations</h1>
        <p style='color: #7f8c8d; font-size: 1.1em; margin-bottom: 30px;'>Projets récents développés pour mes clients.</p>
        
        <div>
            <div {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 200px; object-fit: cover;'>
                <div style='padding: 20px;'>
                    <h3 style='color: #27ae60; margin-top: 0;'>Site E-Commerce</h3>
                    <p style='color: #666;'>Boutique en ligne complète adaptée aux téléphones et ordinateurs.</p>
                </div>
            </div>
            <div {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 200px; object-fit: cover;'>
                <div style='padding: 20px;'>
                    <h3 style='color: #27ae60; margin-top: 0;'>Application Web Flask</h3>
                    <p style='color: #666;'>Outil de gestion fluide et rapide codé sur-mesure en Python.</p>
                </div>
            </div>
        </div>

        <br><br>
        <a href="/" {STYLE_BOUTON}>Retour à l'accueil</a>
    </body>
    </html>
    """

@app.route("/contact")
def contact():
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        {META_VIEWPORT}
        <title>Contact - Sulo Créateur</title>
    </head>
    <body style='background-color: #f8f9fa; font-family: Arial, sans-serif; text-align: center; padding: 40px 15px; margin: 0;'>
        <h1 style='color: #2c3e50; margin-bottom: 20px;'>Contactez-moi</h1>
        <div style='background: white; padding: 25px; border-radius: 15px; display: inline-block; width: 90%; max-width: 420px; box-shadow: 0px 5px 15px rgba(0,0,0,0.1); text-align: left; box-sizing: border-box;'>
            <form action="/traitement-contact" method="POST">
                <label style='color: #2c3e50; font-weight: bold;'>Votre nom :</label>
                <input type="text" name="nom" placeholder="Ex: Jean Dupont" required {STYLE_INPUT}>
                
                <label style='color: #2c3e50; font-weight: bold;'>Votre e-mail :</label>
                <input type="email" name="email" placeholder="Ex: jean@example.com" required {STYLE_INPUT}>
                
                <label style='color: #2c3e50; font-weight: bold;'>Type de projet :</label>
                <select name="projet" {STYLE_INPUT}>
                    <option value="Site Vitrine">Site Vitrine</option>
                    <option value="Application Python / Flask">Application Python / Flask</option>
                    <option value="Design UX/UI">Design UX/UI</option>
                    <option value="Autre demande">Autre demande</option>
                </select>
                
                <label style='color: #2c3e50; font-weight: bold;'>Votre message :</label>
                <textarea name="message" rows="4" placeholder="Parlez-moi de votre besoin..." required style='width: 100%; padding: 12px; margin: 10px 0; border: 1px solid #ddd; border-radius: 5px; box-sizing: border-box; font-family: Arial, sans-serif; font-size: 1em;'></textarea>
                
                <button type="submit" style='width: 100%; padding: 15px; background: #27ae60; color: white; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; margin-top: 10px; font-size: 1em;'>Envoyer le message</button>
            </form>
        </div>
        <br><br>
        <a href="/" {STYLE_BOUTON}>Retour à l'accueil</a>
    </body>
    </html>
    """

@app.route("/traitement-contact", methods=["POST"])
def traitement_contact():
    nom = request.form.get("nom")
    email = request.form.get("email")
    projet = request.form.get("projet")
    message = request.form.get("message")

    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        {META_VIEWPORT}
        <title>Confirmation - Sulo Créateur</title>
    </head>
    <body style='background-color: #f8f9fa; font-family: Arial, sans-serif; text-align: center; padding: 40px 15px; margin: 0;'>
        <h1 style='color: #27ae60;'>Message bien reçu !</h1>
        <div style='background-color: white; padding: 25px; border-radius: 15px; display: inline-block; width: 90%; max-width: 450px; box-shadow: 0px 5px 15px rgba(0,0,0,0.1); text-align: left; box-sizing: border-box;'>
            <p style='color: #2c3e50;'>Merci <b>{nom}</b>, votre demande concernant un <b>{projet}</b> a bien été enregistrée.</p>
            <p style='color: #555;'>Nous vous répondrons rapidement à l'adresse : <b>{email}</b></p>
            <div style='background: #f1f8e9; padding: 12px; border-left: 4px solid #27ae60; margin: 15px 0; color: #555;'>
                <em>"{message}"</em>
            </div>
        </div>
        <br><br>
        <a href="/" {STYLE_BOUTON}>Retour à l'accueil</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
