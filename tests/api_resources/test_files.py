# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from spitch import Spitch, AsyncSpitch
from tests.utils import assert_matches_type
from spitch.types import (
    File,
    FileUsage,
    FileDownloadResponse,
)
from spitch.pagination import SyncFilesCursor, AsyncFilesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Spitch) -> None:
        file = client.files.list()
        assert_matches_type(SyncFilesCursor[File], file, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Spitch) -> None:
        file = client.files.list(
            cursor="cursor",
            limit=99,
            status="uploading",
        )
        assert_matches_type(SyncFilesCursor[File], file, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Spitch) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(SyncFilesCursor[File], file, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Spitch) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(SyncFilesCursor[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: Spitch) -> None:
        file = client.files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_raw_response_delete(self, client: Spitch) -> None:
        response = client.files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    def test_streaming_response_delete(self, client: Spitch) -> None:
        with client.files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_delete(self, client: Spitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    def test_method_download(self, client: Spitch) -> None:
        file = client.files.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileDownloadResponse, file, path=["response"])

    @parametrize
    def test_method_download_with_all_params(self, client: Spitch) -> None:
        file = client.files.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ttl=60,
        )
        assert_matches_type(FileDownloadResponse, file, path=["response"])

    @parametrize
    def test_raw_response_download(self, client: Spitch) -> None:
        response = client.files.with_raw_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileDownloadResponse, file, path=["response"])

    @parametrize
    def test_streaming_response_download(self, client: Spitch) -> None:
        with client.files.with_streaming_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileDownloadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_download(self, client: Spitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.download(
                file_id="",
            )

    @parametrize
    def test_method_get(self, client: Spitch) -> None:
        file = client.files.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Spitch) -> None:
        response = client.files.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Spitch) -> None:
        with client.files.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Spitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.get(
                "",
            )

    @parametrize
    def test_method_upload(self, client: Spitch) -> None:
        file = client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_raw_response_upload(self, client: Spitch) -> None:
        response = client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    def test_streaming_response_upload(self, client: Spitch) -> None:
        with client.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_usage(self, client: Spitch) -> None:
        file = client.files.usage()
        assert_matches_type(FileUsage, file, path=["response"])

    @parametrize
    def test_raw_response_usage(self, client: Spitch) -> None:
        response = client.files.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUsage, file, path=["response"])

    @parametrize
    def test_streaming_response_usage(self, client: Spitch) -> None:
        with client.files.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUsage, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.list()
        assert_matches_type(AsyncFilesCursor[File], file, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.list(
            cursor="cursor",
            limit=99,
            status="uploading",
        )
        assert_matches_type(AsyncFilesCursor[File], file, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSpitch) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(AsyncFilesCursor[File], file, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSpitch) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(AsyncFilesCursor[File], file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncSpitch) -> None:
        response = await async_client.files.with_raw_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(object, file, path=["response"])

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncSpitch) -> None:
        async with async_client.files.with_streaming_response.delete(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_delete(self, async_client: AsyncSpitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @parametrize
    async def test_method_download(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(FileDownloadResponse, file, path=["response"])

    @parametrize
    async def test_method_download_with_all_params(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
            ttl=60,
        )
        assert_matches_type(FileDownloadResponse, file, path=["response"])

    @parametrize
    async def test_raw_response_download(self, async_client: AsyncSpitch) -> None:
        response = await async_client.files.with_raw_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileDownloadResponse, file, path=["response"])

    @parametrize
    async def test_streaming_response_download(self, async_client: AsyncSpitch) -> None:
        async with async_client.files.with_streaming_response.download(
            file_id="182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileDownloadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_download(self, async_client: AsyncSpitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.download(
                file_id="",
            )

    @parametrize
    async def test_method_get(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSpitch) -> None:
        response = await async_client.files.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSpitch) -> None:
        async with async_client.files.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncSpitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.get(
                "",
            )

    @parametrize
    async def test_method_upload(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
        )
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncSpitch) -> None:
        response = await async_client.files.with_raw_response.upload(
            file=b"raw file contents",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncSpitch) -> None:
        async with async_client.files.with_streaming_response.upload(
            file=b"raw file contents",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_usage(self, async_client: AsyncSpitch) -> None:
        file = await async_client.files.usage()
        assert_matches_type(FileUsage, file, path=["response"])

    @parametrize
    async def test_raw_response_usage(self, async_client: AsyncSpitch) -> None:
        response = await async_client.files.with_raw_response.usage()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUsage, file, path=["response"])

    @parametrize
    async def test_streaming_response_usage(self, async_client: AsyncSpitch) -> None:
        async with async_client.files.with_streaming_response.usage() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUsage, file, path=["response"])

        assert cast(Any, response.is_closed) is True
