from colorthief import analyse_image


def test_analyse_image_not_fancy(capsys):
    imgpath = 'images/sunset.jpg'
    analyse_image(imgpath, do_print_fancy=False)
    expected_stdout = """(163, 143, 178)
(9, 6, 5)
(97, 35, 31)
(246, 222, 171)
(148, 81, 64)
"""
    captured = capsys.readouterr()
    assert captured.out == expected_stdout
