def setup():
    global oldColor
    size(500, 500)

    
    img = loadImage("flowers.jpg")
    image(img, 0, 0, 500, 500)
   
    # filter(BLUR, 3) #blurry image
    
    loadPixels()
     
    numPixels = width * height

    for i in range(numPixels):
        oldColor = pixels[i]
        r = red(oldColor) 
        g = green(oldColor)
        b = blue(oldColor)

    #     #flip image   
    # for i in range(len(pixels)):
    #     x = i % width
    #     y = i / width
    #     if x < width / 2:
    #         flipI = (y + 1) * width - x - 1
    #         tmp = pixels[i]
    #         pixels[i] = pixels[flipI]
    #         pixels[flipI] = pixels[i]
    #         pixels[flipI] = tmp

        # avg = ( r + g + b/ 3)
        # pixels[i] = color(avg) #grayscale
    
        # pixels[i] = color( r, 0, 0) #enhances red
        
        # pixels[i] = color(0, g, 0) #enhances green
        
        # pixels[i] = color(0, 0, b) #emhances blue
        
        # pixels[i] = color(r, 0, b) #enhances blue/ red
        
        # pixels[i] = color(0, g, b) #enhances green/ blue
        
        # pixels[i] = color(r, g, 0) #enhances red/ green
        
        # pixels[i] = color(r / 3, g / 3, b + 3)
        
        # pixels[i] = color(r, g + b/ 3) #invert
        
        # pixels[i] = color(255 - r, 255 - g, 255 - b) #negative
        
        # pixels[i] = color(r + 255, g + 228, b + 181) #multiple color change
     

    updatePixels()
     
            

    
    
    
