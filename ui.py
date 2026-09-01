import sys

from config import SETTINGS, set_setting

from PySide6.QtWidgets import (
    QApplication,
    QWidget,
    QLabel,
    QLineEdit,
    QPushButton,
    QFileDialog,
    QMessageBox,
    QVBoxLayout,
    QHBoxLayout,
)


def run(create_callback=None):
    app = QApplication(sys.argv)

    window = QWidget()
    window.setWindowTitle("LyricsMaker")
    window.resize(720, 360)

    # ======================
    # 歌词文件
    # ======================

    lyric_label = QLabel("歌词文件")

    lyric_edit = QLineEdit()
    lyric_edit.setText(SETTINGS["input_file"])
    lyric_edit.setReadOnly(True)

    lyric_button = QPushButton("浏览")

    lyric_layout = QHBoxLayout()
    lyric_layout.addWidget(lyric_edit)
    lyric_layout.addWidget(lyric_button)

    # ======================
    # 输出目录
    # ======================

    output_label = QLabel("输出目录")

    output_edit = QLineEdit()
    output_edit.setText(SETTINGS["output_folder"])
    output_edit.setReadOnly(True)

    output_button = QPushButton("浏览")

    output_layout = QHBoxLayout()
    output_layout.addWidget(output_edit)
    output_layout.addWidget(output_button)

    # ======================
    # PPT名称
    # ======================

    ppt_label = QLabel("PPT名称")

    ppt_edit = QLineEdit()
    ppt_edit.setPlaceholderText("留空则使用歌词文件中的中文歌名")

    # ======================
    # 开始生成
    # ======================

    generate_button = QPushButton("开始生成 PPT")
    generate_button.setFixedHeight(45)

    # ======================
    # 总布局
    # ======================

    layout = QVBoxLayout(window)

    layout.setSpacing(15)
    layout.setContentsMargins(25, 25, 25, 25)

    layout.addWidget(lyric_label)
    layout.addLayout(lyric_layout)

    layout.addWidget(output_label)
    layout.addLayout(output_layout)

    layout.addWidget(ppt_label)
    layout.addWidget(ppt_edit)

    layout.addStretch()

    layout.addWidget(generate_button)

    # ======================
    # 浏览歌词
    # ======================

    def browse_lyric():
        filename, _ = QFileDialog.getOpenFileName(
            window,
            "选择歌词文件",
            "",
            "Text Files (*.txt);;All Files (*)",
        )

        if filename:
            lyric_edit.setText(filename)
            set_setting("input_file", filename)

    lyric_button.clicked.connect(browse_lyric)

    # ======================
    # 浏览输出目录
    # ======================

    def browse_output():
        folder = QFileDialog.getExistingDirectory(
            window,
            "选择输出目录"
        )

        if folder:
            output_edit.setText(folder)
            set_setting("output_folder", folder)

    output_button.clicked.connect(browse_output)

    # ======================
    # 点击生成
    # ======================

    def generate():

        lyric = lyric_edit.text().strip()
        output = output_edit.text().strip()
        title = ppt_edit.text().strip()

        if not lyric:
            QMessageBox.warning(window, "提示", "请选择歌词文件")
            return

        if not output:
            QMessageBox.warning(window, "提示", "请选择导出路径")
            return

        try:

            if not create_callback:
                raise RuntimeError("未配置 PPT 生成器")

            output_file = create_callback(
                lyric,
                output,
                title
            )

            QMessageBox.information(
                window,
                "完成",
                f"PPT 已生成！(∠・ω< )⌒★\n\n{output_file}"
            )

        except FileExistsError as e:

            answer = QMessageBox.question(
                window,
                "文件已存在",
                f"以下文件已经存在：\n{e.args[0]}\n\n是否覆盖？",
                QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                QMessageBox.StandardButton.No
            )

            if answer == QMessageBox.StandardButton.Yes and create_callback:
                try:
                    output_file = create_callback(
                        lyric,
                        output,
                        title,
                        True
                    )
                    QMessageBox.information(
                        window,
                        "完成",
                        f"PPT 已覆盖保存！(∠・ω< )⌒★\n\n{output_file}"
                    )
                except Exception as overwrite_error:
                    QMessageBox.critical(
                        window,
                        "导出失败",
                        str(overwrite_error)
                    )

        except Exception as e:

            QMessageBox.critical(
                window,
                "导出失败",
                str(e)
            )

    generate_button.clicked.connect(generate)

    # ======================
    # 样式
    # ======================

    window.setStyleSheet("""
        QWidget{
            background:#2b2b2b;
            color:white;
            font-size:14px;
        }

        QLabel{
            font-weight:bold;
        }

        QLineEdit{
            background:white;
            color:black;
            border:1px solid #666;
            border-radius:5px;
            padding:6px;
        }

        QPushButton{
            background:#4CAF50;
            color:white;
            border:none;
            border-radius:6px;
            padding:8px;
        }

        QPushButton:hover{
            background:#5cb85c;
        }

        QPushButton:pressed{
            background:#3d8b40;
        }
    """)

    window.show()

    app.exec()
