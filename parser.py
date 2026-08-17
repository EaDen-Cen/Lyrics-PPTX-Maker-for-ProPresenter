def read_lyrics(filename):

    with open(filename,"r",encoding="utf-8") as f:
        lines=f.readlines()


    title_cn=""
    title_en=""

    groups=[]

    current_group=None

    temp=[]


    title_count=0


    for line in lines:

        line=line.strip()


        if not line:
            continue


        # =================
        # 标题
        # =================

        if line.startswith("#"):

            title_count += 1

            if title_count == 1:
                title_cn=line[1:].strip()

            elif title_count == 2:
                title_en=line[1:].strip()

            continue



        # =================
        # Group
        # =================

        if line.startswith("[") and line.endswith("]"):

            current_group={
                "name":line[1:-1],
                "slides":[]
            }

            groups.append(current_group)

            continue



        # =================
        # 中英歌词
        # =================

        temp.append(line)


        if len(temp)==2:

            if len(temp) == 2:

                if current_group is None:
                    current_group = {
                        "name": "Default",
                        "slides": []
                    }

                    groups.append(current_group)

                current_group["slides"].append({

                    "chinese": temp[0],
                    "english": temp[1]

                })

                temp = []



    return {

        "title_cn":title_cn,

        "title_en":title_en,

        "groups":groups

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

    if title_cn:
        filename = title_cn

    else:
        filename = "Untitled Song"

    filename = clean_filename(filename)

    return filename + ".pptx"