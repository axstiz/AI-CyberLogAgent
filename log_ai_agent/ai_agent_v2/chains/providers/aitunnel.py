"""AITUNNEL LLM provider — OpenAI-совместимый API для доступа к нейросетям."""

import logging
from typing import Any

from langchain_openai import ChatOpenAI

logger = logging.getLogger(__name__)


def create_aitunnel_llm(
    model: str | None = None,
    base_url: str | None = None,
    api_key: str | None = None,
    temperature: float | None = None,
    max_tokens: int | None = None,
    timeout: int | None = None,
    **kwargs: Any,
) -> ChatOpenAI:
    from ...config import AgentConfig

    cfg = AgentConfig.from_env()

    model = model or cfg.aitunnel_model
    base_url = base_url or cfg.aitunnel_base_url
    api_key = api_key or cfg.aitunnel_api_key
    temperature = cfg.temperature if temperature is None else temperature
    max_tokens = cfg.max_tokens if max_tokens is None else max_tokens
    timeout = cfg.timeout if timeout is None else timeout
    timeout = timeout if timeout else None

    if not api_key:
        raise ValueError(
            "AITUNNEL_API_KEY is not set. "
            "Set it in .env or pass api_key parameter."
        )

    logger.info(
        "Creating AITUNNEL LLM: model=%s, base_url=%s, temp=%s, timeout=%ss",
        model,
        base_url,
        temperature,
        timeout,
    )

    llm = ChatOpenAI(
        model=model,
        base_url=base_url,
        api_key=api_key,
        temperature=temperature,
        max_tokens=max_tokens,
        timeout=timeout,
        **kwargs,
    )

    logger.info("\u2713 AITUNNEL LLM created: %s @ %s", model, base_url)
    return llm
