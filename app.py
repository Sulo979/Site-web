from flask import Flask

app = Flask(__name__)

META_VIEWPORT = "<meta name='viewport' content='width=device-width, initial-scale=1.0'>"

GLOBAL_STYLE = """
<style>
    .hover-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }
    .hover-card:hover {
        transform: translateY(-8px);
        box-shadow: 0px 20px 40px rgba(16, 185, 129, 0.3) !important;
    }
    .btn-effect {
        transition: all 0.3s ease;
    }
    .btn-effect:hover {
        transform: scale(1.05);
        filter: brightness(1.15);
    }
    .badge {
        display: inline-block;
        padding: 8px 16px;
        background: linear-gradient(135deg, rgba(16, 185, 129, 0.15), rgba(5, 150, 105, 0.15));
        color: #047857;
        border-radius: 20px;
        font-weight: bold;
        margin: 6px;
        border: 2px solid rgba(16, 185, 129, 0.3);
    }
    .price-card {
        background: linear-gradient(135deg, #ffffff, #f0fdf4);
        padding: 30px;
        border-radius: 20px;
        border: 2px solid #10b981;
        flex: 1;
        min-width: 280px;
        max-width: 320px;
        box-shadow: 0 10px 25px rgba(16, 185, 129, 0.12);
        text-align: left;
        display: inline-block;
        margin: 15px;
        vertical-align: top;
    }
    .faq-box {
        background: linear-gradient(135deg, #ffffff, #f0fdf4);
        border-left: 5px solid #10b981;
        padding: 20px;
        margin: 15px auto;
        max-width: 700px;
        text-align: left;
        border-radius: 0 12px 12px 0;
        box-shadow: 0 4px 15px rgba(16, 185, 129, 0.08);
    }
    .social-btn {
        display: inline-block;
        padding: 10px 20px;
        background: linear-gradient(135deg, #3b82f6, #1d4ed8);
        color: white;
        text-decoration: none;
        border-radius: 25px;
        font-weight: bold;
        margin: 5px;
        box-shadow: 0 4px 12px rgba(59, 130, 246, 0.3);
    }
</style>
"""

STYLE_TITRE = "style='color: #ffffff; font-size: 3.2em; font-weight: bold; margin-bottom: 15px; text-shadow: 0 4px 20px rgba(5, 150, 105, 0.6);'"
STYLE_BOUTON = "style='display: inline-block; padding: 15px 30px; background: linear-gradient(135deg, #10b981, #059669); color: white; text-decoration: none; border-radius: 50px; font-weight: bold; margin: 8px; box-shadow: 0 4px 20px rgba(16, 185, 129, 0.5);'"
STYLE_BOUTON_ALT = "style='display: inline-block; padding: 15px 30px; background: linear-gradient(135deg, #0284c7, #0369a1); color: white; text-decoration: none; border-radius: 50px; font-weight: bold; margin: 8px; box-shadow: 0 4px 20px rgba(2, 132, 199, 0.5);'"
STYLE_CARTE = "style='display: inline-block; background: linear-gradient(135deg, #ffffff, #f0fdf4); padding: 0; border-radius: 16px; margin: 20px 10px; box-shadow: 0px 10px 25px rgba(16, 185, 129, 0.12); width: 90%; max-width: 340px; vertical-align: top; text-align: left; overflow: hidden; border: 2px solid rgba(16, 185, 129, 0.2);'"
STYLE_AVIS = "style='display: inline-block; background: linear-gradient(135deg, #ffffff, #ecfdf5); padding: 25px; border-radius: 16px; margin: 15px 10px; box-shadow: 0px 8px 20px rgba(16, 185, 129, 0.08); width: 90%; max-width: 270px; vertical-align: top; font-style: italic; border-left: 6px solid #10b981; text-align: left; box-sizing: border-box;'"
STYLE_FOOTER = "style='background: linear-gradient(135deg, #064e3b, #022c22); color: #cbd5e1; text-align: center; padding: 50px 20px; margin-top: 60px; border-top: 3px solid #10b981;'"
STYLE_INPUT = "style='width: 100%; padding: 14px; margin: 10px 0; border: 2px solid #34d399; border-radius: 8px; box-sizing: border-box; font-size: 1em; background: #fafafa;'"

@app.route("/")
def accueil():
    return f"""
    <!DOCTYPE html>
    <html lang="fr">
    <head>
        <meta charset="UTF-8">
        {META_VIEWPORT}
        <title>Sulo Créateur - Expert Web & Gaming Universe</title>
        {GLOBAL_STYLE}
    </head>
    <body style='background-color: #f4fbf7; font-family: "Segoe UI", Roboto, sans-serif; margin: 0; padding: 0; color: #1e293b;'>
        
        <!-- Bannière haute -->
        <div style='padding: 100px 20px; background: linear-gradient(135deg, #064e3b, #059669, #10b981); text-align: center;'>
            <h1 {STYLE_TITRE}>Sulo Créateur</h1>
            <p style='color: #d1fae5; font-size: 1.3em; max-width: 650px; margin: 0 auto 30px auto; line-height: 1.5; font-weight: 500;'>Développement de sites web modernes, applications interactives et univers gaming sur-mesure.</p>
            <div>
                <a href="/portfolio" class="btn-effect" {STYLE_BOUTON}>Voir mes 12 projets</a>
                <a href="#tarifs-section" class="btn-effect" {STYLE_BOUTON_ALT}>Voir nos tarifs</a>
            </div>
        </div>

        <!-- Section Statistiques -->
        <div style='background: linear-gradient(90deg, #ffffff, #ecfdf5); padding: 40px 20px; text-align: center; border-bottom: 2px solid #34d399;'>
            <div style='display: flex; flex-wrap: wrap; justify-content: center; gap: 35px; max-width: 1100px; margin: 0 auto;'>
                <div>
                    <h2 style='color: #059669; margin: 0; font-size: 2.8em;'>+35</h2>
                    <p style='color: #475569; margin: 5px 0 0 0; font-weight: bold;'>Projets Réalisés</p>
                </div>
                <div>
                    <h2 style='color: #0284c7; margin: 0; font-size: 2.8em;'>100%</h2>
                    <p style='color: #475569; margin: 5px 0 0 0; font-weight: bold;'>Clients Satisfaits</p>
                </div>
                <div>
                    <h2 style='color: #7c3aed; margin: 0; font-size: 2.8em;'>5+</h2>
                    <p style='color: #475569; margin: 5px 0 0 0; font-weight: bold;'>Années de Passion</p>
                </div>
                <div>
                    <h2 style='color: #d97706; margin: 0; font-size: 2.8em;'>24/7</h2>
                    <p style='color: #475569; margin: 5px 0 0 0; font-weight: bold;'>Suivi & Support</p>
                </div>
            </div>
        </div>

        <!-- Section Compétences & Technologies -->
        <div style='padding: 60px 20px; background: #ecfdf5; text-align: center;'>
            <h2 style='color: #047857; font-size: 2.4em; margin-bottom: 15px;'>Technologies & Compétences</h2>
            <p style='color: #64748b; margin-bottom: 30px;'>Les outils puissants que j'utilise :</p>
            <div style='max-width: 800px; margin: 0 auto;'>
                <span class="badge">Python</span>
                <span class="badge">Flask</span>
                <span class="badge">HTML5 / CSS3</span>
                <span class="badge">JavaScript</span>
                <span class="badge">UI / UX Design</span>
                <span class="badge">Game Dev & Web Gaming</span>
                <span class="badge">Intégration Streaming & Discord</span>
                <span class="badge">Responsive Design</span>
            </div>
        </div>

        <!-- Expertises avec images -->
        <div style='padding: 70px 15px; text-align: center; background: #ffffff;'>
            <h2 style='color: #064e3b; font-size: 2.4em; margin-bottom: 10px;'>Mes Domaines d'Expertise</h2>
            <p style='color: #64748b; margin-bottom: 40px;'>Des compétences visuelles et techniques pour vos projets.</p>
            
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1555066931-4365d14bab8c?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;' alt='Code'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Développement Web</h3>
                    <p style='color: #475569; font-size: 0.95em;'>Création de sites sur-mesure, dynamiques et performants.</p>
                </div>
            </div>

            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;' alt='Design'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Design & Ergonomie</h3>
                    <p style='color: #475569; font-size: 0.95em;'>Interfaces modernes, graphismes soignés et UX/UI optimisée.</p>
                </div>
            </div>

            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;' alt='Gaming Universe'>
                <div style='padding: 25px;'>
                    <h3 style='color: #7c3aed; margin-top: 0;'>Univers Gaming & Web</h3>
                    <p style='color: #475569; font-size: 0.95em;'>Conception de plateformes pour joueurs, streamers et mini-jeux interactifs.</p>
                </div>
            </div>
        </div>

        <!-- Section FAQ -->
        <div style='padding: 70px 20px; background: #f0fdf4; text-align: center;'>
            <h2 style='color: #065f46; font-size: 2.4em; margin-bottom: 40px;'>Foire Aux Questions (FAQ)</h2>
            
            <div class="faq-box">
                <h4 style='color: #064e3b; margin: 0 0 8px 0;'>⏱️ Combien de temps prend la création d'un site ?</h4>
                <p style='color: #475569; margin: 0; font-size: 0.95em;'>Cela dépend de la complexité du projet, mais un site vitrine moderne est généralement prêt en quelques jours.</p>
            </div>
            
            <div class="faq-box">
                <h4 style='color: #064e3b; margin: 0 0 8px 0;'>🎨 Puis-je choisir les couleurs et le design ?</h4>
                <p style='color: #475569; margin: 0; font-size: 0.95em;'>Absolument ! Tout est personnalisable selon vos goûts et l'identité de votre projet.</p>
            </div>

            <div class="faq-box">
                <h4 style='color: #064e3b; margin: 0 0 8px 0;'>🎮 Peut-on intégrer des éléments de jeux ou du streaming ?</h4>
                <p style='color: #475569; margin: 0; font-size: 0.95em;'>Oui, nous pouvons intégrer des widgets Twitch, des liens Discord, des classements de joueurs et des mini-jeux web.</p>
            </div>
        </div>

        <!-- Section Avis Clients (5 avis) -->
        <div style='padding: 60px 15px; background: linear-gradient(180deg, #ffffff, #f4fbf7); text-align: center;'>
            <h2 style='color: #064e3b; font-size: 2.4em; margin-bottom: 40px;'>Avis Clients</h2>
            
            <div class="hover-card" {STYLE_AVIS}>
                <p style='margin-top: 0; color: #475569;'>&ldquo;Un site magnifique avec de superbes tons verts, livré très rapidement !&rdquo;</p>
                <b style='color: #059669;'>- Thomas L.</b>
            </div>
            
            <div class="hover-card" {STYLE_AVIS}>
                <p style='margin-top: 0; color: #475569;'>&ldquo;Très professionnel, le rendu visuel et les animations apportent un vrai plus.&rdquo;</p>
                <b style='color: #059669;'>- Sarah M.</b>
            </div>
            
            <div class="hover-card" {STYLE_AVIS}>
                <p style='margin-top: 0; color: #475569;'>&ldquo;Le site gaming créé pour notre communauté de joueurs est tout simplement exceptionnel !&rdquo;</p>
                <b style='color: #7c3aed;'>- Alexandre R.</b>
            </div>

            <div class="hover-card" {STYLE_AVIS}>
                <p style='margin-top: 0; color: #475569;'>&ldquo;Le design correspond exactement à ce qu'on voulait, super boulot !&rdquo;</p>
                <b style='color: #059669;'>- Lucas P.</b>
            </div>

            <div class="hover-card" {STYLE_AVIS}>
                <p style='margin-top: 0; color: #475569;'>&ldquo;Un grand merci pour la réactivité et la qualité du code fourni.&rdquo;</p>
                <b style='color: #7c3aed;'>- Chloé D.</b>
            </div>
        </div>

        <!-- Section Tarifs & Formules -->
        <div id="tarifs-section" style='padding: 70px 20px; background: #ffffff; text-align: center;'>
            <h2 style='color: #064e3b; font-size: 2.6em; margin-bottom: 15px;'>Nos Tarifs & Formules</h2>
            <p style='color: #64748b; font-size: 1.1em; margin-bottom: 40px;'>Des prix ultra-accessibles pour propulser votre projet sans vous ruiner.</p>
            
            <div class="price-card hover-card">
                <h3 style='color: #059669; font-size: 1.8em; margin-top: 0;'>Site Vitrine</h3>
                <h2 style='font-size: 2.5em; color: #1e293b; margin: 10px 0;'>149€</h2>
                <p style='color: #64748b; font-size: 0.95em;'>Idéal pour présenter votre activité professionnelle avec élégance.</p>
                <ul style='color: #475569; padding-left: 20px; line-height: 1.8; text-align: left;'>
                    <li>Design moderne sur-mesure</li>
                    <li>100% Responsive (Mobile & Tablette)</li>
                    <li>Pages essentielles incluses</li>
                    <li>Support technique 1 mois</li>
                </ul>
                <a href="#contact-section" class="btn-effect" style='display: block; text-align: center; padding: 12px; background: #059669; color: white; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 20px;'>Choisir ce forfait</a>
            </div>

            <div class="price-card hover-card" style='border-color: #0284c7;'>
                <h3 style='color: #0284c7; font-size: 1.8em; margin-top: 0;'>Application Web</h3>
                <h2 style='font-size: 2.5em; color: #1e293b; margin: 10px 0;'>299€</h2>
                <p style='color: #64748b; font-size: 0.95em;'>Pour les projets complexes nécessitant de l'interactivité et des données.</p>
                <ul style='color: #475569; padding-left: 20px; line-height: 1.8; text-align: left;'>
                    <li>Tout du Site Vitrine inclus</li>
                    <li>Base de données personnalisée</li>
                    <li>Fonctionnalités avancées / Espace client</li>
                    <li>Optimisation SEO & Sécurité</li>
                </ul>
                <a href="#contact-section" class="btn-effect" style='display: block; text-align: center; padding: 12px; background: #0284c7; color: white; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 20px;'>Choisir ce forfait</a>
            </div>

            <div class="price-card hover-card" style='border-color: #7c3aed;'>
                <h3 style='color: #7c3aed; font-size: 1.8em; margin-top: 0;'>Projet Gaming Pro</h3>
                <h2 style='font-size: 2.5em; color: #1e293b; margin: 10px 0;'>249€</h2>
                <p style='color: #64748b; font-size: 0.95em;'>Conçu sur-mesure pour les streamers, clans, serveurs et créateurs de jeux.</p>
                <ul style='color: #475569; padding-left: 20px; line-height: 1.8; text-align: left;'>
                    <li>Design thématique immersif & sombre</li>
                    <li>Intégration de mini-jeux web jouables</li>
                    <li>Widgets live Twitch / Kick & Discord</li>
                    <li>Espace communauté & actualités</li>
                </ul>
                <a href="#contact-section" class="btn-effect" style='display: block; text-align: center; padding: 12px; background: #7c3aed; color: white; text-decoration: none; border-radius: 8px; font-weight: bold; margin-top: 20px;'>Choisir ce forfait</a>
            </div>
        </div>

        <!-- Section Contact -->
        <div id="contact-section" style='padding: 80px 20px; text-align: center; background: linear-gradient(135deg, #f4fbf7, #e0f2fe);'>
            <h2 style='color: #059669; font-size: 2.6em; margin-bottom: 15px;'>Contactez-moi</h2>
            <p style='color: #64748b; font-size: 1.1em; margin-bottom: 35px;'>Discutons ensemble de votre prochain projet web ou gaming !</p>
            
            <div style='background: linear-gradient(145deg, #ffffff, #f0fdf4); padding: 40px; border-radius: 24px; display: inline-block; width: 90%; max-width: 480px; box-shadow: 0px 15px 40px rgba(16, 185, 129, 0.2); text-align: left; border: 2px solid #34d399;'>
                <form action="https://formspree.io/f/xbgryzjb" method="POST">
                    <label style='color: #047857; font-weight: bold; font-size: 1em;'>✨ Votre nom :</label>
                    <input type="text" name="nom" placeholder="Ex: Jean Dupont" required {STYLE_INPUT}>
                    
                    <label style='color: #047857; font-weight: bold; font-size: 1em;'>📧 Votre e-mail :</label>
                    <input type="email" name="email" placeholder="Ex: jean@example.com" required {STYLE_INPUT}>
                    
                    <label style='color: #047857; font-weight: bold; font-size: 1em;'>💬 Votre message :</label>
                    <textarea name="message" rows="4" placeholder="Parlez-moi de votre besoin ou de votre projet gaming..." required style='width: 100%; padding: 14px; margin: 10px 0; border: 2px solid #34d399; border-radius: 8px; box-sizing: border-box; font-family: inherit; font-size: 1em; background: #fafafa;'></textarea>
                    
                    <button type="submit" class="btn-effect" style='width: 100%; padding: 16px; background: linear-gradient(135deg, #059669, #0284c7); color: white; border: none; border-radius: 12px; font-weight: bold; cursor: pointer; margin-top: 15px; font-size: 1.15em; box-shadow: 0 6px 20px rgba(5, 150, 105, 0.4);'>Envoyer le message 🚀</button>
                </form>
            </div>
        </div>

        <div {STYLE_FOOTER}>
            <p style='margin: 0 0 15px 0; font-size: 1.1em; color: #34d399; font-weight: bold;'>Retrouvez-moi sur mes réseaux :</p>
            <div style='margin-bottom: 25px;'>
                <a href="https://github.com" target="_blank" class="social-btn">GitHub</a>
                <a href="https://linkedin.com" target="_blank" class="social-btn" style='background: linear-gradient(135deg, #0a66c2, #004182);'>LinkedIn</a>
                <a href="https://instagram.com" target="_blank" class="social-btn" style='background: linear-gradient(135deg, #e1306c, #833ab4);'>Instagram</a>
            </div>
            <p style='margin: 0; font-size: 0.95em;'>&copy; 2026 Sulo Créateur - Tous droits réservés.</p>
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
        {GLOBAL_STYLE}
    </head>
    <body style='background-color: #f4fbf7; font-family: "Segoe UI", Roboto, sans-serif; text-align: center; padding: 60px 15px; margin: 0; color: #1e293b;'>
        <h1 style='color: #064e3b; font-size: 3em; font-weight: bold; margin-bottom: 15px;'>Mes Réalisations</h1>
        <p style='color: #64748b; font-size: 1.25em; margin-bottom: 50px;'>Découvrez la liste complète de mes 12 projets professionnels créés pour mes clients.</p>
        
        <div style='max-width: 1200px; margin: 0 auto;'>
            
            <!-- Projet 1 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1460925895917-afdab827c52f?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Site E-Commerce</h3>
                    <p style='color: #475569; line-height: 1.5;'>Boutique en ligne moderne, élégante et ergonomique.</p>
                </div>
            </div>
            
            <!-- Projet 2 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1507238691740-187a5b1d37b8?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Application Web Flask</h3>
                    <p style='color: #475569; line-height: 1.5;'>Outil de gestion sur-mesure propulsé par Python.</p>
                </div>
            </div>

            <!-- Projet 3 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1538481199705-c710c4e965fc?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #7c3aed; margin-top: 0;'>Plateforme Gaming</h3>
                    <p style='color: #475569; line-height: 1.5;'>Site communautaire avec mini-jeux et intégration streaming.</p>
                </div>
            </div>

            <!-- Projet 4 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1551288049-bebda4e38f71?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Dashboard Analytics</h3>
                    <p style='color: #475569; line-height: 1.5;'>Tableau de bord de suivi de données en temps réel.</p>
                </div>
            </div>

            <!-- Projet 5 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1618005182384-a83a8bd57fbe?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #7c3aed; margin-top: 0;'>Bot Discord & Web</h3>
                    <p style='color: #475569; line-height: 1.5;'>Interface web connectée à un bot de modération gaming.</p>
                </div>
            </div>

            <!-- Projet 6 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1498050108023-c5249f4df085?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Site Vitrine Artisan</h3>
                    <p style='color: #475569; line-height: 1.5;'>Présentation d'activité avec galerie photo et contact.</p>
                </div>
            </div>

            <!-- Projet 7 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1488646953014-85cb44e25828?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Blog de Voyage</h3>
                    <p style='color: #475569; line-height: 1.5;'>Récits d'aventures, cartes interactives et articles.</p>
                </div>
            </div>

            <!-- Projet 8 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1633356122544-f134324a6cee?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #7c3aed; margin-top: 0;'>Portfolio Créatif 3D</h3>
                    <p style='color: #475569; line-height: 1.5;'>Showcase artistique pour designer et modélisateur 3D.</p>
                </div>
            </div>

            <!-- Projet 9 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1546069901-ba9599a7e63c?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Application de Recettes</h3>
                    <p style='color: #475569; line-height: 1.5;'>Recherche de plats avec filtres dynamiques et favoris.</p>
                </div>
            </div>

            <!-- Projet 10 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1511512578047-dfb367046420?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #7c3aed; margin-top: 0;'>Mini-Jeu Web Arcade</h3>
                    <p style='color: #475569; line-height: 1.5;'>Jeu rétro jouable directement dans le navigateur en JS.</p>
                </div>
            </div>

            <!-- Projet 11 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1512941937669-90a1b58e7e9c?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #059669; margin-top: 0;'>Application Mobile PWA</h3>
                    <p style='color: #475569; line-height: 1.5;'>Application web progressive optimisée pour smartphones.</p>
                </div>
            </div>

            <!-- Projet 12 -->
            <div class="hover-card" {STYLE_CARTE}>
                <img src='https://images.unsplash.com/photo-1526374965328-7f61d4dc18c5?auto=format&fit=crop&w=600&q=80' style='width: 100%; height: 180px; object-fit: cover;'>
                <div style='padding: 25px;'>
                    <h3 style='color: #7c3aed; margin-top: 0;'>Forum de Discussions</h3>
                    <p style='color: #475569; line-height: 1.5;'>Espace d'échange et de discussion pour passionnés de tech.</p>
                </div>
            </div>

        </div>

        <br><br><br>
        <a href="/" class="btn-effect" {STYLE_BOUTON_ALT}>Retour à l'accueil</a>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
