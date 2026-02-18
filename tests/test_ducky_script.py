import pathlib


def test_ducky_script_contains_commands():
    script_path = pathlib.Path(__file__).resolve().parents[1] / "PentestGPT.txt"
    text = script_path.read_text(encoding='utf-8')
    assert "GUI" in text, "Missing GUI command"
    assert "STRING" in text, "Missing STRING command"
    assert "ENTER" in text, "Missing ENTER command"

