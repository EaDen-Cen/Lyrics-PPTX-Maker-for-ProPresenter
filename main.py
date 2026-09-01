import os

from ppt_creator import create_presentation
from parser import get_output_filename, read_lyrics


def generate(lyric, output, title, overwrite=False):

    if not os.path.isdir(output):
        raise ValueError("输出目录不存在")

    if not os.access(output, os.W_OK):
        raise PermissionError("输出目录不可写")

    lyrics = read_lyrics(lyric)
    output_filename = get_output_filename(lyrics, title)
    output_file = os.path.join(output, output_filename)

    if os.path.exists(output_file) and not overwrite:
        raise FileExistsError(output_file)

    create_presentation(
        lyrics,
        output_file
    )

    return output_file

if __name__ == "__main__":
    from ui import run

    run(generate)
