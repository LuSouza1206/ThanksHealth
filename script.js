@import url('https://fonts.cdnfonts.com/css/venose');
@import url('https://fonts.cdnfonts.com/css/anko-personal-use');

body {
  font-family: Arial, Helvetica, sans-serif;
  margin: 0;
  padding: 0;
  min-height: 100vh;
  position: relative;
}

body.pagina-home main::before,
main::before {
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-size: cover;
  background-attachment: fixed;
  filter: blur(5px);
  z-index: -1;
  display: flex;
  gap: 2rem;
}

body.pagina-home main::before {
  background-image: url('images/Fundo.png');
}

main::before {
  background-image: url('images/Fundo.png');
}

body.contato-page main h1 {
  font-family: 'Anko Personal Use', sans-serif;
  color: #050505;
  text-align: center;
  text-transform: uppercase;
  letter-spacing: 2px;
  margin-bottom: 20px;
  font-size: 53px;
}

header {
  background: linear-gradient(to right, #83f5e2, #33619e);
  color: white;
  padding: 20px 0;
  text-align: center;
  border-radius: 10px 10px 0 0;
}

nav {
  display: flex;
  justify-content: center;
  align-items: center;
}

nav ul {
  list-style: none;
  padding: 0;
  margin: 0;
}

nav ul li {
  display: inline;
  margin-right: 30px;
}

nav ul li a {
  color: white;
  text-decoration: none;
  transition: color 0.3s ease;
  font-size: 18px;
}

nav ul li a:hover {
  color: #6caff7;
  text-shadow: 1px 1px 2px rgba(0, 0, 0, 0.8);
  font-size: 20px;
}

nav ul li a.active {
  color: #007BFF;
  font-weight: bold;
  font-size: 20px;
}


main {
  margin: 0;
  padding: 0;
  width: 100%;
  min-height: 100vh;
  position: relative;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;
  gap: 2rem;
}

main>* {
  position: relative;
  z-index: 1;
}


footer {
  background: linear-gradient(to right, #83f5e2, #33619e);
  color: white;
  text-align: center;
  padding: 20px 0;
  width: 100%;
  border-top: 2px solid #83f5e2, #33619e;
  border-radius: 0px 0px 50px 50px;
  box-shadow: 0px 0px 50px rgba(0, 0, 0, 0.3);
}


.video-container {
  display: flex;
  justify-content: center;
  align-items: center;
  width: 100%;
  max-width: 1200px;
  margin: 0 auto;
}

.video-container video {
  width: 100%;
  height: auto;
}

header.scrolled {
  background-color: rgba(161, 131, 245, 0.9);
  backdrop-filter: blur(10px);
}

nav.scrolled ul li a {
  color: #333;
}

.logo-container {
  text-align: center;
  margin-top: 20px;
}

.logo-container img {
  display: block;
  margin: 0 auto;
}

h1 {
  text-align: center;
}

.contact-section {
  margin: 5px 0;
  padding: 130px 350px;
  background-color: rgba(255, 255, 255, 0.486);
  border-radius: 100px;
  box-shadow: 0 0 100px rgba(0, 0, 0, 0.1);
  text-align: center;
}

.contact-section form {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.contact-section label {
  margin-top: 10px;
}

.contact-section input,
.contact-section textarea {
  width: 100%;
  padding: 10px;
  margin-top: 5px;
  margin-bottom: 15px;
  border: 1px solid #ccc;
  border-radius: 75px;
  box-sizing: border-box;
}

.contact-section button {
  padding: 1.3em 3em;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 2.5px;
  font-weight: 500;
  color: #000;
  background-color: #007BFF;
  border: none;
  border-radius: 45px;
  box-shadow: 0px 8px 15px rgba(0, 0, 0, 0.1);
  transition: all 0.3s ease 0s;
  cursor: pointer;
  outline: none;
}

.contact-section button:hover {
  background-color: #0056b3;
  box-shadow: 0px 15px 20px rgba(46, 104, 229, 0.4);
  color: #fff;
  transform: translateY(-7px);
}

.contact-section button:active {
  transform: translateY(-1px);
}

.logo-container h1 {
  font-family: 'VENOSE', sans-serif;
  font-size: 50px;
  letter-spacing: 2px;
  color: #f8f4f4;
}

.team-section {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

.team-section {
  margin-top: 20px;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 10px;
}

th,
td {
  border: 1px solid #ddd;
  padding: 8px;
  text-align: left;
}

th {
  background-color: #f2f2f2;
}

.team-section table {
  border-spacing: 0;
}

.team-section table img {
  width: 100px;
  height: 100px;
  object-fit: cover;
  border-radius: 50%;
  transition: transform 0.3s ease-in-out;
}

.team-section table img:hover {
  transform: scale(1.1);
  cursor: pointer;
}

td {
  font-family: 'Anko', sans-serif;
  font-size: 16px;
}

.content-container {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin: 20px;
}

.section-image {
  max-width: 600px;
  margin-right: 20px;
}

.section-text {
  flex: 1;
}

.center-image {
  display: block;
  margin: 20px auto;
  max-width: 100%;
}

.image-caption {
  text-align: center;
  font-style: italic;
}

.main h1 {
  font-family: 'VENOSE', sans-serif;
  color: #000;
  text-align: center;
}

.content-container p {
  font-size: 22px;
  color: #333;
}

.section-text {
  background-color: #f9f9f9;
  padding: 40px;
  border-radius: 20px;
  box-shadow: 0 30px 30px rgba(0, 0, 0, 0.1);
}

.section-image {
  max-width: 100%;
  height: auto;
  border-radius: 0px;
}

.text-container {
  font-size: 22px;
  color: #000000;
  background-color: #f9f9f9;
  padding: 10px;
  border-radius: 20px;
  box-shadow: 0 30px 30px rgba(0, 0, 0, 0.1);
  
}
