from dataclasses import dataclass, asdict, fields
import random
from faker import Faker
from typing import List, Tuple


@dataclass
class RegistrationFormDataBasicGenerator:
    name: str
    email: str
    company: str
    phone: Tuple[str, str]
    web_url: str

    @classmethod
    def get_random(cls, is_business_email: bool = False):
        field = [f.name for f in fields(cls)]
        kwargs = _generate(field, is_business_email=is_business_email)
        return cls(**kwargs)

    def to_dict(self) -> dict:
        return asdict(self)


def _generate(args, is_business_email: bool = False) -> dict:
    faker = Faker()
    kwargs = {}
    for arg in args:
        if arg == "name":
            kwargs["name"] = faker.name()
        if arg == "email":
            kwargs["email"] = generate_email_for_sm_account(
                is_business=is_business_email
            )
        if arg == "company":
            kwargs["company"] = faker.company()
        if arg == "phone":
            kwargs["phone"] = ("+1", "855 395 0027")
        if arg == "web_url":
            kwargs["web_url"] = faker.url()
    return kwargs


def generate_email_for_sm_account(is_business: bool = False) -> str:
    email_prefix = "lwoypaeimnjjvtecdu"
    email_domain = "nthrl.com" if is_business else "nthrl.com"
    return f"{email_prefix}@{email_domain}"
