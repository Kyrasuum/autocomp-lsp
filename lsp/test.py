"""LSP Client Test"""
import client
from client import session
from client.utils import as_uri


def test_content_completion():
    """Tests using content completion"""
    content_path = client.TEST_ROOT / ".." / "test_data.py"
    with open(content_path, "r") as text_file:
        contents = text_file.read()

    with session.LspSession() as ls_session:
        uri = as_uri(content_path)
        ls_session.initialize()

        actual = ls_session.text_document_completion(
            {
                "textDocument": {"uri": uri},
                "text": contents,
                "position": {"line": 8, "character": 2},
                "context": {"triggerKind": 1},
            }
        )
        print(actual)
