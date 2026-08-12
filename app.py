from flask import Flask, request

app = Flask(__name__)

STYLE_TITRE = "style='color: #2c3e50; font-size: 3em;'"
STYLE_BOUTON = "style='display: inline-block; padding: 10px 20px; background-color: #3498db; color: white; text-decoration: none; border-radius: 5px; margin: 10px; font-weight: bold;'"
STYLE_INPUT = "style='width: 100%; padding: 10px; margin: 10px 0; border: 1px solid #ccc; border-radius: 5px; box-sizing: border-box;'"
STYLE_CARTE = "style='display: inline-block; background-color: white; padding: 20px; border-radius: 10px; margin: 10px; width: 220px; text-align: left; box-shadow: 0 4px 8px rgba(0,0,0,0.1); vertical-align: top;'"
STYLE_AVIS = "style='display: inline-block; background-color: white; padding: 20px; border-radius: 10px; margin: 10px; width: 250px; text-align: left; box-shadow: 0 4px 8px rgba(0,0,0,0.1); vertical-align: top;'"

@app.route("/")
def accueil():
    return f"""
    <body style='background-color: #f4f7f6; font-family: Arial, sans-serif; text-align: center; padding: 50px;'>
        <h1 {STYLE_TITRE}>Besoin d'un site web ?</h1>
        <p style='color: #7f8c8d; font-size: 1.2em;'>Je crée des sites personnalisés pour vos projets et vos besoins sur Internet.</p>
        
        <img src='https://images.unsplash.com/photo-1498050108023-c5249f4df085?ixlib=rb-4.0.3&auto=format&fit=crop&w=600&q=80' alt='Paysage Web' style='max-width: 100%; border-radius: 15px; box-shadow: 0 4px 8px rgba(0,0,0,0.2); margin: 20px 0;'>
        <br>
        
        <a href="/apropos" {STYLE_BOUTON}>Qui suis-je ?</a>
        <a href="/services" {STYLE_BOUTON}>Mes services</a>
        <a href="/contact" {STYLE_BOUTON}>Me contacter</a>
        
        <br><br><hr style='width: 50%; border: 0; border-top: 1px solid #bdc3c7; margin: 40px auto;'><br>
        
        <h2 style='color: #2c3e50;'>Mes réalisations</h2>
        
        <div {STYLE_CARTE}>
            <h3 style='color: #2c3e50; margin-top: 0;'>Site Vitrine</h3>
            <p style='color: #555;'>Un site moderne et élégant conçu pour présenter une activité professionnelle.</p>
        </div>
        
        <div {STYLE_CARTE}>
            <h3 style='color: #2c3e50; margin-top: 0;'>Boutique en ligne</h3>
            <p style='color: #555;'>Une plateforme e-commerce intuitive pour vendre des produits facilement.</p>
        </div>

        <div {STYLE_CARTE}>
            <h3 style='color: #2c3e50; margin-top: 0;'>Site CV personnel</h3>
            <p style='color: #555;'>Un portfolio interactif pour mettre en valeur ses compétences et son parcours.</p>
        </div>

        <div {STYLE_CARTE}>
            <h3 style='color: #2c3e50; margin-top: 0;'>Blog de voyage</h3>
            <p style='color: #555;'>Un espace personnalisé pour partager des récits et des photos du monde entier.</p>
        </div>

        <div {STYLE_CARTE}>
            <h3 style='color: #2c3e50; margin-top: 0;'>Site de Restaurant</h3>
            <p style='color: #555;'>Une présentation interactive du menu avec un système de réservation en ligne.</p>
        </div>
        
        <br><br><hr style='width: 50%; border: 0; border-top: 1px solid #bdc3c7; margin: 40px auto;'><br>
        
        <h2 style='color: #2c3e50;'>Ce qu'en disent nos clients</h2>
        
        <div {STYLE_AVIS}>
            <p style='color: #555; font-style: italic;'>&quot;Super travail ! Mon site est magnifique et mes ventes ont augmenté.&quot;</p>
            <p style='color: #2980b9; font-weight: bold; margin-bottom: 0;'>- Thomas M.</p>
        </div>
        
        <div {STYLE_AVIS}>
            <p style='color: #555; font-style: italic;'>&quot;Rapide, efficace et à l'écoute. Je recommande les yeux fermés !&quot;</p>
            <p style='color: #2980b9; font-weight: bold; margin-bottom: 0;'>- Sarah L.</p>
        </div>
    </body>
    """

@app.route("/apropos")
def apropos():
    return f"""
    <body style='background-color: #f4f7f6; font-family: Arial, sans-serif; text-align: center; padding: 50px;'>
        <h1 {STYLE_TITRE}>À propos de moi</h1>
        <div style='background-color: white; padding: 30px; border-radius: 10px; display: inline-block; text-align: left; max-width: 600px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
            <p style='color: #34495e; font-size: 1.1em; line-height: 1.6em;'>
                Bonjour ! Je suis développeur web. Vous avez un projet, une idée de boutique en ligne pour vendre vos produits, ou vous avez besoin d'une présence sur Internet ? Je vous accompagne de A à Z pour créer un site sur mesure, moderne et adapté à vos besoins.
            </p>
        </div>
        <br>
        <a href="/" {STYLE_BOUTON}>Retour à l'accueil</a>
    </body>
    """

@app.route("/services")
def services():
    return f"""
    <body style='background-color: #f4f7f6; font-family: Arial, sans-serif; text-align: center; padding: 50px;'>
        <h1 {STYLE_TITRE}>Mes services</h1>
        
        <div style='background-color: white; padding: 25px; border-radius: 10px; display: inline-block; text-align: left; max-width: 500px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); margin-bottom: 20px;'>
            <ul style='list-style-type: none; padding: 0; font-size: 1.1em; color: #34495e; line-height: 2em;'>
                <li>✅ Création de sites vitrine</li>
                <li>✅ Boutiques en ligne / Vente de produits</li>
                <li>✅ Sites personnels ou CV</li>
                <li>📱 Design 100% adapté sur téléphone et ordinateur</li>
            </ul>
            <p style='font-size: 1.3em; color: #27ae60; font-weight: bold; margin-top: 20px;'>Tarif : À partir de 150 €</p>
        </div>
        
        <br>
        <a href="/contact" style='display: inline-block; padding: 12px 25px; background-color: #27ae60; color: white; text-decoration: none; border-radius: 5px; font-weight: bold; margin: 10px;'>Demander un devis gratuit</a>
        <br>
        <a href="/" {STYLE_BOUTON}>Retour à l'accueil</a>
    </body>
    """

@app.route("/contact")
def contact():
    return f"""
    <body style='background-color: #f4f7f6; font-family: Arial, sans-serif; text-align: center; padding: 50px;'>
        <h1 {STYLE_TITRE}>Contactez-moi</h1>
        <div style='background-color: white; padding: 30px; border-radius: 10px; display: inline-block; text-align: left; width: 400px; box-shadow: 0 4px 8px rgba(0,0,0,0.1);'>
            <form action='/traitement-contact' method='POST'>
                <label style='color: #34495e; font-weight: bold;'>Votre nom :</label><br>
                <input type='text' name='nom' placeholder='Ex: Jean Dupont' {STYLE_INPUT}><br>
                
                <label style='color: #34495e; font-weight: bold;'>Votre e-mail :</label><br>
                <input type='email' name='email' placeholder='Ex: jean@example.com' {STYLE_INPUT}><br>
                
                <label style='color: #34495e; font-weight: bold;'>Votre projet / message :</label><br>
                <textarea name='message' rows='4' placeholder='Parlez-moi de votre besoin...' {STYLE_INPUT}></textarea><br>
                
                <button type='submit' style='background-color: #2ecc71; color: white; padding: 10px 20px; border: none; border-radius: 5px; font-weight: bold; cursor: pointer; width: 100%;'>Envoyer le message</button>
            </form>
        </div>
        <br>
        <a href="/" {STYLE_BOUTON}>Retour à l'accueil</a>
    </body>
    """

@app.route("/traitement-contact", methods=["POST"])
def traitement_contact():
    # Récupération des données tapées par l'utilisateur
    nom = request.form.get("nom")
    email = request.form.get("email")
    message = request.form.get("message")
    
    # Pour l'instant, on affiche une page de confirmation simple
    return f"""
    <body style='background-color: #f4f7f6; font-family: Arial, sans-serif; text-align: center; padding: 50px;'>
        <h1 style='color: #27ae60;'>Message bien reçu !</h1>
        <div style='background-color: white; padding: 30px; border-radius: 10px; display: inline-block; max-width: 500px; box-shadow: 0 4px 8px rgba(0,0,0,0.1); text-align: left;'>
            <p style='color: #34495e; font-size: 1.1em;'>Merci <b>{nom}</b>, votre message a bien été pris en compte.</p>
            <p style='color: #555;'>Nous vous répondrons rapidement à l'adresse : <b>{email}</b></p>
        </div>
        <br><br>
        <a href="/" {STYLE_BOUTON}>Retour à l'accueil</a>
    </body>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
