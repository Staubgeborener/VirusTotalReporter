def header():
   block = '''
   <!DOCTYPE html>
   <html>
   <head>
   <meta name="viewport" content="width=device-width, initial-scale=1">
   <style>
   html { height: 90%; }
   body { height: 90%; }

   #wrapper {
     display: flex;
     border: 1px solid black;
     height: 100%;
   }

   .vertical-menu {
     width: 200px;
   }

   .vertical-menu a {
     background-color: #eee;
     color: black;
     display: block;
     padding: 12px;
     text-decoration: none;
   }

   .vertical-menu a:hover {
     background-color: #ccc;
   }

   .vertical-menu a.active {
     background-color: #4CAF50;
     color: white;
   }

   iframe {
     width: 100%;
     height: 100%;
   }

   </style>
   </head>

   <body>
   <h1>Result - VirusTotalReporter</h1>
   <div id="wrapper">
   <div class="vertical-menu">
   '''
   return block

#-------------------------------
def footer():
   block = '''
   </div>
   <iframe src="" name="myFrame"></iframe>
   </body>
   </div>
   <br>
   <center>
   <a href="https://github.com/Staubgeborener/VirusTotalReporter/">Github</a> 
   </center>
   </html>
   '''
   return block