import webbrowser
import os
import re
# Styles and scripting for the page
main_page_head = '''
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="utf-8">
    <title>Fresh Tomatoes!</title>

    <!-- Bootstrap 3 -->
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap.min.css">
    <link rel="stylesheet" href="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/css/bootstrap-theme.min.css">
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
    <script src="https://code.jquery.com/jquery-1.10.1.min.js"></script>
    <script src="https://netdna.bootstrapcdn.com/bootstrap/3.1.0/js/bootstrap.min.js"></script>
    <style type="text/css" media="screen">
            body {
            padding-top: 80px;
        }
        #trailer .modal-dialog {
            margin-top: 200px;
            width: 640px;
            height: 480px;
        }
        .hanging-close {
            position: absolute;
            top: -12px;
            right: -12px;
            z-index: 9001;
        }
        #trailer-video {
            width: 100%;
            height: 100%;
        }
        .movie-tile {
            margin-bottom: 20px;
            padding-top: 20px;
        }
        .movie-tile:hover {
            background-color: #EEE;
            cursor: pointer;
        }
        .scale-media {
            padding-bottom: 56.25%;
            position: relative;
        }
        .scale-media iframe {
            border: none;
            height: 100%;
            position: absolute;
            width: 100%;
            left: 0;
            top: 0;
            background-color: white;
        }
           .cuadro_intro_hover {
            padding: 0px;
            position: relative;
            overflow: hidden;
            height: 400px;
        }
        
        .cuadro_intro_hover:hover .caption {
            opacity: 1;
            transform: translateY(-150px);
            -webkit-transform: translateY(-150px);
            -moz-transform: translateY(-150px);
            -ms-transform: translateY(-150px);
            -o-transform: translateY(-150px);
        }
        
        .cuadro_intro_hover img {
            z-index: 4;
            top : 100%;
        }
        
        .cuadro_intro_hover .caption {
            position: absolute;
            top: 85%;
            -webkit-transition: all 0.3s ease-in-out;
            -moz-transition: all 0.3s ease-in-out;
            -o-transition: all 0.3s ease-in-out;
            -ms-transition: all 0.3s ease-in-out;
            transition: all 0.3s ease-in-out;
            width: 100%;
        }
        
        .cuadro_intro_hover .blur {
            background-color: rgba(0, 0, 0, 0.7);
            height: 300px;
            z-index: 5;
            position: absolute;
            width: 100%;
        }
        
        .cuadro_intro_hover .caption-text {
            z-index: 10;
            color: #fff;
            position: absolute;
            height: 300px;
            text-align: center;
            top: -20px;
            width: 100%;
        }
        .nopadding {
            padding: 0px !important;
            margin: 0 !important;
            outline: 2px solid #333;
            background: #333;
        }
        #dufaaa > ul,
#dufaaa > ul li,
#dufaaa > ul ul {
  list-style: none;
   margin-top:10px;
  padding: 6px;
 
}
#dufaaa > ul {
  position: relative;
  z-index: 597;
  float: left;
}
#dufaaa > ul li {
  float: right;
  min-height: 1px;
  line-height: 1.3em;
  vertical-align: middle;
  padding: 10px;
}
#dufaaa > ul li.hover,
#dufaaa > ul li:hover {
  z-index: 599;
  cursor: default;
}
#dufaaa > ul ul {
  visibility: hidden;
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 598;
}
#dufaaa > ul ul li {
  float: none;
}
#dufaaa > ul li:hover > ul {
  visibility: visible;
}
/* Align last drop down RTL */
/* Theme Styles */
#dufaaa > ul a:link {
  text-decoration: none;
}
#dufaaa > ul a:active {
  color: #ffa500;
}
#dufaaa li {
  padding: 0;
  color: #000;
}
#dufaaa {
  font-family: 'Lato', sans-serif;
  width: auto;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  -ms-border-radius: 3px;
  -o-border-radius: 3px;
  border-radius: 3px;
  background: #0e1a2d;
  font-size: 14px;
  -moz-box-shadow: inset 0 2px 2px rgba(255, 255, 255, 0.3);
  -webkit-box-shadow: inset 0 2px 2px rgba(255, 255, 255, 0.3);
  box-shadow: inset 0 2px 2px rgba(255, 255, 255, 0.3);
}
#dufaaa > ul {
  padding: 0 5px;
  -moz-box-shadow: inset 0 -2px 2px rgba(0, 0, 0, 0.3);
  -webkit-box-shadow: inset 0 -2px 2px rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 -2px 2px rgba(0, 0, 0, 0.3);
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  -ms-border-radius: 3px;
  -o-border-radius: 3px;
  border-radius: 3px;
  display: block;
  float: none;
  zoom: 1;
}
#dufaaa > ul:before {
  content: '';
  display: block;
}
#dufaaa > ul:after {
  content: '';
  display: table;
  clear: both;
}
#dufaaa > ul > li {
  padding: 8px 5px;
}
#dufaaa> ul > li > a,
#dufaaa> ul > li > a:link,
#dufaaa > ul > li > a:visited {
  text-shadow: 0 -1px 1px #004881;
  color: #fff;
  padding: 7px 20px;
  display: block;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  -ms-border-radius: 3px;
  -o-border-radius: 3px;
  border-radius: 3px;
}
#dufaaa > ul > li > a:hover,
#dufaaa > ul > li:hover > a {
  background-color: #0082e7;
}
#dufaaa li li a {
  color: #8b8b8b;
  font-size: 14px;
}
#dufaaa li li a:hover {
  color: #5c5c5c;
  border-color: #5c5c5c;
}
#dufaaa ul ul {
  margin: 0 10px;
  padding: 0 10px;
  float: none;
  background: #efefef;
  border: 2px solid #0e1a2d;
  border-top: none;
  right: 0;
  left: 0;
  -webkit-border-radius: 0 0 3px 3px;
  -moz-border-radius: 0 0 3px 3px;
  -ms-border-radius: 0 0 3px 3px;
  -o-border-radius: 0 0 3px 3px;
  border-radius: 0 0 3px 3px;
  -moz-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}
#dufaaa ul > li > ul > li {
  margin: 0 10px 0 0;
  position: relative;
  padding: 0;
  float: right;
}
#dufaaa ul > li > ul > li > a {
  padding: 10px 20px 10px 10px;
  display: block;
}
#dufaaa ul > li > ul > li.has-sub > a:before {
  content: '';
  position: absolute;
  top: 18px;
  right: 6px;
  border: 5px solid transparent;
  border-top: 5px solid #8b8b8b;
}
#dufaaa ul > li > ul > li.has-sub > a:hover:before {
  border-top: 5px solid #5c5c5c;
}
#dufaaa ul ul ul {
  width: 200px;
  top: 100%;
  border: 2px solid #0e1a2d;
}
#dufaaa ul ul ul li {
  float: none;
}


#dufaa > ul,
#dufaa > ul li,
#dufaa > ul ul {
  list-style: none;
   margin-top:10px;
  padding: 6px;
 
}
#dufaa > ul {
  position: relative;
  z-index: 597;
  float: left;
}
#dufaa > ul li {
  float: right;
  min-height: 1px;
  line-height: 1.3em;
  vertical-align: middle;
  padding: 10px;
}
#dufaa > ul li.hover,
#dufaa > ul li:hover {
  z-index: 599;
  cursor: default;
}
#dufaa > ul ul {
  visibility: hidden;
  position: absolute;
  top: 100%;
  left: 0;
  z-index: 598;
}
#dufaa > ul ul li {
  float: none;
}
#dufaa > ul li:hover > ul {
  visibility: visible;
}
/* Align last drop down RTL */
/* Theme Styles */
#dufaa > ul a:link {
  text-decoration: none;
}
#dufaa > ul a:active {
  color: #ffa500;
}
#dufaa li {
  padding: 0;
  color: #000;
}
#dufaa {
  font-family: 'Lato', sans-serif;
  width: auto;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  -ms-border-radius: 3px;
  -o-border-radius: 3px;
  border-radius: 3px;
  background: #0e1a2d;
  font-size: 18px;
  -moz-box-shadow: inset 0 2px 2px rgba(255, 255, 255, 0.3);
  -webkit-box-shadow: inset 0 2px 2px rgba(255, 255, 255, 0.3);
  box-shadow: inset 0 2px 2px rgba(255, 255, 255, 0.3);
}
#dufaa > ul {
  padding: 0 5px;
  -moz-box-shadow: inset 0 -2px 2px rgba(0, 0, 0, 0.3);
  -webkit-box-shadow: inset 0 -2px 2px rgba(0, 0, 0, 0.3);
  box-shadow: inset 0 -2px 2px rgba(0, 0, 0, 0.3);
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  -ms-border-radius: 3px;
  -o-border-radius: 3px;
  border-radius: 3px;
  display: block;
  float: none;
  zoom: 1;
}
#dufaa > ul:before {
  content: '';
  display: block;
}
#dufaa > ul:after {
  content: '';
  display: table;
  clear: both;
}
#dufaa > ul > li {
  padding: 8px 5px;
}
#dufaa > ul > li > a,
#dufaa > ul > li > a:link,
#dufaa > ul > li > a:visited {
  text-shadow: 0 -1px 1px #004881;
  color: #fff;
  padding: 7px 20px;
  display: block;
  -webkit-border-radius: 3px;
  -moz-border-radius: 3px;
  -ms-border-radius: 3px;
  -o-border-radius: 3px;
  border-radius: 3px;
}
#dufaa > ul > li > a:hover,
#dufaa > ul > li:hover > a {
  background-color: #0082e7;
}
#dufaa li li a {
  color: #8b8b8b;
  font-size: 22px;
}
#dufaa li li a:hover {
  color: #5c5c5c;
  border-color: #5c5c5c;
}
#dufaa ul ul {
  margin: 0 10px;
  padding: 0 10px;
  float: none;
  background: #efefef;
  border: 2px solid #0e1a2d;
  border-top: none;
  right: 0;
  left: 0;
  -webkit-border-radius: 0 0 3px 3px;
  -moz-border-radius: 0 0 3px 3px;
  -ms-border-radius: 0 0 3px 3px;
  -o-border-radius: 0 0 3px 3px;
  border-radius: 0 0 3px 3px;
  -moz-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
  -webkit-box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
  box-shadow: 0 2px 3px rgba(0, 0, 0, 0.2);
}
#dufaa ul > li > ul > li {
  margin: 0 10px 0 0;
  position: relative;
  padding: 0;
  float: right;
}
#dufaa ul > li > ul > li > a {
  padding: 10px 20px 10px 10px;
  display: block;
}
#dufaa ul > li > ul > li.has-sub > a:before {
  content: '';
  position: absolute;
  top: 18px;
  right: 6px;
  border: 5px solid transparent;
  border-top: 5px solid #8b8b8b;
}
#dufaa ul > li > ul > li.has-sub > a:hover:before {
  border-top: 5px solid #5c5c5c;
}
#dufaa ul ul ul {
  width: 200px;
  top: 100%;
  border: 2px solid #0e1a2d;
}
#dufaa ul ul ul li {
  float: none;
}
 .callout-dark {
            padding: 30px;
            color: #fff;
            background-color:#337ab7;
            margin-top:0;

        }
        
        .callout-dark h1,
        h2,
        h3,
        h4 {
            font-weight: 300;
            line-height: 1.4;
        }
        
        .callout-dark p {
            color: #B1B1B1;
            font-size: 17px;
        }
        .footer-distributed{
  background-color: #0e1a2d;
  box-shadow: 0 1px 1px 0 rgba(0, 0, 0, 0.12);
  box-sizing: border-box;
  width: 100%;
  font: bold 16px sans-serif;
  text-align: left;

  padding: 50px 60px 40px;
  margin-top: 80px;
  overflow: hidden;
}

/* Footer left */

.footer-distributed .footer-left{
  float: left;
}

/* The company logo */

.footer-distributed h3{
  color:  #ffffff;
  font: normal 36px 'Cookie', cursive;
  margin: 0 0 10px;
}

.footer-distributed h3 span{
  color:  #ffffff;
}

/* Footer links */

.footer-distributed .footer-links{
  color:  #ffffff;
  margin: 0 0 10px;
  padding: 0;
}

.footer-distributed .footer-links a{
  display:inline-block;
  line-height: 1.8;
  text-decoration: none;
  color:  inherit;
}

.footer-distributed .footer-company-name{
  color:  #8f9296;
  font-size: 14px;
  font-weight: normal;
  margin: 0;
}

/* Footer social icons */

.footer-distributed .footer-icons{
  margin-top: 40px;
}

.footer-distributed .footer-icons a{
  display: inline-block;
  width: 35px;
  height: 35px;
  cursor: pointer;
  background-color:  #337ab7;
  border-radius: 2px;

  font-size: 20px;
  color: #ffffff;
  text-align: center;
  line-height: 35px;

  margin-right: 3px;
  margin-bottom: 5px;
}

/* Footer Right */

.footer-distributed .footer-right{
  float: right;
}

.footer-distributed .footer-right p{
  display: inline-block;
  vertical-align: top;
  margin: 15px 42px 0 0;
  color: #ffffff;
}

/* The contact form */

.footer-distributed form{
  display: inline-block;
}

.footer-distributed form input,
.footer-distributed form textarea{
  display: block;
  border-radius: 3px;
  box-sizing: border-box;
  background-color: #0e1a2d;
  box-shadow: 0 1px 0 0 rgba(255, 255, 255, 0.1);
  border: none;
  resize: none;

  font: inherit;
  font-size: 14px;
  font-weight: normal;
  color:  #ffffff;

  width: 400px;
  padding: 18px;
}

.footer-distributed ::-webkit-input-placeholder {
  color:  #ffffff;
}

.footer-distributed ::-moz-placeholder {
  color:  #ffffff;
  opacity: 1;
}

.footer-distributed :-ms-input-placeholder{
  color:  #ffffff;
}


.footer-distributed form input{
  height: 55px;
  margin-bottom: 15px;
}

.footer-distributed form textarea{
  height: 100px;
  margin-bottom: 20px;
}

.footer-distributed form button{
  border-radius: 3px;
  background-color: #0e1a2d;
  color: #ffffff;
  border: 0;
  padding: 15px 50px;
  font-weight: bold;
  float: right;
}

/* If you don't want the footer to be responsive, remove these media queries */

@media (max-width: 1000px) {

  .footer-distributed {
    font: bold 14px sans-serif;
  }

  .footer-distributed .footer-company-name{
    font-size: 12px;
  }

  .footer-distributed form input,
  .footer-distributed form textarea{
    width: 250px;
  }

  .footer-distributed form button{
    padding: 10px 35px;
  }

}

@media (max-width: 800px) {

  .footer-distributed{
    padding: 30px;
  }

  .footer-distributed .footer-left,
  .footer-distributed .footer-right{
    float: none;
    max-width: 300px;
    margin: 0 auto;
  }

  .footer-distributed .footer-left{
    margin-bottom: 40px;
  }

  .footer-distributed form{
    margin-top: 30px;
  }

  .footer-distributed form{
    display: block;
  }

  .footer-distributed form button{
    float: none;
  }
}


        </style>
    <script type="text/javascript" charset="utf-8">
        // Pause the video when the modal is closed
        $(document).on('click', '.hanging-close, .modal-backdrop, .modal', function (event) {
            // Remove the src so the player itself gets removed, as this is the only
            // reliable way to ensure the video stops playing in IE
            $("#trailer-video-container").empty();
        });
        // Start playing the video whenever the trailer modal is opened
        $(document).on('click', '.movie-tile', function (event) {
            var trailerYouTubeId = $(this).attr('data-trailer-youtube-id')
            var sourceUrl = 'https://www.youtube.com/embed/' + trailerYouTubeId + '?autoplay=1&html5=1';
            $("#trailer-video-container").empty().append($("<iframe></iframe>", {
              'id': 'trailer-video',
              'type': 'text-html',
              'src': sourceUrl,
              'frameborder': 0
            }));
        });
        // Animate in the movies when the page loads
        $(document).ready(function () {
          $('.movie-tile').hide().first().show("fast", function showNext() {
            $(this).next("div").show("fast", showNext);
          });
        });
    </script>
</head>
'''

# The main page layout and title bar
main_page_content = '''
  <body>
  <div class="container">
  <div class="row">
<div id='dufaa'>
<ul>
   <li class='active has-sub'><a href='#'><span>Video type1</span></a>
      <ul>
         <li class='has-sub'><a href='#'><span>Product 1</span></a>
         </li>
         <li class='has-sub'><a href='#'><span>Product 2</span></a>

         </li>
      </ul>
   </li>


<li class='active has-sub'><a href='#'><span>Video type2</span></a>
      <ul>
         <li class='has-sub'><a href='#'><span>Product 1</span></a>
         </li>
         <li class='has-sub'><a href='#'><span>Product 2</span></a>

         </li>
      </ul>
   </li>


   <li class='active has-sub'><a href='#'><span>Video type3</span></a>
      <ul>
         <li class='has-sub'><a href='#'><span>Product 1</span></a>
         </li>
         <li class='has-sub'><a href='#'><span>Product 2</span></a>

         </li>
      </ul>
   </li>

   <li class='active has-sub'><a href='#'><span>Video type4</span></a>
      <ul>
         <li class='has-sub'><a href='#'><span>Product 1</span></a>
         </li>
         <li class='has-sub'><a href='#'><span>Product 2</span></a>

         </li>
      </ul>
   </li>

   <li class='active has-sub'><a href='#'><span>Video type5</span></a>
      <ul>
         <li class='has-sub'><a href='#'><span>Product 1</span></a>
         </li>
         <li class='has-sub'><a href='#'><span>Product 2</span></a>

         </li>
      </ul>
   </li>
</ul>
</div>



                               


                    <div class="callout-dark text-center fade-in-b">
                        <h1>location- <b>Movies</b> -4You</h1>
                        <p><h2><marquee  behavior="scroll" direction="up" scrollamount="1"  style="text-align: center; color:with;">The best Arabic site for short video jobs and a open link to watch</marquee></h2></p>
                    </div>

    <!-- Trailer Video Modal -->
    <div class="modal" id="trailer">
      <div class="modal-dialog">
        <div class="modal-content">
          <a href="#" class="hanging-close" data-dismiss="modal" aria-hidden="true">
            <img src="https://lh5.ggpht.com/v4-628SilF0HtHuHdu5EzxD7WRqOrrTIDi_MhEG6_qkNtUK5Wg7KPkofp_VJoF7RS2LhxwEFCO1ICHZlc-o_=s0#w=24&h=24"/>
          </a>
          <div class="scale-media" id="trailer-video-container">
          </div>
        </div>
      </div>
    </div>

    <!-- Main Page Content -->
    <div class="container">
      <div class="navbar navbar-inverse navbar-fixed-top" role="navigation">
        <div class="container">
          <div class="navbar-header">
            <a class="navbar-brand" href="#">Fresh Tomatoes Movie Trailers</a>
          </div>
        </div>
      </div>
    </div>
    <div class="container">
      {movie_tiles}
    </div>

  </body>
</html>
'''
 

                                         

# A single movie entry html template
movie_tile_content = '''
<div class="col-md-9 col-lg-4 movie-tile text-center" data-trailer-youtube-id="{trailer_youtube_id}" data-toggle="modal" data-target="#trailer">
 <div class="cuadro_intro_hover hidpup" style="background-color:#cccccc;">
                                        <p style="text-align:left; margin-top:20px;">
                                            <img src="{poster_image_url}" class="img-responsive" alt="">
                                        </p>
                                        <div class="caption">
                                            <div class="blur"></div>
                                            <div class="caption-text">
                                                <h3 style="border-top:2px solid white; border-bottom:2px solid white; padding:10px;">{movie_title}</h3>
                                               <p>{storyline}</p>
                                                <a class=" btn btn-default" href="{trailer_youtube_url}"><span class="glyphicon glyphicon-plus">Watch</span></a>
                                            </div>
                                        </div>
                                        </div></div>
'''
ddd = '''<!-- The content of your page would go here. -->

                </div></div>
    <footer class="footer-distributed">

      <div class="footer-left">

        <h3>Movie<span>logo</span></h3>

        <p class="footer-links">
          <a href="#">Home</a>
          
          <a href="#">Blog</a>
          
          <a href="#">Pricing</a>
          
          <a href="#">About</a>
          
          <a href="#">Faq</a>
          
          <a href="#">Contact</a>
        </p>

        <p class="footer-company-name">Advmarkt.com &copy; 2018</p>

        <div class="footer-icons">

          <a href="#"><i class="fa fa-facebook"></i></a>
          <a href="#"><i class="fa fa-twitter"></i></a>
          <a href="#"><i class="fa fa-linkedin"></i></a>
          <a href="#"><i class="fa fa-github"></i></a>

        </div>

      </div>

      <div class="footer-right">

        <p></p>

        <form action="#" method="post">

          <input type="text" name="email" placeholder="Email" />
          <textarea name="message" placeholder="Message"></textarea>
          <button>Send</button>

        </form>

      </div>

    </footer>'''

def create_movie_tiles_content(movies):
    # The HTML content for this section of the page
    content = ''
    for movie in movies:
        # Extract the youtube ID from the url
        youtube_id_match = re.search(
            r'(?<=v=)[^&#]+', movie.trailer_youtube_url)
        youtube_id_match = youtube_id_match or re.search(
            r'(?<=be/)[^&#]+', movie.trailer_youtube_url)
        trailer_youtube_id = (youtube_id_match.group(0) if youtube_id_match
                              else None)

        # Append the tile for the movie with its content filled in
        content += movie_tile_content.format(
            movie_title=movie.title,
            poster_image_url=movie.poster_image_url,
            storyline =movie.storyline,
            trailer_youtube_url =movie.trailer_youtube_url,
            trailer_youtube_id=trailer_youtube_id
        )
    return content


def open_movies_page(movies):
    # Create or overwrite the output file
    output_file = open('fresh_tomatoes.html', 'w')

    # Replace the movie tiles placeholder generated content
    rendered_content = main_page_content.format(
        movie_tiles=create_movie_tiles_content(movies))

    # Output the file
    output_file.write(main_page_head + rendered_content)
    #output_file.close()
    output_file.write(ddd)
    output_file.close()

    # open the output file in the browser (in a new tab, if possible)
    url = os.path.abspath(output_file.name)
    webbrowser.open('file://' + url, new=2)