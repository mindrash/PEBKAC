#!/usr/bin/env python3

from random import randrange
import random
from turtle import color
import pyfiglet
import logging
import datetime
import uuid
import json

def main():
    logging.basicConfig(level=logging.INFO, filename='logs/pebkac.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
    logging.info(pyfiglet.figlet_format("pebkac"))
    console_line = "*" * 80
    logging.info(console_line)
    logging.info("Starting: " + str(datetime.datetime.now()))

    #telemetry_start_date = datetime.datetime(1990, 9, 9)
    telemetry_start_date = datetime.datetime(1977, 9, 9)
    telemetry_end_date = datetime.datetime(1978, 10, 9)
    #telemetry_end_date = datetime.datetime(2005, 1, 21)
    delta = datetime.timedelta(days=1)
    svg_count = 1
    
    while telemetry_start_date <= telemetry_end_date:
        pebkac(telemetry_start_date, svg_count)
        telemetry_start_date += delta
        svg_count += 1

    logging.info(console_line)
    logging.info("Finished: " + str(datetime.datetime.now()))

def pebkac(telemetry_start_date, svg_name):
    description = "The PEBKAC series (pebkac.fyi) is dynamically generated with location and solar wind telemetry data from the Voyager 1 spacecraft. Each is a random view from a celestial body in our solar system. The signal strength of voyager degrades over the series and is highlighted when close to one of the bodies. Major solar storms and other worldly events are highlighted along the way. More project details and variation information can be found at pebkac.fyi."
    voyager_craft = "VOYAGER 1"
    ipfs_url = "[[IPFS]]"
    voyager_location = ""
    voyager_date = telemetry_start_date
    logging.info("Voyager date: " + str(voyager_date))

    palette_options = [
            [
                ["#06113C", "#FF8C32", "#DDDDDD", "#EEEEEE"], # Mercury
                ["#6f6370", "#827397", "#4D4C7D", "#363062"], # Venus 
                ["#031926", "#468189", "#77aca2", "#9dbebb", "#f4e9cd"], # Earth
                ["#333333", "#FFFFFF", "#E1F4F3", "#706C61"], # Moon
                ["#000000", "#6f1d1b", "#bb9457", "#432818", "#99582a", "#ffe6a7"], # Mars
                ["#0f4c5c", "#e36414", "#fb8b24", "#9a031e", "#5f0f40"], # Jupiter 
                ["#000814", "#003566", "#ffc300", "#ffd60a"], # Saturn 
                ["#001b59", "#35858B", "#4FBDBA", "#2e4ab0"], # Uranus :)
                ["#03045E", "#00B4D8", "#90E0EF", "#CAF0F8"], # Neptune
                ["#091353", "#9D84B7", "#D5D5D5", "#B2F9FC"], # Pluto
                ["#000000", "#301B3F", "#3C415C", "#B4A5A5"], # X
            ],
            [
                ["#000000", "#463f3a", "#8a817c", "#bcb8b1"], # Mercury
                ["#8B91A1", "#BBB7AB", "#DDD8D4", "#EFEFEF"], # Venus
                ["#3C4258", "#FBFCFF", "#927E77", "#945B47", "#8CB1DE", "#3B5D38"], # Earth
                ["#000000", "#FFFFFF", "#E1F4F3", "#706C61"], # Moon
                ["#000000", "#99857A", "#C67B5C", "#E27B58", "#FF9D6F", "#663926", "#8E6A5A"], # Mars
                ["#404436", "#A79C86", "#D2CFDA", "#D39C7E", "#90614D", "#C88B3A"], # Jupiter 
                ["#343E47", "#7B7869", "#A49B72", "#C5AB6E", "#C3A171"], # Saturn 
                ["#001b59", "#D5FBFC", "#BBE1E4", "#93B8BE", "#65868B"], # Uranus :)
                ["#061a40", "#b9d6f2", "#0353a4", "#006daa", "#003559"], # Neptune
                ["#676767", "#95999E", "#7588A1", "#4E6D96", "#32527B"], # Pluto
                ["#200A24", "#321A37", "#441E4B", "#4E2C5D"], # X
            ],
            [
                ["#2B4648", "#D06F5C", "#6E4546", "#9E695A", "#CCC2AE"], # Mercury
                ["#6E6A91", "#B88FAE", "#DFD8CA", "#C2A695"], # Venus
                ["#3C4258", "#8CAE98", "#E7DBD1", "#D09768"], # Earth
                ["#000000", "#FFFFFF", "#E1F4F3", "#706C61"], # Moon
                ["#000000", "#99857A", "#C67B5C", "#E27B58", "#FF9D6F", "#663926", "#8E6A5A"], # Mars
                ["#3E1F65", "#39669A", "#FFC72E", "#FC792D", "#E03522"], # Jupiter
                ["#343E47", "#FC6A21", "#FF7E01", "#FFBF01", "#FFE159"], # Saturn 
                ["#001b59", "#094C93", "#0C73B2", "#1C96BA", "#3CBCC7"], # Uranus :)
                ["#061a40", "#0771B8", "#0F7AC0", "#1E97C4", "#2DA7C7"], # Neptune
                ["#676767", "#C5C5FC", "#A1BBF0", "#A5E8E6", "#B0F5D9"], # Pluto
                ["#02055A", "#6D5C55", "#6D5C55", "#4B2A57", "#341C3A"], # X
            ],
        ]

    palette = palette_options[randrange(0, len(palette_options))]

    night_sky = [
        [["Venus", 1], ["Earth", 1], ["Earth", .8], ["Mars", .8], ["Jupiter", .8], ["Saturn", .8]], # Mercury
        [["Mercury", 1], ["Earth", 1], ["Earth2", .8], ["Mars", 1.0], ["Jupiter", 1.0]], # Venus
        [["Mercury", .7], ["Venus", 1], ["Moon", 1], ["Mars", 1], ["Jupiter", 1], ["Saturn", .7]], # Earth
        [["Mercury", .5], ["Venus", 1], ["Earth", 1], ["Mars", 1], ["Jupiter", 1], ["Saturn", .7]], # Moon
        [["Mercury", .8], ["Venus", .8], ["Earth", 1], ["Earth", .8], ["Jupiter", 1], ["Saturn", 1.0]], # Mars
        [["Venus", .8], ["Earth", .8], ["Moon1", 1], ["Moon2", 1], ["Moon3", 1], ["Moon4", 1], ["Saturn", 1]], # Jupiter
        [["Moon1", 1],  ["Jupiter", 1]], # Saturn
        [["Jupiter", 1], ["Saturn", 1], ["Neptune", .7]], # Uranus :)
        [["Jupiter", 1], ["Saturn", 1], ["Triton", 1]], # Neptune
        [["Jupiter", .8], ["Saturn", .7], ["Moon1", 1.0]], # Pluto
        [["Jupiter", .8], ["Saturn", .7]], # X
    ]

    bodies = ["Mercury", "Venus", "Earth", "Moon", "Mars", "Jupiter", "Saturn", "Uranus", "Neptune", "Pluto", "X"]

    vert_size = 1200
    hor_size = 1200
    wave_count = randrange(2, 7)
    curve_count = randrange(8, 20)

    svg = '<!DOCTYPE svg PUBLIC "-//W3C//DTD SVG 1.1//EN" "http://www.w3.org/Graphics/SVG/1.1/DTD/svg11.dtd">'

    body_count = randrange(0, len(palette)) # Ice-T!
    logging.info("Celetial body: " + bodies[body_count])
    base_path_color = palette[body_count][0]
    svg += '<svg width="' + str(hor_size) + 'px" height="' + str(vert_size) + 'px"  style="background-color:' + base_path_color + '" xmlns="http://www.w3.org/2000/svg" version="1.1">'
    svg += '<defs>'
    #svg += '<filter id="grain" filterUnits="objectBoundingBox" x="0%" y="0%" width="100%" height="100%"><feTurbulence type="fractalNoise" baseFrequency="0.4" numOctaves="4"/></filter>'
    svg += '</defs>'
    day_of_year = voyager_date.toordinal() - datetime.date(voyager_date.year, 1, 1).toordinal() + 1

    exp_string = ""
    if (voyager_date.year >= 1977):
        data_file = "data/"
        if voyager_date.year < 1990:
            data_file += "VG1MAG_1HR_1977_1989.TAB.txt"
            with open(data_file) as location:
                for line in location:
                    items = line.split()
                    if items[1] == str(voyager_date.year)[-2:] and int(items[2]) == int(day_of_year):
                        exp_string = (' ').join([items[4], items[4], items[5], items[6], items[7], items[8], items[9], items[10], items[11]])
                        break
        else:
            data_file += "VG1MAG_1HR_1990_2004.TAB.txt"
            with open(data_file) as location:
                for line in location:
                    items = line.split()
                    date_items = items[1].split('.')
                    year = int(date_items[0])
                    comp_year = int(voyager_date.year) - 1900
                    if comp_year > 100:
                        comp_year -= 100
                    dec = float("." + date_items[1])
                    if year == comp_year and round(365 * dec) == day_of_year:
                        exp_string = (' ').join([items[2], items[3], items[3], items[5]])
                        break

    for item in night_sky[body_count]:
        cx = randrange(0, 1200)
        cy = randrange(0, 600)
        if "Moon" not in item[0]:
            if "Jupiter" in item[0]:
                radius = 3
            else:
                radius = 2
            svg += '<circle cx="' + str(cx) + '" cy="' + str(cy) + '" r="' + str(radius) + '" fill-opacity="' + '1' + '" fill="#ffffff" />'
        else:
            radius = randrange(40, 90)
            moon_colors = ["#F0F8FF", "#F0FFFF", "#E0EEEE", "#F5F5DC", "#F8F8FF"]
            color_dim = randrange(0, len(moon_colors))
            svg += '<circle cx="' + str(cx) + '" cy="' + str(cy) + '" r="' + str(radius) + '" fill="' + moon_colors[color_dim] + '" stroke="#f3f3f3" stroke-width="1" />'

    voyager_signal_cy = randrange(0, vert_size)
    start_y = vert_size / wave_count + randrange(10, 400)

    if (voyager_signal_cy + 40 > start_y):
        svg += voyager_signal(voyager_signal_cy, hor_size, voyager_date.year, voyager_date.month, voyager_date.day, bodies[body_count])

    count = 0
    last_start_y = 0
    prev_color = ""
    stroke = "#747373"
    while count < wave_count:
        path_color = get_random_color(palette[body_count], prev_color, base_path_color)
        prev_color = path_color
        if last_start_y == 0:
            pen_y = start_y
            last_start_y = start_y
        else:
            pen_y = last_start_y + randrange(10, 200)
            last_start_y = pen_y

        stroke_width = str(randrange(0, 5))
        svg += '<path stroke="' + stroke + '" stroke-width="' + stroke_width + '" fill="' + path_color + '" d="M 0 ' + str(pen_y) + ' c '

        curve_counter = 0
        while curve_counter < curve_count:        
            svg += get_curve()
            curve_counter += 1

        svg += 'l -40 ' + str(hor_size) + ' H 0 Z" />'
        count += 1

    if (voyager_signal_cy + 40 < start_y):
        svg += voyager_signal(voyager_signal_cy, hor_size, voyager_date.year, voyager_date.month, voyager_date.day, bodies[body_count])

    border_color, text_color = get_border_color(voyager_date)

    svg += '<rect x="0" y="0" width="' + str(hor_size) + '" height="' + str(vert_size) + '" style="stroke:' + border_color + '; fill: none;stroke-width:80px"/>'
    svg += triptych(hor_size, vert_size, voyager_date)
    svg += '<rect x="0" y="0" width="' + str(hor_size) + '" height="' + str(vert_size) + '" style="stroke: #000000; fill: none;stroke-width:1px"/>'
    svg_location, voyager_location = label(hor_size, vert_size, voyager_date)
    svg += svg_location
    svg_exp = top_label(hor_size, vert_size, exp_string, voyager_date)
    svg += svg_exp
    svg += '</svg>'

    with open("svg_out/" + str(svg_name) + ".svg", "w") as svg_file:
        svg_file.write(svg)

    data_name = str(svg_name) + ".json"
    ipfs_url = "ipfs://[[IPS_URL]]/" + str(svg_name) + ".svg"
    nft_json = {
        "name" : voyager_craft + ": " + ('-').join([str(voyager_date.year), str(voyager_date.month), str(voyager_date.day)]),
        "description" : description,
        "image" : ipfs_url,
        "attributes" : [
            {
                "trait_type" : "celestial_body",
                "value" : bodies[body_count]
            },
            {
                "trait_type" : "craft",
                "value" : voyager_craft
            },
            {
                "trait_type" : "voyager_date",
                "value" : str(voyager_date)
            },
            {
                "trait_type" : "day",
                "value" : str(svg_name)
            },
            {
                "trait_type" : "location",
                "value" : voyager_location
            },
        ]
    }

    with open("meta_out/" + data_name, "w") as data_file:
        json.dump(nft_json, data_file, indent = 4)

    return True

def get_border_color(voyager_date):
    border_color = "#fcfceb"
    text_color = "#999999"

    # specific date
    if voyager_date == datetime.datetime(1986, 1, 28): # Challenger
        border_color = "#1f1f1f"
        text_color = "#ffffff"
    elif voyager_date == datetime.datetime(2003, 2, 1):  # Columbia
        border_color = "#1f1f1f"
        text_color = "#ffffff"
    elif voyager_date == datetime.datetime(2001, 9, 11):  # 9/11
        border_color = "#052b73"
        text_color = "#ffffff"
    elif voyager_date == datetime.datetime(1983, 6, 18):  # Sally Ride
        border_color = "#ffe0e0"

    # annual
    if voyager_date.month == 10 and voyager_date.day == 31: # Halloween
        border_color = "#d4a048"
        text_color = "#ffffff"
    elif voyager_date.month == 1 and voyager_date.day == 16:  # MLK
        border_color = "#545454"
        text_color = "#ffffff"
    elif voyager_date.month == 4 and voyager_date.day == 22:  # Earth day
        border_color = "#9cba9e"

    return border_color, text_color

def get_random_date():
    start_date = datetime.date(1977, 9, 5)
    end_date = datetime.date(2005, 1, 24) #datetime.date.today()

    delta = end_date - start_date
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start_date + datetime.timedelta(seconds=random_second)

def label(hor, vert, date_val):
    x = 40
    y = vert - 13
    day_of_year = str(date_val.toordinal() - datetime.date(date_val.year, 1, 1).toordinal() + 1) + ".00"
    locate_data_file = "data/" + "VG1TRAJ_1DAY_1977_2005.TAB.txt"

    location_string = ""
    with open(locate_data_file) as location:
        for line in location:
            items = line.split()
            if items[0] == str(date_val.year) and items[1] == day_of_year:
                location_string = (' ').join([items[3], items[4], items[5], items[6], items[7]])
                break

    date_string = "VOYAGER 1: " + ('-').join([str(date_val.year), str(date_val.month), str(date_val.day)]) + " LOCATION: " + location_string

    border_color, text_color = get_border_color(date_val)

    svg = '<style>.label { font: 20px monospace; fill: ' + text_color + '; }</style>'
    svg += '<g id="label"><text x="' + str(x) + '" y="' + str(y) + '" class="label" >' + date_string + '</text></g>'
    return svg, location_string

def top_label(hor, vert, exp_string, date_val):
    svg = ""
    year = int(date_val.year)
    if len(exp_string) > 0:
        x = 40
        y = 27

        exp_string = "SOLAR WIND: " + exp_string
        if len(exp_string) < 80:
            exp_string += " TRIAXIAL FLUXGATE MAGNETOMETER"
        else:
            exp_string += " MAGNETOMETER"

        if int(year) > 1989:
            exp_string += " - MISSION PHASE: CRUISE"

        border_color, text_color = get_border_color(date_val)
        
        svg = '<style>.top_label { font: 16px monospace; fill: ' + text_color + '; }</style>'
        svg += '<g id="top_label"><text x="' + str(x) + '" y="' + str(y) + '" class="top_label" >' + exp_string + '</text></g>'
    return svg

def triptych(hor, vert, date_val):
    count = 0
    proportion = randrange(3, 5)
    start_x = hor / proportion
    svg = '<g id="triptych">'
    while count < 2:
        if count == 1:
            x = str(hor - start_x)
        else:
            x = str(start_x * ((count + 1)))

        border_color, text_color = get_border_color(date_val)

        svg += '<line x1="' + x + '" y1="0" x2="' + x + '" y2="' + str(vert) + '" style="stroke:' + border_color + ';stroke-width:10px;" />'
        count += 1
    svg += '</g>'
    return svg

def voyager_signal(cy, hor_size, year, month, day, planet):
    stroke_width = 1
    radius_start = 2000
    radius_increment = randrange(15, 30)
    current_radius = radius_start
    cx = randrange(0, hor_size)
    dash_array1 = 0
    dash_array2 = 0
    if year > 1991:
        dash_array1 = (year - 1990) * 1.5
        dash_array2 = (year - 1990) * 1.5
    opacity = randrange(85, 100)
    voyager_color = "#ffffff"

    signal_color = "#ffffff"
    if (year == 1977 and planet == "Earth") or (year == 1977 and planet == "Moon"):
        signal_color = "#feffe6"
        stroke_width = 3
    elif (year == 1979 and planet == "Jupiter"):
        signal_color = "#feffe6"
        stroke_width = 3
    elif (year == 1980 and planet == "Saturn"):
        signal_color = "#feffe6"
        stroke_width = 3
    elif (year == 1986 and planet == "Uranus"):
        signal_color = "#feffe6"
        stroke_width = 3
    elif (year == 1989 and planet == "Neptune"):
        signal_color = "#feffe6"
        stroke_width = 3

    svg = ''
    fill = "none"
    pride_colors = ["#FF0018", "#FFA52C", "#FFFF41", "#008018", "#0000F9", "#86007D"]
    solar_colors = ["#f7cf05", "#f7cf05", "#FFA52C", "#FFA52C", "#fcc308", "#fcf008"]
    use_pride = False
    solar_storm = False

    if month == 6 and 1 == randrange(0, 10):
        use_pride = True

    if (int(year) == 1989 and int(day) > 8 and int(month) == 3) and (int(year) == 1989 and int(day) < 14 and int(month) == 3):
        solar_storm = True
    elif (int(year) == 1991 and int(day) > 7 and int(month) == 11) and (int(year) == 1991 and int(day) < 11 and int(month) == 11):
        solar_storm = True
    elif (int(year) == 2000 and int(day) > 13 and int(month) == 7) and (int(year) == 2000 and int(day) < 17 and int(month) == 7):
        solar_storm = True
    elif (int(year) == 2001 and int(day) > 4 and int(month) == 11) and (int(year) == 2001 and int(day) < 7 and int(month) == 11):
        solar_storm = True
    elif (int(year) == 2003 and int(day) > 18 and int(month) == 10) and (int(year) == 2003 and int(day) < 9 and int(month) == 11):
        solar_storm = True

    color_count = 0
    anim_count = 0
    while current_radius >= radius_increment:
        if use_pride:
            fill = pride_colors[color_count]
            color_count += 1
            opacity = color_count * 3.5
            if color_count == len(pride_colors):
                color_count = 0
        elif solar_storm:
            fill = solar_colors[color_count]
            color_count += 1
            if cy > 400:
                opacity = color_count * 1.5
            else:
                opacity = color_count * 3.5

            if color_count == len(solar_colors):
                color_count = 0

        svg += '<circle cx="' + str(cx) + '" cy="' + str(cy) + '" r="' + str(current_radius) + '" stroke-width="' + str(stroke_width) + '" stroke-dasharray="' + str(dash_array1) + 'px ' + str(dash_array2) +  'px" fill="' + fill + '" stroke="' + signal_color + '" stroke-opacity="100%" opacity="' + str(opacity) + '%">'
        if (anim_count == 10 and 1 == randrange(0, 3)):
            svg += '<animate attributeType="SVG" attributeName="r" begin="0s" dur="2.5s" repeatCount="indefinite" from="5%" to="90%"/>'
            svg += '<animate attributeType="CSS" attributeName="stroke-width" begin="0s"  dur="1.5s" repeatCount="indefinite" from=".5%" to="0%" />'
            svg += '<animate attributeType="CSS" attributeName="opacity" begin="0s"  dur="1.5s" repeatCount="indefinite" from="1" to="0"/>'
        
        anim_count += 1
        svg += '</circle>'
        current_radius -= radius_increment

    svg += '<style>.voyager { font: 20px monospace; fill: ' + voyager_color + '; }</style>'
    svg += '<text x="' + str(cx - 5.5) + '" y="' + str(cy + 5.5) + '" class="voyager" >+</text>'

    return svg

def get_curve():
    x1 = str(randrange(60, 80))
    x2 = str(randrange(120, 150))
    y1 = str(randrange(-20, 20))
    y2 = str(randrange(-20, 20))
    x = str(randrange(220, 260))
    y = str(randrange(-20, 10))

    return x1 + ' ' + y1 + ' ' + x2 + ' ' + y2 + ' ' + x + ' ' + y + ' '

def get_random_color(palette_planet, prev_color, base_path_color):
    color = prev_color
    while True:
        color = palette_planet[randrange(1, len(palette_planet))]
        if color not in prev_color and color not in base_path_color:
            return color
    return color

def clamp(val, minimum=0, maximum=255):
    if val < minimum:
        return minimum
    if val > maximum:
        return maximum
    return val

def colorscale(hexstr, scalefactor):
    """
    Scales a hex string by ``scalefactor``. Returns scaled hex string.

    To darken the color, use a float value between 0 and 1.
    To brighten the color, use a float value greater than 1.

    >>> colorscale("#DF3C3C", .5)
    #6F1E1E
    >>> colorscale("#52D24F", 1.6)
    #83FF7E
    >>> colorscale("#4F75D2", 1)
    #4F75D2
    """

    hexstr = hexstr.strip('#')

    if scalefactor < 0 or len(hexstr) != 6:
        return hexstr

    r, g, b = int(hexstr[:2], 16), int(hexstr[2:4], 16), int(hexstr[4:], 16)

    r = clamp(r * scalefactor)
    g = clamp(g * scalefactor)
    b = clamp(b * scalefactor)

    return "#%02x%02x%02x" % (r, g, b)

if __name__ == "__main__":
    main()