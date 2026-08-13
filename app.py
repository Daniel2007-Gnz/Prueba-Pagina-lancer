from flask import Flask

app = Flask(__name__)


@app.route("/")
def inicio():
    return """
<!DOCTYPE html>
<html lang="es">

<head>

    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">

    <title>Mitsubishi Lancer | Legend</title>

    <style>

        * {
            margin: 0;
            padding: 0;
            box-sizing: border-box;
            scroll-behavior: smooth;
        }

        body {
            font-family: Arial, Helvetica, sans-serif;
            background: #0b0b0b;
            color: white;
        }

        /* =========================
           BARRA DE NAVEGACIÓN
        ========================= */

        nav {
            position: fixed;
            top: 0;
            width: 100%;
            height: 75px;

            display: flex;
            justify-content: space-between;
            align-items: center;

            padding: 0 7%;

            background: rgba(5, 5, 5, 0.92);

            border-bottom: 1px solid #333;

            z-index: 1000;

            backdrop-filter: blur(10px);
        }

        .logo {
            font-size: 25px;
            font-weight: bold;
            letter-spacing: 3px;
        }

        .logo span {
            color: #e30613;
        }

        nav ul {
            display: flex;
            gap: 30px;
            list-style: none;
        }

        nav ul li a {
            text-decoration: none;
            color: white;
            font-size: 14px;
            transition: 0.3s;
        }

        nav ul li a:hover {
            color: #e30613;
        }


        /* =========================
           PORTADA
        ========================= */

        .hero {

            min-height: 100vh;

            display: flex;
            align-items: center;

            padding: 100px 8% 50px;

            background:

                linear-gradient(
                    90deg,
                    rgba(0,0,0,0.95),
                    rgba(0,0,0,0.60),
                    rgba(0,0,0,0.25)
                ),

                url("https://commons.wikimedia.org/wiki/Special:FilePath/Mitsubishi%20Lancer%20Evolution%20X.jpg");

            background-size: cover;
            background-position: center;
        }

        .hero-content {
            max-width: 750px;
        }

        .small-title {
            color: #e30613;
            font-weight: bold;
            letter-spacing: 5px;
            margin-bottom: 20px;
        }

        .hero h1 {
            font-size: clamp(50px, 8vw, 100px);
            line-height: 0.9;
            margin-bottom: 30px;
        }

        .hero h1 span {
            color: #e30613;
        }

        .hero p {
            max-width: 600px;
            color: #ddd;
            font-size: 19px;
            line-height: 1.7;
        }

        .buttons {
            display: flex;
            gap: 15px;
            margin-top: 35px;
            flex-wrap: wrap;
        }

        .btn {
            padding: 15px 30px;
            text-decoration: none;
            border-radius: 5px;
            font-weight: bold;
            transition: 0.3s;
        }

        .btn-red {
            background: #e30613;
            color: white;
        }

        .btn-red:hover {
            background: #a9000b;
            transform: translateY(-3px);
        }

        .btn-outline {
            border: 1px solid white;
            color: white;
        }

        .btn-outline:hover {
            background: white;
            color: black;
        }


        /* =========================
           SECCIONES
        ========================= */

        section {
            padding: 100px 8%;
        }

        .section-title {
            text-align: center;
            margin-bottom: 60px;
        }

        .section-title small {
            color: #e30613;
            letter-spacing: 4px;
            font-weight: bold;
        }

        .section-title h2 {
            font-size: 45px;
            margin-top: 10px;
        }

        .line {
            width: 70px;
            height: 4px;
            background: #e30613;
            margin: 20px auto;
        }


        /* =========================
           HISTORIA
        ========================= */

        #historia {
            background: #111;
        }

        .history-container {
            max-width: 1100px;
            margin: auto;

            display: grid;
            grid-template-columns: 1fr 1fr;

            gap: 50px;

            align-items: center;
        }

        .history-image img {
            width: 100%;
            height: 420px;
            object-fit: cover;
            border-radius: 12px;
        }

        .history-text h3 {
            font-size: 32px;
            margin-bottom: 20px;
        }

        .history-text p {
            color: #bbb;
            line-height: 1.8;
            margin-bottom: 15px;
        }


        /* =========================
           CARACTERÍSTICAS
        ========================= */

        #caracteristicas {
            background: #0d0d0d;
        }

        .cards {

            display: grid;

            grid-template-columns:
            repeat(3, 1fr);

            gap: 25px;

            max-width: 1200px;

            margin: auto;
        }

        .card {

            background: #181818;

            padding: 35px;

            border-radius: 10px;

            border: 1px solid #292929;

            transition: 0.3s;
        }

        .card:hover {

            transform: translateY(-10px);

            border-color: #e30613;

            box-shadow:
                0 15px 40px rgba(227,6,19,0.15);
        }

        .icon {
            font-size: 40px;
            margin-bottom: 20px;
        }

        .card h3 {
            color: #e30613;
            font-size: 23px;
            margin-bottom: 15px;
        }

        .card p {
            color: #aaa;
            line-height: 1.7;
        }


        /* =========================
           EVOLUTION
        ========================= */

        .evolution {

            min-height: 600px;

            display: flex;

            align-items: center;

            background:

                linear-gradient(
                    rgba(0,0,0,0.75),
                    rgba(0,0,0,0.85)
                ),

                url("https://commons.wikimedia.org/wiki/Special:FilePath/Mitsubishi%20Lancer%20Evolution%20IX.jpg");

            background-size: cover;
            background-position: center;
            background-attachment: fixed;
        }

        .evo-content {
            max-width: 700px;
        }

        .evo-content small {
            color: #e30613;
            font-weight: bold;
            letter-spacing: 4px;
        }

        .evo-content h2 {
            font-size: 65px;
            margin: 15px 0;
        }

        .evo-content h2 span {
            color: #e30613;
        }

        .evo-content p {
            color: #ddd;
            font-size: 18px;
            line-height: 1.8;
        }


        /* =========================
           ESPECIFICACIONES
        ========================= */

        #datos {
            background: #111;
        }

        .specs {

            max-width: 1000px;

            margin: auto;

            display: grid;

            grid-template-columns:
            1fr 1fr;

            gap: 20px;
        }

        .spec {

            background: #1a1a1a;

            padding: 25px;

            border-left: 4px solid #e30613;

            display: flex;

            justify-content: space-between;
        }

        .spec span:first-child {
            color: #999;
        }

        .spec span:last-child {
            font-weight: bold;
        }


        /* =========================
           GENERACIONES
        ========================= */

        #generaciones {
            background: #0c0c0c;
        }

        .timeline {

            max-width: 900px;

            margin: auto;
        }

        .generation {

            display: flex;

            gap: 30px;

            padding: 30px 0;

            border-bottom: 1px solid #333;
        }

        .year {

            min-width: 100px;

            color: #e30613;

            font-size: 25px;

            font-weight: bold;
        }

        .generation h3 {
            margin-bottom: 10px;
        }

        .generation p {
            color: #999;
            line-height: 1.6;
        }


        /* =========================
           GALERÍA
        ========================= */

        #galeria {
            background: #111;
        }

        .gallery {

            max-width: 1200px;

            margin: auto;

            display: grid;

            grid-template-columns:
            repeat(3, 1fr);

            gap: 15px;
        }

        .gallery img {

            width: 100%;

            height: 260px;

            object-fit: cover;

            border-radius: 8px;

            transition: 0.4s;
        }

        .gallery img:hover {

            transform: scale(1.04);

            filter: brightness(1.2);
        }


        /* =========================
           FRASE
        ========================= */

        .quote {

            padding: 120px 8%;

            text-align: center;

            background: #e30613;
        }

        .quote h2 {

            max-width: 900px;

            margin: auto;

            font-size: 40px;
        }


        /* =========================
           FOOTER
        ========================= */

        footer {

            padding: 50px 8%;

            background: #050505;

            text-align: center;
        }

        footer h2 {
            margin-bottom: 15px;
        }

        footer span {
            color: #e30613;
        }

        footer p {
            color: #777;
        }


        /* =========================
           RESPONSIVE
        ========================= */

        @media(max-width: 900px) {

            nav ul {
                display: none;
            }

            .history-container {
                grid-template-columns: 1fr;
            }

            .cards {
                grid-template-columns: 1fr;
            }

            .specs {
                grid-template-columns: 1fr;
            }

            .gallery {
                grid-template-columns: 1fr;
            }

            .evo-content h2 {
                font-size: 45px;
            }

        }

    </style>

</head>


<body>


<!-- =========================
     MENÚ
========================= -->

<nav>

    <div class="logo">
        MITSUBISHI <span>LANCER</span>
    </div>

    <ul>

        <li>
            <a href="#inicio">Inicio</a>
        </li>

        <li>
            <a href="#historia">Historia</a>
        </li>

        <li>
            <a href="#caracteristicas">Características</a>
        </li>

        <li>
            <a href="#evolution">Evolution</a>
        </li>

        <li>
            <a href="#galeria">Galería</a>
        </li>

    </ul>

</nav>


<!-- =========================
     PORTADA
========================= -->

<section class="hero" id="inicio">

    <div class="hero-content">

        <div class="small-title">
            MITSUBISHI MOTORS
        </div>

        <h1>
            LANCER
            <span>EVOLUTION</span>
        </h1>

        <p>

            Una leyenda japonesa que combinó
            tecnología, diseño y rendimiento para
            convertirse en uno de los automóviles
            deportivos más reconocidos.

        </p>


        <div class="buttons">

            <a href="#historia" class="btn btn-red">
                DESCUBRIR HISTORIA
            </a>

            <a href="#galeria" class="btn btn-outline">
                VER GALERÍA
            </a>

        </div>

    </div>

</section>


<!-- =========================
     HISTORIA
========================= -->

<section id="historia">

    <div class="section-title">

        <small>DESDE 1973</small>

        <h2>Una historia legendaria</h2>

        <div class="line"></div>

    </div>


    <div class="history-container">


        <div class="history-image">

            <img
                src="https://commons.wikimedia.org/wiki/Special:FilePath/Mitsubishi%20Lancer.jpg"
                alt="Mitsubishi Lancer"
            >

        </div>


        <div class="history-text">

            <h3>
                Más que un automóvil
            </h3>

            <p>

                El Mitsubishi Lancer nació en 1973
                y rápidamente se convirtió en uno de
                los modelos más importantes de
                Mitsubishi Motors.

            </p>

            <p>

                Durante sus diferentes generaciones,
                el Lancer fue ofrecido en múltiples
                configuraciones, desde versiones
                enfocadas en el uso diario hasta
                modelos de alto rendimiento.

            </p>

            <p>

                Su participación en el mundo del rally
                fue fundamental para construir la
                reputación deportiva de la familia Lancer.

            </p>


            <a href="#generaciones" class="btn btn-red">
                VER GENERACIONES
            </a>

        </div>

    </div>

</section>


<!-- =========================
     CARACTERÍSTICAS
========================= -->

<section id="caracteristicas">

    <div class="section-title">

        <small>INGENIERÍA JAPONESA</small>

        <h2>¿Qué hace especial al Lancer?</h2>

        <div class="line"></div>

    </div>


    <div class="cards">


        <div class="card">

            <div class="icon">
                🏎️
            </div>

            <h3>
                Rendimiento
            </h3>

            <p>

                Las versiones deportivas del Lancer
                fueron diseñadas para ofrecer una
                experiencia de conducción enfocada
                en el rendimiento.

            </p>

        </div>


        <div class="card">

            <div class="icon">
                ⚙️
            </div>

            <h3>
                Tecnología
            </h3>

            <p>

                Mitsubishi incorporó diferentes
                tecnologías de motor, transmisión
                y tracción dependiendo de la
                generación y versión.

            </p>

        </div>


        <div class="card">

            <div class="icon">
                🏁
            </div>

            <h3>
                Rally
            </h3>

            <p>

                La competición fue una parte
                fundamental de la historia del
                Lancer y especialmente del
                Lancer Evolution.

            </p>

        </div>


    </div>

</section>


<!-- =========================
     EVOLUTION
========================= -->

<section class="evolution" id="evolution">

    <div class="evo-content">

        <small>
            LA LEYENDA
        </small>

        <h2>
            LANCER
            <span>EVOLUTION</span>
        </h2>

        <p>

            El Lancer Evolution nació con una
            clara orientación hacia el rally.
            Sus diferentes generaciones
            incorporaron motores turboalimentados,
            sistemas de tracción integral y
            configuraciones enfocadas en el
            desempeño.

        </p>

        <br>

        <p>

            Su éxito en competición y su presencia
            en videojuegos, películas y cultura
            automotriz ayudaron a convertirlo en
            un ícono mundial.

        </p>


        <div class="buttons">

            <a href="#datos" class="btn btn-red">
                ESPECIFICACIONES
            </a>

        </div>

    </div>

</section>


<!-- =========================
     ESPECIFICACIONES
========================= -->

<section id="datos">

    <div class="section-title">

        <small>DATOS</small>

        <h2>Características del modelo</h2>

        <div class="line"></div>

    </div>


    <div class="specs">


        <div class="spec">

            <span>
                Marca
            </span>

            <span>
                Mitsubishi
            </span>

        </div>


        <div class="spec">

            <span>
                Modelo
            </span>

            <span>
                Lancer
            </span>

        </div>


        <div class="spec">

            <span>
                Fabricante
            </span>

            <span>
                Mitsubishi Motors
            </span>

        </div>


        <div class="spec">

            <span>
                Tipo
            </span>

            <span>
                Sedán
            </span>

        </div>


        <div class="spec">

            <span>
                Producción
            </span>

            <span>
                1973 - 2017
            </span>

        </div>


        <div class="spec">

            <span>
                Versión deportiva
            </span>

            <span>
                Evolution
            </span>

        </div>


        <div class="spec">

            <span>
                País de origen
            </span>

            <span>
                Japón
            </span>

        </div>


        <div class="spec">

            <span>
                Segmento
            </span>

            <span>
                Automóvil compacto
            </span>

        </div>


    </div>

</section>


<!-- =========================
     GENERACIONES
========================= -->

<section id="generaciones">

    <div class="section-title">

        <small>EVOLUCIÓN</small>

        <h2>Generaciones</h2>

        <div class="line"></div>

    </div>


    <div class="timeline">


        <div class="generation">

            <div class="year">
                1973
            </div>

            <div>

                <h3>
                    Primera generación
                </h3>

                <p>

                    El comienzo de la historia
                    del Mitsubishi Lancer.

                </p>

            </div>

        </div>


        <div class="generation">

            <div class="year">
                1992
            </div>

            <div>

                <h3>
                    Lancer Evolution I
                </h3>

                <p>

                    Nace la familia Evolution,
                    desarrollada con una fuerte
                    influencia del rally.

                </p>

            </div>

        </div>


        <div class="generation">

            <div class="year">
                2007
            </div>

            <div>

                <h3>
                    Lancer Evolution X
                </h3>

                <p>

                    Una nueva generación con
                    un diseño moderno y tecnología
                    orientada al rendimiento.

                </p>

            </div>

        </div>


        <div class="generation">

            <div class="year">
                2017
            </div>

            <div>

                <h3>
                    Fin de producción
                </h3>

                <p>

                    Mitsubishi finalizó la producción
                    del Lancer después de varias
                    décadas de historia.

                </p>

            </div>

        </div>


    </div>

</section>


<!-- =========================
     GALERÍA
========================= -->

<section id="galeria">

    <div class="section-title">

        <small>VISUAL</small>

        <h2>Galería</h2>

        <div class="line"></div>

    </div>


    <div class="gallery">


        <img
            src="https://commons.wikimedia.org/wiki/Special:FilePath/Mitsubishi%20Lancer.jpg"
            alt="Mitsubishi Lancer"
        >


        <img
            src="https://commons.wikimedia.org/wiki/Special:FilePath/Mitsubishi%20Lancer%20Evolution%20X.jpg"
            alt="Lancer Evolution X"
        >


        <img
            src="https://commons.wikimedia.org/wiki/Special:FilePath/Mitsubishi%20Lancer%20Evolution%20IX.jpg"
            alt="Lancer Evolution IX"
        >


        <img
            src="https://images.unsplash.com/photo-1492144534655-ae79c964c9d7?auto=format&fit=crop&w=1200&q=80"
            alt="Automóvil deportivo"
        >


        <img
            src="https://images.unsplash.com/photo-1503376780353-7e6692767b70?auto=format&fit=crop&w=1200&q=80"
            alt="Automóvil deportivo"
        >


        <img
            src="https://images.unsplash.com/photo-1552519507-da3b142c6e3d?auto=format&fit=crop&w=1200&q=80"
            alt="Automóvil deportivo"
        >


    </div>

</section>


<!-- =========================
     FRASE
========================= -->

<section class="quote">

    <h2>

        "Una combinación de ingeniería,
        competición y pasión japonesa."

    </h2>

</section>


<!-- =========================
     FOOTER
========================= -->

<footer>

    <h2>
        MITSUBISHI <span>LANCER</span>
    </h2>

    <p>
        Página web desarrollada con Flask
    </p>

    <br>

    <p>
        Proyecto académico © 2026
    </p>

</footer>


</body>

</html>
    """


if __name__ == "__main__":
    app.run(debug=True)