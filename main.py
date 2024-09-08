from PIL import Image, ImageDraw, ImageFont

def add_watermark(input_image_path, output_image_path, watermark_text):
    original = Image.open(input_image_path).convert('RGBA')
    txt = Image.new('RGBA', original.size, (255, 255, 255, 0))

    try:
        font = ImageFont.truetype('arial.ttf', 40)
    except IOError:
        font = ImageFont.load_default()

    draw = ImageDraw.Draw(txt)
    width, height = original.size
    
    if hasattr(draw, 'textbbox'):
        text_bbox = draw.textbbox((0, 0), watermark_text, font=font)
        text_width = text_bbox[2] - text_bbox[0]
        text_height = text_bbox[3] - text_bbox[1]
    else:
        text_width, text_height = draw.textsize(watermark_text, font=font)

    position = (width - text_width - 40, height - text_height - 40) 

    draw.text(position, watermark_text, fill=(255, 255, 255, 128), font=font)
    
    watermarked = Image.alpha_composite(original, txt)
    watermarked.show()

    watermarked.convert('RGB').save(output_image_path, 'JPEG')

add_watermark('Image.jpg', 'Terrond.jpg', 'TERROND')