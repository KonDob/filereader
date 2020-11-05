import pytest
from main.main_script.outputlines import print_paths_parts


def test_check_output_last_line(capsys):
    print_paths_parts('test_file.txt', 1)
    captured = capsys.readouterr()
    assert captured.out == "end\n\n"


def test_check_return_data():
    assert print_paths_parts('test_file.txt', 2) == None


def test_empty_call():
    with pytest.raises(TypeError):
        print_paths_parts()


def test_call_only_filename():
    with pytest.raises(TypeError):
        print_paths_parts('some.txt')


def test_call_only_number():
    with pytest.raises(TypeError):
        print_paths_parts(2)


def test_file_not_found():
    with pytest.raises(FileNotFoundError):
        print_paths_parts('none.txt', 2)
