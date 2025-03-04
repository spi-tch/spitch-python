# Changelog

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
