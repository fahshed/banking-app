import pytest
from unittest.mock import MagicMock
from pymongo.collection import Collection
from database import get_prod_collection


@pytest.mark.asyncio
async def test_get_prod_collection(mocker):
    mock_client = MagicMock()
    mock_db = MagicMock()
    mock_collection = MagicMock(spec=Collection)
    mock_db.__getitem__.return_value = mock_collection
    mock_client.__getitem__.return_value = mock_db

    mocker.patch("dotenv.dotenv_values", return_value={"MONGODB_CONNECTION_URI": "mock_uri", "DB_NAME": "mock_db"})
    mocker.patch("pymongo.MongoClient", return_value=mock_client)

    collection = await get_prod_collection()

    assert isinstance(collection, Collection)