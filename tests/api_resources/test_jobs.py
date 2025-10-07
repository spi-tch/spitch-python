# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from spitch import Spitch, AsyncSpitch
from tests.utils import assert_matches_type
from spitch.types import Job
from spitch.pagination import SyncFilesCursor, AsyncFilesCursor

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Spitch) -> None:
        job = client.jobs.list()
        assert_matches_type(SyncFilesCursor[Job], job, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Spitch) -> None:
        job = client.jobs.list(
            cursor="cursor",
            limit=99,
            status="queued",
        )
        assert_matches_type(SyncFilesCursor[Job], job, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Spitch) -> None:
        response = client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(SyncFilesCursor[Job], job, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Spitch) -> None:
        with client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(SyncFilesCursor[Job], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_get(self, client: Spitch) -> None:
        job = client.jobs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Spitch) -> None:
        response = client.jobs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Spitch) -> None:
        with client.jobs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_get(self, client: Spitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.jobs.with_raw_response.get(
                "",
            )


class TestAsyncJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncSpitch) -> None:
        job = await async_client.jobs.list()
        assert_matches_type(AsyncFilesCursor[Job], job, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncSpitch) -> None:
        job = await async_client.jobs.list(
            cursor="cursor",
            limit=99,
            status="queued",
        )
        assert_matches_type(AsyncFilesCursor[Job], job, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncSpitch) -> None:
        response = await async_client.jobs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(AsyncFilesCursor[Job], job, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncSpitch) -> None:
        async with async_client.jobs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(AsyncFilesCursor[Job], job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_get(self, async_client: AsyncSpitch) -> None:
        job = await async_client.jobs.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncSpitch) -> None:
        response = await async_client.jobs.with_raw_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        job = await response.parse()
        assert_matches_type(Job, job, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncSpitch) -> None:
        async with async_client.jobs.with_streaming_response.get(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            job = await response.parse()
            assert_matches_type(Job, job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_get(self, async_client: AsyncSpitch) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.jobs.with_raw_response.get(
                "",
            )
