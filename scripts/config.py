#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import configparser
import os

CONFIG_FNAME = "config.ini"
CONFIG_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)),
                           "..")

def argparser():
    """Argument parser to obtain config updates from the commandline."""
    default_config = generate_default_config()

    description = "Update the default values in the configuration file."
    description += " Allowed sections and options are:\n"
    for section in default_config.sections():
        description += f"  {section}\n"
        for option in default_config.options(section):
            description += f"    {option}\n"
    parser = argparse.ArgumentParser(
        description=description,
        formatter_class=argparse.RawTextHelpFormatter)
    
    section = "Config section, e.g., 'global'"
    parser.add_argument("section", metavar="section", type=str,
                        help=section)
    option = "Config option, e.g., 'author'"
    parser.add_argument("option", metavar="option", type=str,
                        help=option) 
    value = "Config value, e.g., 'Jane Doe'"
    parser.add_argument("value", metavar="value", type=str, help=value)         

    return parser.parse_args()

def cmdline_config():
    args = argparser()
    update_config(args.section, args.option, args.value)

def generate_default_config():
    """Generate a default config parser."""
    config = configparser.ConfigParser()
    
    config["global"] = {"author": "Jane Doe"}
    config["python"] = {"license": "BSD-3-Clause"}
    config["latex"] = {"title": "Document"}

    return config 

def update_config(section, option, value):
    """Update an already existing config file."""
    if not os.path.isfile(os.path.join(CONFIG_PATH, CONFIG_FNAME)):
        generate_default_config()
    
    config = configparser.ConfigParser()
    if os.path.isfile(os.path.join(CONFIG_PATH, CONFIG_FNAME)):
        with open(os.path.join(CONFIG_PATH, CONFIG_FNAME), "r") as f:
            config.read_file(f)
    else:
        config = generate_default_config()

    if not config.has_section(section):
        raise TypeError(f"Invalid section: {section}")
    if not config.has_option(section, option):
        raise TypeError(f"Invalid option: {option}")
    config.set(section, option, value)

    with open(os.path.join(CONFIG_PATH, CONFIG_FNAME), "w") as f:
        config.write(f)

