from typing import Optional
from pydantic import BaseModel


class AgentDecision(BaseModel):

    should_send: bool

    channel: Optional[str] = None

    send_time: Optional[str] = None

    subject: Optional[str] = None

    message: Optional[str] = None

    cta: Optional[str] = None

    next_action: Optional[str] = None

    rationale: str