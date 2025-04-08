# 🔓 RSA Encryption Breaker

A Python-based cryptanalysis toolkit for breaking weak or misconfigured RSA encryption schemes. The goal is to explore and implement classic attacks on RSA such as:

- Factoring `n = p*q` with small primes
- Exploiting low public exponent (`e`)
- Recovering plaintext using mathematical attacks (e.g., Wiener's Attack, Common Modulus)
- Implementing Coppersmith's method (if applicable)

---

## 🧠 Use Cases

- Educational demonstration of RSA vulnerabilities
- Practicing cryptanalysis techniques
- Auditing CTF or academic RSA challenges

---

## 🧱 Possible Features

> _(To be filled in once implementation is added)_

- 🔐 Private key recovery via:
  - Trial division
  - Fermat’s factorization
  - Wiener's attack
- 🔎 Plaintext recovery from ciphertext
- 🔄 Common modulus and shared `n` attack
- 📉 Low exponent (`e=3`) brute-force

---

## 📦 Suggested Project Structure

```
rsa-encryption-breaker/
├── attacks/
│   ├── wiener.py
│   ├── common_modulus.py
├── utils/
│   ├── rsa_math.py
│   ├── prime_utils.py
├── main.py
├── README.md
```

---

## 🚀 Getting Started

```bash
git clone https://github.com/mati1mati1/rsa-encryption-breaker.git
cd rsa-encryption-breaker
python3 main.py --attack wiener --n <n> --e <e> --c <ciphertext>
```

---

## 🧪 Dependencies

- Python 3.8+
- `sympy`, `Crypto`, or `gmpy2` for number theory and modular arithmetic

---

## 📜 License

This project is intended for educational use only. Use responsibly.

---

## 👨‍💻 Author

Made with 🔐 by [mati1mati1](https://github.com/mati1mati1)
