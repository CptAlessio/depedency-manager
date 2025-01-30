# Dependency License Checker

A Python-based tool to scan and check licenses for your project dependencies from both NPM and Maven repositories.

## Description

This tool helps developers identify the licenses of their project dependencies by scanning package.json files and querying multiple package repositories. It currently supports:

- NPM packages via npmjs.com
- Maven packages via mvnrepository.com

## Features

- Scans dependencies from package.json files
- Supports both NPM and Maven repository lookups
- Optional dev dependencies scanning
- Configurable request throttling to respect rate limits
- Flexible configuration for different repository sources

## Installation

1. Clone this repository:

```bash
git clone https://github.com/CptAlessio/depedency-manager
```

2. Install required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

Run the script by providing the path to your package.json file:

```bash
python dependency-manager.py path/to/package.json
```

## Configuration Options

You can modify the following settings in `dependency-manager.py`:

- `scanNPMJS`: Enable/disable NPM repository scanning
- `scanMavenRepository`: Enable/disable Maven repository scanning
- `scanDevDependencies`: Enable/disable scanning of devDependencies
- `throttle`: Adjust the request delay (in seconds) to avoid rate limiting

## Output

The tool will output license information for each dependency in the following format:

```
Dependencies:
 NPMJS - package-name license: MIT
 Maven - package-name license: Apache-2.0

Dev Dependencies:
 NPMJS - dev-package-name license: BSD-3-Clause
 Maven - dev-package-name license: MIT
```

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

MIT License

## Disclaimer

This tool is provided as-is and makes no guarantees about the accuracy of license information. Always verify license information manually for critical dependencies.
