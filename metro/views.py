from django.shortcuts import render
from django.shortcuts import render

import random
import colorsys

# Create your views here.

def index(request):

    def hsv_to_hex(hue, saturation=0.85, value=0.53):
        r, g, b = colorsys.hls_to_rgb(hue /360, saturation, value)
        return "#{:02X}{:02X}{:02X}".format(int(r * 255), int(g * 255),int(b * 255))
    
    colors = []
  

    for _ in range(1, 11):
        color = hsv_to_hex(random.randint(0, 261), 0.76, 0.87)
        colors.append(color)

    
    return render(request, 'index.html', {'colors': colors})