from unittest.mock import MagicMock, patch

from app.llm_service import generate_response, generate_json
#"I use patch and MagicMock to mock the LLM API call. This allows me to test my application logic without making an actual LLM/API request."

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


def test_generate_json_parses_output():
    with patch("app.llm_service.chat", return_value=_fake('{"sentiment": "positive"}')):
        assert generate_json("x") == {"sentiment": "positive"}
