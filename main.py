from ui import run
from ppt_creator import create_presentation


def generate(lyric, output, title):

    output_file = f"{output}/{title}.pptx"

    create_presentation(
        lyric,
        output_file
    )


run(generate)