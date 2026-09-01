import os


class LyricsFormatError(ValueError):
    """Raised when a lyric file does not follow the supported TXT format."""

def read_lyrics(filename):

    if not filename:
        raise LyricsFormatError("请选择歌词文件")

    if not os.path.isfile(filename):
        raise LyricsFormatError("歌词文件不存在")

    if os.path.splitext(filename)[1].lower() != ".txt":
        raise LyricsFormatError("歌词文件必须是 TXT 格式")

    try:
        with open(filename, "r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
    except UnicodeDecodeError as exc:
        raise LyricsFormatError("歌词文件必须使用 UTF-8 编码") from exc

    if len(lines) < 4:
        raise LyricsFormatError("歌词文件至少需要中英文标题和一组中英文歌词")

    if not lines[0].startswith("#") or not lines[1].startswith("#"):
        raise LyricsFormatError("歌词文件前两行必须是以 # 开头的中英文标题")

    title_cn = lines[0][1:].strip()
    title_en = lines[1][1:].strip()

    if not title_cn or not title_en:
        raise LyricsFormatError("中英文标题不能为空")

    lyric_lines = lines[2:]

    if any(line.startswith("#") for line in lyric_lines):
        raise LyricsFormatError("歌词文件只能包含两个以 # 开头的标题")

    if len(lyric_lines) % 2 != 0:
        raise LyricsFormatError("中英文歌词没有完整配对，请检查最后一行")

    slides = [
        {
            "chinese": lyric_lines[index],
            "english": lyric_lines[index + 1]
        }
        for index in range(0, len(lyric_lines), 2)
    ]

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

    # Windows 不允许文件名以空格或句点结尾
    name = name.strip().rstrip(".")

    return name


def get_default_filename(lyrics):

    return get_output_filename(lyrics)


def get_output_filename(lyrics, requested_title=""):

    if requested_title:
        filename = requested_title.strip()

        if filename.lower().endswith(".pptx"):
            filename = filename[:-5]
    else:
        title_cn = lyrics.get("title_cn", "")
        source_filename = lyrics.get("filename", "")
        filename = title_cn or os.path.splitext(source_filename)[0] or "Untitled Song"

    filename = clean_filename(filename)

    if not filename:
        raise ValueError("PPT 名称不能只包含文件名非法字符")

    return filename + ".pptx"
