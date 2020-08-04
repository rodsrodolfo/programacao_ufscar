from PIL import Image

print('what you need to do is')
filename = input('file name with .format:')

image=Image.open(filename)
pixels=image.load()
pixelseq=[]
width, height = image.size

for a in range(width):
    for b in range(height):
        if pixels[b,a]==(255,255,255,255):
            pixels[b,a]=(0,200,0,255)
        pixelseq.append(pixels[b,a])

image.putdata(pixelseq)
image.save('New'+filename)
