import ecdsa
import binascii

def pvt_to_pub(pvt_key_hex):
    # Convert the private key from hex to bytes
    pvt_key_bytes = binascii.unhexlify(pvt_key_hex)

    # Get the public key from the private key
    signing_key = ecdsa.SigningKey.from_string(pvt_key_bytes, curve=ecdsa.SECP256k1)
    verifying_key = signing_key.get_verifying_key()

    # Get the uncompressed public key in hex format
    pub_key_hex = "04" + verifying_key.to_string().hex()

    return pub_key_hex

# Input private key in hex
pvt_key_hex = input("Enter Private Key\t:\t")

# Get the uncompressed public key
pub_key_hex = pvt_to_pub(pvt_key_hex)

print("Uncompressed Public Key\t:\t" + pub_key_hex)