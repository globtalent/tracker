import os
import pandas as pd


# Read the Excel file
df = pd.read_excel("/Users/lilywheeler/Desktop/emptycountries.xlsx", engine="openpyxl")

# Create the output directory if it doesn't exist
output_directory = "docs"
os.makedirs(output_directory, exist_ok=True)


# Iterate over each row in the DataFrame
for row_number, row in df.iterrows():
    # Extract the relevant information for the current row
    countries = row['Countries']
    adjective = row['Adjective']

    # Generate the XML content for the student's webpage
    xml_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE html>
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
    <meta http-equiv="content-type" content="application/xhtml+xml; charset=UTF-8" />
    <link href="App_Themes/fav-logo.ico" rel="shortcut icon" type="image/x-icon" />
    <link href="App_Themes/design.css" rel="stylesheet" type="text/css" />
    <link href="App_Themes/index.css" rel="stylesheet" type="text/css" />
    <link href="App_Themes/print.css" rel="stylesheet" type="text/css" media="print" />
    <title>Global Talent Network</title>
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-3.2.1.slim.min.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.9.1/dist/umd/popper.min.js"></script>
    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0/js/bootstrap.min.js"></script>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Merriweather&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Comfortaa:wght@300&family=Merriweather&display=swap');

        body {{
            font-family: 'Comfortaa', cursive;
            background-color: #1b1d1e;
            margin: 0;
            margin: 40px;
            padding: 0;
            overflow: auto;
        }}

        .container {{
            display: flex;
            flex-direction: column;
            min-height: 100vh;
        }}

        .content {{
            flex: 1;
            padding: 2rem;
            margin-left: 20%;
        }}

        .centered-heading {{
            font-family: 'Merriweather', serif;
            margin: 0;
            padding: 0;
            overflow: auto;
            text-align: center;
            font-weight: 700;
            font-size: 50px;
            color: white; /* Set the text color to white */
        }}

        .centered-image {{
            display: flex;
            justify-content: center;
            margin-top: 1rem;
        }}

        #header {{
            background-color: #1b1d1e;
            padding: 2rem;
            color: #ffffff;
        }}

        .top-left-corner {{
            position: absolute;
            top: 12px;
            left: 12px;
            z-index: 1;
        }}

        #menu {{
            font-family: 'Comfortaa', cursive;
            display: flex;
            justify-content: center;
            margin-top: 1rem;
            color: #ffffff;
            font-size: 1.2rem;
            font-weight: 700;
        }}

        #menu a {{
            margin: 0 1rem;
            text-decoration: none;
            color: #ffffff;
            transition: color 0.3s ease-in-out;
        }}

        #menu a:hover {{
            color: #dee0e7;
        }}

   footer {{
 position: fixed;
  bottom: 0;
  left: 0;
  width: 100%;
  padding: 0.2em 2em;
  box-sizing: border-box;
  margin: 0;
  z-index: 5;
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  background-image: url('https://lwheel.github.io/FILESMO/repeat1.png');
  background-size: contain;
  background-repeat: repeat;
  line-height: 1.2;
}}

footer::before {{
  content: "";
  position: absolute;
  top: 0;
  left: 0;
  width: 10%;
  height: 120%; /* Adjust the height to leave space for the text */
  background-color: rgba(255, 255, 255, 0.4); /* Change the opacity to your liking */
  z-index: -1;
}}

   footer b {{
      font-size: 10px;
      font-weight: 600;
      margin-top: auto;
  }}

  footer a {{
      color: rgb(0, 0, 0);
      font-size: 10px;
      font-weight: 600;
  }}

        #main {{
            margin-left: 28px; /* Adjust this value to move the content further to the right */
        }}

        header,
        h1 {{
            font-family: 'Merriweather', serif;
            font-size: 30px;
            font-weight: 700;
            color: #ffffff;
            margin-bottom: 2rem;
        }}

        header,
        h2 {{
            font-family: 'Merriweather', serif;
            color: #ffffff;
            font-size: 50px;
        }}

        #h1 a {{
            text-decoration: none;
            color: #ffffff;
            transition: color 0.3s ease-in-out;
        }}

        #h1 a:hover {{
            color: #dee0e7;
        }}

        .intro {{
            text-align: left;
            margin-left: 1000px;
            margin-right: 1000px;
        }}

        /* Media Queries */
        @media screen and (max-width: 768px) {{
            .centered-heading {{
                font-size: 1.8rem;
            }}

            header,
            h1 {{
                font-size: 50px;
            }}
        }}

        th,
        td {{
            border: 2px solid #1b1d1e;
            font-size: 20px;
            margin: 30px;
            padding: 4px;
            color: white;
            margin-right: 40px; /* Added wider margin between columns */
            padding-left: 20px; /* Added padding to create spacing */
            padding-right: 20px; /* Added padding to create spacing */
            transition: background-color 0.3s ease-in-out; /* Added transition effect */
        }}

        th a {{
          font-size: 30px; /* Increased font size for column titles */
        }}

        th a,
        td a {{
            color: white; /* Set the text color to white */
            text-decoration: none; /* Remove underline */
        }}


        th a:hover,
        td a:hover {{
            color: #dee0e7;
        }}


    .dropdown {{
      position: relative;
      display: inline-block;
    }}

    .dropdown-content {{
      display: none;
      position: absolute;
      background-color: #f9f9f9;
      min-width: 160px;
      box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
      z-index: 1;
    }}

    .dropdown:hover .dropdown-content {{
      display: block;
    }}

    .dropdown-content a {{
      color: black !important;
      padding: 8px 16px;
      text-decoration: none;
      display: block;
    }}

    .dropdown-content a:hover {{
      background-color: #f1f1f1;
    }}
   
   .card-header {{
  background-color: #424547;
  color: white;
  text-decoration: none;
  border: none; /* Remove the border */
    outline: none;
}}

.card {{
    border: none; /* Remove the border */
    margin-bottom: 10px;
  }}

  .card-header button {{
  color: white;
  text-decoration: none;
}}

.card-body {{
  background-color: #1b1d1e;
}}

.accordian {{
  border: none; /* Remove the border */
}}
hr {{
  background-color: white;
}}
  p {{
    color: white;
}}
  </style>
  <script>
    document.addEventListener("DOMContentLoaded", function() {{
    var accordion = document.getElementById("accordion");
    var buttons = accordion.getElementsByClassName("btn");
    var contents = accordion.getElementsByClassName("collapse");

    for (var i = 0; i < buttons.length; i++) {{
        buttons[i].addEventListener("click", function() {{
        var content = this.nextElementSibling;
        var isCollapsed = content.classList.contains("show");

        if (isCollapsed) {{
            content.classList.remove("show");
        }} else {{
            content.classList.add("show");
        }}
        }});

        // Close the content panels by default
        contents[i].classList.remove("show");
    }}
    }});



</script>
</head>
<body>
  <div class = "container">
  <div id="header" style="margin: 0px;">
    <div id="h1">
      <h1 class="centered-heading">
        <a href="https://www.globtalent.org/">Global Talent Network</a>
      </h1>
    </div>
    <div id="menu">
      <a href="https://www.globtalent.org/" style="color: black;">Home</a>  <span style="color: black;">&bull;</span>
      <div class="dropdown">
        <a href="index.html" style="color: black;">Partner Math Olympiads</a>
        <div class="dropdown-content">
          <a href="problems.html">Past Problems</a>
          <a href="total_results.html">Results by Country</a>
        </div>
      </div>


    </div>
  </div>
<div id="main">
    <h2 style="color: black; font-size: 50px; margin-top: .5em; margin-bottom: .5em;">{countries}</h2>
    
<p> {countries} is not currently hosting a math olympiad.</p>

<br>
    <h2 style="color: black; font-size: 50px; margin-top: .5em; margin-bottom: .5em;">Past {adjective} Problem Sets</h2>

    <p> Problems are not available.</p>
</div>
<br>
</body>
<footer>
    <b style: color="white" margin="2 rem">E-mail:</b>
    <a href="mailto:ea@globtalent.org" style: color="white" margin="2 rem">ea@globtalent.org</a>
</footer>
</div>
</html>
'''

    # Save the XML content to a file in the output directory
    output_filename = os.path.join(output_directory, f"{countries}.html")
    with open(output_filename, "w") as file:
        file.write(xml_content)
