import pytest
from main_script.outputlines import print_paths_parts


def test_output_last_line(help_method, capsys):
    print_paths_parts('test_file.txt', 1)
    captured = capsys.readouterr()
    assert captured.out == "end\n\n"


def test_big_input_amount(capsys):
    print_paths_parts('test_file.txt', 90)
    captured = capsys.readouterr()
    assert "Sorry, amount of number is bigger than amount of lines." \
        in captured.out


def test_return_none():
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


def test_file_not_found(capsys):
    print_paths_parts('not_existing_path_to_file.txt', 1)
    captured = capsys.readouterr()
    assert 'Sorry - path to file doesn`t exist.Please provide another path' \
        in captured.out
