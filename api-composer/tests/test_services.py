import pytest
from app.services.api_service import process_natural_language

@pytest.mark.asyncio
async def test_process_natural_language():
    result = await process_natural_language("Create an API for tasks")
    assert "API Specification" in result

