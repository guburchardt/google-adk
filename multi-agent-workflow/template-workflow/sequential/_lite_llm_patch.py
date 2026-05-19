from pydantic import field_serializer
from google.adk.models.lite_llm import LiteLlm as _LiteLlm, LiteLLMClient


class LiteLlm(_LiteLlm):
    @field_serializer("llm_client", when_used="always")
    def _drop_llm_client(self, v: LiteLLMClient, _info):
        return None
