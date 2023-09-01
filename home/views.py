from django.http import HttpResponse
from django.shortcuts import render
# from django.template import loader

# Create your views here.
def homepage(request):
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Coffee's Crib</title>
    <link rel="stylesheet" href="styles.css">
</head>
<body>
    <div class="background-image">
    <img src="/coffee logo.png" id="top"width="170" alt="coffee logo"><br><br>
    <h2>Coffee Junkie</h2><br><br>
    <ul>
        <li><a href="coffee_sight.html">Home</a></li>
        <li><a href="About.html">About</a></li>
        <li><a href="Numbers.html">Numbers</a></li>
        <li><a href="contact.html">Contact</a></li>
    </ul>

    

   
<h2>Featured Products</h2>
<h3>House Blend Coffee</h3>
<img src="/pexels-burst-374885.jpg" height="170"alt="Coffee">
<p>Lorem ipsum dolor sit amet consectetur, adipisicing elit. Molestiae beatae minima sint illum modi officiis deserunt tenetur dolores neque deleniti veritatis reprehenderit quasi, quisquam temporibus provident reiciendis quo. Autem, impedit!</p>
<p><a href="https://www.google.com/" target="_blank">Details</a></p>

<h3>French Roast</h3>
<img src="/pexels-chevanon-photography-302902.jpg" height="170" alt="">
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos officiis fuga incidunt enim, labore provident asperiores vel exercitationem recusandae? Vitae ducimus corporis laboriosam rerum id aliquam? Saepe odio recusandae nulla.</p>
<a href="https://www.google.com/" target="_blank">Details</a>

<h3>Columbian Roast</h3>
<img src="/pexels-viktoria-alipatova-2668498.jpg" height="250" width="250" alt="">
<p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Eos officiis fuga incidunt enim, labore provident
    asperiores vel exercitationem recusandae? Vitae ducimus corporis laboriosam rerum id aliquam? Saepe odio recusandae
    nulla.</p>
<a href="https://www.google.com/" target="_blank">Details</a><br><br>
<p>Copyright&copy;2021</p>
<a href="#top">Back to Top</a>

</div >
</body>
</html>""")



def about(request):
    return render(request, 'home/coffee.html')
    