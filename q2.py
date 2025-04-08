from q2_atm import ATM, ServerResponse,RSA_PUB_KEY_CARD,fast_exponent_and_modulus
from Crypto.PublicKey import RSA

def extract_PIN(encrypted_PIN) -> int:
    """Extracts the original PIN string from an encrypted PIN."""
    # TODO: IMPLEMENT THIS FUNCTION
    atm = ATM()
    for i in range(10000):
        if encrypted_PIN == atm.encrypt_PIN(i):
            return i


def extract_credit_card(encrypted_credit_card) -> int:
    """Extracts a credit card number string from its ciphertext."""
    # TODO: IMPLEMENT THIS FUNCTION
    atm = ATM()
    e = RSA_PUB_KEY_CARD.e
    return round(encrypted_credit_card **(1/e))

    
def forge_signature():
    """Forge a server response that passes verification."""
    # Return a ServerResponse instance.
    # TODO: IMPLEMENT THIS FUNCTION
    atm = ATM()
    status_code = atm.CODE_APPROVAL
    forged_sign = fast_exponent_and_modulus(status_code,RSA_PUB_KEY_CARD.e,RSA_PUB_KEY_CARD.n)
    return ServerResponse(status=status_code,signature=forged_sign)
