from pydantic import BaseModel

class UserContext(BaseModel):
    name: str
    is_premium: bool
    issue_type: str = "general"


