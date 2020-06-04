# Changelog
All notable changes to this project will be documented in this file. The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## 2020-6-4

### Added
- Explanation in `README.md` and `product-description.md` regarding removal of `countries`, `cdc/daily`, `urls` and `press` dataset files.

### Deprecated
- `countries`, `cdc/daily`, `urls` and `press` dataset files, as they are no longer publicly accessible through the COVID Tracking Project's API.

### Removed
- `countries`, `cdc/daily`, `urls` and `press` are no longer included in the "Data Sources" section in `README.md` and `product-description.md`.

### Fixed
- Adjusted Retry logic in `sounce_data.py` to properly raise an error if 5 attempts to access an individual endpoint.