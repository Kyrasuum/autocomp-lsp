"""LSP Client Test"""
import sys
from client import session
from client.utils import as_uri


def test_content_completion(content_path, line, col, contents=''):
    """Tests using content completion"""
    with session.LspSession() as ls_session:
        uri = as_uri(content_path)
        ls_session.initialize()

        if contents != '':
            ls_session.notify_did_open(
                {
                    "textDocument": {
                        "uri": uri,
                        "languageId": "python",
                        "version": 1,
                        "text": contents,
                    }
                }
            )

        actual = ls_session.text_document_completion(
            {
                "textDocument": {"uri": uri},
                "text": contents,
                "position": {"line": line, "character": col},
                "context": {"triggerKind": 1},
            }
        )
        print(actual)


if len(sys.argv) == 2:
    test_content_completion(sys.argv[1], 8, 2)
    sys.exit()
elif len(sys.argv) == 4:
    test_content_completion(sys.argv[1], sys.argv[2], sys.argv[3])
    sys.exit()
elif len(sys.argv) == 5:
    test_content_completion(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4])
    sys.exit()
raise ValueError
