import asyncio

import fire

from metagpt.roles import (
    Architect,
    Engineer,
    ProductManager,
    ProjectManager,
    QaEngineer,
)
from metagpt.software_company import SoftwareCompany


async def startup(
    idea: str,
    investment: float = 3.0,
    n_round: int = 5,
    code_review: bool = False,
    run_tests: bool = False,
    implement: bool = True,
):
    """Run a startup. Be a boss."""
    company = SoftwareCompany()
    company.hire(
        [
            ProductManager(),
            Architect(),
            ProjectManager(),
        ]
    )

    # if implement or code_review
    if implement or code_review:
        # developing features: implement the idea
        company.hire([Engineer(n_borg=5, use_code_review=code_review)])

    if run_tests:
        # developing features: run tests on the spot and identify bugs
        # (bug fixing capability comes soon!)
        company.hire([QaEngineer()])

    company.invest(investment)
    company.start_project(idea)
