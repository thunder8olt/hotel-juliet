Hotel Juliet
============

## What is it?

Hotel Juliet is a framework for classic cryptographic ciphers.  Currently this means various mono- and polyalphabetic substitution ciphers.

If your project requirements include such terms as `AES`, `DES`, `block`, `stream`, or `asymmetric`, it is possible (if not probable) that this framework will disappoint.

This started out as a PHP/JavaScript project long ago. Throughout the years it has transitioned through Perl to its current incarnation in Python.

## What does *Hotel Juliet* mean?

I have no idea where the initialism `HJ`, expanded to the above phrase with the [NATO phonetic alphabet] [1] originated, but [this page] [2] indicates that *Hotel Juliet* occurs when it is time to change one’s keys in an organized (i.e., government-sponsored) program of cryptography.  It seemed memorable enough so I ran with it.

  [1]: http://en.wikipedia.org/wiki/NATO_phonetic_alphabet "NATO phonetic alphabet"
  [2]: http://jproc.ca/crypto/terms.html "Common Crypto Terms"

## What ciphers are supported?

The underlying frameworks are a bit of a playground for me right now.  The code may be messy and/or under-documented and APIs remain subject to change.

### Monoalphabetic substitution

- Affine
- Atbash
- Caesar shift
- Keyword

### Polyalphabetic substitution

- Beaufort
- *Planned:* Della Porta
- Gronsfeld
- Trithemius
- Variant Beaufort
- Vigenère
