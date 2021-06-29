"""LSP Client Translator"""
import client
from client import session
from client.utils import as_uri


def content_completion(fpath, content, line, col):
    """Takes content and filepath to get LSP results"""
    content_path = client.TEST_ROOT / "../.." / fpath

    with session.LspSession() as ls_session:
        uri = as_uri(content_path)
        ls_session.initialize()

        actual = ls_session.text_document_completion(
            {
                "textDocument": {"uri": uri},
                "text": content,
                "position": {"line": line, "character": col},
                "context": {"triggerKind": 1},
            }
        )
        return actual
