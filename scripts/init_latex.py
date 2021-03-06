#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os


def main():
    """Generate a LaTeX file."""
    init_latex()

def init_latex():
    """Generate a LaTeX file."""
    args = argparser()
    
    main_fname = "main.tex"
    preamble_fname = "preamble.tex"
    bib_fname = "bibliography.bib"
    cwd = os.getcwd()

    if not args.current_dir:
        if os.path.isdir(args.dirname):
            msg = f"Directory '{args.dirname}' already exists!"
            raise IsADirectoryError(msg)
    else:
        if (os.path.isfile(main_fname)
                or os.path.isfile(preamble_fname)):
            msg = (f"'{main_fname}' and/or {preamble_fname} already "
                   + "exists!")
            raise FileExistsError(msg)
        if args.bib and os.path.isfile(bib_fname):
            msg = f"'{bib_fname}' already exists!"
            raise FileExistsError(msg)

    if not args.current_dir:
        os.mkdir(args.dirname)
        os.chdir(args.dirname)

    with open(main_fname, "w") as f:
        lines = main_file(args)
        for line in lines:
            f.write(line + "\n")

    with open(preamble_fname, "w") as f:
        lines = preamble_file(args)
        for line in lines:
            f.write(line + "\n")

    if args.bib:
        with open(bib_fname, "w"):
            pass

def argparser():
    """Argument parser."""
    description = "Initialise the main files needed in a LaTeX article."
    parser = argparse.ArgumentParser(description=description)
    
    group = parser.add_mutually_exclusive_group(required=True)
    dirname = ("Name of the directory in which the LaTeX files will be"
               + " generated into.")
    group.add_argument("dirname", metavar="directory name", type=str,
                       nargs='?', help=dirname)
    current_dir = ("If this flag is set, the files are generated into "
                   + "the current working directory.")
    group.add_argument("--current_dir", action="store_true",
                       help=current_dir)
    
    # Document-specific stuff.
    author = "Author of the LaTeX article."
    parser.add_argument("--author", type=str, default="Max Schalz",
                        help=author)
    title = "Title of the LaTeX article."
    parser.add_argument("--title", type=str, default="Document",
                        help=title)
    bib = "If this flag is set, a biblatex bibliography is added."
    parser.add_argument("--bib", action="store_true", help=bib)

    no_toc = "If this flag is set, do not include a table of contents."
    parser.add_argument("--no_toc", action="store_true", help=no_toc)

    return parser.parse_args()

def main_file(args):
    """Generate main.tex"""
    document = []
    document.append(r"\documentclass[a4paper]{article}")
    document.append("")
    document.append(r"\input{preamble}")
    document.append("")
    document.append(r"\title{" + f"{args.title}" + r"}")
    document.append(r"\author{" + f"{args.author}" + r"}")
    document.append(r"\date{\today}")
    document.append("")
    document.append(r"\begin{document}")
    document.append("")
    document.append(r"  \maketitle")
    if not args.no_toc:
        document.append(r"  \tableofcontents")
    document.append("")
    if args.bib:
        document.append(r"  \appendix")
        document.append(r"  \input{appendix}")
        document.append(r"  \printbibliography[heading=bibintoc]")
        document.append("")
    document.append(r"\end{document}")
    
    return document

def preamble_file(args):
    document = []

    document.append(r"\usepackage[utf8]{inputenc}")
    document.append(r"\usepackage[british]{babel}")
    document.append("")
    if args.bib:
        document.append(r"\usepackage{biblatex}")
        document.append(r"\addbibresource{bibliography.bib}")
        document.append("")
    document.append(r"\usepackage[dvipsnames]{xcolor}")
    document.append(r"\newcommand{\red}[1]{{\color{red}#1}}")
    document.append(r"\newcommand{\todo}[1]{\red{\textbf{#1}}}")
    document.append("")
    document.append(r"\usepackage[colorlinks=true]{hyperref}")
    document.append(r"\usepackage[nameinlink,capitalize]{cleveref}")
    document.append("")

    return document

if __name__=="__main__":
    main()
