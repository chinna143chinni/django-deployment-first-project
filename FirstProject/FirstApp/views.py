from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def display(request):#views-function (/welcome/)
    print("welcome/url is request& display()is executed");
    ss = "<center><h2 style='color:green;'>Hello CHINNA, Welcome to Django First-ProjectFirst-App</h2><hr/> color='red' width='80%'size='5' /></center>";
    return HttpResponse(ss);
    

def show (request):       #(welcome/url)
    ss = '''<!-- 
        HTML Wadpage to display"Welcome-massage" with different Headings
		        (F:CHINNA\HTML\Welcome.html)
-->


<html>
			<head>
                    <title>***Welcome-page***</title>
                    <style>
                            h1{
                                color:blue;
                            }
                           	
                            h2{
                                color:green;
                            }
                            
                            h3{
                                color:red;
                            }
                            
                            h4{
                                color:blue;
                            }
							
                            h5{
                                color:;
                            }
                            h1,h3,h5{
							            background-color:yellow;
							}			
							h2,h4,h6{
                                        background-color:ligtgreen;
                            }

		</style>
</head>
<body>
            <center>
                        
						<h1>Welcome to DJANGO HTML Webpage CHINNA</h1>
                        <hr color='RED' Width='95%'/>						
						
                        <h2>Welcome to DJANGO HTML Webpage</h2>
                        <hr color='brown' Width='85%'/>				

                        <h3>Welcome to CHINNA DJANGO FILE HTML Webpage</h3>
                        <hr color='brown' Width='75%'/>
						
                        <h4>Welcome CHINNA MASSAGE WITH WEB PAGES</h4>
                        <hr color='brown' Width='65%'/>
						
                        <h5>Welcome to DJANGO HTML Webpage</h5>
                        <hr color='brown' Width='55%'/>
						
                        <h6>Welcome to DJANGO HTML Webpage</h6>
                        <hr color='brown' Width='45%'/>
			</center>
    </body>
</html> 
''';        
                 
    return HttpResponse(ss);    


def hello (request):
    print("hello/ url is request& hello() is executed");
    ss =''' 
    <html>
        <head>
            <title>Hello webpage</title>
            <style>
                h1{
                color :blue;
                }
                h2{
                color:Green;
                }
                h3{
                color:red;
                }
                h1,h2,h3{
                background-color:bule;
                width:50%;
                border:2px solid Brown;
                }
            </style>    
        </head>
        <body>
            <center>
                <h1>Hello CHINNA User/..!!!</h1>
                <hr/>
                <h2>Welcome to Django=App CHINNA</h2>
                <hr /> 
                <h3>Have a nice day CHINNA...</h3>
            </center>    
        </body>
    </html>
    ''';
    return HttpResponse(ss); 

import time;
def senddatetime(request):
    print("dtime/ url is requested & senddatetime() is executed");
    ct = time.ctime()
    print("Client Request Date & time on server :: ",ct);
    ss =''' 
    <html>
        <head>
            <title>Date-time webpage</title>
            <style>
                h1{
                color :blue;
                }
                h2{
                color:Green;
                }
                h3{
                color:red;
                }
                h1,h2,h3{
                background-color:bule;
                width:60%;
                border:2px solid Brown;
                }
            </style>    
        </head>
        <body>
            <center>
                <h1>welcome to DJANGO CHINNA User/..!!!</h1>
                <hr/>color ='brown' width='80%'/>
                <h2>server-Date & Timem:: </h2>
                <hr/>color = 'brown'width='80%'/>
                <h3>''',ct,'''</h3>
            </center>    
        </body>
    </html>
    ''';
    return HttpResponse(ss); 


def demo(request):
    print("mulitple=Request=URLs same respose");
    htmldata= '''<center>
        <h1>Welcome CHINNI Demo User!!!</h1>
        <hr />
        <h2>This is Same-Output for diff-mulitple-requests-URLs</h2>
        <hr />
        <h3>Have a Great Day... CHINNA</h3>
        </center>''';
    return HttpResponse(htmldata);  


def chinna(request):
    htmldata= '''<center>
        <h1>welcome to DEFAULT chinna Home-page!!!</h1>
        <hr />
        <h2>Your Request Page is Not-Found...</h2>
        <hr />
        <h3>plz try other URL or Links!!!,/h3>
        </center>''';
    return HttpResponse(htmldata);  


















    
        
    


































                        
                        
