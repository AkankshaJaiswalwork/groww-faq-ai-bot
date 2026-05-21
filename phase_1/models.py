from pydantic import BaseModel, Field
from typing import List, Optional

class Holding(BaseModel):
    company_name: str
    allocation_percentage: float
    sector: str

class MutualFund(BaseModel):
    fund_id: str
    fund_name: str
    category: str
    aum_cr: float
    expense_ratio: float
    nav: float
    pe_ratio: float
    returns_1y: float
    returns_3y: float
    returns_5y: float
    risk_level: str
    fund_manager: str
    amc: str
    holdings: List[Holding]
