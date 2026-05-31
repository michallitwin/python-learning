from datetime import datetime, UTC
from functools import partial
from typing import Literal, Annotated
from uuid import UUID, uuid4
from pydantic import (
    BaseModel,
    ValidationError, 
    Field, 
    HttpUrl, 
    SecretStr, 
    EmailStr, 
    field_validator, 
    model_validator, 
    ValidationInfo,
    computed_field,

    )



class User(BaseModel):
    uid: UUID = Field(default_factory=uuid4)
    username: Annotated[str, Field(min_length=3, max_length=20)]
    email: EmailStr
    password: SecretStr
    website: HttpUrl | None = None
    bio: str = ""
    is_active: bool = True
    verified_at: datetime | None = None

    first_name: str =""
    last_name: str = ""
    follower_count: int = 0

    @field_validator("username")
    @classmethod
    def validate_username(cls, v: str) ->str:
        if not v.replace("_","").isalnum():
            raise ValueError("Username must be alphanumeric (underscores allowed)")
        return v.lower()
    
    @field_validator('website', mode = "before")
    @classmethod
    def add_https(cls, v: str | None) -> str | None:
        if v and not v.startswith(('http://', 'https://')):
            return f'https://{v}'
        return v

    @computed_field
    @property
    def display_name(self) -> str:
        if self.first_name and self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username
    
    @computed_field
    @property
    def is_influencer(self) -> bool:
        return self.follower_count >= 10000



class Comment(BaseModel):
    content: str
    author_email: EmailStr
    likes: int = 0



class BlogPost(BaseModel):
    title: Annotated[str, Field(min_length=9)]
    content: str
    view_count: int = 0
    is_published: bool = False
    tags: list[str] = Field(default_factory=list)
    create_at: datetime = Field(default_factory=partial(datetime.now, tz=UTC))
    author: User
    status: Literal["draft", "published", "archived"] = "draft"
    comments: list[Comment] = Field(default_factory=list)

class UserRegistration(BaseModel):
    email: EmailStr
    password: str
    confirm_password: str

    @model_validator(mode="after")
    def passwords_match(self) -> "UserRegistration":
        if self.password != self.confirm_password:
            raise ValueError("Passwords do not match")
        return self

#try:
 #   registration = UserRegistration(
  #      email="michal123@wp.pl",
   #     password="secret123",
   #     confirm_password="secret456"
   # )
#except ValidationError as e:
 #   print(e)


post_data = {
    "title": "Understanding Pydantic Models",
    "content": "Pydantic makes data validation easy and intuitive...",
    "author": {
        "username": "coreyms",
        "email": "CoreyMSchafer@gmail.com",
        "age": 39,
        "password": "secret123",
    },
    "comments": [
        {
            "content": "I think I understand nested models now!",
            "author_email": "student@example.com",
            "likes": 25,
        },
        {
            "content": "Can you cover FastAPI next?",
            "author_email": "viewer@example.com",
            "likes": 15,
        },
    ],
}

post = BlogPost(**post_data)

print(post.model_dump_json(indent=2))




# user = User(
#     username="Michal",
#     email="abc@wp.pl",
#     age=23,
#     website="abcd123",
#     password="abcdefgh123",
#     first_name="Michal",
#     last_name="Litwin",
#     follower_count= 15000
# )


#print(user.model_dump_json(indent=2))





post = BlogPost(
    title = "Getting Started with Python",
    content = "Here's how to begin...",
    author_id= "12345"
)

#print(post)