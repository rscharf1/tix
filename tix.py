#!/usr/bin/python

from PIL import Image, ImageFont, ImageDraw 
import os, re, sys

# Method that takes in the base ticket and other parameters

def blues_test():

    my_image = Image.open("model_tix/blues.jpeg")

    time_font = ImageFont.truetype('fonts/avenir-bold.ttf', 22)
    time_text = "7:00 PM"

    date_font = ImageFont.truetype('fonts/arial.ttf', 40)
    date_text = "Oct 28, 2021"

    round_text = "St. Louis Blues vs. Colorado Avalanche"
    round_font = ImageFont.truetype('fonts/arial.ttf', 39)

    section_text = "115"
    section_font = ImageFont.truetype('fonts/arial.ttf', 37)

    row_text = "J"
    row_font = ImageFont.truetype('fonts/arial.ttf', 37)

    seat_text = "8"
    seat_font = ImageFont.truetype('fonts/arial.ttf', 37)

    entry_text = "PORTAL 15"
    entry_font = ImageFont.truetype('fonts/arial.ttf', 38)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((765,250), time_text, (51,153,255,255), font = time_font, anchor="rm")
    image_editable.text((765,280), date_text, (255, 255, 255), font = date_font, anchor="rm")
    image_editable.text((60,612), round_text, (255, 255, 255), font = round_font, anchor="lm")
    image_editable.text((62,707), section_text, (255, 255, 255), font = section_font, anchor="lm")
    image_editable.text((410,707), row_text, (255, 255, 255), font = row_font, anchor="lm")
    image_editable.text((714,705), seat_text, (255, 255, 255), font = seat_font, anchor="lm")
    image_editable.text((60,802), entry_text, (255, 255, 255), font = entry_font, anchor="lm")

    my_image = my_image.convert('RGB')
    my_image.save("test.jpg")

    print("Done")

def bruins(time, date, game, section, row, seat, entry, path):
    my_image = Image.open("model_tix/bruins.jpeg")

    time_font = ImageFont.truetype('fonts/avenir-bold.ttf', 33)
    date_font = ImageFont.truetype('fonts/arial.ttf', 60)
    game_font = ImageFont.truetype('fonts/arial.ttf', 60)
    section_font = ImageFont.truetype('fonts/arial.ttf', 55)   
    row_font = ImageFont.truetype('fonts/arial.ttf', 50)
    seat_font = ImageFont.truetype('fonts/arial.ttf', 50)
    entry_font = ImageFont.truetype('fonts/arial.ttf', 45)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((1035,366), time, (241,199,83), font = time_font, anchor="rm")
    image_editable.text((1035,410), date, (255, 255, 255), font = date_font, anchor="rm")
    image_editable.text((91,875), "Boston Bruins vs " + game, (255, 255, 255), font = game_font, anchor="lm")
    image_editable.text((93,1015), section, (255, 255, 255), font = section_font, anchor="lm")
    image_editable.text((595,1015), row, (255, 255, 255), font = row_font, anchor="lm")
    image_editable.text((962,1015), seat, (255, 255, 255), font = seat_font, anchor="lm")
    image_editable.text((91,1160), entry, (255, 255, 255), font = entry_font, anchor="lm")

    # my_image.save("temp_tix/result2.jpg")
    my_image.save(path)
    
    print("Done")

def blues(time, date, game, section, row, seat, entry, path):
    my_image = Image.open("model_tix/blues.jpeg")

    time_font = ImageFont.truetype('fonts/avenir-bold.ttf', 22)
    date_font = ImageFont.truetype('fonts/arial.ttf', 40)
    game_font = ImageFont.truetype('fonts/arial.ttf', 39)
    section_font = ImageFont.truetype('fonts/arial.ttf', 37)   
    row_font = ImageFont.truetype('fonts/arial.ttf', 37)
    seat_font = ImageFont.truetype('fonts/arial.ttf', 37)
    entry_font = ImageFont.truetype('fonts/arial.ttf', 38)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((765,250), time, (51,153,255,255), font = time_font, anchor="rm")
    image_editable.text((765,280), date, (255, 255, 255), font = date_font, anchor="rm")
    image_editable.text((60,612), "St. Louis Blues vs. " + game, (255, 255, 255), font = game_font, anchor="lm")
    image_editable.text((62,707), section, (255, 255, 255), font = section_font, anchor="lm")
    image_editable.text((410,707), row, (255, 255, 255), font = row_font, anchor="lm")
    image_editable.text((714,705), seat, (255, 255, 255), font = seat_font, anchor="lm")
    image_editable.text((60,802), entry, (255, 255, 255), font = entry_font, anchor="lm")

    # image_editable = ImageDraw.Draw(my_image)
    # image_editable.text((1035,366), time, (241,199,83), font = time_font, anchor="rm")
    # image_editable.text((1035,410), date, (255, 255, 255), font = date_font, anchor="rm")
    # image_editable.text((91,875), "St. Louis Blues vs. " + game, (255, 255, 255), font = game_font, anchor="lm")
    # image_editable.text((93,1015), section, (255, 255, 255), font = section_font, anchor="lm")
    # image_editable.text((595,1015), row, (255, 255, 255), font = row_font, anchor="lm")
    # image_editable.text((962,1015), seat, (255, 255, 255), font = seat_font, anchor="lm")
    # image_editable.text((91,1160), entry, (255, 255, 255), font = entry_font, anchor="lm")

    my_image = my_image.convert('RGB')
    my_image.save(path)

    print("Done")

def main():
    print("main function")
    blues_test()

if __name__ == "__main__":
    from PIL import Image, ImageFont, ImageDraw 
    import os, re, sys
    main()