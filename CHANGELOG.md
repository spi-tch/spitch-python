# Changelog

## 1.41.1 (2025-11-12)

Full Changelog: [v1.41.0...v1.41.1](https://github.com/spi-tch/spitch-python/compare/v1.41.0...v1.41.1)

### Bug Fixes

* compat with Python 3.14 ([1ab2493](https://github.com/spi-tch/spitch-python/commit/1ab24934076718e95b5db05ea4bfdd241f8f81da))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([c57a49c](https://github.com/spi-tch/spitch-python/commit/c57a49c4da4c7002b18875e8e9ba01f96f09b7ae))


### Chores

* **package:** drop Python 3.8 support ([84254f4](https://github.com/spi-tch/spitch-python/commit/84254f4b0040778492d21e0a6dc1e1d6c72f3989))

## 1.41.0 (2025-11-04)

Full Changelog: [v1.40.1...v1.41.0](https://github.com/spi-tch/spitch-python/compare/v1.40.1...v1.41.0)

### Features

* **api:** manual updates ([550cf54](https://github.com/spi-tch/spitch-python/commit/550cf54a42a6f06a043d99eff54999db93d49efe))

## 1.40.1 (2025-11-04)

Full Changelog: [v1.40.0...v1.40.1](https://github.com/spi-tch/spitch-python/compare/v1.40.0...v1.40.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([caff450](https://github.com/spi-tch/spitch-python/commit/caff4506e7e4984cb6b9d553cfc144d79658db5b))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([c306d2e](https://github.com/spi-tch/spitch-python/commit/c306d2ea2e61562f51a561efd1b08f251fec4fa2))
* **internal/tests:** avoid race condition with implicit client cleanup ([1c74fa9](https://github.com/spi-tch/spitch-python/commit/1c74fa902f76c4206b881d3f48175511251dc1da))
* **internal:** grammar fix (it's -&gt; its) ([2986b36](https://github.com/spi-tch/spitch-python/commit/2986b360854db3075b0cdf6ac5d02be004c26fc1))

## 1.40.0 (2025-10-16)

Full Changelog: [v1.39.0...v1.40.0](https://github.com/spi-tch/spitch-python/compare/v1.39.0...v1.40.0)

### Features

* **api:** manual updates ([578dbb8](https://github.com/spi-tch/spitch-python/commit/578dbb81d604d24899f6687fe6dd2a32a923ac15))


### Chores

* **internal:** detect missing future annotations with ruff ([36529fc](https://github.com/spi-tch/spitch-python/commit/36529fcafde8b0aa37800296b6b27b4f8fbe7984))

## 1.39.0 (2025-10-07)

Full Changelog: [v1.38.0...v1.39.0](https://github.com/spi-tch/spitch-python/compare/v1.38.0...v1.39.0)

### Features

* **api:** manual updates ([c02e088](https://github.com/spi-tch/spitch-python/commit/c02e088c99193debbbea6d29f648dfe5435a6585))

## 1.38.0 (2025-10-06)

Full Changelog: [v1.37.1...v1.38.0](https://github.com/spi-tch/spitch-python/compare/v1.37.1...v1.38.0)

### Features

* **api:** manual updates ([d84dc7a](https://github.com/spi-tch/spitch-python/commit/d84dc7a2ba91e736117d50c1c5423775ca1c6ed9))
* **api:** manual updates ([b9b9d1f](https://github.com/spi-tch/spitch-python/commit/b9b9d1fff4e55d8063e2986558385bc6c70a6294))
* **api:** manual updates ([71da782](https://github.com/spi-tch/spitch-python/commit/71da7823c6b7dd8873204c50854856f4e9f64f6d))


### Chores

* update SDK settings ([eb3676c](https://github.com/spi-tch/spitch-python/commit/eb3676c9b3641a8ec0ed493b730081d925fb9f38))

## 1.37.1 (2025-10-06)

Full Changelog: [v1.37.0...v1.37.1](https://github.com/spi-tch/spitch-python/compare/v1.37.0...v1.37.1)

## 1.37.0 (2025-10-06)

Full Changelog: [v1.36.0...v1.37.0](https://github.com/spi-tch/spitch-python/compare/v1.36.0...v1.37.0)

### Features

* **api:** manual updates ([c8f4f39](https://github.com/spi-tch/spitch-python/commit/c8f4f3942e2a9a7a2c3897a81288ab03e9172885))

## 1.36.0 (2025-10-06)

Full Changelog: [v1.35.0...v1.36.0](https://github.com/spi-tch/spitch-python/compare/v1.35.0...v1.36.0)

### Features

* **api:** manual updates ([813fc60](https://github.com/spi-tch/spitch-python/commit/813fc60ce810fc61aa542eae3a780bce8b21e506))

## 1.35.0 (2025-10-06)

Full Changelog: [v1.34.0...v1.35.0](https://github.com/spi-tch/spitch-python/compare/v1.34.0...v1.35.0)

### Features

* **api:** manual updates ([574df33](https://github.com/spi-tch/spitch-python/commit/574df333fdbdc5da00db8995c76764ef35525a98))
* **api:** manual updates ([ead4d0f](https://github.com/spi-tch/spitch-python/commit/ead4d0f08f3b28578c1a5caea262290dc04d8b27))
* improve future compat with pydantic v3 ([d0bad68](https://github.com/spi-tch/spitch-python/commit/d0bad682b3e6b51dc0c37c7779a1a87476bd06b2))
* **types:** replace List[str] with SequenceNotStr in params ([7c4068d](https://github.com/spi-tch/spitch-python/commit/7c4068d1941ff82258c64ea2308574d7f18fd9eb))


### Bug Fixes

* avoid newer type syntax ([8ca197e](https://github.com/spi-tch/spitch-python/commit/8ca197e3a5dee3caa13c202561a571bd27f426d6))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([65b9b27](https://github.com/spi-tch/spitch-python/commit/65b9b27f367eaf8acd5ac279477133bcc16d474e))
* **internal:** add Sequence related utils ([165bc5b](https://github.com/spi-tch/spitch-python/commit/165bc5bf7aab042eb26329511d7c3710e8f3013f))
* **internal:** change ci workflow machines ([47a8c37](https://github.com/spi-tch/spitch-python/commit/47a8c37c9f69a1ab81018ef18e210a6b9ccd3b61))
* **internal:** codegen related update ([2b78c91](https://github.com/spi-tch/spitch-python/commit/2b78c91f092d0a21452bdf49c1ca030aad41659e))
* **internal:** fix ruff target version ([8b255f3](https://github.com/spi-tch/spitch-python/commit/8b255f361be3c261ea1949109566caa3ab149000))
* **internal:** move mypy configurations to `pyproject.toml` file ([a72dfb3](https://github.com/spi-tch/spitch-python/commit/a72dfb3a9f8664c9fe65b8828c730e32d6eb2fe6))
* **internal:** update comment in script ([b369538](https://github.com/spi-tch/spitch-python/commit/b369538413c8f30c37f58ff479c93cbc592512ee))
* **internal:** update pydantic dependency ([a187d65](https://github.com/spi-tch/spitch-python/commit/a187d658fd4b0b6dfadac17a88f50bf93569cdda))
* **internal:** update pyright exclude list ([c2f65df](https://github.com/spi-tch/spitch-python/commit/c2f65df82191ffc6f25baf52eb8b5a30fbbaa4df))
* **types:** change optional parameter type from NotGiven to Omit ([aa74911](https://github.com/spi-tch/spitch-python/commit/aa74911c2a673a56720e2dab3264151423f88b25))
* update @stainless-api/prism-cli to v5.15.0 ([d0371a7](https://github.com/spi-tch/spitch-python/commit/d0371a73586deac608ce2e4fae2439b477f90702))
* update github action ([c3e1045](https://github.com/spi-tch/spitch-python/commit/c3e1045cbfbf202f009042c0de01cd0007881e25))

## 1.34.0 (2025-08-05)

Full Changelog: [v1.33.0...v1.34.0](https://github.com/spi-tch/spitch-python/compare/v1.33.0...v1.34.0)

### Features

* **api:** update via SDK Studio ([e1eddc1](https://github.com/spi-tch/spitch-python/commit/e1eddc115253f0d959068f0096abbbad58e1ca41))
* **api:** update via SDK Studio ([fc00ced](https://github.com/spi-tch/spitch-python/commit/fc00ceda503d7721e38daaba609625f1b44613ae))
* **api:** update via SDK Studio ([910add6](https://github.com/spi-tch/spitch-python/commit/910add6ee71ff113f4471677094d5e385585e70c))

## 1.33.0 (2025-08-02)

Full Changelog: [v1.32.0...v1.33.0](https://github.com/spi-tch/spitch-python/compare/v1.32.0...v1.33.0)

### Features

* **api:** update via SDK Studio ([9d14152](https://github.com/spi-tch/spitch-python/commit/9d14152165cda3b68febf16ccd6d7c662420db76))

## 1.32.0 (2025-08-02)

Full Changelog: [v1.31.0...v1.32.0](https://github.com/spi-tch/spitch-python/compare/v1.31.0...v1.32.0)

### Features

* **api:** update via SDK Studio ([49e48bf](https://github.com/spi-tch/spitch-python/commit/49e48bf33fc79945d5828b3524ecaa49a0186d6e))

## 1.31.0 (2025-08-02)

Full Changelog: [v1.30.0...v1.31.0](https://github.com/spi-tch/spitch-python/compare/v1.30.0...v1.31.0)

### Features

* **api:** update via SDK Studio ([cbe2e04](https://github.com/spi-tch/spitch-python/commit/cbe2e040af49ed35c984afc10c1484d35a9e0582))

## 1.30.0 (2025-08-02)

Full Changelog: [v1.29.0...v1.30.0](https://github.com/spi-tch/spitch-python/compare/v1.29.0...v1.30.0)

### Features

* **api:** update via SDK Studio ([24e67c7](https://github.com/spi-tch/spitch-python/commit/24e67c70d35112615debb4aa0e8a78ffc3259d3b))

## 1.29.0 (2025-08-02)

Full Changelog: [v1.28.0...v1.29.0](https://github.com/spi-tch/spitch-python/compare/v1.28.0...v1.29.0)

### Features

* **api:** update via SDK Studio ([8e660c1](https://github.com/spi-tch/spitch-python/commit/8e660c165c47bb8b062e976eebfbdc62691044ce))

## 1.28.0 (2025-08-01)

Full Changelog: [v1.27.1...v1.28.0](https://github.com/spi-tch/spitch-python/compare/v1.27.1...v1.28.0)

### Features

* **api:** update via SDK Studio ([9db6264](https://github.com/spi-tch/spitch-python/commit/9db6264b632e315387983917ab7b42387e7c40c3))
* **api:** update via SDK Studio ([8fff307](https://github.com/spi-tch/spitch-python/commit/8fff307f77fee14c52877ff581338f3ec08a173e))
* clean up environment call outs ([fd8997e](https://github.com/spi-tch/spitch-python/commit/fd8997e1a67c568cf3f6e7061124ac27ded0a742))
* **client:** add support for aiohttp ([716f429](https://github.com/spi-tch/spitch-python/commit/716f4298354f2018155a9fd0a22b5446116081e3))
* **client:** support file upload requests ([60d3ce3](https://github.com/spi-tch/spitch-python/commit/60d3ce3ebc58ab4c0639b19c8e36078123ac7cc3))


### Bug Fixes

* **ci:** correct conditional ([1734cf4](https://github.com/spi-tch/spitch-python/commit/1734cf46a42f752642f04df64c701dd2ca7d60f5))
* **ci:** release-doctor — report correct token name ([1a09341](https://github.com/spi-tch/spitch-python/commit/1a09341c5dc0adc06a53824a7effcb987c1a3f33))
* **client:** don't send Content-Type header on GET requests ([b5a10cf](https://github.com/spi-tch/spitch-python/commit/b5a10cf567f59d90c259c8c6400b0cdf06af4ab3))
* **parsing:** correctly handle nested discriminated unions ([3e1a25b](https://github.com/spi-tch/spitch-python/commit/3e1a25b7953ed4611ca17c7ff4c84ffd032b5e4c))
* **parsing:** ignore empty metadata ([fc15e0e](https://github.com/spi-tch/spitch-python/commit/fc15e0ec9875c16f7aa8e00d6d8d8d4c60a866a8))
* **parsing:** parse extra field types ([8be1102](https://github.com/spi-tch/spitch-python/commit/8be11026e3d93b62aa77b170dd90acb5f246203a))


### Chores

* **ci:** change upload type ([d9bf40f](https://github.com/spi-tch/spitch-python/commit/d9bf40f2b21338b7e3e1201b01ccd652417acfe4))
* **ci:** only run for pushes and fork pull requests ([bcba93e](https://github.com/spi-tch/spitch-python/commit/bcba93e8a69c3dec830e9d8040c76ebdda50cecf))
* **internal:** bump pinned h11 dep ([bd7d84b](https://github.com/spi-tch/spitch-python/commit/bd7d84b66fd468aabbc7dd6943579a330598bb98))
* **internal:** codegen related update ([8c23505](https://github.com/spi-tch/spitch-python/commit/8c235055fa37c950b3559e57a70ecd925ddaf518))
* **package:** mark python 3.13 as supported ([12c842b](https://github.com/spi-tch/spitch-python/commit/12c842bc7b4d6dbdd4376b79bf1581398363258e))
* **project:** add settings file for vscode ([8b0274c](https://github.com/spi-tch/spitch-python/commit/8b0274cb3d4c369550a823600bb4e493eb7b3638))
* **readme:** fix version rendering on pypi ([bf4b720](https://github.com/spi-tch/spitch-python/commit/bf4b720b71d72a1073179e68a3e55f2208bd0649))
* **tests:** skip some failing tests on the latest python versions ([9f60f27](https://github.com/spi-tch/spitch-python/commit/9f60f27835eccba43797fab6d033cdb116ec2a59))

## 1.27.1 (2025-06-19)

Full Changelog: [v1.27.0...v1.27.1](https://github.com/spi-tch/spitch-python/compare/v1.27.0...v1.27.1)

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([e6df2f6](https://github.com/spi-tch/spitch-python/commit/e6df2f6b390f5f3313ff1e20ee2890fd2ac53265))


### Chores

* **readme:** update badges ([d272526](https://github.com/spi-tch/spitch-python/commit/d2725265a638bba5ef65bf8ab468a33af6b5b594))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([d8af609](https://github.com/spi-tch/spitch-python/commit/d8af609deca7a01713250544babf4ced45dc2376))

## 1.27.0 (2025-06-17)

Full Changelog: [v1.26.0...v1.27.0](https://github.com/spi-tch/spitch-python/compare/v1.26.0...v1.27.0)

### Features

* **client:** add follow_redirects request option ([23f17af](https://github.com/spi-tch/spitch-python/commit/23f17afc3292d6641890115e849134e14412ab7c))


### Bug Fixes

* **client:** correctly parse binary response | stream ([43997d9](https://github.com/spi-tch/spitch-python/commit/43997d9e1f67269df4f5ed9472f1abb6dfc8afc3))
* **package:** support direct resource imports ([3b664db](https://github.com/spi-tch/spitch-python/commit/3b664db8de2fe51363215430c04ef0d45a96ef15))


### Chores

* broadly detect json family of content-type headers ([1358fe6](https://github.com/spi-tch/spitch-python/commit/1358fe6da25145ce5d57317a835bf306e9886f5c))
* **ci:** enable for pull requests ([f21c633](https://github.com/spi-tch/spitch-python/commit/f21c633b3bc746fdfcf95214bda7e664212fce3f))
* **ci:** fix installation instructions ([c23d223](https://github.com/spi-tch/spitch-python/commit/c23d22393563b50ac77742d75cda7f7b95e8a4a0))
* **ci:** only use depot for staging repos ([86c82b9](https://github.com/spi-tch/spitch-python/commit/86c82b989e1599bc9d71060f2f2998eaa4b79081))
* **ci:** upload sdks to package manager ([a40305e](https://github.com/spi-tch/spitch-python/commit/a40305e129dd6795b0e0e1408b863758cfad62d0))
* **docs:** grammar improvements ([e31d3bb](https://github.com/spi-tch/spitch-python/commit/e31d3bbe8aa390cdbae514e16e31e45b3ee5a4d5))
* **docs:** remove reference to rye shell ([b7f1703](https://github.com/spi-tch/spitch-python/commit/b7f1703ce312c6733e2986d045568b003ac4bba1))
* **internal:** avoid errors for isinstance checks on proxies ([aaf12a5](https://github.com/spi-tch/spitch-python/commit/aaf12a5580a673adbf303bea88f958f384b0ebcd))
* **internal:** codegen related update ([fc70ee0](https://github.com/spi-tch/spitch-python/commit/fc70ee0bf2bb47f12ec36a35fad1b27d257897ce))
* **internal:** update conftest.py ([1b062cd](https://github.com/spi-tch/spitch-python/commit/1b062cdf9d6200399d24bceb73e31779a80be190))
* **tests:** add tests for httpx client instantiation & proxies ([a57f4cc](https://github.com/spi-tch/spitch-python/commit/a57f4cc2105706eb53c9483ac74e2ec4995bd757))
* **tests:** run tests in parallel ([da93455](https://github.com/spi-tch/spitch-python/commit/da93455365f885480cf4553ab138fc71eebd59f9))

## 1.26.0 (2025-04-23)

Full Changelog: [v1.25.0...v1.26.0](https://github.com/spi-tch/spitch-python/compare/v1.25.0...v1.26.0)

### Features

* **api:** update via SDK Studio ([9e64faf](https://github.com/spi-tch/spitch-python/commit/9e64faf9bbbc57c8e44d1a347a64ef3396ed4472))
* **api:** update via SDK Studio ([2fc4429](https://github.com/spi-tch/spitch-python/commit/2fc442984db836b5432b07891ea9a777822a5cac))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([f5079d4](https://github.com/spi-tch/spitch-python/commit/f5079d48e4adc75593d5656512946569ca8f2932))


### Chores

* **ci:** add timeout thresholds for CI jobs ([8dd6edf](https://github.com/spi-tch/spitch-python/commit/8dd6edf6523812a052ce8b900c387f4fc0928925))
* **client:** minor internal fixes ([d9a6927](https://github.com/spi-tch/spitch-python/commit/d9a69272125832cfab65cf88ede7527770e447f3))
* **internal:** base client updates ([b900090](https://github.com/spi-tch/spitch-python/commit/b9000901050f076ce2c2485c878ea7a8535c9257))
* **internal:** bump pyright version ([a281060](https://github.com/spi-tch/spitch-python/commit/a28106063e43b6f6d7d9af738a6cc4a0b0e2ebed))
* **internal:** fix list file params ([21ca206](https://github.com/spi-tch/spitch-python/commit/21ca2061b42069c0405e6302ab8841e7a7683670))
* **internal:** import reformatting ([65b55d9](https://github.com/spi-tch/spitch-python/commit/65b55d9ed72e5656b5cd70152d652295d3925b4b))
* **internal:** refactor retries to not use recursion ([be7d9aa](https://github.com/spi-tch/spitch-python/commit/be7d9aac3cd43ea510181717329acd4607c37c07))
* **internal:** update models test ([05a0518](https://github.com/spi-tch/spitch-python/commit/05a0518e8db6186e2c7ac031352b336f5c43e68d))
* **internal:** update pyright settings ([8df5838](https://github.com/spi-tch/spitch-python/commit/8df58385cb95aadcfe2b341cd7a49142b64d960e))

## 1.25.0 (2025-04-14)

Full Changelog: [v1.24.1...v1.25.0](https://github.com/spi-tch/spitch-python/compare/v1.24.1...v1.25.0)

### Features

* Update _base_client.py ([dca19f3](https://github.com/spi-tch/spitch-python/commit/dca19f316d3d1b59aa39012618c6700e8236c4a3))


### Bug Fixes

* **api:** updates for https client ([dca19f3](https://github.com/spi-tch/spitch-python/commit/dca19f316d3d1b59aa39012618c6700e8236c4a3))

## 1.24.1 (2025-04-14)

Full Changelog: [v1.24.0...v1.24.1](https://github.com/spi-tch/spitch-python/compare/v1.24.0...v1.24.1)

### Bug Fixes

* **ci:** ensure pip is always available ([#135](https://github.com/spi-tch/spitch-python/issues/135)) ([761ba1e](https://github.com/spi-tch/spitch-python/commit/761ba1e39992907bff53ae44b4332579dc08239b))
* **ci:** remove publishing patch ([#136](https://github.com/spi-tch/spitch-python/issues/136)) ([f43dc79](https://github.com/spi-tch/spitch-python/commit/f43dc79390698c45ed10756420728263a8f50881))
* **perf:** optimize some hot paths ([1259f9c](https://github.com/spi-tch/spitch-python/commit/1259f9c3cce0cc184954586edc5cc47cc9cefc27))
* **perf:** skip traversing types for NotGiven values ([bb37b4e](https://github.com/spi-tch/spitch-python/commit/bb37b4eaff98d495dd2a717030629c73a1200050))
* **types:** handle more discriminated union shapes ([#133](https://github.com/spi-tch/spitch-python/issues/133)) ([6c0a695](https://github.com/spi-tch/spitch-python/commit/6c0a6959efc1f3ffd1da2f5af4117ccf0e1f3488))


### Chores

* fix typos ([#137](https://github.com/spi-tch/spitch-python/issues/137)) ([d6fedfb](https://github.com/spi-tch/spitch-python/commit/d6fedfb2ad26407907d40738e3897e47676657bd))
* **internal:** bump rye to 0.44.0 ([#132](https://github.com/spi-tch/spitch-python/issues/132)) ([3ff0800](https://github.com/spi-tch/spitch-python/commit/3ff08004657e1e2bd0e0bca888808ec1e45dd87c))
* **internal:** codegen related update ([#131](https://github.com/spi-tch/spitch-python/issues/131)) ([d4355bf](https://github.com/spi-tch/spitch-python/commit/d4355bfb4f5a231335066471af0bc9f42958b971))
* **internal:** expand CI branch coverage ([a10e485](https://github.com/spi-tch/spitch-python/commit/a10e4852c17d5bfac1f07846e740aeb00693a34c))
* **internal:** reduce CI branch coverage ([bb74d2c](https://github.com/spi-tch/spitch-python/commit/bb74d2c5719c2dedeca969227177fc2e5a1d34ca))
* **internal:** remove extra empty newlines ([#129](https://github.com/spi-tch/spitch-python/issues/129)) ([606964f](https://github.com/spi-tch/spitch-python/commit/606964f05336f9bb47cea4a8e0b51b9720b8d866))
* **internal:** remove trailing character ([#138](https://github.com/spi-tch/spitch-python/issues/138)) ([713749a](https://github.com/spi-tch/spitch-python/commit/713749a9ec9db9d52e013dd65dd13e49f3c6918d))
* **internal:** slight transform perf improvement ([#139](https://github.com/spi-tch/spitch-python/issues/139)) ([3362024](https://github.com/spi-tch/spitch-python/commit/3362024e9b76f382378ddebf7cb708710ddbcf48))
* slight wording improvement in README ([#140](https://github.com/spi-tch/spitch-python/issues/140)) ([77cd1b3](https://github.com/spi-tch/spitch-python/commit/77cd1b3d2608dcd2af9e57bdd53ec8a90c9867fe))

## 1.24.0 (2025-03-11)

Full Changelog: [v1.23.0...v1.24.0](https://github.com/spi-tch/spitch-python/compare/v1.23.0...v1.24.0)

### Features

* **api:** update via SDK Studio ([#126](https://github.com/spi-tch/spitch-python/issues/126)) ([123d303](https://github.com/spi-tch/spitch-python/commit/123d303e48eb1baaf3eb8880e6e1d66294409c98))

## 1.23.0 (2025-03-11)

Full Changelog: [v1.22.0...v1.23.0](https://github.com/spi-tch/spitch-python/compare/v1.22.0...v1.23.0)

### Features

* **api:** update via SDK Studio ([#123](https://github.com/spi-tch/spitch-python/issues/123)) ([38f463f](https://github.com/spi-tch/spitch-python/commit/38f463f3cb88e5db4b10ef261f8a6ab9a2c30edc))
* Update _response.py ([3d23d77](https://github.com/spi-tch/spitch-python/commit/3d23d779d3fe974d4ce466e66c585ff3eb8bd9d1))

## 1.22.0 (2025-03-11)

Full Changelog: [v1.21.1...v1.22.0](https://github.com/spi-tch/spitch-python/compare/v1.21.1...v1.22.0)

### Features

* **api:** update via SDK Studio ([#120](https://github.com/spi-tch/spitch-python/issues/120)) ([d0d2514](https://github.com/spi-tch/spitch-python/commit/d0d2514fdac33ef10c695d9e80c4620745596063))

## 1.21.1 (2025-03-11)

Full Changelog: [v1.21.0...v1.21.1](https://github.com/spi-tch/spitch-python/compare/v1.21.0...v1.21.1)

## 1.21.0 (2025-03-04)

Full Changelog: [v1.20.0...v1.21.0](https://github.com/spi-tch/spitch-python/compare/v1.20.0...v1.21.0)

### Features

* **api:** update via SDK Studio ([#114](https://github.com/spi-tch/spitch-python/issues/114)) ([2cb4f31](https://github.com/spi-tch/spitch-python/commit/2cb4f316c23ec0ea1ca0388681e1b0ae20d8d160))

## 1.20.0 (2025-03-04)

Full Changelog: [v1.19.0...v1.20.0](https://github.com/spi-tch/spitch-python/compare/v1.19.0...v1.20.0)

### Features

* **api:** update via SDK Studio ([#109](https://github.com/spi-tch/spitch-python/issues/109)) ([6e29edd](https://github.com/spi-tch/spitch-python/commit/6e29eddfb89bf0512bd87cd712c29ba19e145b7a))
* **client:** allow passing `NotGiven` for body ([#103](https://github.com/spi-tch/spitch-python/issues/103)) ([6f2bdd1](https://github.com/spi-tch/spitch-python/commit/6f2bdd15f3f6089eaf79d0841cd013258c19eaa5))
* **client:** send `X-Stainless-Read-Timeout` header ([#97](https://github.com/spi-tch/spitch-python/issues/97)) ([5aa6876](https://github.com/spi-tch/spitch-python/commit/5aa687627fa5a4d9815b865144b084a70401205d))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#101](https://github.com/spi-tch/spitch-python/issues/101)) ([06e16f9](https://github.com/spi-tch/spitch-python/commit/06e16f920106f8f7f79ed13e9a5fe173c982381b))
* **client:** mark some request bodies as optional ([6f2bdd1](https://github.com/spi-tch/spitch-python/commit/6f2bdd15f3f6089eaf79d0841cd013258c19eaa5))
* **tests:** make test_get_platform less flaky ([#91](https://github.com/spi-tch/spitch-python/issues/91)) ([f0263dc](https://github.com/spi-tch/spitch-python/commit/f0263dc026f74d0f9a94857b084075fba05e1c78))


### Chores

* **docs:** update client docstring ([#107](https://github.com/spi-tch/spitch-python/issues/107)) ([c08016e](https://github.com/spi-tch/spitch-python/commit/c08016e27757afb2408b0a60a3b91d59ab9cd674))
* **internal:** avoid pytest-asyncio deprecation warning ([#92](https://github.com/spi-tch/spitch-python/issues/92)) ([2a58481](https://github.com/spi-tch/spitch-python/commit/2a58481308d998c02cfb80723802b3d3d3508f11))
* **internal:** bummp ruff dependency ([#96](https://github.com/spi-tch/spitch-python/issues/96)) ([bac43d8](https://github.com/spi-tch/spitch-python/commit/bac43d88bf6c06fbc207149bc877bf4eb2b012b7))
* **internal:** change default timeout to an int ([#95](https://github.com/spi-tch/spitch-python/issues/95)) ([148bc16](https://github.com/spi-tch/spitch-python/commit/148bc16f85dcd9f8baea266a61a7aeb868858c97))
* **internal:** codegen related update ([#102](https://github.com/spi-tch/spitch-python/issues/102)) ([cca3a53](https://github.com/spi-tch/spitch-python/commit/cca3a532412587cc3fe38bfe565102b661152045))
* **internal:** codegen related update ([#88](https://github.com/spi-tch/spitch-python/issues/88)) ([3c27c0e](https://github.com/spi-tch/spitch-python/commit/3c27c0ecabaf2c48c43d941d52365375650c6a83))
* **internal:** codegen related update ([#93](https://github.com/spi-tch/spitch-python/issues/93)) ([9564863](https://github.com/spi-tch/spitch-python/commit/95648632bcbe45c844531fd591f3785df20109e2))
* **internal:** fix devcontainers setup ([#104](https://github.com/spi-tch/spitch-python/issues/104)) ([10214c2](https://github.com/spi-tch/spitch-python/commit/10214c2803d80f734c1aa4ebe5338bbf1b98a6ef))
* **internal:** fix type traversing dictionary params ([#98](https://github.com/spi-tch/spitch-python/issues/98)) ([2d78d6d](https://github.com/spi-tch/spitch-python/commit/2d78d6d92183b5487fe5518f84107e1705f1d178))
* **internal:** minor formatting changes ([#94](https://github.com/spi-tch/spitch-python/issues/94)) ([e3edcec](https://github.com/spi-tch/spitch-python/commit/e3edcecc0ba046c41e5d1aa0bdb7550278fb45c3))
* **internal:** minor type handling changes ([#99](https://github.com/spi-tch/spitch-python/issues/99)) ([9a472ea](https://github.com/spi-tch/spitch-python/commit/9a472ea5ad908b7ddf9944f9e8bf0a2b49710cbb))
* **internal:** properly set __pydantic_private__ ([#105](https://github.com/spi-tch/spitch-python/issues/105)) ([13df700](https://github.com/spi-tch/spitch-python/commit/13df700ecf4651a18b84757bd5602030f9ae8c35))
* **internal:** remove unused http client options forwarding ([#108](https://github.com/spi-tch/spitch-python/issues/108)) ([5e96250](https://github.com/spi-tch/spitch-python/commit/5e96250dc6b2cbfe81cda0f663324df6305ee144))
* **internal:** update client tests ([#100](https://github.com/spi-tch/spitch-python/issues/100)) ([53adf81](https://github.com/spi-tch/spitch-python/commit/53adf817e1d1df6ad125ab6a05c6c3c753367d1c))


### Documentation

* **raw responses:** fix duplicate `the` ([#90](https://github.com/spi-tch/spitch-python/issues/90)) ([ad3e50f](https://github.com/spi-tch/spitch-python/commit/ad3e50fb36232cc0ecab6c4eb1f61176319b46a5))
* update URLs from stainlessapi.com to stainless.com ([#106](https://github.com/spi-tch/spitch-python/issues/106)) ([b7bedc2](https://github.com/spi-tch/spitch-python/commit/b7bedc2b02e508d317e57ba74c6396e2f8c2aa88))

## 1.19.0 (2025-01-14)

Full Changelog: [v1.18.0...v1.19.0](https://github.com/spi-tch/spitch-python/compare/v1.18.0...v1.19.0)

### Features

* **api:** api update ([#34](https://github.com/spi-tch/spitch-python/issues/34)) ([1cfe384](https://github.com/spi-tch/spitch-python/commit/1cfe38416d8c82453609132080a167c0ab735f51))
* **api:** api update ([#37](https://github.com/spi-tch/spitch-python/issues/37)) ([34e4fba](https://github.com/spi-tch/spitch-python/commit/34e4fba09e3744cfb443a3a0de5bf6a59bac50bc))
* **api:** api update ([#39](https://github.com/spi-tch/spitch-python/issues/39)) ([4cc3eb2](https://github.com/spi-tch/spitch-python/commit/4cc3eb24be8de66ae662de62c45818c0100bf894))
* **api:** api update ([#42](https://github.com/spi-tch/spitch-python/issues/42)) ([1575f47](https://github.com/spi-tch/spitch-python/commit/1575f47becd40467509030e2f56e2c73ac771958))
* **api:** api update ([#45](https://github.com/spi-tch/spitch-python/issues/45)) ([feb59bc](https://github.com/spi-tch/spitch-python/commit/feb59bc1cca800efff147800d51ff8bbf486e38b))
* **api:** api update ([#49](https://github.com/spi-tch/spitch-python/issues/49)) ([f4099b6](https://github.com/spi-tch/spitch-python/commit/f4099b6db02bcc4951d0ced67f7729a04cfa4e92))
* **api:** api update ([#52](https://github.com/spi-tch/spitch-python/issues/52)) ([1633f60](https://github.com/spi-tch/spitch-python/commit/1633f603f789c4e140ff9455fffaee21c77a5ebd))
* **api:** api update ([#55](https://github.com/spi-tch/spitch-python/issues/55)) ([f987e48](https://github.com/spi-tch/spitch-python/commit/f987e48d65d4ef24a650bfc3d01757a565766c18))
* **api:** api update ([#58](https://github.com/spi-tch/spitch-python/issues/58)) ([be32dce](https://github.com/spi-tch/spitch-python/commit/be32dcec8d8a6f7c868208a7f73e2d7568588f84))
* **api:** update via SDK Studio ([1fd8e69](https://github.com/spi-tch/spitch-python/commit/1fd8e69e19951c5c08b2620a187b02c83e65a6fd))
* **api:** update via SDK Studio ([9edba8c](https://github.com/spi-tch/spitch-python/commit/9edba8c215b16905ac04b11f151e8c04f556727e))
* **api:** update via SDK Studio ([41dd345](https://github.com/spi-tch/spitch-python/commit/41dd34562573b2d2807cedc4722c53b7350ef4dc))
* **api:** update via SDK Studio ([#10](https://github.com/spi-tch/spitch-python/issues/10)) ([74819f2](https://github.com/spi-tch/spitch-python/commit/74819f278e9e2bfa4bb3f5d06c59c3fda3ed069f))
* **api:** update via SDK Studio ([#13](https://github.com/spi-tch/spitch-python/issues/13)) ([fdb3beb](https://github.com/spi-tch/spitch-python/commit/fdb3bebe5701a188e2c4f62a3a6d2e72c267532c))
* **api:** update via SDK Studio ([#16](https://github.com/spi-tch/spitch-python/issues/16)) ([77235df](https://github.com/spi-tch/spitch-python/commit/77235df6b0d1f15d064da89bab6f836e78c1db61))
* **api:** update via SDK Studio ([#20](https://github.com/spi-tch/spitch-python/issues/20)) ([d1b3421](https://github.com/spi-tch/spitch-python/commit/d1b3421f383b9a575c0721baa32e687aa6609dd6))
* **api:** update via SDK Studio ([#23](https://github.com/spi-tch/spitch-python/issues/23)) ([b0ee3b3](https://github.com/spi-tch/spitch-python/commit/b0ee3b3f10059097252b95498097a4ebeb203afb))
* **api:** update via SDK Studio ([#26](https://github.com/spi-tch/spitch-python/issues/26)) ([1fb1268](https://github.com/spi-tch/spitch-python/commit/1fb12681c9bbdadd7dd4cb41f06ee03d38be235f))
* **api:** update via SDK Studio ([#29](https://github.com/spi-tch/spitch-python/issues/29)) ([1dae398](https://github.com/spi-tch/spitch-python/commit/1dae398c9f7ba96bc45d59f4faa2934b2cad59e4))
* **api:** update via SDK Studio ([#4](https://github.com/spi-tch/spitch-python/issues/4)) ([22bbf05](https://github.com/spi-tch/spitch-python/commit/22bbf059f4f95bd1f5e99e5d4d71df73977eb17b))
* **api:** update via SDK Studio ([#5](https://github.com/spi-tch/spitch-python/issues/5)) ([a97e4d7](https://github.com/spi-tch/spitch-python/commit/a97e4d77f0bcc97f1b222d1a8500901273b56f9a))
* **api:** update via SDK Studio ([#6](https://github.com/spi-tch/spitch-python/issues/6)) ([b650ea2](https://github.com/spi-tch/spitch-python/commit/b650ea223e9c2e87e0c1a8f9e904a889686decc2))
* **api:** update via SDK Studio ([#65](https://github.com/spi-tch/spitch-python/issues/65)) ([75d0335](https://github.com/spi-tch/spitch-python/commit/75d0335fa27259e3c41e2591f0f8a89773f5ff02))
* **api:** update via SDK Studio ([#7](https://github.com/spi-tch/spitch-python/issues/7)) ([3956108](https://github.com/spi-tch/spitch-python/commit/39561080f65b7098a2bd7851159a0a1ac2bd1b5e))
* **api:** update via SDK Studio ([#71](https://github.com/spi-tch/spitch-python/issues/71)) ([38389b4](https://github.com/spi-tch/spitch-python/commit/38389b4341e7e8dc76ff4d2561ddda848ac30f84))
* **api:** update via SDK Studio ([#72](https://github.com/spi-tch/spitch-python/issues/72)) ([d015bdc](https://github.com/spi-tch/spitch-python/commit/d015bdc2571612e8a202cf5aa610d870c7009f5c))
* **api:** update via SDK Studio ([#73](https://github.com/spi-tch/spitch-python/issues/73)) ([616bdb1](https://github.com/spi-tch/spitch-python/commit/616bdb1edfd9e2a70f09101de19563a82a8ea7b7))
* **api:** update via SDK Studio ([#74](https://github.com/spi-tch/spitch-python/issues/74)) ([462077d](https://github.com/spi-tch/spitch-python/commit/462077d3057796ceefae2e5ba4c36191294bd7a0))
* **api:** update via SDK Studio ([#75](https://github.com/spi-tch/spitch-python/issues/75)) ([9a53106](https://github.com/spi-tch/spitch-python/commit/9a531068e9033ade5bf1fbdfd2123e29092f370f))
* **api:** update via SDK Studio ([#76](https://github.com/spi-tch/spitch-python/issues/76)) ([84a921c](https://github.com/spi-tch/spitch-python/commit/84a921c58ca2ee0876f2ab47997d508eaf89ce7f))
* **api:** update via SDK Studio ([#77](https://github.com/spi-tch/spitch-python/issues/77)) ([521f8ef](https://github.com/spi-tch/spitch-python/commit/521f8efb93d7f35a26dd66176e6f8f275c7f7868))
* **api:** update via SDK Studio ([#78](https://github.com/spi-tch/spitch-python/issues/78)) ([0b1d2f6](https://github.com/spi-tch/spitch-python/commit/0b1d2f63b38571f3514e5bc2debb29b41784bbd2))
* **api:** update via SDK Studio ([#79](https://github.com/spi-tch/spitch-python/issues/79)) ([17bb43b](https://github.com/spi-tch/spitch-python/commit/17bb43bf5e1086b667fb11d4a7e82ca808ef1ca7))
* **api:** update via SDK Studio ([#8](https://github.com/spi-tch/spitch-python/issues/8)) ([75481cc](https://github.com/spi-tch/spitch-python/commit/75481cc5cc576e2a16e056bdd885def8cad0060d))
* **api:** update via SDK Studio ([#9](https://github.com/spi-tch/spitch-python/issues/9)) ([3a43e4f](https://github.com/spi-tch/spitch-python/commit/3a43e4f9c97e5afeaa8374c2eafa815e26d85680))
* commits ([e741720](https://github.com/spi-tch/spitch-python/commit/e74172090c8a263621ef44d67d4aa8db973526f8))
* commits ([f3fecf7](https://github.com/spi-tch/spitch-python/commit/f3fecf7635f8d20747c4f7ed09687a3d0050dd67))
* commits ([50e3396](https://github.com/spi-tch/spitch-python/commit/50e339659a24e1c9c74f604301992fc6071c31f6))
* commits ([ce1277c](https://github.com/spi-tch/spitch-python/commit/ce1277c1c951918182e1b7f79408287a96f974c9))
* commits ([d623a03](https://github.com/spi-tch/spitch-python/commit/d623a03efb0eb839fc17e10069d4238f14994c59))
* commits ([b3eb065](https://github.com/spi-tch/spitch-python/commit/b3eb06504bd4b81fb269df7b2cb2b97b70579c47))
* commits ([b79d3d2](https://github.com/spi-tch/spitch-python/commit/b79d3d24dd3679f94079b963a809f62342513e23))
* commits ([c546c4b](https://github.com/spi-tch/spitch-python/commit/c546c4bafe7fc28df4e22b423d7aae0d0d2ddc95))


### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#30](https://github.com/spi-tch/spitch-python/issues/30)) ([1e63664](https://github.com/spi-tch/spitch-python/commit/1e63664f64fa1f38f2294df8e06bd60a17885d2f))


### Chores

* add repr to PageInfo class ([#32](https://github.com/spi-tch/spitch-python/issues/32)) ([ea3c95d](https://github.com/spi-tch/spitch-python/commit/ea3c95d2ce4a9fdd1e558931f8a92904a9394321))
* configure new SDK language ([b2c715e](https://github.com/spi-tch/spitch-python/commit/b2c715ecc0f6656bd21a6817d2371d1721e19f89))
* go live ([#1](https://github.com/spi-tch/spitch-python/issues/1)) ([46370f0](https://github.com/spi-tch/spitch-python/commit/46370f02575812eda0c2dcd53a007375720fea97))
* **internal:** version bump ([#85](https://github.com/spi-tch/spitch-python/issues/85)) ([37c9ff3](https://github.com/spi-tch/spitch-python/commit/37c9ff35421d35361f1259ebe313c087e98371e5))
* rebuild project due to codegen change ([#61](https://github.com/spi-tch/spitch-python/issues/61)) ([7041078](https://github.com/spi-tch/spitch-python/commit/70410787cb6255e839e3633b0732295f0d98f2bb))
* rebuild project due to codegen change ([#63](https://github.com/spi-tch/spitch-python/issues/63)) ([1761ce9](https://github.com/spi-tch/spitch-python/commit/1761ce946924b818037c3d055f422020814119a1))
* rebuild project due to codegen change ([#64](https://github.com/spi-tch/spitch-python/issues/64)) ([99cc2fc](https://github.com/spi-tch/spitch-python/commit/99cc2fcfe79bbc09242230a5dcdbce085107fed9))
* rebuild project due to codegen change ([#67](https://github.com/spi-tch/spitch-python/issues/67)) ([4b6aa68](https://github.com/spi-tch/spitch-python/commit/4b6aa6839c2aeba8e4a4fbe20786b69634c3c5bc))
* update SDK settings ([#3](https://github.com/spi-tch/spitch-python/issues/3)) ([a9af774](https://github.com/spi-tch/spitch-python/commit/a9af774f183fdf2b50684adf5714c6b5e5354653))

## 1.17.0 (2025-01-14)

Full Changelog: [v1.16.0...v1.17.0](https://github.com/spi-tch/spitch-python/compare/v1.16.0...v1.17.0)

### Features

* **api:** update via SDK Studio ([#79](https://github.com/spi-tch/spitch-python/issues/79)) ([17bb43b](https://github.com/spi-tch/spitch-python/commit/17bb43bf5e1086b667fb11d4a7e82ca808ef1ca7))

## 1.16.0 (2024-11-21)

Full Changelog: [v1.15.1...v1.16.0](https://github.com/spi-tch/spitch-python/compare/v1.15.1...v1.16.0)

### Features

* **api:** update via SDK Studio ([1fd8e69](https://github.com/spi-tch/spitch-python/commit/1fd8e69e19951c5c08b2620a187b02c83e65a6fd))
* **api:** update via SDK Studio ([9edba8c](https://github.com/spi-tch/spitch-python/commit/9edba8c215b16905ac04b11f151e8c04f556727e))
* **api:** update via SDK Studio ([#71](https://github.com/spi-tch/spitch-python/issues/71)) ([38389b4](https://github.com/spi-tch/spitch-python/commit/38389b4341e7e8dc76ff4d2561ddda848ac30f84))
* **api:** update via SDK Studio ([#72](https://github.com/spi-tch/spitch-python/issues/72)) ([d015bdc](https://github.com/spi-tch/spitch-python/commit/d015bdc2571612e8a202cf5aa610d870c7009f5c))
* **api:** update via SDK Studio ([#73](https://github.com/spi-tch/spitch-python/issues/73)) ([616bdb1](https://github.com/spi-tch/spitch-python/commit/616bdb1edfd9e2a70f09101de19563a82a8ea7b7))
* **api:** update via SDK Studio ([#74](https://github.com/spi-tch/spitch-python/issues/74)) ([462077d](https://github.com/spi-tch/spitch-python/commit/462077d3057796ceefae2e5ba4c36191294bd7a0))
* **api:** update via SDK Studio ([#75](https://github.com/spi-tch/spitch-python/issues/75)) ([9a53106](https://github.com/spi-tch/spitch-python/commit/9a531068e9033ade5bf1fbdfd2123e29092f370f))
* **api:** update via SDK Studio ([#76](https://github.com/spi-tch/spitch-python/issues/76)) ([84a921c](https://github.com/spi-tch/spitch-python/commit/84a921c58ca2ee0876f2ab47997d508eaf89ce7f))
* **api:** update via SDK Studio ([#77](https://github.com/spi-tch/spitch-python/issues/77)) ([521f8ef](https://github.com/spi-tch/spitch-python/commit/521f8efb93d7f35a26dd66176e6f8f275c7f7868))
* **api:** update via SDK Studio ([#78](https://github.com/spi-tch/spitch-python/issues/78)) ([0b1d2f6](https://github.com/spi-tch/spitch-python/commit/0b1d2f63b38571f3514e5bc2debb29b41784bbd2))


### Chores

* configure new SDK language ([b2c715e](https://github.com/spi-tch/spitch-python/commit/b2c715ecc0f6656bd21a6817d2371d1721e19f89))

## 1.15.1 (2024-11-18)

Full Changelog: [v1.15.0...v1.15.1](https://github.com/spi-tch/spitch-python/compare/v1.15.0...v1.15.1)

### Chores

* rebuild project due to codegen change ([#67](https://github.com/spi-tch/spitch-python/issues/67)) ([4b6aa68](https://github.com/spi-tch/spitch-python/commit/4b6aa6839c2aeba8e4a4fbe20786b69634c3c5bc))

## 1.15.0 (2024-11-15)

Full Changelog: [v1.14.0...v1.15.0](https://github.com/spi-tch/spitch-python/compare/v1.14.0...v1.15.0)

### Features

* **api:** update via SDK Studio ([#65](https://github.com/spi-tch/spitch-python/issues/65)) ([75d0335](https://github.com/spi-tch/spitch-python/commit/75d0335fa27259e3c41e2591f0f8a89773f5ff02))


### Chores

* rebuild project due to codegen change ([#61](https://github.com/spi-tch/spitch-python/issues/61)) ([7041078](https://github.com/spi-tch/spitch-python/commit/70410787cb6255e839e3633b0732295f0d98f2bb))
* rebuild project due to codegen change ([#63](https://github.com/spi-tch/spitch-python/issues/63)) ([1761ce9](https://github.com/spi-tch/spitch-python/commit/1761ce946924b818037c3d055f422020814119a1))
* rebuild project due to codegen change ([#64](https://github.com/spi-tch/spitch-python/issues/64)) ([99cc2fc](https://github.com/spi-tch/spitch-python/commit/99cc2fcfe79bbc09242230a5dcdbce085107fed9))

## 1.14.0 (2024-10-18)

Full Changelog: [v1.13.0...v1.14.0](https://github.com/spi-tch/spitch-python/compare/v1.13.0...v1.14.0)

### Features

* **api:** api update ([#58](https://github.com/spi-tch/spitch-python/issues/58)) ([be32dce](https://github.com/spi-tch/spitch-python/commit/be32dcec8d8a6f7c868208a7f73e2d7568588f84))

## 1.13.0 (2024-10-18)

Full Changelog: [v1.12.0...v1.13.0](https://github.com/spi-tch/spitch-python/compare/v1.12.0...v1.13.0)

### Features

* **api:** api update ([#55](https://github.com/spi-tch/spitch-python/issues/55)) ([f987e48](https://github.com/spi-tch/spitch-python/commit/f987e48d65d4ef24a650bfc3d01757a565766c18))

## 1.12.0 (2024-10-18)

Full Changelog: [v1.11.0...v1.12.0](https://github.com/spi-tch/spitch-python/compare/v1.11.0...v1.12.0)

### Features

* **api:** api update ([#52](https://github.com/spi-tch/spitch-python/issues/52)) ([1633f60](https://github.com/spi-tch/spitch-python/commit/1633f603f789c4e140ff9455fffaee21c77a5ebd))

## 1.11.0 (2024-10-17)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/spi-tch/spitch-python/compare/v1.10.0...v1.11.0)

### Features

* **api:** api update ([#49](https://github.com/spi-tch/spitch-python/issues/49)) ([f4099b6](https://github.com/spi-tch/spitch-python/commit/f4099b6db02bcc4951d0ced67f7729a04cfa4e92))

## 1.10.0 (2024-10-17)

Full Changelog: [v1.9.0...v1.10.0](https://github.com/spi-tch/spitch-python/compare/v1.9.0...v1.10.0)

### Features

* **api:** api update ([#45](https://github.com/spi-tch/spitch-python/issues/45)) ([feb59bc](https://github.com/spi-tch/spitch-python/commit/feb59bc1cca800efff147800d51ff8bbf486e38b))

## 1.9.0 (2024-10-17)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/spi-tch/spitch-python/compare/v1.8.0...v1.9.0)

### Features

* **api:** api update ([#42](https://github.com/spi-tch/spitch-python/issues/42)) ([1575f47](https://github.com/spi-tch/spitch-python/commit/1575f47becd40467509030e2f56e2c73ac771958))

## 1.8.0 (2024-10-17)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/spi-tch/spitch-python/compare/v1.7.0...v1.8.0)

### Features

* **api:** api update ([#37](https://github.com/spi-tch/spitch-python/issues/37)) ([34e4fba](https://github.com/spi-tch/spitch-python/commit/34e4fba09e3744cfb443a3a0de5bf6a59bac50bc))
* **api:** api update ([#39](https://github.com/spi-tch/spitch-python/issues/39)) ([4cc3eb2](https://github.com/spi-tch/spitch-python/commit/4cc3eb24be8de66ae662de62c45818c0100bf894))

## 1.7.0 (2024-10-14)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/spi-tch/spitch-python/compare/v1.6.0...v1.7.0)

### Features

* **api:** api update ([#34](https://github.com/spi-tch/spitch-python/issues/34)) ([1cfe384](https://github.com/spi-tch/spitch-python/commit/1cfe38416d8c82453609132080a167c0ab735f51))

## 1.6.0 (2024-10-07)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/spi-tch/spitch-python/compare/v1.5.0...v1.6.0)

### Features

* **api:** update via SDK Studio ([#29](https://github.com/spi-tch/spitch-python/issues/29)) ([1dae398](https://github.com/spi-tch/spitch-python/commit/1dae398c9f7ba96bc45d59f4faa2934b2cad59e4))


### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#30](https://github.com/spi-tch/spitch-python/issues/30)) ([1e63664](https://github.com/spi-tch/spitch-python/commit/1e63664f64fa1f38f2294df8e06bd60a17885d2f))


### Chores

* add repr to PageInfo class ([#32](https://github.com/spi-tch/spitch-python/issues/32)) ([ea3c95d](https://github.com/spi-tch/spitch-python/commit/ea3c95d2ce4a9fdd1e558931f8a92904a9394321))

## 1.5.0 (2024-10-07)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/spi-tch/spitch-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** update via SDK Studio ([#26](https://github.com/spi-tch/spitch-python/issues/26)) ([1fb1268](https://github.com/spi-tch/spitch-python/commit/1fb12681c9bbdadd7dd4cb41f06ee03d38be235f))

## 1.4.0 (2024-10-07)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/spi-tch/spitch-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** update via SDK Studio ([#20](https://github.com/spi-tch/spitch-python/issues/20)) ([d1b3421](https://github.com/spi-tch/spitch-python/commit/d1b3421f383b9a575c0721baa32e687aa6609dd6))
* **api:** update via SDK Studio ([#23](https://github.com/spi-tch/spitch-python/issues/23)) ([b0ee3b3](https://github.com/spi-tch/spitch-python/commit/b0ee3b3f10059097252b95498097a4ebeb203afb))

## 1.3.0 (2024-10-07)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/spi-tch/spitch-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** update via SDK Studio ([#16](https://github.com/spi-tch/spitch-python/issues/16)) ([77235df](https://github.com/spi-tch/spitch-python/commit/77235df6b0d1f15d064da89bab6f836e78c1db61))

## 1.2.0 (2024-10-07)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/spi-tch/spitch-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** update via SDK Studio ([#13](https://github.com/spi-tch/spitch-python/issues/13)) ([fdb3beb](https://github.com/spi-tch/spitch-python/commit/fdb3bebe5701a188e2c4f62a3a6d2e72c267532c))

## 1.1.0 (2024-10-07)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/spi-tch/spitch-python/compare/v1.0.0...v1.1.0)

### Features

* commits ([e741720](https://github.com/spi-tch/spitch-python/commit/e74172090c8a263621ef44d67d4aa8db973526f8))
* commits ([f3fecf7](https://github.com/spi-tch/spitch-python/commit/f3fecf7635f8d20747c4f7ed09687a3d0050dd67))
* commits ([50e3396](https://github.com/spi-tch/spitch-python/commit/50e339659a24e1c9c74f604301992fc6071c31f6))
* commits ([ce1277c](https://github.com/spi-tch/spitch-python/commit/ce1277c1c951918182e1b7f79408287a96f974c9))
* commits ([d623a03](https://github.com/spi-tch/spitch-python/commit/d623a03efb0eb839fc17e10069d4238f14994c59))
* commits ([b3eb065](https://github.com/spi-tch/spitch-python/commit/b3eb06504bd4b81fb269df7b2cb2b97b70579c47))
* commits ([b79d3d2](https://github.com/spi-tch/spitch-python/commit/b79d3d24dd3679f94079b963a809f62342513e23))
* commits ([c546c4b](https://github.com/spi-tch/spitch-python/commit/c546c4bafe7fc28df4e22b423d7aae0d0d2ddc95))

## 1.0.0 (2024-10-07)

Full Changelog: [v0.0.1-alpha.0...v1.0.0](https://github.com/spi-tch/spitch-python/compare/v0.0.1-alpha.0...v1.0.0)

### Features

* **api:** update via SDK Studio ([41dd345](https://github.com/spi-tch/spitch-python/commit/41dd34562573b2d2807cedc4722c53b7350ef4dc))
* **api:** update via SDK Studio ([#10](https://github.com/spi-tch/spitch-python/issues/10)) ([74819f2](https://github.com/spi-tch/spitch-python/commit/74819f278e9e2bfa4bb3f5d06c59c3fda3ed069f))
* **api:** update via SDK Studio ([#4](https://github.com/spi-tch/spitch-python/issues/4)) ([22bbf05](https://github.com/spi-tch/spitch-python/commit/22bbf059f4f95bd1f5e99e5d4d71df73977eb17b))
* **api:** update via SDK Studio ([#5](https://github.com/spi-tch/spitch-python/issues/5)) ([a97e4d7](https://github.com/spi-tch/spitch-python/commit/a97e4d77f0bcc97f1b222d1a8500901273b56f9a))
* **api:** update via SDK Studio ([#6](https://github.com/spi-tch/spitch-python/issues/6)) ([b650ea2](https://github.com/spi-tch/spitch-python/commit/b650ea223e9c2e87e0c1a8f9e904a889686decc2))
* **api:** update via SDK Studio ([#7](https://github.com/spi-tch/spitch-python/issues/7)) ([3956108](https://github.com/spi-tch/spitch-python/commit/39561080f65b7098a2bd7851159a0a1ac2bd1b5e))
* **api:** update via SDK Studio ([#8](https://github.com/spi-tch/spitch-python/issues/8)) ([75481cc](https://github.com/spi-tch/spitch-python/commit/75481cc5cc576e2a16e056bdd885def8cad0060d))
* **api:** update via SDK Studio ([#9](https://github.com/spi-tch/spitch-python/issues/9)) ([3a43e4f](https://github.com/spi-tch/spitch-python/commit/3a43e4f9c97e5afeaa8374c2eafa815e26d85680))


### Chores

* go live ([#1](https://github.com/spi-tch/spitch-python/issues/1)) ([46370f0](https://github.com/spi-tch/spitch-python/commit/46370f02575812eda0c2dcd53a007375720fea97))
* update SDK settings ([#3](https://github.com/spi-tch/spitch-python/issues/3)) ([a9af774](https://github.com/spi-tch/spitch-python/commit/a9af774f183fdf2b50684adf5714c6b5e5354653))
