# Bitcoin Private Key to Uncompressed Public Key Converter

## Description

This Python script is part of a Coding Assignment for CCS 6354 - Blockchain & Smart Contracts during Trimester 2 - 2023/2024 (2410) .

This Python script converts a Bitcoin private key provided in hexadecimal format into its corresponding uncompressed public key. The script utilizes the `ecdsa` library to perform elliptic curve cryptography operations required for key generation.

## Usage

1. Ensure you have Python installed on your system.
2. Navigate to the project directory.
3. Create a virtual environment:

```bash
python -m venv env
```

4. Activate the virtual environment:
Linux/Mac:
```bash
source env/bin/activate
```
Windows:
```bash
.\env\Scripts\activate
```

5. Install the required library using `pip`:

```bash
pip install -r requirements.txt
```

6. Run the script and enter the Bitcoin private key in hexadecimal format when prompted:

```bash
python btc_key_converter.py
```

7. The script will output the uncompressed public key in hexadecimal format.

## Example

```bash
Enter Private Key       :       d2d45c47357887c4eebc6fa9c7a3ce43de5736513f0dbab49f5ec8b6f538168e
Uncompressed Public Key :       04f7136fbf59b39ad825b0c5b9a685f8417280a41331be899cb999b654b196800e5a1a85bfaf80ff5ded4111e88ac966de185a25e15bbf775b6e5705cc270a5e39
```

## References

- [ECDSA Python Library](https://pypi.org/project/ecdsa/)
- [Bitcoin Address Generator](https://blockchain-academy.hs-mittweida.de/bitcoin-address-generator/)
- [Bitcoin Developer Guide - Public Key](https://bitcoin.org/en/developer-guide#public-key)

## Libraries

- [ecdsa](https://pypi.org/project/ecdsa/): Python library for performing Elliptic Curve Digital Signature Algorithm (ECDSA) operations.