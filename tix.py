#!/usr/bin/python

from PIL import Image, ImageFont, ImageDraw 
import os, re, sys

# Method that takes in the base ticket and other parameters

def bruins_test():

    my_image = Image.open("model_tix/bruins.jpeg")

    time_font = ImageFont.truetype('fonts/avenir-bold.ttf', 33)
    time_text = "7:00 PM"

    date_font = ImageFont.truetype('fonts/arial.ttf', 60)
    date_text = "Nov 4, 2021"

    round_text = "Boston Bruins vs Detroit Red Wings"
    round_font = ImageFont.truetype('fonts/arial.ttf', 60)

    section_text = "LOGE3"
    section_font = ImageFont.truetype('fonts/arial.ttf', 55)

    row_text = "11"
    row_font = ImageFont.truetype('fonts/arial.ttf', 50)

    seat_text = "4"
    seat_font = ImageFont.truetype('fonts/arial.ttf', 50)

    entry_text = "ENTER GATE 3"
    entry_font = ImageFont.truetype('fonts/arial.ttf', 45)

    image_editable = ImageDraw.Draw(my_image)
    image_editable.text((1035,366), time_text, (241,199,83), font = time_font, anchor="rm")
    image_editable.text((1035,410), date_text, (255, 255, 255), font = date_font, anchor="rm")
    image_editable.text((91,875), round_text, (255, 255, 255), font = round_font, anchor="lm")
    image_editable.text((93,1015), section_text, (255, 255, 255), font = section_font, anchor="lm")
    image_editable.text((595,1015), row_text, (255, 255, 255), font = row_font, anchor="lm")
    image_editable.text((962,1015), seat_text, (255, 255, 255), font = seat_font, anchor="lm")
    image_editable.text((91,1160), entry_text, (255, 255, 255), font = entry_font, anchor="lm")

    my_image.save("results/result.jpg")

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
    image_editable.text((91,875), game, (255, 255, 255), font = game_font, anchor="lm")
    image_editable.text((93,1015), section, (255, 255, 255), font = section_font, anchor="lm")
    image_editable.text((595,1015), row, (255, 255, 255), font = row_font, anchor="lm")
    image_editable.text((962,1015), seat, (255, 255, 255), font = seat_font, anchor="lm")
    image_editable.text((91,1160), entry, (255, 255, 255), font = entry_font, anchor="lm")

    # my_image.save("temp_tix/result2.jpg")
    my_image.save(path)

    print("Done")

def main():
    print("main function")
    # bruins_test()
    print(sys.argv[1])

if __name__ == "__main__":
    from PIL import Image, ImageFont, ImageDraw 
    import os, re, sys
    main()