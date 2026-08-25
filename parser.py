import os

def read_lyrics(filename):

    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    title_cn = ""
    title_en = ""

    slides = []

    temp = []

    title_count = 0

    for line in lines:

        line = line.strip()

        if not line:
            continue

        # =================
        # 标题
        # =================

        if line.startswith("#"):

            title_count += 1

            if title_count == 1:
                title_cn = line[1:].strip()

            elif title_count == 2:
                title_en = line[1:].strip()

            continue

        # =================
        # 中英歌词
        # =================

        temp.append(line)

        if len(temp) == 2:

            slides.append({
                "chinese": temp[0],
                "english": temp[1]
            })

            temp = []

    return {
        "title_cn": title_cn,
        "title_en": title_en,
        "filename": os.path.basename(filename),
        "slides": slides
    }


def clean_filename(name):

    # Windows/macOS 不允许的字符
    invalid_chars = '<>:"/\\|?*'

    for c in invalid_chars:
        name = name.replace(c, "")

    # 防止文件名太长
    name = name.strip()

    return name


def get_default_filename(lyrics):

    title_cn = lyrics["title_cn"]
    filename = lyrics["filename"]

    if title_cn:
        filename = title_cn

    elif filename:
        filename = filename

    else:
        filename = "Untitled Song"

    filename = clean_filename(filename)

    return filename + ".pptx"