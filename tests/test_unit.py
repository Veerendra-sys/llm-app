from unittest.mock import MagicMock, patch

from app.llm_service import generate_response


def _fake(text):
    fake = MagicMock()
    fake.message.content = text
    return fake


def test_returns_model_text():
    with patch("app.llm_service.chat", return_value=_fake("Hello!")):
        assert generate_response("hi") == "Hello!"


def test_prompt_is_sent_to_model():
    with patch("app.llm_service.chat", return_value=_fake("x")) as mock_chat:
        generate_response("my prompt")
    sent = mock_chat.call_args.kwargs["messages"][0]["content"]
    assert sent == "my prompt"
