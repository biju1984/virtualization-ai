import pytest
from app.services.api_service import process_natural_language


@pytest.mark.asyncio
async def test_process_natural_language_with_error():
    result = await process_natural_language("This should cause an error")
    assert "API Specification" in result or "error" in result
